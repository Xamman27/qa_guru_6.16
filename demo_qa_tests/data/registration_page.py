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
        self.input_state = browser.element('#state')
        self.input_city = browser.element('#city')
        self.submit_button = browser.element('#submit')

        self.result_student_name = browser.element('//tbody/tr[1]/td[2]')
        self.result_mail = browser.element('//tbody/tr[2]/td[2]')
        self.result_gender = browser.element('//tbody/tr[3]/td[2]')
        self.result_phone = browser.element('//tbody/tr[4]/td[2]')
        self.result_birthday = browser.element('//tbody/tr[5]/td[2]')
        self.result_subject = browser.element('//tbody/tr[6]/td[2]')
        self.result_hobbies = browser.element('//tbody/tr[7]/td[2]')
        self.result_image = browser.element('//tbody/tr[8]/td[2]')
        self.result_city = browser.element('//tbody/tr[9]/td[2]')
        self.result_address = browser.element('//tbody/tr[10]/td[2]')




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
        self.input_city.perform(command.js.scroll_into_view)
        self.input_state.type(student.state).press_enter()
        self.input_city.type(student.city).press_enter()
        self.submit_button.should(be.visible).click()
        # browser.element('#state').click()
        # browser.all('[id^=react-select][id*=option]').element_by(
        #     have.exact_text(student.state)
        # ).click()
        #

        # browser.element('#city').perform(command.js.scroll_into_view)
        # browser.element('#city').click()
        # browser.all('[id^=react-select][id*=option]').element_by(
        #     have.exact_text(student.city)
        # ).click()

        # self.input_state.should(be.visible).type(student.state).press_enter()
        # self.input_city.should(be.clickable).type(student.city).press_enter()

    def chech_registr(self, student=Users):
        self.result_student_name.should(have.text(f'{student.first_name} {student.last_name}'))
        self.result_mail.should(have.text(student.mail))






