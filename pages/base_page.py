from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def set_text(self, locator,text):
        self.wait_for_clickable(locator).send_keys(text)


   