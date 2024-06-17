from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class InteractPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def upvote(self):
        upvote_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Dukung Naik'])[1]")))
        upvote_button.click()

    def downvote(self):
        downvote_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(@aria-label,'Dukung Turun')])[1]")))
        downvote_button.click()

    def comment(self, text):
        comment_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'q-inlineFlex qu-mr--tiny')])[2]")))
        comment_button.click()


        # comment_area = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "(//div[@class='doc'])[1]")))
        # comment_area.send_keys(text)
        #
        # submit_button = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'q-flex qu-alignItems--center qu-justifyContent--flex-end')]//button[contains(@role,'button')]")))
        # submit_button.click()

        time.sleep(6)


        comment_area = self.driver.find_element(By.XPATH, "(//div[@class='doc'])[1]")
        comment_area.send_keys(text)

        time.sleep(6)

        submit_button = self. driver.find_element(By.XPATH, "//div[contains(@class,'q-flex qu-alignItems--center qu-justifyContent--flex-end')]//button[contains(@role,'button')]")
        submit_button.click()
