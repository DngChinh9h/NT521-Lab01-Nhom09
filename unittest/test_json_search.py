# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *


class json_search_test(unittest.TestCase):

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    # Security Test 1:
    # viewer must not be allowed to read apiKey
    def test_api_key_viewer_forbidden(self):
        result = json_search("apiKey", data, role="viewer")
        self.assertEqual(result, [])

    # Security Test 2:
    # viewer must not be allowed to read managementIpAddress
    def test_management_ip_viewer_forbidden(self):
        result = json_search("managementIpAddress", data, role="viewer")
        self.assertEqual(result, [])

    # Security Test 3:
    # viewer is allowed to read issueSummary
    def test_issue_summary_viewer_allowed(self):
        result = json_search("issueSummary", data, role="viewer")
        self.assertNotEqual(result, [])


if __name__ == '__main__':
    unittest.main()
