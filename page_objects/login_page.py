from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.submit_button = (By.XPATH, "//div[@class='q-text qu-ellipsis qu-whiteSpace--nowrap'][normalize-space()='Masuk']")

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_input)
        ).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        ).send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()
