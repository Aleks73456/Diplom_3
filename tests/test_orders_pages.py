from pages.orders_page import OrderPage
import allure






class TestOrderPage:

    
    @allure.title('Проверка оформления заказа')
    def test_profile(self,login_with_driver):
        order_page = OrderPage(login_with_driver)
        order_page.click_button_order_feed()
        order_page.click_button_constructor()
        order_page.click_burger_ingredient()
        order_page.click_button_close_modal_ingredient()
        order_page.set_burger_ingredient_in_ingredients_bascet()
        counter = order_page.check_counter_burger_ingredient()
        counter == '2'
        order_page.click_button_order()
        modal_order = order_page.check_modal_order()
        assert modal_order.is_displayed()

    
