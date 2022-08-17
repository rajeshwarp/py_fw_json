from useless.TestStep import TestStep
from useless.TestSuite import TestSuite


class TestCase(TestSuite):
    def __init__(self):
        pass

    testid = ''
    testName = ''
    testDescription = ''
    testSteps = [TestStep]
