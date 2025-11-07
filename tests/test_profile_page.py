from pages.profile_page import ProfilePage
import allure


class TestProfilePage:

    
       
    
    @allure.title('Проверка работы личного кабинета')
    def test_profile(self,login_with_driver):
        driver = login_with_driver
        profile_page = ProfilePage(driver)
        profile_page.click_button_profile()
        profile_page.click_button_history_profile()
        profile_page.click_button_exit()
        expected_result = profile_page.check_auth_form()
        assert expected_result.is_displayed()

        
        


