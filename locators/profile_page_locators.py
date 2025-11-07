from selenium.webdriver.common.by import By

button_profile = (By.XPATH, "//p[text()='Личный Кабинет']")
button_history_profile = (By.XPATH, ".//a[text()='История заказов']")
button_exit = (By.XPATH, "//button[text()='Выход']") 
auth_form = (By.CSS_SELECTOR, "form.Auth_form__3qKeq.mb-20")
email_field = (By.NAME, "name")
password_field = (By.NAME, "Пароль")
button_login = (By.XPATH, "//button[text()='Войти']")