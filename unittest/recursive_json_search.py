# Fill the Python code in this file
try:
    from .policy import POLICY
    from .test_data import data
except ImportError:  # Support running this file directly from unittest/.
    from policy import POLICY
    from test_data import data


def json_search(key, input_object, role=None):
    """Search nested JSON-like data, applying POLICY when a role is supplied.

    Calls without a role preserve unrestricted search behavior. Keys absent
    from POLICY are denied by default for role-based calls.
    """
    if role is not None and role not in POLICY.get(key, []):
        return []

    ret_val = []
    if isinstance(input_object, dict):
        for current_key, value in input_object.items():
            if current_key == key:
                ret_val.append({current_key: value})
            if isinstance(value, (dict, list)):
                ret_val.extend(json_search(key, value, role))
    elif isinstance(input_object, list):
        for item in input_object:
            if isinstance(item, (dict, list)):
                ret_val.extend(json_search(key, item, role))

    return ret_val


if __name__ == "__main__":
    print(json_search("issueSummary", data))
