import time
import allure
import locators.password_forgot_page_locators as loc
from pages.base_page import BasePage

class PasswordForgotPage(BasePage):

    
    @allure.step('нажимаем на кнопку "Восстановить пароль"')
    def click_button_forgot_password(self):
        time.sleep(3)
        self.click(loc.button_forgot_password)
        

    @allure.step('вводим email')
    def set_email_text(self,email):
        self.set_text(loc.email_field,email)
        
    
    @allure.step('нажимаем на кнопку "Восстановить"')
    def click_button_type_primary(self):
        self.click(loc.button_type_primary)
        


    @allure.step('вводим пароль')
    def set_password_field(self,password):
        self.set_text(loc.password_field,password)

   
    @allure.step('нажимаем на кнопку глаза')
    def click_button_eye(self):
        self.click(loc.button_eye)


    @allure.step('возвращаем поле ввода пароля после клика на глаз')
    def check_password_field_after_click_eye(self):
        self.wait_for_visibility(loc.password_field_after_click_eye)
 