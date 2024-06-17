from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfileOtherUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.follow_unfollow_button = (By.CSS_SELECTOR, ".q-click-wrapper.qu-active--textDecoration--none.qu-focus--textDecoration--none.qu-borderRadius--pill.qu-alignItems--center.qu-justifyContent--center.qu-whiteSpace--nowrap.qu-userSelect--none.qu-display--inline-flex.qu-bg--blue.qu-tapHighlight--white.qu-textAlign--center.qu-cursor--pointer.qu-hover--textDecoration--none.ClickWrapper___StyledClickWrapperBox-zoqi4f-0.iyYUZT.base___StyledClickWrapper-lx6eke-1.hIqLpn")
        self.text_followed = (By.XPATH, "//div[contains(@class,'q-text qu-ellipsis qu-whiteSpace--nowrap')][normalize-space()='Mengikuti']")
        self.text_not_flowed = (By.XPATH, "//div[contains(text(),'Ikuti')]")



    def click_follow(self):
        self.driver.find_element(*self.follow_unfollow_button).click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(self.follow_unfollow_button)
        # ).click()

    def click_unfollow(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.follow_unfollow_button)
        ).click()

    def is_followed_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.text_followed)
        ).is_displayed()

    def is_unfollow_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.unfollow_button)
        ).is_displayed()
