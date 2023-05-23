import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils.attachment import AllureAttachmentManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser-version',
        default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser-version')
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': browser_version,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver=driver))

    yield browser

    allure_attachments = AllureAttachmentManager(browser)
    allure_attachments.gather_all_attachments()
