import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_BUTTON = (By.ID, 'nohook_logo_link')
    VK_SERVICES_BUTTON = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.VK_SERVICES_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f'Не удалось найти элемент{locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f'Не удалось найти элементы{locator}')

    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step('Нажимаем на кнопку Сервисы ВК')
    def click_vk_ecosystem(self):
        self.find_element(BasePageLocators.VK_SERVICES_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Еще"')
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()