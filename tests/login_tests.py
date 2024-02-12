from selenium import webdriver

from pages.login_page import LoginPage


class LoginTests:
    DRIVER = webdriver.Chrome()
    STANDARD_USERNAME = 'standard_user'
    PASSWORD_ALL = 'secret_sauce'

    @staticmethod
    def login_standard_user(self, ):
        # Navigate to login page, and login
        loginPage = LoginPage(LoginTests.DRIVER)
        loginPage.goToLoginPage()
        loginPage.login(LoginTests.STANDARD_USERNAME, LoginTests.PASSWORD_ALL)