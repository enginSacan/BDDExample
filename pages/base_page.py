__author__ = "Mehmet Engin Sacan"


class BasePage:

    """
        This page class is the initialization of the webdriver
    """
    def __init__(self, driver):
        self.driver = driver
