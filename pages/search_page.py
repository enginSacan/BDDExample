from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.variables import Variables
from hamcrest import assert_that, equal_to


class SearchPage(BasePage):

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
        try:
            self.accept_button.click()
        except NoSuchElementException:
            print("Already accepted")
        self.search_bar.input_text(text)
        self.search_button.click()
        assert_that(self.driver.find_elements_by_xpath(Variables.search_result_xpath)[0].text, equal_to("https://teknasyon.com"))

    def open_search_page(self, url):
        self.driver.get(url)
        assert_that(self.google_icon.attribute("alt"), equal_to("Google"))

    def go_to(self):
        self.driver.find_elements_by_xpath(Variables.search_result_xpath)[0].click()
