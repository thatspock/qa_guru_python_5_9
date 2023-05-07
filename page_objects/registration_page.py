import os

from selene import browser, have

from data.users import User
from tests.constants import THANKS_FOR_SUBMITTING_TEXT


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_in_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_in_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_in_email(self, value):
        browser.element('#userEmail').type(value)

    def pick_gender(self, value):
        browser.all('.custom-control-label').element_by(have.text(value)).click()

    def fill_in_phone_number(self, value):
        browser.element('#userNumber').type(value)

    @property
    def date_of_birth(self):
        return browser.element('#dateOfBirthInput')

    def fill_in_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth
        self.date_of_birth.click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        self.date_of_birth.send_keys(f'{day} {month} {year}').press_enter()

    def fill_in_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def pick_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

    def upload_picture_file(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resourсes/{value}'))

    def fill_in_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.execute_script('document.getElementById("submit").click()')

    def assert_form_submission_text(self, expected_text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(expected_text))

    def assert_user_data(self, student: User):
        expected_values = [
            f'Student Name {student.first_name} {student.last_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone_number}',
            f'Date of Birth {student.date_of_birth[0]} {student.date_of_birth[1]},{student.date_of_birth[2]}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobby}',
            f'Picture {student.picture_file}',
            f'Address {student.address}',
            f'State and City {student.state} {student.city}'
        ]
        browser.all('tbody tr').should(have.exact_texts(*expected_values))

    def close_submission_form(self):
        browser.element('#closeLargeModal').click()

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

    def should_have_registered(self, student: User):
        self.assert_user_data(student)
        self.close_submission_form()
