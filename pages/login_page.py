import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.sidebar_menu import SideBarMenu


class LoginPage(BasePage):
    USERNAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    ERROR_MESSAGE_CONTAINER = (By.CSS_SELECTOR, '.error-message-container')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Go to login page")
    def goToLoginPage(self):
        self.goToPage('https://www.saucedemo.com/')

    @allure.step("Fill Login form with username and password")
    def fillLoginForm(self, username, password):
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)

    @allure.step("Click login Button")
    def clickLoginButton(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Go to Login Page and complete login flow")
    def login(self, username, password):
        self.goToLoginPage()
        self.fillLoginForm(username, password)
        self.clickLoginButton()

    @allure.step("Check that user is logged in - Side menu button is present")
    def is_login_success(self):
        sideBarMenu = SideBarMenu(self)
        return self.is_element_displayed(sideBarMenu.SIDE_MENU_HAMBURGER_BUTTON)

    def getLoginErrorText(self):
        return self.get_text(self.ERROR_MESSAGE_CONTAINER)
