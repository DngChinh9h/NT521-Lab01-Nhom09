# Fill the Python code in this file
from test_data import *


def json_search(key, input_object):
    ret_val = []

    if isinstance(input_object, dict):
        for k, v in input_object.items():

            if k == key:
                ret_val.append({k: v})

            if isinstance(v, (dict, list)):
                ret_val.extend(json_search(key, v))

    elif isinstance(input_object, list):
        for item in input_object:

            if isinstance(item, (dict, list)):
                ret_val.extend(json_search(key, item))

    return ret_val


print(json_search("issueSummary", data))
