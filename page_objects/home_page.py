from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.tambah_pertanyaan_button = (By.XPATH, "//div[contains(text(),'Tambah pertanyaan')]")
        self.profile_icon = (By.CSS_SELECTOR, "div[class='q-relative qu-display--inline-flex qu-alignItems--center qu-justifyContent--center'] div[class='q-box qu-borderRadius--circle qu-borderAll qu-borderColor--darken Photo___StyledBox-sc-1x7c6d3-0']")  # Gantilah dengan selector yang sesuai
        self.profile_name = (By.CSS_SELECTOR, ".q-box.Link___StyledBox-t2xg9c-0.dFkjrQ.puppeteer_test_link.qu-display--block.qu-px--medium.qu-py--small.qu-borderBottom.qu-color--gray_dark.qu-cursor--pointer.qu-hover--textDecoration--none")  # Gantilah dengan selector yang sesuai

    def click_tambah_pertanyaan(self):
        self.driver.find_element(*self.tambah_pertanyaan_button).click()

    def click_profile_icon(self):
        self.driver.find_element(*self.profile_icon).click()

    def click_profile_name(self):
        self.driver.find_element(*self.profile_name).click()
