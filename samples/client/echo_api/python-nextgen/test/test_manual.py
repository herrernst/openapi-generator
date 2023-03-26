# coding: utf-8

"""
    Echo Server API

    Echo Server API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.api.query_api import QueryApi # noqa: E501
from openapi_client.rest import ApiException

class TestManual(unittest.TestCase):
    """Manually written tests"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDateTimeQueryWithDateTimeFormat(self):
        api_instance = openapi_client.QueryApi()
        api_instance.api_client.configuration.datetime_format = "%Y-%m-%d %a %H:%M:%S%Z"
        datetime_query = datetime.datetime.fromisoformat('2013-10-20T19:20:30-05:00') # datetime |  (optional)
        date_query = '2013-10-20' # date |  (optional)
        string_query = 'string_query_example' # str |  (optional)

        # Test query parameter(s)
        api_response = api_instance.test_query_datetime_date_string(datetime_query=datetime_query, date_query=date_query, string_query=string_query)
        e = EchoServerResponseParser(api_response)
        self.assertEqual(e.path, "/query/datetime/date/string?datetime_query=2013-10-20%20Sun%2019%3A20%3A30UTC-05%3A00&date_query=2013-10-20&string_query=string_query_example")

    def testDateTimeQueryWithDateTime(self):
        api_instance = openapi_client.QueryApi()
        datetime_query = datetime.datetime.fromisoformat('2013-10-20T19:20:30-05:00') # datetime |  (optional)
        date_query = '2013-10-20' # date |  (optional)
        string_query = 'string_query_example' # str |  (optional)
    
        # Test query parameter(s)
        api_response = api_instance.test_query_datetime_date_string(datetime_query=datetime_query, date_query=date_query, string_query=string_query)
        e = EchoServerResponseParser(api_response)
        self.assertEqual(e.path, "/query/datetime/date/string?datetime_query=2013-10-20T19%3A20%3A30.000000-0500&date_query=2013-10-20&string_query=string_query_example")

class EchoServerResponseParser():
    def __init__(self, http_response):
        if http_response is None:
            raise ValueError("http response must not be None.")

        lines = http_response.split("\n")
        self.headers = dict()
        x = 0
        while x < len(lines):
            if x == 0:
                items = lines[x].split(" ")
                self.method = items[0];
                self.path = items[1];
                self.protocol = items[2];
            elif lines[x] == "": # blank line
                self.body = "\n".join(lines[x:])
            else:
                key_value = lines[x].split(": ")
                # store the header key-value pair in headers
                if len(key_value) == 2:
                    self.headers[key_value[0]] = key_value[1]
            x = x+1
            
if __name__ == '__main__':
    unittest.main()
