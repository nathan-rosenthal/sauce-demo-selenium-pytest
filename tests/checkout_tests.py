from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_1_page import CheckoutFirstStage
from pages.checkout_step_2_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.products_page import ProductsPage
from pages.sitewide_ui import SiteWideUI


class CheckoutTests:
    DRIVER = webdriver.Chrome()
    STANDARD_USERNAME = 'standard_user'
    PASSWORD_ALL = 'secret_sauce'

    @staticmethod
    def checkout_items():
        driver = CheckoutTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CheckoutTests.STANDARD_USERNAME, CheckoutTests.PASSWORD_ALL)

        # Select product from products page, and add to cart
        productsPage = ProductsPage(driver)
        productsPage.select_item_by_position(0)
        productItemPage = ProductItemPage(driver)
        productItemPage.add_item_to_cart()
        productItemPage.back_to_products()

        # Select another product from products page, and add to cart
        productsPage.select_item_by_position(1)
        productItemPage.add_item_to_cart()
        productItemPage.back_to_products()

        # Go to cart & checkout
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.checkout()
        checkoutStage1 = CheckoutFirstStage(driver)
        checkoutStage1.fill_your_information_form('nate', 'dog', '91210')
        checkoutStage2 = CheckoutOverviewPage(driver)
        checkoutStage2.finish_checkout()

        # After checkout completed, return to products page
        checkOutCompleted = CheckoutCompletePage(driver)
        checkOutCompleted.back_home()

    @staticmethod
    def checkout_cheapest_item():
        driver = CheckoutTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CheckoutTests.STANDARD_USERNAME, CheckoutTests.PASSWORD_ALL)

        # Sort products by price lowest-highest
        productsPage = ProductsPage(driver)
        productsPage.sort_products_by_price_ascending()

        # add cheapest product to cart
        productsPage.add_item_to_cart_by_order(0)

        # Checkout
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.checkout()
        checkoutStage1 = CheckoutFirstStage(driver)
        checkoutStage1.fill_your_information_form('nate', 'dog', '91210')
        checkoutStage2 = CheckoutOverviewPage(driver)
        checkoutStage2.finish_checkout()

    @staticmethod
    def cancel_checkout_stage1():
        driver = CheckoutTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CheckoutTests.STANDARD_USERNAME, CheckoutTests.PASSWORD_ALL)

        # add an item to cart
        productsPage = ProductsPage(driver)
        productsPage.add_item_to_cart_by_order(0)

        # Checkout flow till step 1 [user info]
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.checkout()
        checkoutStage1 = CheckoutFirstStage(driver)

        #cancel checkout
        checkoutStage1.cancel_checkout()

    @staticmethod
    def cancel_checkout_stage2():
        driver = CheckoutTests.DRIVER

        # Login
        loginPage = LoginPage(driver)
        loginPage.goToLoginPage()
        loginPage.login(CheckoutTests.STANDARD_USERNAME, CheckoutTests.PASSWORD_ALL)

        # Add an item to cart
        productsPage = ProductsPage(driver)
        productsPage.add_item_to_cart_by_order(0)

        # Checkout Flow till step 2 [order overview]
        site_wide_ui = SiteWideUI(driver)
        site_wide_ui.click_on_shopping_cart_button()
        cartPage = CartPage(driver)
        cartPage.checkout()
        checkoutStage1 = CheckoutFirstStage(driver)
        checkoutStage1.fill_your_information_form('nate', 'dog', '91210')
        checkoutStage2 = CheckoutOverviewPage(driver)

        # Cancel checkout
        checkoutStage2.cancel_checkout()














