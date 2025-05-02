# pytest -v --tb=line test_first_script.py

from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_download_page import SbisDownloadPage


# def test_guest_can_go_download_page(browser):
#     link = "https://sbis.ru/"
#     page = SbisMainPage(browser, link)
#     page.open()
#     page.should_be_download_page_link()
#     page.go_to_download_page()

def test_guest_can_download_web_installer(browser):
    link = "https://saby.ru/download"
    page = SbisDownloadPage(browser, link)
    page.open()
    page.should_be_saby_plugin_section()
    page.should_be_saby_plugin_windows_section()
    # page.click_to_download_web_plugin()