from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.choseFirstResult = (By.XPATH, '//button[text()="Hapus"]')

    def search(self, keyword):
        search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Cari Quora']")))
        search_box.clear()
        search_box.send_keys(keyword)
        # search_box.send_keys(Keys.RETURN)  # Tekan tombol Enter
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='selector-option-0']//div//div[@class='q-flex qu-alignItems--center qu-py--small qu-overflow--hidden']"))).click()


    def get_results(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//body/div[@id='root']/div[@class='q-box']/div[@class='q-box']/div[@class='q-box']/div[@class='q-box']/div[@class='q-box']/div[@class='q-text qu-dynamicFontSize--regular qu-display--flex qu-px--large qu-pb--large qu-flexDirection--row']/div[@id='mainContent']/div[@class='q-box']/div[@class='q-box qu-borderAll qu-borderRadius--small qu-borderColor--raised qu-boxShadow--small qu-bg--raised']/div[2]/div[1]")))

    def get_no_results_message(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Kami tidak bisa menemukan hasil apa pun untuk')]"))).text

    def verify_results_contain_keyword(self, results, keyword):
        for result in results:
            if keyword.lower() not in result.text.lower():
                return False
        return True
