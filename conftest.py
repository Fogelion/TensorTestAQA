import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    print(f"\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser..")
    browser.quit()
