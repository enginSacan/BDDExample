from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = "Mehmet Engin Sacan"


class BaseElement:

    """
        This class contains the web element properties such as location and
        which kind of selector could be used to get them.
    """
    def __init__(self, driver, by, value):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        )
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
