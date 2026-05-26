# Lab10 - Offline Password Cracking

## Objective

Gain access to the victim account by extracting and cracking password hashes offline.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Offline Password Cracking
```

The application exposes credential-derived information inside persistent authentication cookies.

Attackers can extract password hashes and crack them offline without interacting with the application further.

---

## Understanding Offline Password Cracking

Offline password cracking occurs when attackers obtain password hashes and attempt to recover plaintext passwords locally.

Unlike online brute-force attacks:

- no rate limiting exists
- no account lockout occurs
- attacks are extremely fast

---

## Why Offline Cracking Is Dangerous

Once attackers obtain hashes:

- defenses such as CAPTCHA become useless
- brute-force speed increases significantly
- password recovery becomes practical

---

# Reconnaissance

The login functionality and remember-me mechanism were analyzed using Burp Suite Proxy.

---

## Initial Observations

After enabling persistent login functionality, the application generated an authentication cookie.

Example:

```http
Cookie: stay-logged-in=TOKEN
```

---

## Step 1 - Decode Authentication Cookie

The cookie value was decoded using:

```text
CyberChef
Burp Decoder
```

Decoded example:

```text
wiener:51dc30ddc473d43a6011e9ebba6ca770
```

This revealed:

- username
- password hash

---

# Step 2 - Identify Hashing Algorithm

The extracted hash format matched:

```text
MD5
```

MD5 is considered insecure because it is vulnerable to rapid brute-force attacks.

---

# Attack Methodology

The attack focused on:

1. Extracting password hashes
2. Performing offline cracking
3. Recovering plaintext credentials

---

# Step 3 - Crack Password Hash Offline

The hash was cracked using:

- hash databases
- password wordlists
- cracking tools

Example recovered password:

```text
peter
```

---

## Why Offline Cracking Is Powerful

Unlike online authentication attacks:

| Online Attack | Offline Attack |
|---|---|
| Rate Limited | Unlimited Speed |
| Account Locking | No Restrictions |
| Detectable | Harder to Detect |
| Slow | Extremely Fast |

---

# Step 4 - Use Recovered Credentials

The recovered credentials were used to authenticate successfully.

Example:

```http
username=wiener
password=peter
```

---

# Result

The victim password was recovered successfully through offline password cracking.

Authenticated access was obtained.

---

# Root Cause

The application exposed password-derived information inside authentication cookies.

Additionally:

- weak hashing algorithms were used
- no salting was implemented
- predictable token structures existed

---

# Why MD5 Is Weak

MD5 is insecure because:

- it is computationally fast
- rainbow tables exist
- modern hardware cracks MD5 rapidly

---

# Common Testing Methodology

During testing, attackers commonly analyze:

- authentication cookies
- token structures
- encoding methods
- hash algorithms
- predictable credential storage

---

# Real-World Risks

Offline password cracking may allow attackers to:

- recover user passwords
- compromise reused credentials
- bypass authentication protections
- escalate privileges

---

# Mitigation

Applications should:

- avoid exposing password-derived data
- use secure password hashing
- use salted hashes
- use random authentication tokens
- avoid MD5 and SHA1

---

# Recommended Hashing Algorithms

Applications should prefer:

- bcrypt
- Argon2
- PBKDF2

---

# Secure Authentication Principles

Persistent authentication systems should:

- use random tokens
- validate sessions server-side
- avoid storing credential-derived values client-side

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| CyberChef | Decode Base64 |
| Burp Decoder | Analyze tokens |
| Hash Cracking Tools | Recover passwords |

---

# Key Learnings

- Learned how offline password cracking works.
- Practiced extracting password hashes from cookies.
- Improved understanding of weak hashing risks.
- Understood why secure token generation is critical.

---

# Attack Flow Summary

```text
Capture Authentication Cookie
        ↓
Decode Cookie Structure
        ↓
Extract Password Hash
        ↓
Identify Hash Algorithm
        ↓
Perform Offline Cracking
        ↓
Recover Plaintext Password
        ↓
Gain Authenticated Access
```

---

> [!IMPORTANT]
> Offline password cracking bypasses many traditional authentication defenses.

> [!TIP]
> During testing, always inspect cookies for credential-derived values and weak hashing.

> [!WARNING]
> Weak hashing algorithms such as MD5 should never be used for authentication-related functionality.