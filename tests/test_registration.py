import os
from selene import browser, have, be
from page_objects.registration_page import RegistrationPage


def test_registration_form():
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
    registration_page.assert_form_submission_text('Thanks for submitting the form')
    # THEN
    registration_page.assert_user_data(
        'Student Name Mr Spock', 'Student Email mrspock@enterprise.com', 'Gender Male',
        'Mobile 1800666553', 'Date of Birth 13 May,1985', 'Subjects English', 'Hobbies Sports',
        'Picture test.jpg', 'Address Enterprise (NCC-1701)', 'State and City NCR Delhi'
    )
    registration_page.close_submission_form()
