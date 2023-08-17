from selene import browser, have, be
class RegistrationDonePage():

    def result_name(self, value):
        browser.element('//tbody/tr[1]/td[2]').should(have.text(value))

    def result_mail(self, value):
        browser.element('//tbody/tr[2]/td[2]').should(have.text(value))

    def result_gender(self, value):
        browser.element('//tbody/tr[3]/td[2]').should(have.text(value))

    def result_phone(self, value):
        browser.element('//tbody/tr[4]/td[2]').should(have.text(value))

    def result_birthday(self, value):
        browser.element('//tbody/tr[5]/td[2]').should(have.text(value))

    def result_subject(self, value):
        browser.element('//tbody/tr[6]/td[2]').should(have.text(value))

    def result_hobies(self, value):
        browser.element('//tbody/tr[7]/td[2]').should(have.text(value))

    def result_image(self, value):
        browser.element('//tbody/tr[8]/td[2]').should(have.text(value))

    def result_city(self, value):
        browser.element('//tbody/tr[9]/td[2]').should(have.text(value))

    def result_adress(self, value):
        browser.element('//tbody/tr[10]/td[2]').should(have.text(value))







