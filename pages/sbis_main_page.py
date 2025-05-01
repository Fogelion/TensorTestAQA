from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisMainPagePageLocators


class SbisMainPage(BasePage):

    def click_contacts_block(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPagePageLocators.CONTACTS_BLOCK)
        )
        element.click()

    def go_to_contacts_page(self):
        link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPagePageLocators.CONTACTS_LINK)
        )
        link.click()

    def should_be_contacts_block(self):
        assert self.is_element_present(*SbisMainPagePageLocators.CONTACTS_BLOCK), "Contacts block is not presented"