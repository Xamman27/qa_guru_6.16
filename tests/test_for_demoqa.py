from unittest import result
from demo_qa_tests.data.users import Users
from selene import browser, be, have
from demo_qa_tests.data.path import image_path
from demo_qa_tests.data.registration_page import RegistrationPage
from demo_qa_tests.data.registration_done_page import RegistrationDonePage

student = Users(
    'Valery', 'Maksimov', 'xam@gmail.com', 'Male', '8911123457', '1 May,1989',
    'English', 'Sports', image_path, 'SPB', 'NCR', 'Delhi'
)
reg_page = RegistrationPage()


def test_simple():
    reg_page.open()
    reg_page.register(student)
    #reg_page.chech_registr(student)

# def test_registration_page():
#     reg_page = RegistrationPage()
#     result_page = RegistrationDonePage()
#
#     reg_page.open()
#     reg_page.first_name('Valery')
#     reg_page.last_name('Maksimov')
#     reg_page.email('xam@gmail.com')
#     reg_page.gender()
#     reg_page.phone_number('8911123457')
#     reg_page.birthday()
#     reg_page.subject()
#     reg_page.hobbies()
#     reg_page.picture(image_path)
#     reg_page.adress()
#
#     result_page.name('Valery Maksimov')
#     result_page.mail('xam@gmail.com')
#     result_page.gender('Male')
#     result_page.phone('8911123457')
#     result_page.birthday('1 May,1989')
#     result_page.subject('English')
#     result_page.hobies('Sports')
#     result_page.image('image.jpeg')
#     result_page.city('SPB')
#     result_page.adress('NCR Delhi')
