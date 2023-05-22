import allure
from allure_commons.types import Severity
from page_objects.registration_page import RegistrationPage
from data.users import student


@allure.tag('DemoQA')
@allure.description("This test covers the complete student registration procedure, from form filling to submission.")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.feature('Student Registration Form')
@allure.story("Complete Student Registration Procedure")
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_registration_form(browser_management):
    browser = browser_management()
    registration_page = RegistrationPage(browser)
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
