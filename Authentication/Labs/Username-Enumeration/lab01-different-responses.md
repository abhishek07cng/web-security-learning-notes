# Lab01 - Username Enumeration via Different Responses

## Objective

Gain access to the victim account by identifying valid credentials through observable differences in authentication responses.

---

## Lab Difficulty

```text
Apprentice
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Username Enumeration
```

The application behaves differently when valid and invalid usernames are supplied during authentication.

Attackers can analyze these behavioral differences to identify valid usernames before performing password brute-force attacks.

---

## What is Username Enumeration?

Username enumeration occurs when an application unintentionally reveals whether a username exists on the system.

This commonly happens through differences in:

- Error messages
- Response length
- HTTP status codes
- Response timing
- Redirect behavior

---

## Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

### Authentication Endpoint

```http
POST /login HTTP/1.1
```

---

## Initial Observations

During testing, the application returned different response behavior for:

- invalid usernames
- valid usernames

The response length changed noticeably when a valid username was supplied.

This confirmed the presence of a username enumeration vulnerability.

---

## Attack Methodology

The attack was performed in two phases:

1. Enumerate valid usernames
2. Brute-force the password for the identified user

---

# Phase 1 - Username Enumeration

## Step 1 - Capture Login Request

The login request was intercepted using Burp Suite Proxy.

---

## Step 2 - Send Request to Burp Intruder

The request was sent to:

```text
Burp Suite → Intruder
```

---

## Step 3 - Configure Username Payload

The username parameter was marked as the payload position.

Example:

```http
username=§user§&password=test
```

---

## Step 4 - Load Username Wordlist

A candidate username wordlist was loaded into Intruder.

Example usernames:

```text
carlos
administrator
admin
wiener
support
```

---

## Step 5 - Launch Attack

The Intruder attack was started.

Responses were analyzed using:

- Response length
- HTTP status code
- Response content

---

## Step 6 - Identify Valid Username

One response returned a noticeably different response length.

This indicated that the supplied username existed on the system.

---

# Phase 2 - Password Brute Force

After identifying a valid username, password brute-forcing was performed.

---

## Step 1 - Configure Password Payload

The identified username was fixed inside the request.

Example:

```http
username=carlos&password=§password§
```

---

## Step 2 - Load Password Wordlist

A password wordlist was loaded into Intruder.

---

## Step 3 - Launch Password Attack

The attack was started and responses were analyzed.

Indicators of successful authentication included:

- Different response length
- HTTP redirect
- Successful session creation

---

## Result

The valid password corresponding to the identified username was discovered successfully.

The account was compromised.

---

# Burp Suite Configuration

## Attack Type

```text
Sniper Attack
```

---

## Payload Positions

### Username Enumeration

```http
username=§payload§
```

### Password Brute Force

```http
password=§payload§
```

---

## Response Analysis

Responses were filtered using:

- Response length
- HTTP status code
- Redirect behavior

---

# Root Cause

The application handled authentication responses differently for:

- valid usernames
- invalid usernames

This allowed attackers to determine whether accounts existed on the system.

---

# Security Risks

Username enumeration significantly reduces brute-force complexity.

Attackers can:

- identify valid users
- target administrator accounts
- conduct credential stuffing attacks
- automate authentication attacks efficiently

---

# Mitigation

Applications should:

- Use generic authentication messages
- Normalize response lengths
- Normalize response timing
- Return consistent status codes
- Prevent account discovery

---

# Secure Example

## Insecure Response

```text
Invalid username
```

## Secure Response

```text
Invalid username or password
```

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Intruder | Automate enumeration |
| Wordlists | Username/password guessing |

---

# Key Learnings

- Learned how username enumeration occurs through response differences.
- Practiced using Burp Intruder for automated authentication testing.
- Improved response analysis techniques.
- Understood why consistent authentication responses are critical.

---

# Attack Flow Summary

```text
Capture Request
        ↓
Send to Intruder
        ↓
Enumerate Usernames
        ↓
Analyze Responses
        ↓
Identify Valid User
        ↓
Brute-Force Password
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Even small response differences may reveal valid usernames.

> [!TIP]
> Always compare response length and redirect behavior during authentication testing.

> [!WARNING]
> Username enumeration dramatically increases the effectiveness of brute-force attacks.