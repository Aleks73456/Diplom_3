import pytest
from helpers import BASE_URL
from selenium import webdriver
import helpers


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    wd = webdriver.Chrome() if browser == "chrome" else webdriver.Firefox()
    yield wd
    wd.quit()



@pytest.fixture
def login_with_driver(driver):

    driver.get(f'{BASE_URL}/login')
    user = helpers.regist_user_for_login_and_get_token()
    helpers.login(driver, user["email"], user["password"])

    yield driver
    helpers.delete_user(user["accessToken"])