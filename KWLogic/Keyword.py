import requests
import logging
import Utilities.custom_logger as cl
import unittest
import pytest
import sys


class RequestsUtility:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self):
        pass

    def RestAPIAction(params_list):
        if "request" in params_list:
            j_request = vars(params_list["request"])
            j_url = str(j_request["url"])
            print(j_url)
            rs_api = requests.get(j_url)
            status_code = rs_api.status_code
            # # #rs_api.expected_status_code = status_code
            # # rs_json = rs_api.json()
            # # # logger.debug(f"GET API response: {rs_json}")
            print(status_code)
