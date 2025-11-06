from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import allure
import locators.profile_page_locators as loc


class ProfilePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('вводим email')
    def click_email_field(self,email):
        self.driver.find_element(*loc.email_field).send_keys(email)
    
    @allure.step('вводим пароль')
    def click_password_field(self,password):
        self.driver.find_element(*loc.password_field).send_keys(password)

    @allure.step('нажимаем "войти"')
    def click_button_login(self):
        self.driver.find_element(*loc.button_login).click()
    
    @allure.step('входим в профиль')
    def click_button_profile(self):
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.button_profile))
        self.driver.find_element(*loc.button_profile).click()
    
    @allure.step('открываем вкладку с историей заказов')
    def click_button_history_profile(self):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.button_history_profile))
        time.sleep(3)
        self.driver.find_element(*loc.button_history_profile).click()
    
    @allure.step('выходим из аккаунта')
    def click_button_exit(self):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.button_exit))
        self.driver.find_element(*loc.button_exit).click()

    @allure.step('возвращаем форму авторизации')
    def check_auth_form(self):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.visibility_of_element_located(loc.auth_form))
        return self.driver.find_element(*loc.auth_form)
    
    