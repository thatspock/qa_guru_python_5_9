import allure
from allure_commons.types import Severity
from page_objects.registration_page import RegistrationPage
from data.users import student
from utils.attachment import AllureAttachmentManager
from selene import browser


@allure.tag('DemoQA')
@allure.description("This test covers the complete student registration procedure, from form filling to submission.")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.feature('Student Registration Form')
@allure.story("Complete Student Registration Procedure")
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)

    allure_attachments = AllureAttachmentManager(browser)
    allure_attachments.gather_all_attachments()
