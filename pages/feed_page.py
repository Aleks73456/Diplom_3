import time
import allure
import locators.feed_page_locators as loc
from pages.base_page import BasePage

class FeedPage(BasePage):
    



    @allure.step('переход по клику на «Лента заказов»')
    def click_button_feed(self):
        time.sleep(1)
        self.click(loc.button_feed)

    @allure.step('если кликнуть на заказ, откроется всплывающее окно с деталями»')
    def click_button_feed_order(self):
        self.click(loc.button_feed_order)
    
    @allure.step('возвращаем всплывающее окно с деталями заказа')
    def check_modal_order(self):
        return self.wait_for_visibility(loc.modal_feed_order)

    
    @allure.step('проверяем, что заказ отображается в истории заказов')
    def check_order_in_history(self):
        return self.get_text(loc.order_in_history)
    
    
    @allure.step('закрываем модалку заказа в ленте заказов')
    def click_button_close_order_in_history(self):
        self.click(loc.close_button_order_in_history)
    
    @allure.step('возвращаем количество заказов за все время')
    def check_order_feed_number_all_time(self):
        return self.get_text(loc.order_feed_number_all_time)
    
    @allure.step('возвращаем количество заказов за сегодня')
    def check_order_feed_number_today(self):
        return self.get_text(loc.order_feed_number_today)
    
    @allure.step('возвращаем номер заказа в работе')
    def check_order_list_ready(self):
        return self.get_text(loc.order_list_ready)

    @allure.step('возвращаем номер заказа в ленте заказов')
    def check_number_feed_order(self):
        return self.get_text(loc.number_feed_order)
