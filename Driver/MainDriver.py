from KWLogic.Keyword import RequestsUtility
from Utilities import read_json


class MDriver:
    # json_path = 'TestCase.json'

    def __init__(self):
        self.json_path = 'TestCase.json'

    def maind(self):
        ts_json = read_json.ReadJson(self.json_path)
        ts = ts_json.readJson()

        # Capture field
        suiteName = ts.suiteName
        suiteDescription = ts.suiteDescription
        testCases = ts.testCases
        if len(testCases) > 0:
            for test in testCases:
                testcaseId = test.testId
                testName = test.testName
                testcaseId = test.testDescription
                testSteps = test.testSteps
                if len(testSteps) > 0:
                    for step in testSteps:
                        stepname = step.name
                        stepClass = step.pclass
                        stepmethod = step.method
                        stepparameters = step.parameters
                        params_list = vars(stepparameters)
                        #print("--->" + stepClass)
                        #print(type(params_list))
                        driver_step(stepClass, params_list)


def driver_step(stepClass, params_list):
    funcToCall = getattr(RequestsUtility, stepClass)
    funcToCall(params_list)



md = MDriver()
md.maind()
