import pytest
from selene import browser
from selenium import webdriver
import os

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.driver.maximize_window()
    chromedriver_path = os.path.abspath('drivers/chromedriver')
    driver = webdriver.Chrome(chromedriver_path)
    driver.set_window_size(1920, 1200)
    browser.config.driver = lambda: driver
    browser.config.base_url = 'https://demoqa.com'
