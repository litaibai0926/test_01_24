

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import url, driver_path
@pytest.fixture(scope='session')
def login():
    e = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=e)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()