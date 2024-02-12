import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    BACK_HOME_BUTTON = (By.CSS_SELECTOR, '#back-to-products')
    CHECKOUT_COMPLETE_TEXT = (By.CSS_SELECTOR, '#checkout_complete_container > .complete-text')

    def __init__(self, driver):
        super().__init__(driver)

    def back_home(self):
        self.click(self.BACK_HOME_BUTTON)

    @allure.step("Get Checkout Completed confirmation text")
    def get_checkout_complete_confirmation_text(self):
        return self.get_text(self.CHECKOUT_COMPLETE_TEXT)
