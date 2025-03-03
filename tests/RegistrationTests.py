from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelpers
from pages.RegistrationPage import RegistrationPageHelper
import  allure

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка формы регистрации')
@allure.title('Проверка на совпадение кода страны со страной')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelpers(browser)
    LoginPage.click_registration_button()
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code