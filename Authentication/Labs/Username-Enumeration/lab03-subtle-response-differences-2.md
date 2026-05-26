# Lab03 - Username Enumeration via Subtle Response Differences 2

## Objective

Gain access to the victim account by identifying valid usernames through subtle authentication response discrepancies and then brute-forcing the password.

---

## Lab Difficulty

```text
Apprentice
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Username Enumeration via Subtle Response Differences
```

The application attempts to hide account existence using generic authentication messages.

However, small differences in server responses still reveal whether usernames are valid.

---

## Understanding the Vulnerability

Applications sometimes try to prevent enumeration by displaying identical error messages such as:

```text
Invalid username or password
```

Despite this, subtle backend processing differences may still expose valid usernames through:

- response length
- response timing
- hidden formatting
- redirect behavior
- additional backend validation

---

## Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

### Authentication Endpoint

```http
POST /login HTTP/1.1
```

---

## Initial Observations

At first glance, all responses appeared identical.

However, after careful inspection:

- one response contained a slightly different response length
- backend processing behavior differed subtly
- valid usernames triggered additional validation logic

This confirmed the presence of username enumeration.

---

# Attack Methodology

The attack was performed in two phases:

1. Enumerate valid usernames
2. Brute-force the password

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
username=§user§&password=test
```

---

## Step 4 - Load Username Wordlist

A candidate username wordlist was loaded into Intruder.

Example usernames:

```text
administrator
carlos
wiener
support
```

---

## Step 5 - Launch Enumeration Attack

The Intruder attack was started.

---

## Step 6 - Analyze Responses

Responses were carefully analyzed using:

| Indicator | Purpose |
|---|---|
| Response Length | Detect subtle differences |
| HTTP Status Codes | Identify authentication behavior |
| Redirects | Detect state changes |
| Response Content | Identify formatting anomalies |

---

## Step 7 - Identify Valid Username

One username produced a slightly different response compared to the others.

This indicated the supplied username existed on the system.

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
- Different response size
- Authenticated session cookies
- Access to internal pages

---

## Result

The valid password for the victim account was successfully identified.

Authenticated access was obtained successfully.

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

Although the application used generic error messages, backend authentication logic still behaved differently for:

- valid usernames
- invalid usernames

This unintentionally exposed account existence.

---

# Common Backend Causes

Enumeration often occurs because applications:

- validate passwords only for existing users
- process database queries differently
- generate inconsistent responses
- return hidden formatting changes

---

# Security Risks

Username enumeration allows attackers to:

- identify valid users
- target privileged accounts
- reduce brute-force complexity
- automate credential attacks

---

# Mitigation

Applications should:

- normalize authentication responses
- normalize response timing
- use generic error messages
- avoid backend behavioral differences
- prevent account discovery entirely

---

# Secure Error Handling Example

## Insecure

```text
Incorrect password
```

## Secure

```text
Invalid username or password
```

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Request interception |
| Burp Intruder | Automated enumeration |
| Response Analysis | Detect subtle anomalies |

---

# Key Learnings

- Learned how subtle backend differences expose usernames.
- Improved response comparison techniques.
- Practiced automated enumeration using Burp Intruder.
- Understood why consistent authentication behavior is critical.

---

# Attack Flow Summary

```text
Capture Login Request
        ↓
Send to Intruder
        ↓
Enumerate Usernames
        ↓
Analyze Subtle Response Differences
        ↓
Identify Valid Username
        ↓
Brute-Force Password
        ↓
Gain Authenticated Access
```

---

> [!IMPORTANT]
> Applications may still leak usernames even when generic error messages are used.

> [!TIP]
> Sorting Intruder results by response length helps identify anomalies quickly.

> [!WARNING]
> Small backend behavioral differences may completely undermine authentication protections.