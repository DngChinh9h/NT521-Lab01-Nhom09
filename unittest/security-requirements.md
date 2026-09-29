# Security Requirements - json_search()

## 1. Context

The `json_search()` function recursively searches JSON data returned by a network infrastructure monitoring API.

The returned JSON data may contain information about network devices, including management IP addresses, device information, and SNMP/API credentials.

## 2. Actors and Roles

The system has three roles:

- `admin`: authorized to access all fields defined in the access policy.
- `operator`: authorized to access operational information but not sensitive credentials.
- `viewer`: authorized to view non-sensitive information only.

## 3. Sensitive Assets

The following fields are considered sensitive:

- `apiKey`: contains credential information and must only be accessible by `admin`.
- `managementIpAddress`: contains network management information and is accessible by `admin` and `operator`.

The `issueSummary` field is considered non-sensitive and can be accessed by `admin`, `operator`, and `viewer`.

## 4. Trust Boundary

The trust boundary exists between the caller of `json_search()` and the JSON data returned by the network infrastructure monitoring API.

The function must not return a field to a caller unless the caller's role is authorized to access that field according to `POLICY`.


