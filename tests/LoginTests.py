from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelpers
import  allure

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
FIELD_TEXT_MOBILE = '9110008877'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки, если не введен логин')
def test_empty_login(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelpers(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки, если не введен пароль')
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelpers(browser)
    LoginPage.click_field_email_mobile(FIELD_TEXT_MOBILE)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR
