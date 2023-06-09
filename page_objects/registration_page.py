import os
import allure
import requests
from selene import have
from data.users import User
from tests.constants import THANKS_FOR_SUBMITTING_TEXT, PICTURE_FILE, URL_DEMOQA


class RegistrationPage():
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open automation practice form')
    def open(self):
        self.browser.open(URL_DEMOQA)

    @allure.step('Filling in first name with value: {value}')
    def fill_in_first_name(self, value):
        self.browser.element('#firstName').type(value)

    @allure.step('Filling in last name with value: {value}')
    def fill_in_last_name(self, value):
        self.browser.element('#lastName').type(value)

    @allure.step('Filling in email with value: {value}')
    def fill_in_email(self, value):
        self.browser.element('#userEmail').type(value)

    @allure.step('Pick gender with value: {value}')
    def pick_gender(self, value):
        self.browser.all('.custom-control-label').element_by(have.text(value)).click()

    @allure.step('Filling in phone number with value: {value}')
    def fill_in_phone_number(self, value):
        self.browser.element('#userNumber').type(value)

    @property
    def date_of_birth(self):
        return self.browser.element('#dateOfBirthInput')

    @allure.step('Filling in date of birth with value: {date_of_birth}')
    def fill_in_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth
        self.date_of_birth.click()
        self.browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        self.date_of_birth.send_keys(f'{day} {month} {year}').press_enter()

    @allure.step('Filling in subjects with value: {value}')
    def fill_in_subjects(self, value):
        self.browser.element('#subjectsInput').type(value).press_enter()

    @allure.step('Pick hobby with value: {value}')
    def pick_hobby(self, value):
        self.browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

    @allure.step('Upload picture with value: {value}')
    def upload_picture_file(self, value):
        image_url = PICTURE_FILE
        image_content = requests.get(image_url).content

        with open('test.jpg', 'wb') as f:
            f.write(image_content)

        self.browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpg'))

    @allure.step('Filling in address with value: {value}')
    def fill_in_address(self, value):
        self.browser.element('#currentAddress').type(value)

    @allure.step('Select state with value: {value}')
    def select_state(self, value):
        self.browser.element('#state #react-select-3-input').type(value).press_enter()

    @allure.step('Select city with value: {value}')
    def select_city(self, value):
        self.browser.element('#city #react-select-4-input').type(value).press_enter()

    @allure.step('Submitting the registration form')
    def submit_form(self):
        self.browser.execute_script('document.getElementById("submit").click()')

    @allure.step('Checking the submission confirmation message')
    def assert_form_submission_text(self, expected_text):
        self.browser.element('#example-modal-sizes-title-lg').should(have.text(expected_text))

    @allure.step('Verifying the user data')
    def assert_user_data(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        full_birthday = f'{student.date_of_birth[0]} {student.date_of_birth[1]},{student.date_of_birth[2]}'
        expected_values = [
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone_number}',
            f'Date of Birth {full_birthday}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobby}',
            f'Picture {student.picture_file}',
            f'Address {student.address}',
            f'State and City {student.state} {student.city}'
        ]
        self.browser.all('tbody tr').should(have.exact_texts(*expected_values))

    @allure.step('Closing the submission form')
    def close_submission_form(self):
        self.browser.element('#closeLargeModal').click()

    @allure.step('Registering the user')
    def register(self, student: User):
        self.fill_in_first_name(student.first_name)
        self.fill_in_last_name(student.last_name)
        self.fill_in_email(student.email)
        self.pick_gender(student.gender)
        self.fill_in_phone_number(student.phone_number)
        self.fill_in_date_of_birth(student.date_of_birth)
        self.fill_in_subjects(student.subject)
        self.pick_hobby(student.hobby)
        self.upload_picture_file(student.picture_file)
        self.fill_in_address(student.address)
        self.select_state(student.state)
        self.select_city(student.city)
        self.submit_form()
        self.assert_form_submission_text(THANKS_FOR_SUBMITTING_TEXT)

    @allure.step('Verifying the registration')
    def should_have_registered(self, student: User):
        self.assert_user_data(student)
        self.close_submission_form()
