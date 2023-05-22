import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.attachment import AllureAttachmentManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    def build_browser():
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options)

        browser = Browser(Config(driver))
        yield browser

        allure_attachments = AllureAttachmentManager(browser)
        allure_attachments.gather_all_attachments()

        return browser

    yield build_browser
    # browser.config.driver = driver

    # browser.driver.set_window_size(1920, 1200)
    # browser.config.base_url = 'https://demoqa.com'
