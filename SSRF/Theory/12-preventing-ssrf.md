# Preventing SSRF

## Overview

SSRF vulnerabilities occur because applications allow untrusted input to determine where the server sends requests.

The most effective defense is to ensure that only trusted destinations can be accessed.

---

# Validate Destinations

Applications should validate the destination before making any server-side request.

Prefer strict allowlists over blocklists.

Example:

```
Allowed:

stock.example.com

Rejected:

Everything Else
```

---

# Avoid Blacklists

Blocking values such as:

```
127.0.0.1

localhost
```

is insufficient because attackers can use alternative representations and encoding techniques.

---

# Restrict Outbound Network Access

Limit which systems the application server can contact.

For example:

- Only approved APIs
- Required backend services
- Trusted external endpoints

---

# Disable Unnecessary Redirects

If redirects are not required, disable automatic redirect following.

Otherwise, validate the redirected destination before connecting.

---

# Protect Internal Services

Administrative interfaces should require authentication regardless of request origin.

Do not rely on:

- localhost
- Private IP ranges
- Internal network location

as the only security control.

---

# Secure Cloud Metadata

Restrict access to cloud metadata endpoints.

Ensure sensitive credentials cannot be retrieved by application requests.

---

# Monitor Outbound Requests

Log and review outbound HTTP requests.

Unexpected requests may indicate:

- SSRF attempts
- Malware
- Compromised applications

---

# Bug Bounty Perspective

When reporting SSRF, recommend:

- Strict allowlists
- URL validation
- Network segmentation
- Authentication for internal services
- Outbound request restrictions

---

# Key Learnings

Preventing SSRF requires both secure input validation and strong network controls. Internal services should never rely solely on network location for security.