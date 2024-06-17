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
from page_objects.search_page import SearchPage


class TestSearchFeature(unittest.TestCase):

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

        self.search_page = SearchPage(self.driver)
        time.sleep(5)  # Wait for home page to load fully

    # Sukses menampilkan hasil pencarian sesuai dengan kata kunci
    def test_search_valid_keyword(self):
        keyword = "kucing lucu"
        self.search_page.search(keyword)
        time.sleep(5)  # Jeda 2 detik untuk menunggu hasil pencarian

        results = self.search_page.get_results()

        self.assertTrue(len(results) > 0, "No search results found for valid keyword")

        # Verifikasi bahwa semua hasil pencarian mengandung keyword
        is_relevant = self.search_page.verify_results_contain_keyword(results, keyword)
        self.assertTrue(is_relevant, "Some search results do not contain the keyword")

    # Mencari dengan kata kunci tidak valid
    def test_search_invalid_keyword(self):
        keyword = "jdwidjiwdwdwj"
        self.search_page.search(keyword)
        time.sleep(2)  # Jeda 2 detik untuk menunggu hasil pencarian

        no_results_message = self.search_page.get_no_results_message()
        self.assertIn("Kami tidak bisa menemukan hasil apa pun untuk", no_results_message,
                      "No results message not displayed for invalid keyword")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
