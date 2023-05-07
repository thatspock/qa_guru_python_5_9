from page_objects.registration_page import RegistrationPage
from data.users import student


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
