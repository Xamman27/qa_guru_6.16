from selene import browser, be, have


class RegistrationPage():
    def __init__(self):
        self.input_first_name = browser.element('#firstName')
        self.input_last_name = browser.element('#lastName')
        self.input_email = browser.element('#userEmail')
        self.input_phone_number = browser.element('#userNumber')

    def open(self):
        browser.open('automation-practice-form')

    def first_name(self, value: str):
        self.input_first_name.should(be.blank).type(value)

    def last_name(self, value):
        self.input_last_name.should(be.blank).type(value)

    def email(self, value):
        self.input_email.should(be.blank).type(value)

    def gender(self):
        browser.element("[value='Male']+label").should(be.clickable).click()

    def phone_number(self, value):
        self.input_phone_number.should(be.blank).type(value)

    def birthday(self):
        browser.element('#dateOfBirthInput').should(be.clickable).click()
        browser.element("[value='4']").should(be.clickable).click()
        browser.element("[value='1989']").should(be.clickable).click()
        browser.element("[value='1989']").should(be.clickable).click()
        browser.element("[aria-label='Choose Monday, May 1st, 1989']").should(be.clickable).click()

    def subject(self):
        browser.element('#subjectsInput').should(be.blank).type('Eng').press_enter()

    def hobbies(self):
        browser.element('[for=hobbies-checkbox-1][class="custom-control-label"]').should(be.clickable).click()

    def picture(self, path):
        browser.element('#uploadPicture').set_value(path)

    def adress(self):
        browser.element('#currentAddress').should(be.blank).type('SPB')
        browser.element('#react-select-3-input').should(be.blank).type('ncr').press_enter()
        browser.element('#react-select-4-input').should(be.blank).type('Delhi').press_enter().press_enter()







