# Lab05 - Broken Brute-Force Protection via IP Block

## Objective

Gain access to the victim account by bypassing flawed brute-force protection mechanisms.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Broken Brute-Force Protection
```

The application attempts to prevent brute-force attacks using IP-based protection and account lock behavior.

However, flawed implementation logic allows attackers to bypass these protections.

---

## Understanding the Vulnerability

The application blocks authentication attempts after repeated failed logins.

However:

- failed-attempt counters reset improperly
- successful logins reset protections
- brute-force logic can be manipulated

This allows attackers to continue automated password attacks.

---

# Initial Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

### Authentication Endpoint

```http
POST /login HTTP/1.1
```

---

## Initial Observations

During testing:

- multiple failed attempts triggered temporary restrictions
- IP blocking behavior was inconsistent
- successful authentication reset protection counters

This indicated flawed brute-force protection logic.

---

# Understanding the Protection Logic

The application used:

- IP-based login restrictions
- failed-attempt counters
- temporary blocking behavior

However, the protection mechanism failed to properly track authentication state.

---

# Attack Strategy

The attack worked by:

1. Sending several failed login attempts
2. Logging into a valid account
3. Resetting the protection counter
4. Continuing brute-force attempts

This bypassed the lockout mechanism entirely.

---

# Attack Methodology

---

# Phase 1 - Identify Protection Behavior

## Step 1 - Send Failed Login Attempts

Several invalid login attempts were submitted.

Example:

```http
username=carlos&password=test123
```

---

## Step 2 - Observe Application Behavior

After repeated failures:

- login restrictions appeared
- temporary blocking occurred
- response behavior changed

---

## Step 3 - Test Counter Reset Behavior

A successful login using a known valid account was performed.

Example:

```http
username=wiener&password=peter
```

After successful authentication:

- brute-force protections reset
- login attempts became available again

This confirmed flawed lockout logic.

---

# Phase 2 - Automate the Attack

## Attack Logic

The attack alternated between:

- invalid login attempts
- valid login requests

This continuously reset protection counters.

---

## Example Workflow

```text
Attempt 1 → Invalid
Attempt 2 → Invalid
Attempt 3 → Valid Login
Counter Reset
Repeat
```

---

# Burp Intruder Configuration

## Step 1 - Capture Login Request

The login request was intercepted using Burp Suite Proxy.

---

## Step 2 - Send Request to Intruder

The request was sent to:

```text
Burp Suite → Intruder
```

---

## Step 3 - Configure Payload Positions

Payload positions were configured for:

- username
- password

depending on attack stage.

---

## Step 4 - Load Password Wordlist

A password list was loaded into Intruder.

---

## Step 5 - Launch Attack

The attack was automated while alternating successful requests to bypass restrictions.

---

# Custom Automation Logic

To automate the bypass process efficiently, custom payload logic was used.

The workflow continuously:

1. attempted brute-force passwords
2. inserted successful login attempts
3. reset lockout counters
4. resumed brute-forcing

---

# Response Analysis

Successful authentication was identified using:

| Indicator | Purpose |
|---|---|
| HTTP 302 Redirect | Successful login |
| Response Length | Behavioral changes |
| Session Cookie | Authenticated state |
| Redirect Location | Account access |

---

# Result

The valid password for the target account was successfully discovered.

Authenticated access was obtained despite brute-force protections.

---

# Root Cause

The application improperly reset brute-force protections after successful authentication.

This allowed attackers to manipulate authentication state and bypass lockout restrictions.

---

# Security Risks

Weak brute-force protections may allow attackers to:

- automate credential attacks
- bypass account lockouts
- compromise accounts
- conduct credential stuffing attacks

---

# Why IP-Based Blocking Is Weak

IP-only protection is insufficient because attackers may use:

- VPNs
- proxies
- TOR
- distributed infrastructure

---

# Mitigation

Applications should:

- implement strong rate limiting
- enforce MFA
- track suspicious authentication behavior
- prevent counter reset abuse
- monitor login anomalies
- use behavioral analysis

---

# Secure Authentication Principles

Applications should:

- separate successful login state from brute-force counters
- prevent authentication reset abuse
- detect automation behavior
- monitor repeated login patterns

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Request interception |
| Burp Intruder | Automated brute force |
| Wordlists | Password attacks |
| Custom Payload Logic | Counter reset bypass |

---

# Key Learnings

- Learned how flawed brute-force protections can be bypassed.
- Practiced authentication automation techniques.
- Improved understanding of lockout mechanisms.
- Understood why authentication logic flaws are dangerous.

---

# Attack Flow Summary

```text
Capture Login Request
        ↓
Trigger Lockout Protection
        ↓
Analyze Counter Reset Logic
        ↓
Perform Valid Login
        ↓
Reset Protection Counter
        ↓
Continue Brute Force
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Weak brute-force protection logic may be bypassed through authentication state manipulation.

> [!TIP]
> During testing, always analyze how failed-attempt counters reset.

> [!WARNING]
> IP-based protections alone provide limited defense against automated attacks.