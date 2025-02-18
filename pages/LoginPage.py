from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    HOME_ENTER_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    HOME_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_LINK = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_LINK = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_LINK = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelpers(BasePage):
    pass



