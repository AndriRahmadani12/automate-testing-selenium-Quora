import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.login_page import LoginPage

class TestQuoraLogin(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.get("https://www.quora.com/")
        self.login_page = LoginPage(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )

    # Sukses login dengan valid email dan password
    def test_login_success(self):
        self.login_page.enter_email("2110817110008@mhs.ulm.ac.id")
        time.sleep(2)  # Jeda 2 detik
        self.login_page.enter_password("#Rahmadani123")
        time.sleep(2)  # Jeda 2 detik
        print("Please solve the CAPTCHA within the next 20 seconds...")
        time.sleep(20)  # Wait for manual CAPTCHA solving
        self.login_page.submit()

        # Verifikasi login berhasil
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//a[@aria-label='Beranda']//span[@class='q-inlineBlock qu-width--28 qu-height--28']//span[1]//*[name()='svg']//*[name()='path' and contains(@class,'icon_svg-f')]"))
        )
        home_icon = self.driver.find_element(By.XPATH,
                                             "//a[@aria-label='Beranda']//span[@class='q-inlineBlock qu-width--28 qu-height--28']//span[1]//*[name()='svg']//*[name()='path' and contains(@class,'icon_svg-f')]")
        self.assertTrue(home_icon.is_displayed())

        # Save cookies to file
        cookies = self.driver.get_cookies()
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

    # Gagal login dengan invalid email dan valid password
    def test_login_failure_invalid_email(self):
        self.login_page.enter_email("21108171108@mhs.ulm.ac.id")
        time.sleep(2)  # Jeda 2 detik
        self.login_page.enter_password("#Rahmadani123")
        time.sleep(2)  # Jeda 2 detik
        error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Tidak ada akun yang ditemukan untuk surel ini. Coba lagi')]")
        self.assertTrue(error_message.is_displayed())

    # Gagal login dengan valid email dan invalid password
    def test_login_failure_invalid_password(self):
        self.login_page.enter_email("2110817110008@mhs.ulm.ac.id")
        time.sleep(2)  # Jeda 2 detik
        self.login_page.enter_password("passwordsalah123")
        time.sleep(2)  # Jeda 2 detik
        print("Please solve the CAPTCHA within the next 20 seconds...")
        time.sleep(20)  # Wait for manual CAPTCHA solving

        self.login_page.submit()
        time.sleep(4)
        # Verifikasi login gaga
        error_message = self.driver.find_element(By.XPATH,
                                                 "//div[@class='q-text qu-dynamicFontSize--small qu-color--red_error']")
        self.assertTrue(error_message.is_displayed())


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
