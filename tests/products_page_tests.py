from selenium import webdriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class ProductsPageTests:

    DRIVER = webdriver.Chrome()
    STANDARD_USERNAME = 'standard_user'
    PASSWORD_ALL = 'secret_sauce'

    @staticmethod
    def sort_products():
        loginPage = LoginPage(ProductsPageTests.DRIVER)
        loginPage.goToLoginPage()
        loginPage.login(ProductsPageTests.STANDARD_USERNAME, ProductsPageTests.PASSWORD_ALL)
        productsPage = ProductsPage(ProductsPageTests.DRIVER)
        productsPage.sort_products_by_price_descending()
        productsPage.sort_products_by_price_ascending()
        productsPage.sort_products_by_name_ascending()
        productsPage.sort_products_by_name_descending()


