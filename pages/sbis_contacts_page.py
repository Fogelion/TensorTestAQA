from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisContactsPagePageLocators


class SbisContactsPage(BasePage):

    def click_banner_tensor(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPagePageLocators.BANNER_TENSOR)
        )
        element.click()

    def should_be_banner_tensor(self):
        assert self.is_element_present(*SbisContactsPagePageLocators.BANNER_TENSOR), "Banner Tensor is not presented"

