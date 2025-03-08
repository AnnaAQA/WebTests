from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelpers
import  allure

BASE_URL = 'https://ok.ru/'
EMAIL_TEXT = 'email'
PASSWORD_TEXT = 'psw'



@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к странице восстановления после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_auth_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_field_email_mobile(EMAIL_TEXT)

    for i in range(3):
        LoginPage.click_field_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelperHelpers(browser)