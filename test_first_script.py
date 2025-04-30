# pytest -v --tb=line test_first_script.py

import time
from .pages.base_page import BasePage


def test_guest_can_go_to_contacts_page(browser):
    link = "https://sbis.ru/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_contacts_block()
    page.click_contacts_block()
    # time.sleep(2)
    page.go_to_contacts_page()
    # time.sleep(10)

def test_guest_can_click_banner(browser):
    link = "https://saby.ru/contacts"
    page = BasePage(browser, link)
    page.open()
    # time.sleep(1000)
