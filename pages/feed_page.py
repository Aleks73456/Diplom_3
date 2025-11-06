import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators.feed_page_locators as loc

class FeedPage:
    

    
    def __init__(self, driver):
        self.driver = driver


    @allure.step('переход по клику на «Лента заказов»')
    def click_button_feed(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.button_feed))
        self.driver.find_element(*loc.button_feed).click()

    @allure.step('если кликнуть на заказ, откроется всплывающее окно с деталями»')
    def click_button_feed_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.button_feed_order))
        self.driver.find_element(*loc.button_feed_order).click()
    
    @allure.step('возвращаем всплывающее окно с деталями заказа')
    def check_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.modal_feed_order))
        return self.driver.find_element(*loc.modal_feed_order)
    
    @allure.step('проверяем, что заказ отображается в истории заказов')
    def check_order_in_history(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.order_in_history))
        result = self.driver.find_element(*loc.order_in_history)
        return result.text
    
    
    @allure.step('закрываем модалку заказа в ленте заказов')
    def click_button_close_order_in_history(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.close_button_order_in_history))
        self.driver.find_element(*loc.close_button_order_in_history).click()
    
    @allure.step('возвращаем количество заказов за все время')
    def check_order_feed_number_all_time(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.order_feed_number_all_time))
        result = self.driver.find_element(*loc.order_feed_number_all_time)
        return result.text
    
    @allure.step('возвращаем количество заказов за сегодня')
    def check_order_feed_number_today(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.order_feed_number_today))
        result = self.driver.find_element(*loc.order_feed_number_today)
        return result.text
    
    @allure.step('возвращаем номер заказа в работе')
    def check_order_list_ready(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.order_list_ready))
        result = self.driver.find_element(*loc.order_list_ready)
        return result.text

    @allure.step('возвращаем номер заказа в ленте заказов')
    def check_number_feed_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.number_feed_order))
        result = self.driver.find_element(*loc.number_feed_order)
        return result.text
