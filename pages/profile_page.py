import time
import allure
import locators.profile_page_locators as loc
from pages.base_page import BasePage


class ProfilePage(BasePage):
    
    
    @allure.step('вводим email')
    def click_email_field(self,email):
        self.set_text(loc.email_field,email)
    
    @allure.step('вводим пароль')
    def click_password_field(self,password):
        self.set_text(loc.password_field,password)

    @allure.step('нажимаем "войти"')
    def click_button_login(self):
        self.click(loc.button_login)
    
    
    @allure.step('входим в профиль')
    def click_button_profile(self):
        time.sleep(3)
        self.click(loc.button_profile)
        
    
    @allure.step('открываем вкладку с историей заказов')
    def click_button_history_profile(self):
        time.sleep(3)
        self.click(loc.button_history_profile)

    
    @allure.step('выходим из аккаунта')
    def click_button_exit(self):
        self.click(loc.button_exit)


    @allure.step('возвращаем форму авторизации')
    def check_auth_form(self):
        return self.wait_for_visibility(loc.auth_form)
    
    