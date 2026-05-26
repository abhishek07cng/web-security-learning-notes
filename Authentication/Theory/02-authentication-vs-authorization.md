# 02 - Authentication vs Authorization

## Overview

Authentication and authorization are fundamental security concepts in web applications.

Although these terms are often used together, they serve completely different purposes.

| Concept        | Purpose                                                              |
| -------------- | -------------------------------------------------------------------- |
| Authentication | Verifies the identity of a user                                      |
| Authorization  | Determines what actions the authenticated user is allowed to perform |

---

## Authentication

Authentication is the process of verifying whether a user is genuinely who they claim to be.

Applications commonly verify identity using:

* Username and password
* Multi-factor authentication
* Security tokens
* Biometrics

### Example

When a user attempts to log in using:

```text
Username: carlos
Password: password123
```

the application checks whether the credentials are valid.

If the credentials are correct, the user is authenticated.

---

## Authorization

Authorization occurs after successful authentication.

It determines what resources or actions the authenticated user can access.

### Example

An administrator may be authorized to:

* Delete accounts
* Modify application settings
* Access sensitive records

A normal user may only be allowed to:

* View personal profile
* Update account information
* Access limited features

---

## Common Authorization Weaknesses

Improper authorization controls can lead to:

* Privilege escalation
* Insecure Direct Object References (IDOR)
* Access control vulnerabilities
* Unauthorized data access

---

## Key Takeaways

* Authentication verifies identity.
* Authorization verifies permissions.
* Both mechanisms must be implemented securely.
* Broken authentication and broken access control are among the most critical web vulnerabilities.

---


## Overview

Authentication vulnerabilities occur when authentication mechanisms are improperly designed or implemented.

These vulnerabilities may allow attackers to:

* Gain unauthorized access
* Enumerate valid users
* Bypass authentication entirely
* Escalate privileges
* Compromise sensitive accounts

---

## How Authentication Vulnerabilities Arise

Authentication vulnerabilities generally occur in two major ways.

---

## 1. Weak Authentication Mechanisms

Authentication systems may fail to properly defend against attacks such as:

* Brute-force attacks
* Credential stuffing
* Password spraying
* Username enumeration

### Example Weaknesses

* No rate limiting
* Weak password policies
* Predictable usernames
* Missing CAPTCHA protection

---

## 2. Broken Authentication Logic

Poor implementation logic can allow attackers to bypass authentication controls entirely.

This is commonly known as:

> Broken Authentication

### Common Examples

* Skipping MFA verification
* Predictable session tokens
* Insecure remember-me cookies
* Weak password reset workflows
* Missing token validation

---

## Why Authentication Vulnerabilities Are Dangerous

Authentication systems protect the primary security boundary of applications.

If authentication fails:

* attackers gain legitimate access
* security monitoring becomes harder
* malicious actions appear as valid user activity

---

## Common Authentication Attack Types

| Attack               | Purpose                                |
| -------------------- | -------------------------------------- |
| Brute Force          | Guess passwords                        |
| Username Enumeration | Discover valid users                   |
| Credential Stuffing  | Reuse leaked credentials               |
| Password Spraying    | Use common passwords across many users |
| MFA Bypass           | Circumvent additional verification     |
| Session Hijacking    | Steal authenticated sessions           |

---

## Typical Indicators During Testing

During authentication testing, pay attention to:

* Response length differences
* HTTP status code changes
* Error message inconsistencies
* Response timing differences
* Lockout behavior
* Session token patterns

---

## Attack Methodology

A common authentication testing workflow includes:

1. Identify authentication endpoints
2. Capture requests using Burp Suite
3. Test for username enumeration
4. Analyze brute-force protections
5. Test MFA implementation
6. Inspect cookies and session handling
7. Review password reset functionality
8. Document findings and mitigations

---

## Mitigation Strategies

Applications should:

* Use strong password policies
* Implement rate limiting
* Prevent username enumeration
* Enforce MFA
* Validate all tokens securely
* Use secure session management
* Normalize error messages

---

## Key Takeaways

* Authentication vulnerabilities are extremely high impact.
* Broken authentication can lead to full account compromise.
* Response analysis is critical during testing.
* Secure implementation is as important as strong security policies.

> [!IMPORTANT]
> Authentication flaws are one of the most common attack surfaces in web applications.

> [!TIP]
> Always compare response behavior carefully during login testing.
