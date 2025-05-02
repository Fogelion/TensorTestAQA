from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def click_contacts_block(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPageLocators.CONTACTS_BLOCK)
        )
        element.click()

    def go_to_contacts_page(self):
        link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPageLocators.CONTACTS_LINK)
        )
        link.click()

    def go_to_download_page(self):
        link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisMainPageLocators.DOWNLOAD_LINK)
        )
        link.click()

    def should_be_contacts_block(self):
        assert self.is_element_present(*SbisMainPageLocators.CONTACTS_BLOCK), "Contacts block is not presented"

    def should_be_download_page_link(self):
        assert self.is_element_present(*SbisMainPageLocators.DOWNLOAD_LINK), "Download local link is not presented"