# pytest -v --tb=line test_first_script.py

import time
from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage


def test_guest_can_go_to_contacts_page(browser):
    link = "https://sbis.ru/"
    page = SbisMainPage(browser, link)
    page.open()
    page.should_be_contacts_block()
    page.click_contacts_block()
    page.go_to_contacts_page()
    # time.sleep(10)

def test_guest_can_click_banner(browser):
    link = "https://saby.ru/contacts"
    page = SbisContactsPage(browser, link)
    page.open()
    page.should_be_banner_tensor()
    page.click_banner_tensor()
    # time.sleep(1000)
