import allure
from selenium.webdriver import ActionChains
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HelpPageLocators:
    SEARCH_INPUT = (By.XPATH, '//*[@data-tsid="help_search_input"]')
    TODAY_ACTUAL = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    ACCESS_TO_PROFILE = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAID_FUNCTIONS = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES_APPS = (By.XPATH, '//a[contains(@href, "igry-i-prilojeniya")]')
    OTHER_SERVICES = (By.XPATH, '//a[contains(@href, "drugie-servisy")]')
    USEFUL_INFO = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISING_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelpers(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_INPUT)
        self.find_element(HelpPageLocators.TODAY_ACTUAL)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.ACCESS_TO_PROFILE)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAID_FUNCTIONS)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.USEFUL_INFO)
        self.find_element(HelpPageLocators.ADVERTISING_CABINET)

    def scrollToElement(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
