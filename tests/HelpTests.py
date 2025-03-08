from core.BaseTest import browser
from pages.AdvertisingCabinetHelp import AdvertisingCabinetHelpHelpers
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelpers, HelpPageLocators
import  allure

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка скролла')
@allure.title('Проверка скролла до Рекламного кабинета')
def test_empty_login(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelpers(browser)
    HelpPage.scrollToElement(HelpPageLocators.ADVERTISING_CABINET)
    AdvertisingCabinetHelpHelpers(browser)