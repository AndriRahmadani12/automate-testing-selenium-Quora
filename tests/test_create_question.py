import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.home_page import HomePage
from page_objects.add_question_page import AddQuestionPage


class TestCreateQuestion(unittest.TestCase):

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
        self.add_question_page = AddQuestionPage(self.driver)
        time.sleep(5)  # Wait for home page to load fully

    # Membuat pertanyaan yang similiar dengan pengguna lain
    def test_create_similar_question(self):
        self.home_page.click_tambah_pertanyaan()
        time.sleep(3)

        self.add_question_page.enter_question("mengapa kucing lucu")
        self.add_question_page.click_submit()
        time.sleep(3)

        self.assertTrue(self.add_question_page.is_suggestion_displayed(),
                        "Suggestion to view similar questions is not displayed")

    # Membuat pertanyaan mengandung kalimat typo
    def test_create_question_with_typo(self):
        self.home_page.click_tambah_pertanyaan()
        time.sleep(2)

        self.add_question_page.enter_question("cara merawath kucing")
        self.add_question_page.click_submit()
        time.sleep(2)

        self.assertTrue(self.add_question_page.is_typo_suggestion_displayed(), "Typo suggestion is not displayed")

    # Membuat pertanyaan valid dan belum pernah ditanyakan oleh pengguna lain
    def test_create_valid_unique_question(self):
        self.home_page.click_tambah_pertanyaan()
        time.sleep(2)

        self.add_question_page.enter_question("Bagaimana cara melakukan pengujian untuk situs web Quora")
        time.sleep(3)
        self.add_question_page.click_submit()
        time.sleep(2)

        self.add_question_page.click_complete()
        time.sleep(4)

        # Verifikasi apakah pertanyaan berhasil ditambahkan
        self.assertIn("Bagaimana cara melakukan pengujian untuk situs web Quora?", self.driver.page_source,
                      "Question was not added successfully")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
