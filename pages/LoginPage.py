import allure

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
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelpers(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.EMAIL_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.HOME_ENTER_TAB)
        self.find_element(LoginPageLocators.HOME_QR_TAB)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.RECOVERY_LINK)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_LINK)
        self.find_element(LoginPageLocators.MAIL_LINK)
        self.find_element(LoginPageLocators.YANDEX_LINK)

    @allure.step('Кликаем на кнопку Войти в Одноклассники')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Вводим в поле ввода валидный номер телефона')
    def click_field_email_mobile(self, value=None):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(value)