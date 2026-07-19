# CORS Observations

## Purpose

This document contains practical observations and notes gathered while studying CORS vulnerabilities, solving PortSwigger labs, and performing bug bounty reconnaissance.

---

# Observation 1

CORS is **not** a server-side access control mechanism.

It only determines whether browser JavaScript can read a cross-origin response.

Attackers using tools such as Burp Suite, curl, or Postman can still send requests regardless of CORS.

---

# Observation 2

The most dangerous CORS vulnerability is:

```
Origin Reflection

+

Access-Control-Allow-Credentials: true
```

This allows an attacker-controlled website to read authenticated responses.

---

# Observation 3

Always inspect API endpoints.

Endpoints such as:

```
/api/
/me
/profile
/account
/settings
```

often return sensitive user information.

---

# Observation 4

The `Origin` header should never be blindly reflected.

Poor implementations often do:

```
Origin

↓

Access-Control-Allow-Origin
```

instead of validating against an allowlist.

---

# Observation 5

A wildcard (`*`) is usually low risk unless sensitive public information is exposed.

The highest-impact findings typically involve:

- Credentialed requests
- Sensitive data
- Dynamic origin reflection

---

# Observation 6

The special `null` origin is frequently overlooked.

Always test:

```http
Origin: null
```

---

# Observation 7

Trusted origins should also be audited.

Questions to ask:

- Does the trusted domain have XSS?
- Is it served over HTTP?
- Is it a staging environment?
- Is it still maintained?

---

# Observation 8

CORS findings become significantly more valuable when combined with:

- XSS
- Weak authentication
- Sensitive APIs
- Internal services

---

# Personal Notes

(Add your own findings here while solving labs or testing bug bounty targets.)

- _______________________________________

- _______________________________________

- _______________________________________