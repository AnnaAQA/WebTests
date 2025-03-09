import  allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKprojectsPage import VKprojectsPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка toolbar')
@allure.title('Проверка перехода к проектам ВК')
def test_open_vk_projects(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_ecosystem()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window_id)
    VKprojectsPage = VKprojectsPageHelper(browser)
    VKprojectsPage.switch_window(current_window_id)
    LoginPageHelper(browser)