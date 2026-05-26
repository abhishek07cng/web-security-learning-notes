# 03 - Authentication Vulnerabilities

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
