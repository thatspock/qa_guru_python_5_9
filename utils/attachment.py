import allure
from allure_commons.types import AttachmentType


class AllureAttachmentManager:
    def __init__(self, browser):
        self.browser = browser

    def gather_all_attachments(self):
        self.add_screenshot()
        self.add_logs()
        self.add_html()

    def add_screenshot(self):
        png = self.browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

    def add_logs(self):
        log = "".join(f'{text}\n' for text in self.browser.driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

    def add_html(self):
        html = self.browser.driver.page_source
        allure.attach(html, 'page_source', AttachmentType.HTML, '.html')
