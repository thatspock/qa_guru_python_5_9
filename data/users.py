import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: [str]
    subject: str
    hobby: str
    picture_file: str
    address: str
    state: str
    city: str


student = User(
    first_name='Mr',
    last_name='Spock',
    email='mrspock@enterprise.com',
    gender='Male',
    phone_number='1800666553',
    date_of_birth=['13', 'May', '1985'],
    subject='English',
    hobby='Sports',
    picture_file='test.jpg',
    address='Enterprise (NCC-1701)',
    state='NCR',
    city='Delhi')
