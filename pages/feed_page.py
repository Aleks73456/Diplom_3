from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class FeedPage:
    
    button_feed = (By.XPATH, "//p[text()='Лента Заказов']")
    button_feed_order =  (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]")
    number_feed_order= (By.XPATH, "//p[contains(text(), '#')]")
    modal_feed_order = (By.CLASS_NAME, "Modal_orderBox__1xWdi") 
    order_in_history = (By.CSS_SELECTOR, "p.text_type_digits-default") 
    close_button_order_in_history = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]/div/button")
    order_feed_number_all_time = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[1]")
    order_feed_number_today = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[2]")
    order_list_ready = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__")]//li')

    
    def __init__(self, driver):
        self.driver = driver


    @allure.step('переход по клику на «Лента заказов»')
    def click_button_feed(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.button_feed))
        self.driver.find_element(*self.button_feed).click()

    @allure.step('если кликнуть на заказ, откроется всплывающее окно с деталями»')
    def click_button_feed_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.button_feed_order))
        self.driver.find_element(*self.button_feed_order).click()
    
    @allure.step('возвращаем всплывающее окно с деталями заказа')
    def check_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.modal_feed_order))
        return self.driver.find_element(*self.modal_feed_order)
    
    @allure.step('проверяем, что заказ отображается в истории заказов')
    def check_order_in_history(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.order_in_history))
        result = self.driver.find_element(*self.order_in_history)
        return result.text
    
    
    @allure.step('закрываем модалку заказа в ленте заказов')
    def click_button_close_order_in_history(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.close_button_order_in_history))
        self.driver.find_element(*self.close_button_order_in_history).click()
    
    @allure.step('возвращаем количество заказов за все время')
    def check_order_feed_number_all_time(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.order_feed_number_all_time))
        result = self.driver.find_element(*self.order_feed_number_all_time)
        return result.text
    
    @allure.step('возвращаем количество заказов за сегодня')
    def check_order_feed_number_today(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.order_feed_number_today))
        result = self.driver.find_element(*self.order_feed_number_today)
        return result.text
    
    @allure.step('возвращаем номер заказа в работе')
    def check_order_list_ready(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.order_list_ready))
        result = self.driver.find_element(*self.order_list_ready)
        return result.text

    @allure.step('возвращаем номер заказа в ленте заказов')
    def check_number_feed_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.number_feed_order))
        result = self.driver.find_element(*self.number_feed_order)
        return result.text
