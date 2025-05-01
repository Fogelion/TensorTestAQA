# pytest -v --tb=line test_first_script.py

from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.tensor_main_page import TensorMainPage
from .pages.tensor_about_page import TensorAboutPage


def test_guest_can_go_to_contacts_page(browser):
    link = "https://sbis.ru/"
    page = SbisMainPage(browser, link)
    page.open()
    page.should_be_contacts_block()
    page.click_contacts_block()
    page.go_to_contacts_page()

def test_guest_can_click_banner(browser):
    link = "https://saby.ru/contacts"
    page = SbisContactsPage(browser, link)
    page.open()
    page.should_be_banner_tensor()
    page.go_to_tensor()
#
def test_should_be_power_in_people_block(browser):
    link = "https://tensor.ru/"
    page = TensorMainPage(browser, link)
    page.open()
    page.should_be_power_in_people_block()

def test_guest_can_click_people_about(browser):
    link = "https://tensor.ru/"
    page = TensorMainPage(browser, link)
    page.open()
    page.go_to_people_about()

def test_should_be_about_page(browser):
    link = "https://tensor.ru/"
    correct_url = "https://tensor.ru/about"
    page = TensorMainPage(browser, link)
    page.open()
    page.go_to_people_about()
    page.should_be_current_url(correct_url)

def test_should_be_same_size_images(browser):
    link = "https://tensor.ru/about"
    page = TensorAboutPage(browser, link)
    page.open()
    page.should_be_contacts_block()
    page.should_be_same_size_images()


