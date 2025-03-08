import  allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelpers
from pages.VKprojectsPage import VKprojectsPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка toolbar')
@allure.title('Проверка перехода к проектам ВК')
def test_open_vk_projects(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelperHelpers(browser)
    LoginPage.click_vk_ecosystem()
    LoginPage.click_more_button()
    VKprojectsPageHelper(browser)