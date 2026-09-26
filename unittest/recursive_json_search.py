# Fill the Python code in this file
from test_data import *
from policy import POLICY


def json_search(key, input_object, role=None):
    ret_val = []

    # Kiểm tra quyền truy cập nếu role được cung cấp
    if role is not None:
        allowed_roles = POLICY.get(key, [])

        if role not in allowed_roles:
            return []

    if isinstance(input_object, dict):
        for k, v in input_object.items():

            if k == key:
                ret_val.append({k: v})

            if isinstance(v, (dict, list)):
                ret_val.extend(json_search(key, v, role))

    elif isinstance(input_object, list):
        for item in input_object:

            if isinstance(item, (dict, list)):
                ret_val.extend(json_search(key, item, role))

    return ret_val


print(json_search("issueSummary", data))
