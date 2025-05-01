from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def should_be_same_size_images(self):
        images = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located(TensorAboutPageLocators.WORK_IMAGES))
        sizes = []
        for img in images:
            width = img.get_attribute('width')
            height = img.get_attribute('height')
            sizes.append((int(width), int(height)))
        unique_sizes = set(sizes)
        assert len(unique_sizes) == 1, "Images with different sizes"

    def should_be_contacts_block(self):
        assert self.is_element_present(*TensorAboutPageLocators.WORK_BLOCK), "Work block is not presented"