import time
import traceback
import random, string
import utilities.custom_logger as clo
import logging

class Util(object):

    log = clo.customLoggerTpr(logging.INFO)

    def sleepTpr(self, sec, info=""):

        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

