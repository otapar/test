import utilities.custom_logger as clo
import logging
from base.onder_driver import OnderDriver
from traceback import print_stack

class TesStatus(OnderDriver):

    log = clo.customLoggerTpr(logging.INFO)

    def __init__(self, driver):

        super(TesStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("!!! VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("!!! VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShotTpr(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("!!! VERIFICATION FAILED :: + " + resultMessage)
                self.screenShotTpr(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("!!! Exception Occurred !!!")
            self.screenShotTpr(resultMessage)
            print_stack()

    def markTpr(self, result, resultMessage):

        self.setResult(result, resultMessage)

    def markFinalTpr(self, testName, result, resultMessage):

        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +  " !!! TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " !!! TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True