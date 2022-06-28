from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.variables import Variables
from hamcrest import assert_that, equal_to


class SearchPage(BasePage):
    """
        This class is created for the search page elements and actions for ui tests
        Properties are defined for the elements in the page and each property waiting
        element could be clickable or visible
    """
    @property
    def search_bar(self):
        locator = (By.XPATH, Variables.search_bar_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def google_icon(self):
        locator = (By.XPATH, Variables.google_icon_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def accept_button(self):
        locator = (By.ID, Variables.accept_btn_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def search_button(self):
        locator = (By.XPATH, Variables.search_btn_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def search_result_url(self):
        locator = (By.XPATH, Variables.search_result_url_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def search_word(self, text):
        """
        This function is searching the text that user gives in the search bar.
        :param text: this variable is for the text that user want to search in the search bar.
        """
        try:
            self.accept_button.click()
        except NoSuchElementException:
            print("Already accepted")
        self.search_bar.input_text(text)
        self.search_button.click()
        assert_that(self.driver.find_elements_by_xpath(Variables.search_result_xpath)[0].text, equal_to("https://teknasyon.com"))

    def open_search_page(self, url):
        """
        This function opens the search page in the browser.
        :param url: URL of the search page
        """
        self.driver.get(url)
        assert_that(self.google_icon.attribute("alt"), equal_to("Google"))

    def go_to(self):
        """
        This function clicks the search result element
        """
        self.driver.find_elements_by_xpath(Variables.search_result_xpath)[0].click()
