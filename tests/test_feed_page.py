from pages.feed_page import FeedPage
import helpers
import allure


class TestFeedPages:
    
    
    @allure.title('Проверка ленты заказов')
    def test_feed_page(self,login_with_driver):
        driver = login_with_driver
        feed_page = FeedPage(driver)
        feed_page.click_button_feed()
        feed_page.click_button_feed_order()
        order_details = feed_page.check_modal_order()
        assert order_details.is_displayed()
        feed_page.click_button_close_order_in_history()
        all_time_before_order = feed_page.check_order_feed_number_all_time()
        today_before_order = feed_page.check_order_feed_number_today()
        helpers.order(driver)
        helpers.profile_page(driver)
        order_number_in_history_text = feed_page.check_order_in_history()
        feed_page.click_button_feed()
        order_number_in_feed_order_text = feed_page.check_number_feed_order()
        assert order_number_in_feed_order_text == order_number_in_history_text
        order_number_in_ready_text = feed_page.check_order_list_ready()
        order_number_clear_feed_order_text = order_number_in_feed_order_text.replace("#", "")
        assert order_number_in_ready_text == order_number_clear_feed_order_text
        all_time_after_order = feed_page.check_order_feed_number_all_time()
        today_after_order = feed_page.check_order_feed_number_today()
        assert int(all_time_before_order) < int(all_time_after_order)
        assert int(today_before_order)  < int(today_after_order)
        order_number_clear_feed_order_text = order_number_in_feed_order_text.replace("#", "")
        assert order_number_in_ready_text == order_number_clear_feed_order_text
        

    


