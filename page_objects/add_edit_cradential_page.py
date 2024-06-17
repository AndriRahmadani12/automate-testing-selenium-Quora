from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEditCredentialPage:
    def __init__(self, driver):
        self.driver = driver
        self.position_input = (By.XPATH, '//input[@name="position"]')
        self.organization_input = (By.XPATH, '//input[@name="organization"]')
        self.start_year_input = (By.XPATH, '//input[@name="start_year"]')
        self.end_year_input = (By.XPATH, '//input[@name="end_year"]')
        self.currently_working_checkbox = (By.XPATH, '//input[@name="currently_working"]')
        self.save_button = (By.XPATH, '//button[text()="Simpan"]')
        self.error_message = (By.XPATH, '//div[contains(text(),"Rentang tanggal tidak valid")]')

    def enter_position(self, position):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.position_input)
        ).send_keys(position)

    def enter_organization(self, organization):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.organization_input)
        ).send_keys(organization)

    def enter_start_year(self, start_year):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_year_input)
        ).send_keys(start_year)

    def enter_end_year(self, end_year):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.end_year_input)
        ).send_keys(end_year)

    def check_currently_working(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.currently_working_checkbox)
        ).click()

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def is_error_message_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).is_displayed()
