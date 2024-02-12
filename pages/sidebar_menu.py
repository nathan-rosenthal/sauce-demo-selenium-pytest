import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SideBarMenu(BasePage):

    SIDE_MENU_HAMBURGER_BUTTON = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    SIDEBAR_ALL_ITEMS_LINK = (By.CSS_SELECTOR, '#inventory_sidebar_link')
    SIDEBAR_ABOUT_LINK = (By.CSS_SELECTOR, '#about_sidebar_link')
    SIDEBAR_LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_sidebar_link')
    SIDEBAR_RESET_APP_STATE_LINK = (By.CSS_SELECTOR, '#reset_sidebar_link')

    def open_side_menu(self):
        self.click(self.SIDE_MENU_HAMBURGER_BUTTON)

    def click_all_items(self):
        self.open_side_menu()
        self.click(self.SIDEBAR_ALL_ITEMS_LINK)

    def click_about(self):
        self.open_side_menu()
        self.click(self.SIDEBAR_ABOUT_LINK)

    @allure.step("Logout from side menu")
    def click_logout(self):
        self.open_side_menu()
        self.click(self.SIDEBAR_LOGOUT_LINK)

    @allure.step("Reset App State from side menu")
    def click_reset_app_state(self):
        self.open_side_menu()
        self.click(self.SIDEBAR_RESET_APP_STATE_LINK)

    @allure.step("Test cleanup - Reset app state and logout")
    def reset_app_state_and_logout(self):
        self.open_side_menu()
        self.click(self.SIDEBAR_RESET_APP_STATE_LINK)
        self.click(self.SIDEBAR_LOGOUT_LINK)




