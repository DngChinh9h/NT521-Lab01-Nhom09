# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''test module to search function in recursive_json_search.py'''

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    def test_viewer_cannot_read_api_key(self):
        self.assertEqual(json_search("apiKey", data, role="viewer"), [])

    def test_viewer_cannot_read_management_ip_address(self):
        self.assertEqual(json_search("managementIpAddress", data, role="viewer"), [])

    def test_viewer_can_read_issue_summary(self):
        self.assertNotEqual(json_search("issueSummary", data, role="viewer"), [])

    def test_admin_can_read_api_key(self):
        self.assertNotEqual(json_search("apiKey", data, role="admin"), [])

    def test_operator_can_read_management_ip_address(self):
        self.assertNotEqual(json_search("managementIpAddress", data, role="operator"), [])

if __name__ == '__main__':
    unittest.main()