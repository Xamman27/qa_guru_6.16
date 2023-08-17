from selene import browser, have, be


class RegistrationDonePage():

    def name(self, value):
        browser.element('//tbody/tr[1]/td[2]').should(have.text(value))

    def mail(self, value):
        browser.element('//tbody/tr[2]/td[2]').should(have.text(value))

    def gender(self, value):
        browser.element('//tbody/tr[3]/td[2]').should(have.text(value))

    def phone(self, value):
        browser.element('//tbody/tr[4]/td[2]').should(have.text(value))

    def birthday(self, value):
        browser.element('//tbody/tr[5]/td[2]').should(have.text(value))

    def subject(self, value):
        browser.element('//tbody/tr[6]/td[2]').should(have.text(value))

    def hobies(self, value):
        browser.element('//tbody/tr[7]/td[2]').should(have.text(value))

    def image(self, value):
        browser.element('//tbody/tr[8]/td[2]').should(have.text(value))

    def city(self, value):
        browser.element('//tbody/tr[9]/td[2]').should(have.text(value))

    def adress(self, value):
        browser.element('//tbody/tr[10]/td[2]').should(have.text(value))







