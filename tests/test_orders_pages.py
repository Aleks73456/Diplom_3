from selenium import webdriver
from pages.orders_page import OrderPage
import helpers
import allure
from helpers import BASE_URL





class TestOrderPage:

    
    @allure.title('Проверка оформления заказа')
    def test_profile(self,driver):
        driver.get(f'{BASE_URL}/login')
        user = helpers.regist_user_for_login_and_get_token()
        helpers.login(driver, user["email"], user["password"])
        order_page = OrderPage(driver)
        order_page.click_button_order_feed()
        order_page.click_button_constructor()
        order_page.click_burger_ingredient()
        order_page.click_button_close_modal_ingredient()
        order_page.set_burger_ingredient_in_ingredients_bascet()
        counter = order_page.check_counter_burger_ingredient()
        assert counter.text == '2'
        order_page.click_button_order()
        modal_order = order_page.check_modal_order()
        assert modal_order.is_displayed()
        helpers.delete_user(user["accessToken"])

    
