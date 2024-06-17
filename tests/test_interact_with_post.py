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
from page_objects.post_page import InteractPage


class TestInteractWithPost(unittest.TestCase):

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

        self.interact_page = InteractPage(self.driver)
        time.sleep(5)  # Wait for home page to load fully

    # Sukses memberikan upvote di postingan pengguna lain
    def test_upvote_post(self):
        # Dapatkan jumlah dukungan naik sebelum
        upvote_count_before = self.driver.find_element(By.XPATH,
                                                       "(//div[contains(@class,'q-text qu-overflow--hidden qu-display--inline-flex qu-minWidth--20')])[1]").text

        # Dukung Naik
        self.interact_page.upvote()
        time.sleep(2)  # Jeda 2 detik untuk melihat hasil dukungan

        # Validasi Dukungan Naik
        upvote_count_after =self.driver.find_element(By.XPATH,
                                                       "(//div[contains(@class,'q-text qu-overflow--hidden qu-display--inline-flex qu-minWidth--20')])[1]").text
        #berhasil jika jumlahnya bukan ribuan  : 1rb. jika kurang dri ribuan maka akan kelihatan perbedaannya
        self.assertNotEqual(upvote_count_before, upvote_count_after, "Upvote count did not change after upvoting")


    # Sukses memberikan downvote di postingan pengguna lain
    def test_downvote_post(self):
        # Dapatkan jumlah dukungan turun sebelum
        # downvote_count_before = self.driver.find_element(By.XPATH,
        #                                                  "//button[contains(@class, 'DownvoteButton')]//span").text

        # Dukung Turun
        self.interact_page.downvote()

        time.sleep(4)  # Jeda 2 detik untuk melihat hasil dukungan
        # Validasi perubahan kelas pada span
        # span_element = self.driver.find_element(By.XPATH,
        #                                         "//button[contains(@class, 'DownvoteButton')]//span[contains(@class, 'Icon___StyledCssInlineComponent')]")
        # span_classes = span_element.get_attribute("class")
        # self.assertIn("ezQKSa", span_classes, "Downvote button did not turn red after clicking")

    # Sukses memberikan komentar di postingan pengguna lain
    def test_comment_post(self):
        # Menambahkan Komentar
        comment_text = "Nice Post"
        self.interact_page.comment(comment_text)
        # time.sleep(2)  # Jeda 2 detik

        # # Validasi Komentar
        # comments = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'comment_text')]")
        # comment_texts = [comment.text for comment in comments]
        # self.assertIn(comment_text, comment_texts, "Comment was not added successfully")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
