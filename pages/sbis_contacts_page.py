from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisContactsPageLocators


class SbisContactsPage(BasePage):
    def go_to_tensor(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.BANNER_TENSOR)
        )
        # Удаление аттрибута открытия нового окна на ссылке баннера
        self.browser.execute_script("arguments[0].removeAttribute('target')", element)
        element.click()

    def open_regions_list(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.REGION_NAME)
        )
        element.click()

    def should_be_banner_tensor(self):
        assert self.is_element_present(*SbisContactsPageLocators.BANNER_TENSOR), "Banner Tensor is not presented"

    def should_be_correct_region(self, expected_region):
        current_region = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.REGION_NAME)
        )
        assert current_region.text == expected_region, "Region name is not correct"

