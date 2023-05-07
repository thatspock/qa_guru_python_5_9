import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.driver.maximize_window()
    browser.driver.set_window_size(1920, 1200)
    browser.config.base_url = 'https://demoqa.com'
