from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import allure
import locators.orders_page_locators as loc


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('переход по клику на «Лента заказов»')
    def click_button_order_feed(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.button_order_feed))
        self.driver.find_element(*loc.button_order_feed).click()
    
    @allure.step('переход по клику на «Конструктор»')
    def click_button_constructor(self):
        self.driver.find_element(*loc.button_constructor).click()
    
    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_burger_ingredient(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.burger_ingredient))
        self.driver.find_element(*loc.burger_ingredient).click()
    
    @allure.step('Закрываем модалку ингредиента')
    def click_button_close_modal_ingredient(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.button_close_modal_ingredient))
        self.driver.find_element(*loc.button_close_modal_ingredient).click()

    # Здесь пришлось искать помощь в интернете для создания JS для drag-and-drop, 
    # так как ActionChains не работает корректно в Firefox. В Chrome такой проблемы нет.
    @allure.step('перемещаем ингредиент в корзину')
    def set_burger_ingredient_in_ingredients_bascet(self):
        burger_ingredient = self.driver.find_element(*loc.burger_ingredient)
        ingredients_basket = self.driver.find_element(*loc.ingredients_bascet)

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
        expected_conditions.visibility_of_element_located(loc.counter_burger_ingredient))
        result = self.driver.find_element(*loc.counter_burger_ingredient)
        return result.text
    
    @allure.step('нажимаем на кнопку "Оформить заказ"')
    def click_button_order(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.button_order))
        self.driver.find_element(*loc.button_order).click()

    @allure.step('возвращаем модалку с деталями заказа"')
    def check_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.modal_order))
        return self.driver.find_element(*loc.modal_order)
    
    @allure.step('закрываем модалку с деталями заказа')
    def click_close_modal_order(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(loc.close_modal_order))
        self.driver.find_element(*loc.close_modal_order).click()

    