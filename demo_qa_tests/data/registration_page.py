from selene import browser, be, have


class RegistrationPage():
 
    def __init__(self):
        self.input_first_name = browser.element('#firstName')
        self.input_last_name = browser.element('#lastName')
        self.input_email = browser.element('#userEmail')
        self.input_phone_number = browser.element('#userNumber')

    def open(self):
        browser.open('automation-practice-form')

    def fill_first_name(self, value: str):
        self.input_first_name.type(value)

    def fill_last_name(self, value):
        self.input_last_name.type(value)

    def fill_email(self, value):
        self.input_email.type(value)

    def fill_gender(self,value):
        browser.element(f"[value='{value}']+label").click()

    def fill_phone_number(self, value):
        self.input_phone_number.type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f"[value='{month-1}']").click()
        browser.element(f"[value='{year}']").click()

        browser.element(f"[aria-label='Choose Monday, May {day}st, {year}']").should(be.clickable).click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(f'{value}').press_enter()

    def fill_hobbies(self):
        browser.element('[for=hobbies-checkbox-1][class="custom-control-label"]').click()

    def fill_picture(self, path):
        browser.element('#uploadPicture').set_value(path)

    def fill_adress(self):
        browser.element('#currentAddress').should(be.blank).type('SPB')
        browser.element('#react-select-3-input').type('ncr').press_enter()
        browser.element('#react-select-4-input').type('Delhi').press_enter()

    def submit(self):
        browser.element('#submit').submit()






