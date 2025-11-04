import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    wd = webdriver.Chrome() if browser == "chrome" else webdriver.Firefox()
    yield wd
    wd.quit()