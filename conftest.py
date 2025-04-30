import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    print(f"\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser..")
    browser.quit()