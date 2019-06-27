from base.onder_driver import OnderDriver 
from traceback import print_stack
from utilities.util import Util

class BasePage(OnderDriver):

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
