
from pages.orders_page import OrderPage
from pages.profile_page import ProfilePage
import time
import requests
import string
import random
import allure


BASE_URL = 'https://stellarburgers.education-services.ru'


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
@allure.step('регистрируем пользователя для получения данных, чтобы авторизироваться и удалить пользователя после теста')
def regist_user_for_login_and_get_token():
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)
        
        payload = {"email": email , "password": password, "name": name}
        requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        
        login_payload = {"email": email, "password": password}
        login_resp = requests.post(f'{BASE_URL}/api/auth/login', json=login_payload)
        access_token = login_resp.json().get('accessToken')
        
        return {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": access_token
    }

    
       
@allure.step('удаляем пользователя по токену')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    response = requests.delete(f'{BASE_URL}/api/auth/register/api/auth/user', headers=headers)
    return response

@allure.step('выполняем авторизацию')
def login(driver, email, password):
        profile_page = ProfilePage(driver)
        profile_page.click_email_field(email)
        profile_page.click_password_field(password)
        profile_page .click_button_login()

@allure.step('оформляем заказ')
def order(driver):
        order_page = OrderPage(driver)
        time.sleep(3)
        order_page.click_button_constructor()
        order_page.set_burger_ingredient_in_ingredients_bascet()
        order_page.click_button_order()
        time.sleep(5)
        order_page.click_close_modal_order()

@allure.step('заходим в историю заказов в профиле пользователя')
def profile_page(driver):
        profile_page = ProfilePage(driver)
        profile_page.click_button_profile()
        profile_page.click_button_history_profile()