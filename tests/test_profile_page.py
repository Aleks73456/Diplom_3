from selenium import webdriver
from pages.profile_page import ProfilePage
import helpers
import allure
from helpers import BASE_URL


class TestProfilePage:

    
       
    
    @allure.title('Проверка работы личного кабинета')
    def test_profile(self,driver):
        driver.get(f'{BASE_URL}/login')
        user = helpers.regist_user_for_login_and_get_token()
        helpers.login(driver, user["email"], user["password"])
        profile_page = ProfilePage(driver)
        profile_page.click_button_profile()
        profile_page.click_button_history_profile()
        profile_page.click_button_exit()
        expected_result = profile_page.check_auth_form()
        assert expected_result.is_displayed()
        helpers.delete_user(user["accessToken"])
        
        


