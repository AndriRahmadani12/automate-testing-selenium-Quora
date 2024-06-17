from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.add_credential_link = (By.XPATH, "(//a[@class='q-box Link___StyledBox-t2xg9c-0 dFkjrQ puppeteer_test_link qu-cursor--pointer qu-hover--textDecoration--underline'])[1]")
        self.edit_credential_icon = (By.LINK_TEXT, "Tambahkan kredensial pekerjaan")
        self.delete_button = (By.XPATH, '//button[text()="Hapus"]')

    # def click_add_credential(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.add_credential_link)
    #     ).click()

    # def click_add_credential(self):
    #     self.driver.find_element(*self.add_credential_link).click()

    def click_add_credential(self):
        # Menggunakan JavaScript path untuk menargetkan elemen dan klik menggunakan execute_script
        jsPath = "document.querySelector('a:nth-child(1) div:nth-child(1) div:nth-child(2) span:nth-child(1)')"
        self.driver.execute_script(f"document.querySelector('{jsPath}').click();")



    def click_edit_credential(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_credential_icon)
        ).click()

    def click_delete_credential(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()
