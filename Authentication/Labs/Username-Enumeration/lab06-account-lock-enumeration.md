# Lab06 - Username Enumeration via Account Lock

## Objective

Gain access to the victim account by exploiting username enumeration through account lock behavior.

---

## Lab Difficulty

```text
Apprentice
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Username Enumeration via Account Locking
```

The application reveals valid usernames through differences in lockout behavior after multiple failed login attempts.

---

## Understanding the Vulnerability

Many applications implement account locking to defend against brute-force attacks.

However, if lockout behavior differs between:

- valid usernames
- invalid usernames

attackers can use these differences to enumerate valid accounts.

---

## Example Scenario

### Invalid Username

```text
Invalid username or password
```

### Valid Username After Multiple Attempts

```text
Too many incorrect login attempts
```

This confirms the username exists on the system.

---

# Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

### Authentication Endpoint

```http
POST /login HTTP/1.1
```

---

## Initial Observations

During testing:

- invalid usernames consistently returned generic responses
- valid usernames triggered account lock behavior after repeated failures

This indicated a username enumeration vulnerability.

---

# Attack Methodology

The attack was performed in two phases:

1. Enumerate valid usernames using account locking behavior
2. Brute-force the password for the identified user

---

# Phase 1 - Username Enumeration

## Step 1 - Capture Login Request

The login request was intercepted using Burp Suite Proxy.

---

## Step 2 - Send Request to Intruder

The request was sent to:

```text
Burp Suite → Intruder
```

---

## Step 3 - Configure Username Payload

The username parameter was selected as the payload position.

Example:

```http
username=§user§&password=invalidpassword
```

---

## Step 4 - Load Username Wordlist

A username wordlist was loaded into Intruder.

Example usernames:

```text
administrator
carlos
wiener
support
```

---

## Step 5 - Launch Attack

The Intruder attack was started.

Each username received multiple failed login attempts.

---

## Step 6 - Analyze Responses

Responses were analyzed for:

| Indicator | Purpose |
|---|---|
| Lockout Messages | Identify valid usernames |
| Response Length | Detect behavioral differences |
| HTTP Status Codes | Authentication changes |
| Response Content | Account lock behavior |

---

## Step 7 - Identify Valid Username

One username triggered a lockout response such as:

```text
Too many incorrect login attempts
```

This confirmed the username existed on the system.

---

# Phase 2 - Password Brute Force

After identifying the valid username, password brute-forcing was performed.

---

## Step 1 - Fix Username

The valid username was inserted into the request.

Example:

```http
username=carlos&password=§password§
```

---

## Step 2 - Configure Password Payload

A password wordlist was loaded into Intruder.

---

## Step 3 - Launch Password Attack

Responses were analyzed for successful authentication indicators.

---

## Indicators of Successful Login

Successful authentication commonly produced:

- HTTP 302 redirect
- Different response length
- Session cookie creation
- Access to authenticated pages

---

## Result

The valid password for the victim account was successfully identified.

Authenticated access was obtained.

---

# Burp Suite Configuration

## Attack Type

```text
Sniper Attack
```

---

## Username Enumeration Payload

```http
username=§payload§
```

---

## Password Brute Force Payload

```http
password=§payload§
```

---

# Why the Vulnerability Exists

The application handled authentication differently for:

- existing users
- non-existent users

Valid accounts triggered lockout behavior while invalid usernames did not.

This exposed valid usernames to attackers.

---

# Security Risks

Username enumeration allows attackers to:

- reduce brute-force complexity
- identify administrator accounts
- automate credential attacks
- perform credential stuffing

---

# Additional Risk - Denial of Service

Attackers may intentionally trigger lockouts against legitimate users.

This can create denial-of-service conditions.

---

# Mitigation

Applications should:

- use identical responses for all failures
- normalize lockout behavior
- avoid exposing account existence
- implement proper rate limiting
- monitor suspicious authentication activity

---

# Secure Authentication Principle

Applications should ensure that:

- lockout messages do not reveal valid usernames
- authentication responses remain consistent
- attackers cannot distinguish account existence

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Intruder | Automate enumeration |
| Wordlists | Username/password testing |

---

# Key Learnings

- Learned how account lock behavior may expose usernames.
- Practiced response analysis using Burp Intruder.
- Improved understanding of authentication state handling.
- Understood why consistent lockout behavior is critical.

---

# Attack Flow Summary

```text
Capture Login Request
        ↓
Send to Intruder
        ↓
Trigger Multiple Failed Attempts
        ↓
Observe Lockout Behavior
        ↓
Identify Valid Username
        ↓
Brute-Force Password
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Account lock behavior should never reveal whether usernames exist.

> [!TIP]
> During testing, compare how applications behave after repeated failed login attempts.

> [!WARNING]
> Authentication protections themselves may accidentally introduce username enumeration vulnerabilities.