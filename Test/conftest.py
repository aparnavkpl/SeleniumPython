import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/Aparna/Downloads/chromedriver_win32/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    base = 'http://pinglend.dev/#/login'
    driver.get(base)
    request.cls.driver = driver
    yield
    driver.close()
