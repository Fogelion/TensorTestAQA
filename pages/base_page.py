import os
import time
from pathlib import Path
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.download_dir = str(Path(__file__).parent.parent / "downloads")

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    def open(self):
        self.browser.get(self.url)

    def should_be_current_url(self, expected_url, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.url_to_be(expected_url),
            message=f"Expected URL {expected_url}, not current URL {self.browser.current_url}"
        )

    def wait_for_download_plugin(self, filename, timeout=20):
        file_path = os.path.join(self.download_dir, filename)
        end_time = time.time() + timeout
        while time.time() < end_time:
            if os.path.exists(file_path):
                if not filename.endswith('.crdownload') and not filename.endswith('.tmp'):
                    return
            time.sleep(1)
        raise TimeoutError("Plugin does not download in time")

    def clear_downloads_dir(self):
        for file in os.listdir(self.download_dir):
            file_path = os.path.join(self.download_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception:
                print("File cannot be deleted")