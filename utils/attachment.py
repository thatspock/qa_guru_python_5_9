import allure
from allure_commons.types import AttachmentType
from selene import browser


class AllureAttachmentManager:
    def gather_all_attachments(self):
        self.add_screenshot()
        self.add_logs()
        self.add_html()
        self.add_video()

    @allure.step('Adding screenshots')
    def add_screenshot(self):
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

    @allure.step('Adding logs')
    def add_logs(self):
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

    @allure.step('Adding HTML page')
    def add_html(self):
        html = browser.driver.page_source
        allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

    @allure.step('Adding video capture')
    def add_video(self):
        video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
        html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
               + video_url \
               + "' type='video/mp4'></video></body></html>"
        allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
