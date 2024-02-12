from selenium import webdriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.sitewide_ui import SiteWideUI


class CartTests:
    DRIVER = webdriver.Chrome()
    STANDARD_USERNAME = 'standard_user'
    PASSWORD_ALL = 'secret_sauce'

    @staticmethod
    def remove_item_from_cart():
        driver = CartTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CartTests.STANDARD_USERNAME, CartTests.PASSWORD_ALL)

        #add first product to cart
        productsPage = ProductsPage(driver)
        productsPage.add_item_to_cart_by_order(0)

        #go to cart, and remove item
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.remove_cart_item(0)
        cartPage.continue_shopping()



    @staticmethod
    def remove_all_cart_items():
        driver = CartTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CartTests.STANDARD_USERNAME, CartTests.PASSWORD_ALL)

        # add all items in page to cart
        productsPage = ProductsPage(driver)
        productsPage.add_all_page_items_to_cart()

        # go to cart, and remove all items in cart
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.remove_all_cart_items()
        cartPage.continue_shopping()
