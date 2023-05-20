import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.driver.maximize_window()
    driver = webdriver.Chrome('./drivers/chromedriver')
    driver.set_window_size(1920, 1200)
    browser.config.driver = lambda: driver
    browser.config.base_url = 'https://demoqa.com'
