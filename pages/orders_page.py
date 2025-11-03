
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure



class OrderPage:
    button_constructor = (By.XPATH, "//div/header/nav/ul/li[1]/a/p[text()='Конструктор']")
    button_order_feed = (By.XPATH, "//div/header/nav/ul/li[2]/a/p[text()='Лента Заказов']")
    burger_ingredient = (By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a[1]") 
    burger_ingredient_two = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]")
    button_close_modal_ingredient = (By.XPATH, "//div/section[1]/div[1]/button")
    ingredients_bascet = (By.XPATH, "/html/body/div/div/main/section[2]")
    counter_burger_ingredient = (By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p[text()='2']")
    button_order = (By.XPATH, "//div/main/section[2]/div/button[text()='Оформить заказ']")
    modal_order = (By.XPATH, "//div/section/div[1]/div/p[text()='идентификатор заказа']")
    close_modal_order = (By.XPATH, "//div/section/div[1]/button")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('переход по клику на «Лента заказов»')
    def click_button_order_feed(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.button_order_feed))
        self.driver.find_element(*self.button_order_feed).click()
    
    @allure.step('переход по клику на «Конструктор»')
    def click_button_constructor(self):
        self.driver.find_element(*self.button_constructor).click()
    
    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_burger_ingredient(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.burger_ingredient))
        self.driver.find_element(*self.burger_ingredient).click()
    
    @allure.step('Закрываем модалку ингредиента')
    def click_button_close_modal_ingredient(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.button_close_modal_ingredient))
        self.driver.find_element(*self.button_close_modal_ingredient).click()

    # Здесь пришлось искать помощь в интернете для создания JS для drag-and-drop, 
    # так как ActionChains не работает корректно в Firefox. В Chrome такой проблемы нет.
    @allure.step('перемещаем ингредиент в корзину')
    def set_burger_ingredient_in_ingredients_bascet(self):
        burger_ingredient = self.driver.find_element(*self.burger_ingredient)
        ingredients_basket = self.driver.find_element(*self.ingredients_bascet)

        self.driver.execute_script("""
        const src = arguments[0];
        const dst = arguments[1];
        const dataTransfer = new DataTransfer();

        let dropHandled = false;
        const dropListener = (e) => { 
            dropHandled = true; 
            e.preventDefault(); 
        };
        dst.addEventListener('drop', dropListener);

        src.dispatchEvent(new DragEvent('dragstart', { 
            dataTransfer,
            bubbles: true,
            cancelable: true
        }));
        dst.dispatchEvent(new DragEvent('dragover', { 
            dataTransfer,
            bubbles: true,
            cancelable: true
        }));
        dst.dispatchEvent(new DragEvent('drop', { 
            dataTransfer,
            bubbles: true,
            cancelable: true
        }));
        src.dispatchEvent(new DragEvent('dragend', { 
            dataTransfer,
            bubbles: true,
            cancelable: true
        }));

        dst.removeEventListener('drop', dropListener);
        return dropHandled;
        """, burger_ingredient, ingredients_basket)

        
    @allure.step('получаем каунтер данного ингредиента')
    def check_counter_burger_ingredient(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.counter_burger_ingredient))
        return self.driver.find_element(*self.counter_burger_ingredient)
    
    @allure.step('нажимаем на кнопку "Оформить заказ"')
    def click_button_order(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.button_order))
        self.driver.find_element(*self.button_order).click()

    @allure.step('возвращаем модалку с деталями заказа"')
    def check_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.modal_order))
        return self.driver.find_element(*self.modal_order)
    
    @allure.step('закрываем модалку с деталями заказа')
    def click_close_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(self.close_modal_order))
        self.driver.find_element(*self.close_modal_order).click()

    