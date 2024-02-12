from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SiteWideUI(BasePage):

    SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')

    def click_on_shopping_cart_button(self):
        self.click(self.SHOPPING_CART_BUTTON)

    def get_shopping_cart_badge_counter(self):
        return int(self.get_text(self.SHOPPING_CART_BADGE))

