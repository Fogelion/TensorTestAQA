from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except (NoSuchElementException):
    #         return False
    #     return True

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    def open(self):
        self.browser.get(self.url)




