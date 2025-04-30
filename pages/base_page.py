import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_contacts_block(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(BasePageLocators.CONTACTS_BLOCK)
        )
        element.click()

    def go_to_contacts_page(self):
        link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(BasePageLocators.CONTACTS_LINK)
        )
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_contacts_block(self):
        assert self.is_element_present(*BasePageLocators.CONTACTS_BLOCK), "Contacts block is not presented"



