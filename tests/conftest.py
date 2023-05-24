import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from tests.constants import DEFAULT_BROWSER_VERSION
from utils.attachment import AllureAttachmentManager
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--browser-version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_env()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser-version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
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

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options)

    browser = Browser(Config(driver=driver))

    yield browser

    allure_attachments = AllureAttachmentManager(browser)
    allure_attachments.gather_all_attachments()
