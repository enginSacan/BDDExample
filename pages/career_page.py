import time

from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.variables import Variables

__author__ = "Mehmet Engin Sacan"


class CareerPage(BasePage):
    """
        This class is created for the career page elements and actions for ui tests
        Properties are defined for the elements in the page and each property waiting
        element could be clickable or visible.

        Methods ,which start with check, are the assertion functions

    """
    @property
    def description(self):
        locator = (By.XPATH, Variables.description_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def apply_button(self):
        locator = (By.XPATH, Variables.apply_btn_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def job_title(self):
        locator = (By.XPATH, Variables.job_title_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def check_description(self):
        return "Kodluyoruz" in self.description.text

    def choose_job(self, job):
        """
         This function is choosing the job that is given as parameter.
        :param job: This variable is given by user for job title search
        """
        jobs = self.driver.find_elements_by_xpath(Variables.jobs_xpath)
        time.sleep(1)
        for job_found in jobs:
            if job_found.get_attribute("title") in job:
                job_found.click()
                self.check_job_title(job)
                time.sleep(1)
                self.apply_button.click()
                break

    def check_job_title(self, title):
        assert_that(self.job_title.text, equal_to(title))
