import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()