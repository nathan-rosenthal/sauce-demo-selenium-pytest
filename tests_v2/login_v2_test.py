import allure
import pytest
from allure_commons.types import Severity


@allure.epic("Authorization & Authentication")
@allure.feature("Login")
class TestLogin:
    STANDARD_USERNAME = 'standard_user'
    LOCKED_OUT_USERNAME = 'locked_out_user'
    PROBLEM_USERNAME = 'problem_user'
    PERFORMANCE_GLITCH_USERNAME = 'performance_glitch_user'
    ERROR_USERNAME = 'error_user'
    VISUAL_USERNAME = 'visual_user'
    PASSWORD_ALL = 'secret_sauce'

    @allure.severity(Severity.BLOCKER)
    @allure.description("Log in with standard user credentials and check user is logged in")
    @allure.title("Login as a Standard User")
    @allure.story("As a regular user, i should be able to log in to the application")
    @pytest.mark.exclude_login
    def test_login_standard_user(self, page_objects):
        # Navigate to login page, and login
        page_objects["login_page"].login(TestLogin.STANDARD_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is logged in - menu element displayed
        assert page_objects["login_page"].is_login_success(), "Element is not displayed for logged in user state"

    @pytest.mark.exclude_login
    @pytest.mark.exclude_logout
    @allure.severity(Severity.CRITICAL)
    @allure.story("As a Locked out user, i should be prevented from login to the application")
    def test_login_locked_out_user(self, page_objects):
        # Navigate to login page, and login
        page_objects["login_page"].login(self.LOCKED_OUT_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is not logged in - Locked out error message displayed
        locked_out_error_phrase = 'user has been locked out'
        actual_error_text = page_objects["login_page"].getLoginErrorText()
        allure.attach(body=actual_error_text, name="Error Message text", attachment_type=allure.attachment_type.TEXT)
        assert locked_out_error_phrase in actual_error_text, f"Error message is incorrect or not displayed: {actual_error_text}"
        # allure.attach(body=self.driver.get_screenshot_as_png(), name="screenshot test", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.exclude_login
    @allure.severity(Severity.NORMAL)
    @allure.story("As a problem user, i should be able to log in to the application")
    def test_login_problem_user(self, page_objects):
        # Navigate to login page, and login
        # allure.attach(body="HELLO WORLD!!!!!", name="Attachment POC", attachment_type=allure.attachment_type.TEXT)
        page_objects["login_page"].login(TestLogin.PROBLEM_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is logged in - menu element displayed
        assert page_objects["login_page"].is_login_success(), "Element is not displayed for logged in user state"

    @pytest.mark.exclude_login
    @allure.severity(Severity.NORMAL)
    @allure.story("As a performance glitch user, i should be able to log in to the application")
    def test_login_performance_glitch_user(self, page_objects):
        # Navigate to login page, and login
        page_objects["login_page"].login(TestLogin.PERFORMANCE_GLITCH_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is logged in - menu element displayed
        assert page_objects["login_page"].is_login_success(), "Element is not displayed for logged in user state"

    @pytest.mark.exclude_login
    @allure.severity(Severity.NORMAL)
    @allure.story("As an error user, i should be able to log in to the application")
    def test_login_error_user(self, page_objects):
        # Navigate to login page, and login
        page_objects["login_page"].login(TestLogin.ERROR_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is logged in - menu element displayed
        assert page_objects["login_page"].is_login_success(), "Element is not displayed for logged in user state"

    @pytest.mark.exclude_login
    @allure.severity(Severity.MINOR)
    @allure.story("As a visual user, i should be able to log in to the application")
    def test_login_visual_user(self, page_objects):
        # Navigate to login page, and login
        page_objects["login_page"].login(TestLogin.VISUAL_USERNAME, TestLogin.PASSWORD_ALL)
        # Check user is logged in - menu element displayed
        assert page_objects["login_page"].is_login_success(), "Element is not displayed for logged in user state"
