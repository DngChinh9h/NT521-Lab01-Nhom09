## 5. Threat Model

### Threat 1 - Information Disclosure

A user with the `viewer` role requests the `apiKey` field.

If `json_search()` does not enforce role-based access control, the function may return sensitive credential information.

Impact:

- Disclosure of sensitive authentication information.
- Potential unauthorized access to network infrastructure.

### Threat 2 - Unauthorized Access to Management Information

A user with the `viewer` role requests the `managementIpAddress` field.

If access control is not enforced, network management information may be disclosed to an unauthorized role.

## 6. Security Requirements

### SR-01 - Role-Based Access Control

`json_search()` must accept an optional `role` parameter.

The function must check the requested key against `POLICY` before returning matching values.

### SR-02 - Protect apiKey

Only the `admin` role may retrieve values of the `apiKey` field.

For example:

`json_search("apiKey", data, role="viewer")` must return an empty list.

### SR-03 - Protect managementIpAddress

Only `admin` and `operator` may retrieve values of the `managementIpAddress` field.

A `viewer` requesting this field must receive an empty list.

### SR-04 - Allow issueSummary

The roles `admin`, `operator`, and `viewer` may retrieve values of the `issueSummary` field.

### SR-05 - Recursive Search

`json_search()` must recursively search nested dictionaries and lists.

All matching values found at any nesting level must be aggregated into the returned list.

### SR-06 - Unauthorized Access Must Not Return Data

When a role is not authorized to access a requested key, `json_search()` must return an empty list instead of returning the matching sensitive values.

## 7. Verification

The implementation must be verified using Python `unittest`.

The test suite must include:

- At least three functional tests.
- At least three security tests derived from the threat model and security requirements.

All tests must pass before the implementation is approved.
