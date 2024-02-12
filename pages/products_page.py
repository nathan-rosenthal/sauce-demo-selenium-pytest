import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.helpers import Helpers
from pages.sitewide_ui import SiteWideUI


class ProductsPage(BasePage):
    PRODUCT_NAME_LINKS = (By.CSS_SELECTOR, '.inventory_item_name')
    PRODUCT_ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, '.inventory_list button')
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    SORT_MENU = (By.CSS_SELECTOR, '.product_sort_container')
    PRODUCTS_PAGE_HEADER_TITLE = (By.CSS_SELECTOR, '#header_container .title')
    PRODUCT_PRICES = (By.CSS_SELECTOR, '.inventory_item_price')
    PRODUCT_ITEM_NAMES = (By.CSS_SELECTOR, '.inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Select an item by position: item_position")
    def select_item_by_position(self, item_position):
        self.click_item_from_elements_list_by_position(self.PRODUCT_NAME_LINKS, item_position)

    @allure.step("Add an item to cart by position: item_position")
    def add_item_to_cart_by_order(self, item_position):
        self.click_item_from_elements_list_by_position(self.PRODUCT_ADD_TO_CART_BUTTONS, item_position)

    @allure.step("Add all items in page to cart")
    def add_all_page_items_to_cart(self):
        self.click_all_list_elements(self.PRODUCT_ADD_TO_CART_BUTTONS)

    @allure.step("Click on Go to Cart")
    def go_to_cart(self):
        site_wide_ui = SiteWideUI(self)
        site_wide_ui.click_on_shopping_cart_button()

    @allure.step("Sort products by price: Ascending")
    def sort_products_by_price_ascending(self):
        self.select_from_dropdown_by_value(self.SORT_MENU, 'lohi')

    @allure.step("Sort products by price: Descending")
    def sort_products_by_price_descending(self):
        self.select_from_dropdown_by_value(self.SORT_MENU, 'hilo')

    @allure.step("Sort products by Name: Ascending")
    def sort_products_by_name_ascending(self):
        self.select_from_dropdown_by_value(self.SORT_MENU, 'az')

    @allure.step("Sort products by Name: Descending")
    def sort_products_by_name_descending(self):
        self.select_from_dropdown_by_value(self.SORT_MENU, 'za')

    def get_header_title(self):
        return self.get_text(self.PRODUCTS_PAGE_HEADER_TITLE)

    def get_products_item_names(self):
        # return product item names in current sort order
        return self.get_list_of_elements_text(self.PRODUCT_ITEM_NAMES)

    def get_products_prices(self):
        # return products prices in current sort order
        return self.get_list_of_elements_text(self.PRODUCT_PRICES)

    def get_products_prices_as_floats(self):
        # return products prices sliced and converted to floats for comparison
        return [float(price[1:]) for price in self.get_products_prices()]

    def validate_correct_ordering_by_price_high_low(self):
        products_prices = self.get_products_prices_as_floats()
        return Helpers.compare_list_items_for_descending_order(products_prices)

    def validate_correct_ordering_by_price_low_high(self):
        products_prices = self.get_products_prices_as_floats()
        return Helpers.compare_list_items_for_ascending_order(products_prices)

    def validate_correct_ordering_by_name_a_z(self):
        product_item_names = self.get_products_item_names()
        return Helpers.compare_list_items_for_ascending_order(product_item_names)

    def validate_correct_ordering_by_name_z_a(self):
        product_item_names = self.get_products_item_names()
        return Helpers.compare_list_items_for_descending_order(product_item_names)
