import allure

from demo_qa_tests.data.users import Users
from demo_qa_tests.data.path import image_path
from demo_qa_tests.data.registration_page import RegistrationPage


student = Users(
    'Valery', 'Maksimov', 'xam@gmail.com', 'Male', '8911123457', '1 May,1989',
    'English', 'Sports', image_path, 'SPB', 'NCR', 'Delhi'
)
reg_page = RegistrationPage()

@allure.title("Successful registration")
def test_simple():
    with allure.step("Open registration form"):
        reg_page.open()
    with allure.step("Fill form"):
        reg_page.register(student)
    with allure.step("Assert form results"):
        reg_page.chech_registr(student)
