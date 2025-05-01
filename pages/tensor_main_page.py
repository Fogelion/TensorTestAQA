from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import TensorMainPageLocators

class TensorMainPage(BasePage):
    def should_be_power_in_people_block(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_BLOCK), "Power in people block is not presented"