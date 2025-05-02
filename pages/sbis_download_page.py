import time
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisDownloadPageLocators


class SbisDownloadPage(BasePage):
    def click_to_download_web_plugin(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisDownloadPageLocators.SABY_PLUGIN_DOWNLOAD_WEB)
        )
        element.click()

    def should_be_saby_plugin_section(self):
        assert self.is_element_present(*SbisDownloadPageLocators.SABY_PLUGIN_SECTION), "Saby Plugin is not selected"

    def should_be_saby_plugin_windows_section(self):
        assert self.is_element_present(*SbisDownloadPageLocators.SABY_PLUGIN_WINDOWS_SECTION), "Saby Plugin for Windows is not selected"