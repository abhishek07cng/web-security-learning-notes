# Lab02 - Username Enumeration via Subtle Response Differences

## Objective

Gain access to the victim account by identifying valid usernames through subtle differences in authentication responses.

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

Unlike obvious enumeration vulnerabilities, the application attempts to use generic authentication messages.

However, subtle behavioral differences still expose valid usernames.

---

## What Makes This Vulnerability Different?

The application does NOT reveal usernames directly through obvious error messages.

Instead, attackers must carefully analyze subtle differences such as:

- Response length
- Extra whitespace
- Hidden characters
- Minor content changes
- Response timing

These small inconsistencies may still expose valid accounts.

---

## Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

### Authentication Endpoint

```http
POST /login HTTP/1.1
```

---

## Initial Observations

The application returned nearly identical responses for:

- valid usernames
- invalid usernames

However, careful inspection revealed:

- slight response length variations
- subtle formatting differences

This indicated possible username enumeration.

---

# Attack Methodology

The attack was performed in two phases:

1. Enumerate valid usernames
2. Brute-force the password

---

# Phase 1 - Username Enumeration

## Step 1 - Capture Login Request

The authentication request was intercepted using Burp Suite Proxy.

---

## Step 2 - Send Request to Intruder

The request was sent to:

```text
Burp Suite → Intruder
```

---

## Step 3 - Configure Payload Position

The username parameter was selected as the payload position.

Example:

```http
username=§user§&password=test
```

---

## Step 4 - Load Username Wordlist

A candidate username wordlist was loaded into Intruder.

---

## Step 5 - Launch Attack

The Intruder attack was started.

---

## Step 6 - Analyze Responses Carefully

Since the differences were subtle, response analysis became critical.

The following indicators were analyzed:

| Indicator | Purpose |
|---|---|
| Response Length | Detect hidden differences |
| Response Content | Identify formatting variations |
| HTTP Status Codes | Detect authentication changes |
| Redirect Behavior | Identify successful processing |

---

## Step 7 - Identify Valid Username

One username produced a slightly different response length compared to the others.

This confirmed the existence of a valid account.

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

Successful responses commonly included:

- HTTP redirects
- Different response length
- Session cookies
- Access to authenticated pages

---

## Result

The valid password for the identified user account was successfully discovered.

The account was compromised.

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

# Why This Vulnerability Exists

The application attempted to prevent enumeration using generic error messages.

However, subtle implementation differences still exposed valid usernames through:

- response size variations
- formatting inconsistencies
- backend processing differences

---

# Security Risks

Subtle enumeration vulnerabilities are dangerous because developers may incorrectly believe the application is secure.

Attackers can still:

- identify valid users
- target administrator accounts
- automate password attacks
- conduct credential stuffing

---

# Mitigation

Applications should:

- Return identical responses
- Normalize response sizes
- Normalize response timing
- Avoid backend behavioral differences
- Prevent account discovery entirely

---

# Secure Authentication Principles

Applications should ensure:

- consistent error handling
- consistent response length
- consistent redirects
- consistent timing behavior

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Intruder | Automate enumeration |
| Response Analysis | Identify subtle differences |

---

# Key Learnings

- Learned how subtle response differences can expose valid usernames.
- Improved response analysis skills.
- Practiced identifying hidden behavioral inconsistencies.
- Understood why generic error messages alone are insufficient.

---

# Attack Flow Summary

```text
Capture Login Request
        ↓
Send to Intruder
        ↓
Enumerate Usernames
        ↓
Analyze Subtle Differences
        ↓
Identify Valid User
        ↓
Brute-Force Password
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Even tiny response differences may reveal valid usernames.

> [!TIP]
> During testing, always sort responses by length to identify anomalies quickly.

> [!WARNING]
> Generic error messages alone do not fully prevent username enumeration.