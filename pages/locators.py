from selenium.webdriver.common.by import By

class SbisMainPageLocators():
    CONTACTS_BLOCK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) >"
                                       " div.sbisru-Header-ContactsMenu > div.sbisru-Header__menu-link")
    CONTACTS_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) a.sbisru-link")
    DOWNLOAD_LINK = (By.XPATH, "//*[contains(@class, 'sbisru-Footer__link') and"
                                     " contains(., 'Скачать локальные версии')]")

class SbisContactsPageLocators():
    BANNER_TENSOR = (By.CSS_SELECTOR, "#contacts_clients a.sbisru-Contacts__logo-tensor")
    REGION_NAME = (By.CSS_SELECTOR, ".sbisru-Contacts__relative span.sbis_ru-Region-Chooser__text.sbis_ru-link")
    REGIONS_LIST = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel__header-text")
    REGION_KAMCHATKA = (By.CSS_SELECTOR, "[title='Камчатский край']")
    PARTNER_NAME = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name")

class SbisDownloadPageLocators():
    SABY_PLUGIN_SECTION = (By.XPATH, "//*[contains(@class, 'controls-TabButton__caption') and"
                                     " contains(., 'Saby Plugin')]")
    SABY_PLUGIN_WINDOWS_SECTION = (By.XPATH, "//*[contains(@class, 'sbis_ru-DownloadNew-innerTabs__title') and"
                                     " contains(., 'Windows')]")
    SABY_PLUGIN_DOWNLOAD_WEB = (By.XPATH, "//a[contains(@class, 'sbis_ru-DownloadNew-loadLink__link') and"
                                          " contains(text(), 'Скачать (Exe')]")

class TensorMainPageLocators():
    POWER_BLOCK = (By.XPATH, "//*[contains(@class, 'tensor_ru-Index__card-title') and contains(., 'Сила в людях')]")
    PEOPLE_ABOUT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg a.tensor_ru-link")

class TensorAboutPageLocators():
    WORK_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-About__block3")
    WORK_IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image")