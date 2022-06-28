from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.variables import Variables
from hamcrest import assert_that, equal_to


class CompanyPage(BasePage):
    """
        This class is created for the company page elements and actions for ui tests
        Properties are defined for the elements in the page and each property waiting
        element could be clickable or visible

        Methods ,which start with check, are the assertion functions
        Method starts with click contain click actions
    """
    @property
    def company_logo(self):
        locator = (By.XPATH, Variables.company_logo_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def career_page_link(self):
        locator = (By.XPATH, Variables.career_link_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def check_company_page_loaded(self):
        assert_that(self.company_logo.text, equal_to("Teknasyon"))

    def check_career_button(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        assert_that(self.career_page_link.text, equal_to("Kariyer"))

    def click_page(self, page):
        if page in "career":
            self.career_page_link.click()
