from selenium.webdriver.common.by import By

class BasePageLocators():
    CONTACTS_BLOCK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) >"
                                       " div.sbisru-Header-ContactsMenu > div.sbisru-Header__menu-link")
    CONTACTS_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu > li.sbisru-Header__menu-item:nth-child(2) a.sbisru-link")