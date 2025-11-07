from selenium.webdriver.common.by import By

button_forgot_password = (By.XPATH, "//a[text()='Восстановить пароль']")
email_field = (By.NAME, "name")
button_type_primary = (By.XPATH, "//button[text()='Восстановить']")
password_field = (By.XPATH, "//input[@type='password']")
button_eye = (By.CSS_SELECTOR, ".input__icon.input__icon-action")
password_field_after_click_eye = (By.XPATH, "//input[@type='text']")