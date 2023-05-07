from selene import browser, have, be
import os


class RegistrationPage():
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

    def fill_in_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        browser.element('#dateOfBirthInput').send_keys(f'{day} {month} {year}').press_enter()

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

    def should_have_form_submission_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def should_have_registration_data(self, *values):
        browser.all('tbody tr').should(
            have.exact_texts(*values))

    def close_submission_form(self):
        browser.element('#closeLargeModal').click()


def test_homework():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_in_first_name('Mr')
    registration_page.fill_in_last_name('Spock')
    registration_page.fill_in_email('mrspock@enterprise.com')
    registration_page.pick_gender('Male')
    registration_page.fill_in_phone_number('1800666553')
    registration_page.fill_in_date_of_birth('13', 'May', '1985')
    registration_page.fill_in_subjects('English')
    registration_page.pick_hobby('Sports')
    registration_page.upload_picture_file('test.jpg')
    registration_page.fill_in_address('Enterprise (NCC-1701)')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit_form()
    registration_page.should_have_form_submission_text('Thanks for submitting the form')
    # THEN
    registration_page.should_have_registration_data(
        'Student Name Mr Spock', 'Student Email mrspock@enterprise.com', 'Gender Male',
        'Mobile 1800666553', 'Date of Birth 13 May,1985', 'Subjects English', 'Hobbies Sports',
        'Picture test.jpg', 'Address Enterprise (NCC-1701)', 'State and City NCR Delhi'
    )
    registration_page.close_submission_form()
