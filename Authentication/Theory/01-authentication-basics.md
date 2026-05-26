# Authentication Basics

## Overview

Authentication is the process of verifying the identity of a user, client, or system before granting access to protected resources.

Since web applications are publicly accessible over the internet, robust authentication mechanisms are one of the most critical components of web security.

Weak or improperly implemented authentication systems can allow attackers to:

* Gain unauthorized access to user accounts
* Escalate privileges
* Access sensitive information
* Completely compromise applications and infrastructure

---

# Types of Authentication Factors

Authentication mechanisms generally rely on one or more of the following authentication factors.

| Authentication Factor | Description                    | Example                                    |
| --------------------- | ------------------------------ | ------------------------------------------ |
| Something You Know    | Knowledge-based authentication | Password, PIN, Security Question           |
| Something You Have    | Physical possession factor     | Mobile Phone, Hardware Token, Security Key |
| Something You Are     | Biometric or behavioral factor | Fingerprint, Face ID, Voice Pattern        |

Modern applications often combine multiple authentication factors to improve security.

---

# Authentication vs Authorization

Authentication and authorization are closely related concepts but serve different purposes.

| Concept        | Purpose                                 |
| -------------- | --------------------------------------- |
| Authentication | Verifies who the user is                |
| Authorization  | Verifies what the user is allowed to do |

## Example

* Authentication verifies whether a user logging in as `Carlos123` is actually the legitimate owner of that account.
* Authorization determines what actions the authenticated user can perform.

For example, an authenticated administrator may be authorized to:

* Delete user accounts
* View sensitive information
* Modify application settings

A low-privileged user may only be authorized to:

* View their own profile
* Update personal information
* Access limited functionality

---

# How Authentication Vulnerabilities Arise

Authentication vulnerabilities commonly occur due to one of the following reasons.

## 1. Weak Authentication Mechanisms

Authentication systems may fail to adequately protect against attacks such as:

* Brute-force attacks
* Credential stuffing
* Password guessing
* Username enumeration

Weak brute-force protection can allow attackers to automate login attempts until valid credentials are discovered.

---

## 2. Broken Authentication Logic

Poor implementation or flawed verification logic can allow attackers to bypass authentication mechanisms entirely.

This is commonly referred to as:

> Broken Authentication

Examples include:

* Skipping 2FA verification
* Improper session validation
* Insecure password reset workflows
* Predictable authentication tokens

Authentication logic flaws are especially dangerous because authentication is a core security boundary.

---

# Impact of Authentication Vulnerabilities

The impact of vulnerable authentication mechanisms can be severe.

If an attacker successfully compromises an account, they gain access to all data and functionality associated with that account.

## Potential Consequences

### Compromise of Sensitive Data

Attackers may gain access to:

* Personal user information
* Financial data
* Business documents
* Internal application functionality

---

### Privilege Escalation

If a high-privileged account such as an administrator account is compromised, attackers may:

* Take full control of the application
* Access internal infrastructure
* Modify or delete data
* Create backdoor accounts

---

### Expanded Attack Surface

Even low-privileged accounts may expose additional internal functionality that is inaccessible to unauthenticated users.

This can increase the overall attack surface of the application.

---

# Common Authentication Attack Types

Authentication systems are frequently targeted using the following attacks.

| Attack Type          | Purpose                                |
| -------------------- | -------------------------------------- |
| Brute Force          | Guess valid credentials                |
| Username Enumeration | Identify valid usernames               |
| Credential Stuffing  | Reuse leaked credentials               |
| Password Spraying    | Try common passwords across many users |
| MFA Bypass           | Circumvent multi-factor authentication |
| Session Attacks      | Abuse session tokens or cookies        |

---

# Authentication Security Principles

Secure authentication systems should:

* Use strong password policies
* Enforce HTTPS
* Implement robust rate limiting
* Prevent username enumeration
* Use secure session management
* Properly validate MFA
* Use high-entropy tokens
* Protect password reset workflows

---

# Key Takeaways

* Authentication verifies identity.
* Authorization determines permissions.
* Weak authentication mechanisms are a major attack surface.
* Broken authentication logic can completely compromise applications.
* Multi-factor authentication significantly improves security when implemented correctly.
* Proper brute-force protection and generic error handling are essential.

---

# Tools Commonly Used During Authentication Testing

| Tool          | Purpose                             |
| ------------- | ----------------------------------- |
| Burp Suite    | Intercepting and modifying requests |
| Burp Intruder | Brute-force and enumeration attacks |
| Burp Repeater | Manual request testing              |
| ffuf          | Automated fuzzing and brute-forcing |
| Hashcat       | Offline password cracking           |
| CyberChef     | Encoding and decoding operations    |

---

# Real-World Testing Methodology

A common authentication testing workflow includes:

1. Identify authentication endpoints
2. Capture requests using Burp Suite
3. Test for username enumeration
4. Analyze brute-force protections
5. Test MFA implementation
6. Inspect cookies and session tokens
7. Test password reset functionality
8. Review remember-me functionality
9. Analyze authorization boundaries
10. Document findings and mitigations

---

> [!IMPORTANT]
> Authentication mechanisms are one of the most heavily targeted components of modern web applications.

> [!TIP]
> During testing, always compare status codes, response lengths, error messages, and response timing differences.

> [!WARNING]
> Improperly implemented authentication can lead to complete application compromise.
