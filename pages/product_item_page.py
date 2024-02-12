from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductItemPage(BasePage):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn_inventory')
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, '#back-to-products')

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def back_to_products(self):
        self.click(self.BACK_TO_PRODUCTS_BUTTON)


