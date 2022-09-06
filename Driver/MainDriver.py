import allure

from KWLogic.Keyword import RequestsUtility
from Utilities import read_json, custom_logger
import pytest


logger = custom_logger.customLogger()


class MDriver:

    logger = custom_logger.customLogger()

    def __init__(self):
        self.json_path = 'Driver/TestCase.json'

    def maind(self):
        #self.logger.info("\n \n")
        self.logger.info("******** Reading JSON **********")
        ts_json = read_json.ReadJson(self.json_path)
        ts = ts_json.readJson()

        self.logger.info("******** Capturing Nodes **********")
        suiteName = ts.suiteName
        suiteDescription = ts.suiteDescription
        testCases = ts.testCases
        if len(testCases) > 0:
            testCaseNo = 0
            for test in testCases:
                testCaseNo = testCaseNo + 1
                self.logger.info(f"******** Running Test case no: {testCaseNo} with ID > {test.testId}")
                testcaseId = test.testId
                testName = test.testName
                testcaseId = test.testDescription
                testSteps = test.testSteps
                if len(testSteps) > 0:
                    self.logger.info("********  Test Step initiated **********")
                    stepsno = 0
                    for step in testSteps:
                        stepsno = stepsno + 1
                        stepname = step.name
                        self.logger.info(f"******** Running Test Step - {stepsno} with NAME > {stepname} ")
                        stepClass = step.pclass
                        stepmethod = step.method
                        stepparameters = step.parameters
                        params_list = vars(stepparameters)
                        driver_step(stepClass, params_list)


def driver_step(stepClass, params_list):
    funcToCall = getattr(RequestsUtility, stepClass)
    logger.info(f"******** Calling Function : {funcToCall.__name__}")
    funcToCall(params_list)


## Running Test

@pytest.mark.sanity
def test_driver():
    md = MDriver()
    md.maind()
