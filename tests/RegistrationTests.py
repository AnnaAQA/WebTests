from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelpers
from pages.RegistrationPage import RegistrationPageHelperHelper
import  allure

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка формы регистрации')
@allure.title('Проверка на совпадение кода страны со страной')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelpers(browser)
    LoginPage.click_registration_button()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code