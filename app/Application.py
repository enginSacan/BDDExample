from pages.search_page import SearchPage
from pages.company_page import CompanyPage
from pages.career_page import CareerPage
from pages.job_page import JobPage

__author__ = "Mehmet Engin Sacan"


class Application:
    """
    This class constructing the pages for the application
    """
    def __init__(self, driver):
        self.search_page = SearchPage(driver)
        self.company_page = CompanyPage(driver)
        self.career_page = CareerPage(driver)
        self.job_page = JobPage(driver)

