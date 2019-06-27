import utilities.custom_logger as clo
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = clo.customLoggerTpr(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "//ul[@class='toolbar nav navbar-nav navbar-right']//a[@class='nav-link']"
    _user_field = "login-form-login"
    _password_field = "login-form-password"
    _login_button = "//form[@id='login-form']/button[@type='submit']"

    def clickLoginLink(self):
        self.switchToFrameTpr(xpath="//iframe[@src='http://demo-web.usecomer.com/tr-tr/ana-sayfa']")
        self.clickTpr(locator=self._login_link, locatorType="xpath")
        self.switchToDefaultContentTpr()

    def enterUserName(self,username):
        self.switchToFrameTpr(xpath="//iframe[@src='http://demo-web.usecomer.com/tr-tr/ana-sayfa']")
        self.sendKeysTpr(username, locator=self._user_field)
    
    def enterPassword(self,password):
        self.sendKeysTpr(password,locator=self._password_field)
    
    def clickLoginButton(self):
        self.clickTpr(locator=self._login_button,locatorType="xpath")

    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def unsuccessfulLogin(self):
        result = self.isElementPresentTpr("//div[contains(text(),'Invalid login or password')]",locatorType="xpath")
        return result
        