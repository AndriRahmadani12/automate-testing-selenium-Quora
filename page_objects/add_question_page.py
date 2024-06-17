from selenium.webdriver.common.by import By


class AddQuestionPage:
    def __init__(self, driver):
        self.driver = driver
        self.question_textarea = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
        self.submit_button = (By.XPATH, "//button[contains(@class,'q-click-wrapper qu-active--textDecoration--none qu-focus--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-bg--blue qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none ClickWrapper___StyledClickWrapperBox-zoqi4f-0 iyYUZT base___StyledClickWrapper-lx6eke-1 hIqLpn puppeteer_test_modal_submit')]")
        self.suggestion_button = (By.XPATH, "//body/div[@id='root']/div[contains(@class,'q-box')]/div[contains(@class,'q-box')]/div[contains(@class,'q-box')]/div[contains(@class,'bUYbPX')]/div[@class='q-text qu-dynamicFontSize--regular qu-display--flex qu-lineHeight--regular qu-overflowX--auto qu-zIndex--modal_desktop qu-alignItems--center']/div[@class='q-fixed qu-full qu-display--flex qu-justifyContent--center qu-alignItems--flex-start']/div[@role='dialog']/div/div[@class='q-flex qu-flexDirection--column qu-overflow--hidden']/div[@class='q-flex qu-flexDirection--column qu-overflowY--auto']/div[@class='q-sticky qu-bg--white qu-borderTop']/div[@class='q-flex qu-flexDirection--column qu-alignItems--center qu-px--medium qu-py--small']/div[@class='q-flex qu-justifyContent--flex-end qu-alignItems--center']/button[1]")
        self.typo_suggestion = (By.XPATH, "//div[contains(text(),'Mungkin maksud Anda:')]")
        self.complete_button = (By.XPATH, "//div[@class='q-flex qu-flexDirection--row qu-alignItems--center qu-justifyContent--space-between qu-px--medium qu-py--small']//button[@role='button']")

    def enter_question(self, question):
        self.driver.find_element(*self.question_textarea).send_keys(question)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def is_suggestion_displayed(self):
        return self.driver.find_element(*self.suggestion_button).is_displayed()

    def is_typo_suggestion_displayed(self):
        return self.driver.find_element(*self.typo_suggestion).is_displayed()

    def click_complete(self):
        self.driver.find_element(*self.complete_button).click()
