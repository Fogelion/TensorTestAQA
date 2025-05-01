# pytest -v --tb=line test_first_script.py

from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.tensor_main_page import TensorMainPage
from .pages.tensor_about_page import TensorAboutPage


import time

# def test_guest_can_go_to_contacts_page(browser):
#     link = "https://sbis.ru/"
#     page = SbisMainPage(browser, link)
#     page.open()
#     page.should_be_contacts_block()
#     page.click_contacts_block()
#     page.go_to_contacts_page()
#
# def test_should_be_correct_region(browser):
#     link = "https://saby.ru/contacts"
#     correct_region = "Нижегородская обл."
#     page = SbisContactsPage(browser, link)
#     page.open()
#     page.should_be_correct_region(correct_region)

def test_guest_can_go_to_kamchatka(browser):
    link = "https://saby.ru/contacts"
    partners = []
    correct_region = "Камчатский край"
    page = SbisContactsPage(browser, link)
    page.open()
    partners = page.get_partners()
    page.open_regions_list()
    page.should_be_regions_list()
    page.choose_kamchatka()
    page.should_be_changes_region(correct_region)
    page.should_be_changes_partners(partners)
    # time.sleep(1)












# def test_should_be_kamchatka(browser):
#     link = "https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients"
#     correct_region = "Камчатский край"
#     page = SbisContactsPage(browser, link)
#     page.open()
#     page.should_be_correct_region(correct_region)