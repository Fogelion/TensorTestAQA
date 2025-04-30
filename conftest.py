from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser(request):
    browser = webdriver.Chrome
    print(f"\nstart browser")
    yield browser
    print("quit browser..")
    browser.quit()