from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import allure
import locators.password_forgot_page_locators as loc

class PasswordForgotPage:

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('нажимаем на кнопку "Восстановить пароль"')
    def click_button_forgot_password(self):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.button_forgot_password))
        time.sleep(3)
        self.driver.find_element(*loc.button_forgot_password).click()

    @allure.step('вводим email')
    def set_email_text(self,email):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(loc.email_field))
        self.driver.find_element(*loc.email_field).send_keys(email)
    
    @allure.step('нажимаем на кнопку "Восстановить"')
    def click_button_type_primary(self):
        self.driver.find_element(*loc.button_type_primary).click()


    @allure.step('вводим пароль')
    def set_password_field(self,password):
        WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(loc.password_field)) 
        self.driver.find_element(*loc.password_field).send_keys(password)
   
    @allure.step('нажимаем на кнопку глаза')
    def click_button_eye(self):
        self.driver.find_element(*loc.button_eye).click()

    @allure.step('возвращаем поле ввода пароля после клика на глаз')
    def check_password_field_after_click_eye(self):
        return self.driver.find_element(*loc.password_field_after_click_eye)