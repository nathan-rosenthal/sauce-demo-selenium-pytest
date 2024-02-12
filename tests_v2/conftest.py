# instantiate driver object before running tests in class
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.product_item_page import ProductItemPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_1_page import CheckoutFirstStage
from pages.checkout_step_2_page import CheckoutOverviewPage
from pages.sidebar_menu import SideBarMenu
from pages.sitewide_ui import SiteWideUI
import allure

STANDARD_USERNAME = 'standard_user'
PASSWORD_ALL = 'secret_sauce'


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish() -> None:
    environment_properties = {
        'browser': driver.name,
        'browser_version': driver.capabilities['browserVersion'],
        'platform_name': driver.capabilities['platformName']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    request.cls.driver = driver
    driver.maximize_window()
    yield
    # Teardown - close browser and shutdown driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def page_objects():
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    site_wide_ui = SiteWideUI(driver)
    cart_page = CartPage(driver)
    side_bar_menu = SideBarMenu(driver)
    product_item_page = ProductItemPage(driver)
    checkout_stage_1 = CheckoutFirstStage(driver)
    checkout_stage_2 = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    return {
        "login_page": login_page,
        "products_page": products_page,
        "product_item_page": product_item_page,
        "cart_page": cart_page,
        "checkout_stage_1": checkout_stage_1,
        "checkout_stage_2": checkout_stage_2,
        "checkout_complete_page": checkout_complete_page,
        "site_wide_ui": site_wide_ui,
        "side_bar_menu": side_bar_menu
    }


@pytest.fixture(scope="function", autouse=True)
def login(request, page_objects):
    # Get marker named 'exclude_login' associated to test function.
    # If marker found, variable is set to true (is not None - value is not absent)
    exclude_login = request.node.get_closest_marker("exclude_login") is not None
    exclude_logout = request.node.get_closest_marker("exclude_logout") is not None

    # Login as standard user unless test contains its own login flow
    if not exclude_login:
        page_objects["login_page"].login(STANDARD_USERNAME, PASSWORD_ALL)
    yield
    # App Teardown - Reset App State & Logout at the end of each test that did login
    if not exclude_logout:
        page_objects["side_bar_menu"].reset_app_state_and_logout()
