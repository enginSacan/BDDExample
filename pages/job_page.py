import time


from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.variables import Variables


class JobPage(BasePage):
    """
        This class is created for the job page elements and actions for ui tests
        Properties are defined for the elements in the page and each property waiting
        element could be clickable or visible
    """
    @property
    def apply_title(self):
        locator = (By.XPATH, Variables.apply_title_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def error_surname(self):
        locator = (By.ID, Variables.error_surname_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def error_email(self):
        locator = (By.ID, Variables.error_email_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def error_file(self):
        locator = (By.ID, Variables.error_file_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def error_let(self):
        locator = (By.ID, Variables.error_let_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def error_captcha(self):
        locator = (By.ID, Variables.error_captcha_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def apply_title(self):
        locator = (By.XPATH, Variables.apply_title_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def submit_button(self):
        locator = (By.XPATH, Variables.submit_btn_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def surname_field(self):
        locator = (By.ID, Variables.surname_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def email_field(self):
        locator = (By.ID, Variables.email_id)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def captcha_box_checkmark(self):
        locator = (By.XPATH, Variables.captcha_box_checkmark_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def captcha_box(self):
        locator = (By.XPATH, Variables.captcha_box_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    @property
    def successful_message(self):
        locator = (By.XPATH, Variables.successful_message_xpath)
        return BaseElement(self.driver, locator[0], locator[1])

    def check_error_messages(self):
        """
            This method is asserting the error messages related with the application form for job.
        """
        assert_that(self.apply_title.text, equal_to("Başvuru Formu"))
        time.sleep(1)
        self.submit_button.click()
        assert_that(self.error_surname.text, equal_to("Bu alanın doldurulması zorunludur."))
        assert_that(self.error_email.text, equal_to("Bu alanın doldurulması zorunludur."))
        assert_that(self.error_file.text, equal_to("Bu alanın doldurulması zorunludur."))
        assert_that(self.error_let.text, equal_to("CV'nizi bizimle paylaşmadan önce, Aydınlatma Metni’ni okuyup, kutucuğu işaretlemeniz gerekmektedir."))
        assert_that(self.error_captcha.text, equal_to("Lütfen recaptcha doğrulamasını yapınız."))

    def fill_all_form(self):
        """
            This method is asserting that uploading resume of the user works fine.
        """
        self.surname_field.input_text(Variables.surname)
        self.email_field.input_text(Variables.email)
        self.driver.find_element_by_id(Variables.file_upload_id).send_keys("C:\\Users\\z003f2nt\\Downloads\\CV.pdf")
        self.driver.find_elements_by_xpath(Variables.check_boxes_xpath)[0].click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, Variables.error_let_id)))
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-border']"))).click()
        self.driver.switch_to.default_content()
        self.submit_button.click()
        assert_that(self.successful_message.text, equal_to("Başvurunuz alınmıştır."))


