from KWLogic.Keyword import RequestsUtility
from Utilities import read_json

# Read Test Suite Json
jo = read_json.ReadJson('../Driver/TestCase.json')
jdict = (jo.readJson())

# Capture field
suiteName = jdict.suiteName
suiteDescription = jdict.suiteDescription
#
if len(jdict.testCases) > 0:
    testcaseId = jdict.testCases[0].testId
    testName = jdict.testCases[0].testName
    testcaseId = jdict.testCases[0].testDescription
    testSteps = jdict.testCases[0].testSteps
    stepname = testSteps[0].name
    stepClass = testSteps[0].pclass
    stepmethod = testSteps[0].method
    stepparameters = testSteps[0].parameters

    rp_url = stepparameters.request.url
    rp_header = stepparameters.request.headers
    rp_Authorization = rp_header.Authorization

    rp_queryParams = stepparameters.request.queryParams

    rp_q = rp_queryParams.q
    rp_sort = rp_queryParams.sort
    rp_sort = rp_queryParams.order

#def run_test(StepName, stepClass , stepmethod,stepparameters):




def driver_step(rp_url, stepname=None, stepClass=None, stepmethod=None, stepparameters=None):
    funcToCall = getattr(RequestsUtility, 'get')
    resJSON = funcToCall(rp_url)
    return resJSON


print(driver_step(rp_url))
