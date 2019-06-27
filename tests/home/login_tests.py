from pages.home.login_page import LoginPage
from utilities.teststatus import TesStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUpTpr", "setUpTpr")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpTpr):
        self.lp = LoginPage(self.driver)
        self.ts = TesStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_unseccessfulLogin(self):
        self.lp.login("abcd", "123")
        result = self.lp.unsuccessfulLogin()
        self.ts.markFinalTpr("test unsuccessfulLogin", result, "login verification")