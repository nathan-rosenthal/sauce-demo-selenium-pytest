import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    CART_REMOVE_ITEM_BUTTONS = (By.CSS_SELECTOR, '.cart_list button')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '#continue-shopping')
    CART_ITEMS = (By.CSS_SELECTOR, '.cart_item')
    CART_PAGE_HEADER_TITLE = (By.CSS_SELECTOR, '#header_container .title')

    def __init__(self, driver):
        super().__init__(driver)

    allure.step("Click on Checkout button")
    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def remove_cart_item(self, item_number):
        self.click_item_from_elements_list_by_position(self.CART_REMOVE_ITEM_BUTTONS, item_number)

    def remove_all_cart_items(self):
        self.click_all_list_elements(self.CART_REMOVE_ITEM_BUTTONS)

    def get_number_items_in_cart(self):
        return self.get_number_of_list_elements(self.CART_ITEMS)

    def get_header_title(self):
        return self.get_text(self.CART_PAGE_HEADER_TITLE)



