import time
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import SbisContactsPageLocators


class SbisContactsPage(BasePage):
    def get_partners(self):
        partners_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(SbisContactsPageLocators.PARTNER_NAME)
        )
        partners = [name.text for name in partners_element]
        return partners

    def choose_kamchatka(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.REGION_KAMCHATKA)
        )
        time.sleep(0.5)
        element.click()

    def go_to_tensor(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.BANNER_TENSOR)
        )
        # Удаление аттрибута открытия нового окна на ссылке баннера
        self.browser.execute_script("arguments[0].removeAttribute('target')", element)
        element.click()

    def open_regions_list(self):
        attempts = 0
        while attempts < 3:
            try:
                region = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located(SbisContactsPageLocators.REGION_NAME))
                region.click()
                return
            except StaleElementReferenceException:
                attempts += 1
                time.sleep(1)
        raise Exception("Regions list does not opened after 3 times")

    def should_be_banner_tensor(self):
        assert self.is_element_present(*SbisContactsPageLocators.BANNER_TENSOR), "Banner Tensor is not presented"

    def should_be_changes_partners(self, expected_partners):
        partners_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(SbisContactsPageLocators.PARTNER_NAME)
        )
        partners = [name.text for name in partners_element]
        assert partners != expected_partners, "Partners names does not change"

    def should_be_changes_region(self, expected_region):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.text_to_be_present_in_element(SbisContactsPageLocators.REGION_NAME, expected_region)
            )
        except TimeoutException:
            raise AssertionError("Region name does not changes")

    def should_be_correct_region(self, expected_region):
        current_region = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(SbisContactsPageLocators.REGION_NAME)
        )
        assert current_region.text == expected_region, "Region name is not correct"

    def should_be_correct_region_title(self, expected_region_title):
        current_region_title = self.browser.title
        assert expected_region_title in current_region_title, "Region title is not correct"

    def should_be_correct_region_url(self, expected_region_url):
        current_region_url = self.browser.current_url
        assert expected_region_url in current_region_url, "Region url is not correct"

    def should_be_regions_list(self):
        assert self.is_element_present(*SbisContactsPageLocators.REGIONS_LIST), "Regions list is not presented"