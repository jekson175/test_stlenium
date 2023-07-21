from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://seleniumbase.io/help_docs/recorder_mode/")
        # self.check_if_unchecked("input#__search")
        self.type('input[name="query"]', "hi")
        # self.js_click('h1:contains("👥 macOS Hidden Files")')
        self.click('a[href="../shadow_dom/"]')
        self.click('a[href="../using_safari_driver/"]')
        self.click('a[href="../../examples/example_logs/ReadMe/"]')
        self.click('nav[aria-label="Navigation"] ul')
        self.click('a[href="../../../help_docs/recorder_mode/"]')
        self.click('a[href="../method_summary/"]')
