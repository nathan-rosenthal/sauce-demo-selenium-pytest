import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutFirstStage(BasePage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#last-name')
    ZIP_POSTAL_CODE_FIELD = (By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '#cancel')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Fill Personal information: first_name , last_name , zip_postal code ")
    def fill_your_information_form(self, first_name, last_name, zip_post_code):
        self.fill_text(self.FIRST_NAME_FIELD, first_name)
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        self.fill_text(self.ZIP_POSTAL_CODE_FIELD, zip_post_code)
        self.click(self.CONTINUE_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)