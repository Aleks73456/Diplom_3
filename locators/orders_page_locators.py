from selenium.webdriver.common.by import By


button_constructor = (By.XPATH, "//p[text()='Конструктор']")
button_order_feed = (By.XPATH, "//p[text()='Лента Заказов']")
burger_ingredient = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  
button_close_modal_ingredient = (By.CLASS_NAME, "Modal_modal__close__TnseK")
ingredients_bascet = (By.CLASS_NAME, "BurgerConstructor_basket__29Cd7")
counter_burger_ingredient = (By.XPATH, "//p[text()='2']")
button_order = (By.XPATH, "//button[text()='Оформить заказ']")
modal_order = (By.XPATH, "//p[text()='идентификатор заказа']")
close_modal_order = (By.CLASS_NAME, "Modal_modal__close__TnseK")