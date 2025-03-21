import allure
import random
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class RegistarionPageLocators:
    PHONE_FIELD = (By.XPATH, '//*[@id="field_phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistarionPageLocators.PHONE_FIELD)
            self.find_element(RegistarionPageLocators.COUNTRY_LIST)
            self.find_element(RegistarionPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistarionPageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistarionPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistarionPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].text
        country_items[random_number].click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistarionPageLocators.PHONE_FIELD).get_attribute('value')