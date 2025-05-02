import pytest
from selenium import webdriver
from pathlib import Path
import os


project_dir = Path(__file__).parent
download_directory = str(project_dir / "downloads")
os.makedirs(download_directory, exist_ok=True)

@pytest.fixture(scope="session")
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
        "profile.default_content_settings.popups": 0,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    print("\nstart Browser")
    browser = webdriver.Chrome(options=chrome_options)
    browser.execute_cdp_cmd(
        "Page.setDownloadBehavior",
        {
            "behavior": "allow",
            "downloadPath": download_directory
        }
    )

    yield browser
    print("quit browser..")
    browser.quit()