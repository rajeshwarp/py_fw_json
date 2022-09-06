import logging
import sys

import pytest
from reportportal_client import RPLogger, RPLogHandler


########## pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'ProjectName-001'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rajeshwar'
#

# @pytest.fixture(scope='session', autouse=True)
# def pytest_html_report_title(report):
#     report.title = "Hola Report is customized"

#
# @pytest.fixture(scope='session', autouse=True)
# def configure_html_report_env(request):
#     request.config._metadata.update(
#         {'foo': 'bar'}
#     )
#

@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)

        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)

    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger
