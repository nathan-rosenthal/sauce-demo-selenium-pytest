import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def goToPage(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)

    def clear_field_text(self, locator):
        self.driver.find_element(*locator).clear()

    def fill_text(self, locator, text):
        self.clear_field_text(locator)
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        time.sleep(1)
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def get_text(self, locator):
        try:
            return self.driver.find_element(*locator).text
        except Exception as error:
            print(error)

    def select_from_dropdown_by_value(self, locator, value):
        selector = self.driver.find_element(*locator)
        Select(selector).select_by_value(value)

    def click_item_from_elements_list_by_position(self, locator, item_position):
        time.sleep(1)
        list_items = self.driver.find_elements(*locator)
        list_items[item_position].click()

    def click_all_list_elements(self, locator):
        list_elements = self.driver.find_elements(*locator)
        for item in list_elements:
            item.click()

    def get_number_of_list_elements(self, locator):
        time.sleep(2)
        list_items = self.driver.find_elements(*locator)
        return len(list_items)

    def is_element_displayed(self, locator):
        time.sleep(2)
        is_element_displayed = False
        try:
            is_element_displayed = self.driver.find_element(*locator).is_displayed()
        except Exception as error:
            print({error})
        return is_element_displayed

    def is_element_enabled(self, locator):
        time.sleep(2)
        is_element_enabled = False
        try:
            is_element_displayed = self.driver.find_element(*locator).is_enabled()
        except Exception as error:
            print({error})
        return is_element_enabled

    def is_element_selected(self, locator):
        time.sleep(2)
        is_element_selected = False
        try:
            is_element_selected = self.driver.find_element(*locator).is_selected()
        except Exception as error:
            print({error})
        return is_element_selected

    def get_list_of_elements_text(self, locator):
        list_elements = self.driver.find_elements(*locator)
        price_list = []
        for element in list_elements:
            price_list.append(element.text)
        return price_list






