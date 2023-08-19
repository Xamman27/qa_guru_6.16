from selene import browser, be, have, command
from demo_qa_tests.data.users import Users
from demo_qa_tests.data.path import image_path
class RegistrationPage():
    def __init__(self):
        self.input_first_name = browser.element('#firstName')
        self.input_last_name = browser.element('#lastName')
        self.input_email = browser.element('#userEmail')
        self.input_phone_number = browser.element('#userNumber')
        self.input_birthday = browser.element('#dateOfBirthInput')
        self.input_subject = browser.element('#subjectsInput')
        self.radio_button_hobies = browser.all
        self.upload_picture = browser.element('#uploadPicture')
        self.input_current_address = browser.element('#currentAddress')
        self.input_state = browser.element('#react-select-3-input')
        self.input_city = browser.element('#react-select-4-input')


    def open(self):
        browser.open('automation-practice-form')
        browser.element('#adplus-anchor').perform(command.js.remove)
        browser.element('#fixedban').perform(command.js.remove)
        browser.element('footer').perform(command.js.remove)

    def register(self, student=Users):
        self.input_first_name.should(be.blank).type(student.first_name)
        self.input_last_name.should(be.blank).type(student.last_name)
        self.input_email.should(be.blank).type(student.email)
        browser.element(f'[name=gender][value={student.gender}]+label').click()
        self.input_phone_number.should(be.blank).type(student.phone_number)
        self.input_birthday.should(be.visible).type(student.birthday)
        self.input_subject.click().send_keys(student.subject).press_enter()
        browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()
        self.upload_picture.set_value(image_path)
        self.input_current_address.should(be.blank).type(student.current_address)
        self.input_state.should(be.clickable).type(student.state)
        self.input_state.should(be.clickable).type(student.city)







