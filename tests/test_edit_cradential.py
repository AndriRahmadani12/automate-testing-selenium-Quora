import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.home_page import HomePage
from page_objects.profile_page import ProfilePage
from page_objects.add_edit_cradential_page import AddEditCredentialPage


class TestEditCredential(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.get("https://www.quora.com/")

        # Load cookies from file
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.add_edit_credential_page = AddEditCredentialPage(self.driver)
        time.sleep(5)  # Wait for home page to load fully

    # Menambahkan kradensial pekerjaan dengan tahun tidak valid
    def test_add_invalid_year_credential(self):
        self.home_page.click_profile_icon()
        time.sleep(2)
        self.home_page.click_profile_name()
        time.sleep(4)

        self.profile_page.click_add_credential()
        time.sleep(15)
        #
        # self.add_edit_credential_page.enter_position("Mahasiswa")
        # self.add_edit_credential_page.enter_organization("Universitas Lambung Mangkurat")
        # self.add_edit_credential_page.enter_start_year("2024")
        # self.add_edit_credential_page.enter_end_year("2021")
        # self.add_edit_credential_page.click_save()
        # time.sleep(2)
        #
        # self.assertTrue(self.add_edit_credential_page.is_error_message_displayed(),
        #                 "Error message for invalid date range is not displayed")

    # Menambahkan kredensial pekerjaan dengan data valid
    def test_add_valid_credential(self):
        self.home_page.click_profile_icon()
        time.sleep(2)
        self.home_page.click_profile_name()
        time.sleep(2)

        self.profile_page.click_add_credential()
        time.sleep(2)

        self.add_edit_credential_page.enter_position("Mahasiswa")
        self.add_edit_credential_page.enter_organization("Universitas Lambung Mangkurat")
        self.add_edit_credential_page.enter_start_year("2021")
        self.add_edit_credential_page.check_currently_working()
        self.add_edit_credential_page.click_save()
        time.sleep(2)

        self.assertIn("Mahasiswa di Universitas Lambung Mangkurat2021–saat ini", self.driver.page_source,
                      "Credential was not added successfully")

    # Menghapus kradensial
    def test_delete_credential(self):
        self.home_page.click_profile_icon()
        time.sleep(2)
        self.home_page.click_profile_name()
        time.sleep(2)

        self.profile_page.click_edit_credential()
        time.sleep(2)

        self.profile_page.click_delete_credential()
        time.sleep(2)

        self.assertIn("Tambahkan kredensial pekerjaan", self.driver.page_source,
                      "Credential was not deleted successfully")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
