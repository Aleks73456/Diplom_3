from selenium.webdriver.common.by import By



button_feed = (By.XPATH, "//p[text()='Лента Заказов']")
button_feed_order =  (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]")
number_feed_order= (By.XPATH, "//p[contains(text(), '#')]")
modal_feed_order = (By.CLASS_NAME, "Modal_orderBox__1xWdi") 
order_in_history = (By.CSS_SELECTOR, "p.text_type_digits-default") 
close_button_order_in_history = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]/div/button")
order_feed_number_all_time = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[1]")
order_feed_number_today = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__')])[2]")
order_list_ready = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__")]//li')
