import unittest
import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.profile_other_user_page import ProfileOtherUserPage
from page_objects.search_page import SearchPage
from selenium.webdriver.common.by import By

class FollowUnfollowUserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.get("https://www.quora.com/")

        # Load cookies from file
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.search_page = SearchPage(self.driver)
        self.profil_page = ProfileOtherUserPage(self.driver)
        time.sleep(5)

    # Telah login dan belum mengikuti pengguna yang diuji
    def test_follow_user(self):
        keyword = "Andri Rahmadaniiii"
        self.search_page.search(keyword)
        time.sleep(5)  # Jeda 2 detik untuk menunggu hasil pencarian
        choose_profile = self.driver.find_element(By.XPATH,
                                                 "(//a[contains(@class,'q-box Link___StyledBox-t2xg9c-0 dFkjrQ puppeteer_test_link qu-color--blue_dark qu-cursor--pointer qu-hover--textDecoration--underline')])[1]")
        choose_profile.click()
        time.sleep(5)
        self.profil_page.click_follow()
        time.sleep(2)
        self.driver.refresh()

        # time.sleep(3)
        # self.assertTrue(self.profil_page.is_followed_button_displayed())

    # Berhenti mengikuti pengguna lain
    def test_unfollow_user(self):
        keyword = "Andri Rahmadaniiii"
        self.search_page.search(keyword)
        time.sleep(5)  # Jeda 2 detik untuk menunggu hasil pencarian
        choose_profile = self.driver.find_element(By.XPATH,
                                                  "(//a[contains(@class,'q-box Link___StyledBox-t2xg9c-0 dFkjrQ puppeteer_test_link qu-color--blue_dark qu-cursor--pointer qu-hover--textDecoration--underline')])[1]")
        choose_profile.click()
        time.sleep(5)
        self.profil_page.click_unfollow()
        time.sleep(2)
        # self.assertTrue(self.profile_page.is_follow_button_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
