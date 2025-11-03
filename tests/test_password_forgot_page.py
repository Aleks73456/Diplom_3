from selenium import webdriver
from pages.password_forgot_page import PasswordForgotPage
from helpers import BASE_URL
import allure


class TestPasswordForgotPage:


    @staticmethod
    def getwebdriver(browserName):
       if browserName == "firefox":
           return webdriver.Firefox()
       elif browserName == "chrome":
           return webdriver.Chrome()
       

    @classmethod
    def setup_class(cls):
        cls.driver = cls.getwebdriver("chrome")
       

    
    @allure.title('Проверка восстановления пароля')
    def test_password_forgot(self):
        self.driver.get(f'{BASE_URL}/login')
        password_forgot_page = PasswordForgotPage(self.driver)
        password_forgot_page.click_button_forgot_password()
        password_forgot_page.set_email_text('aser@mail.ru')
        password_forgot_page.click_button_type_primary()
        password_forgot_page.set_password_field('testiksss')
        password_forgot_page.click_button_eye()
        expected_result = password_forgot_page.check_password_field_after_click_eye()
        assert expected_result.is_displayed()
        


    classmethod
    def teardown_class(cls):
        cls.driver.quit()