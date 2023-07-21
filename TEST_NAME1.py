from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://www.google.com/intl/ru/gmail/about/")
        self.click("span.mobile-before-hero-only")
        self.open_if_not_url("https://www.google.com/intl/ru/gmail/about/")
        self.click("body main div div div div:nth-of-type(3) a")
        self.open_if_not_url("https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https://mail.google.com/mail/&flowName=GlifWebSignIn&flowEntry=SignUp")
        self.type("input#firstName", "fgdfgdgsf")
        self.type("input#lastName", "1111111111111111111")
        self.click("div.VfPpkd-RLmnJb")
        self.type("input#day", "12")
        self.select_option_by_text("select#month", "Январь")
        self.type("input#year", "1234")
        self.select_option_by_text("select#gender", "Женский")
        self.click('button:contains("Далее")')
