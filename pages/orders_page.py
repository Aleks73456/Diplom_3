import time
import allure
import locators.orders_page_locators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):


    @allure.step('переход по клику на «Лента заказов»')
    def click_button_order_feed(self):
        time.sleep(1)
        self.click(loc.button_order_feed)
        
    
    @allure.step('переход по клику на «Конструктор»')
    def click_button_constructor(self):
        self.click(loc.button_constructor)
    
    
    @allure.step('Кликаем на ингредиент в конструкторе')
    def click_burger_ingredient(self):
        self.click(loc.burger_ingredient)
        
        
    @allure.step('Закрываем модалку ингредиента')
    def click_button_close_modal_ingredient(self):
        self.click(loc.button_close_modal_ingredient)
        
        

    # Здесь пришлось искать помощь в интернете для создания JS для drag-and-drop, 
    # так как ActionChains не работает корректно в Firefox. В Chrome такой проблемы нет.
    @allure.step('перемещаем ингредиент в корзину')
    def set_burger_ingredient_in_ingredients_bascet(self):
        burger_ingredient = self.wait_for_visibility(loc.burger_ingredient)
        ingredients_basket = self.wait_for_visibility(loc.ingredients_bascet)

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
        return self.get_text(loc.counter_burger_ingredient)
        
    
    @allure.step('нажимаем на кнопку "Оформить заказ"')
    def click_button_order(self):
        time.sleep(1)
        self.click(loc.button_order)
        

    @allure.step('возвращаем модалку с деталями заказа"')
    def check_modal_order(self):
        return self.wait_for_visibility(loc.modal_order)
    
    
    @allure.step('закрываем модалку с деталями заказа')
    def click_close_modal_order(self):
        self.click(loc.close_modal_order)
        

    