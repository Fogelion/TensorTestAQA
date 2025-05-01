from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
# from .locators import TensorAboutPageLocators

class TensorAboutPage(BasePage):
    def should_be_tensor_about_page(self):
        expected_url = "https://tensor.ru/about"
        pass