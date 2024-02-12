import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '#cancel')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Complete checkout")
    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)