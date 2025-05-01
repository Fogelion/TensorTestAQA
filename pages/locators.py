from selenium.webdriver.common.by import By

class SbisMainPageLocators():
    CONTACTS_BLOCK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) >"
                                       " div.sbisru-Header-ContactsMenu > div.sbisru-Header__menu-link")
    CONTACTS_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) a.sbisru-link")

class SbisContactsPageLocators():
    BANNER_TENSOR = (By.CSS_SELECTOR, "#contacts_clients a.sbisru-Contacts__logo-tensor")

class TensorMainPageLocators():
    # POWER_BLOCK = (By.XPATH, "//p[@class='tensor_ru-Index__card-title' and contains(text(), 'Сила в людях')]")
    POWER_BLOCK = (By.XPATH, "//*[contains(@class, 'tensor_ru-Index__card-title') and contains(., 'Сила в людях')]")
    # POWER_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title")