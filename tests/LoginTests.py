from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelpers

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
FIELD_TEXT_MOBILE = '9110008877'

def test_empty_login(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelpers(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelpers(browser)
    LoginPage.click_field_email_mobile(FIELD_TEXT_MOBILE)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR
