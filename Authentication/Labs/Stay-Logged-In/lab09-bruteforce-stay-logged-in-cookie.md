# Lab09 - Brute-Forcing Stay Logged In Cookie

## Objective

Gain access to the victim account by exploiting weak remember-me cookie generation and brute-forcing authentication credentials.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Weak Remember-Me Cookie Generation
```

The application uses predictable remember-me cookies based on weak cryptographic construction.

Attackers can analyze the cookie structure and brute-force authentication credentials offline.

---

## Understanding the Vulnerability

The application provides a:

```text
Stay Logged In
Remember Me
```

feature using persistent authentication cookies.

However, the cookie is generated insecurely using predictable values.

---

## Vulnerable Cookie Structure

The remember-me cookie followed a structure similar to:

```text
base64(username:md5(password))
```

This design is insecure because:

- Base64 is reversible
- MD5 is weak
- password hashes become brute-force targets

---

# Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

---

## Initial Observations

After enabling:

```text
Stay Logged In
```

the application generated a persistent authentication cookie.

Example:

```http
Cookie: stay-logged-in=TOKEN
```

---

## Step 1 - Decode Cookie

The cookie value was decoded using:

```text
CyberChef
Burp Decoder
```

Decoded structure:

```text
wiener:51dc30ddc473d43a6011e9ebba6ca770
```

This revealed:

- username
- MD5 password hash

---

# Attack Methodology

The attack focused on:

1. Understanding cookie generation logic
2. Cracking the password hash
3. Reconstructing the victim cookie

---

# Step 2 - Identify Hashing Algorithm

The extracted hash matched the format of:

```text
MD5
```

MD5 is considered cryptographically weak and highly vulnerable to brute-force attacks.

---

## Step 3 - Crack Password Hash

The MD5 hash was cracked using:

- online hash databases
- wordlists
- offline cracking techniques

Example cracked password:

```text
peter
```

---

## Step 4 - Construct Victim Cookie

After understanding the cookie format:

```text
base64(username:md5(password))
```

a new cookie was generated for the victim account.

Example:

```text
carlos:md5(victim_password)
```

---

## Step 5 - Encode Cookie

The constructed value was Base64 encoded.

---

## Step 6 - Replace Authentication Cookie

The attacker replaced the original cookie with the forged victim cookie.

Example:

```http
Cookie: stay-logged-in=FORGED_TOKEN
```

---

## Step 7 - Access Victim Account

The application trusted the forged remember-me cookie and authenticated the attacker as the victim user.

---

# Result

Authenticated access to the victim account was obtained successfully.

---

# Root Cause

The application used insecure remember-me cookie generation based on:

- predictable values
- weak hashing
- reversible encoding

Instead of secure random authentication tokens.

---

# Why This Is Dangerous

Remember-me cookies effectively function as authentication credentials.

Weak token generation allows attackers to:

- bypass passwords
- forge authentication cookies
- persist access indefinitely

---

# Why Base64 Is Weak

Base64:

```text
IS NOT ENCRYPTION
```

It only encodes data and can be reversed instantly.

---

# Why MD5 Is Dangerous

MD5 is considered insecure because:

- it is extremely fast
- it is vulnerable to brute-force attacks
- rainbow tables already exist for common hashes

---

# Common Testing Methodology

During testing, attackers commonly analyze:

- cookie structure
- encoding methods
- hashing algorithms
- token predictability
- expiration behavior

---

# Real-World Risks

Weak remember-me functionality may allow attackers to:

- bypass authentication
- hijack sessions
- persist access
- compromise multiple accounts

---

# Mitigation

Applications should:

- use random high-entropy tokens
- avoid storing credential-derived values
- use secure server-side token validation
- expire tokens appropriately
- invalidate tokens after logout

---

# Secure Cookie Practices

Applications should use:

```http
HttpOnly
Secure
SameSite
```

cookie attributes whenever possible.

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| CyberChef | Decode Base64 |
| Burp Decoder | Cookie analysis |
| Hash Cracking Tools | Password recovery |

---

# Key Learnings

- Learned how weak remember-me cookies may expose credentials.
- Practiced Base64 decoding and hash analysis.
- Improved understanding of persistent authentication risks.
- Understood why secure token generation is critical.

---

# Attack Flow Summary

```text
Login with Remember Me Enabled
        ↓
Capture Authentication Cookie
        ↓
Decode Base64 Structure
        ↓
Identify MD5 Hash
        ↓
Crack Password Hash
        ↓
Forge Victim Cookie
        ↓
Gain Authenticated Access
```

---

> [!IMPORTANT]
> Persistent authentication cookies should never contain predictable credential-derived values.

> [!TIP]
> During testing, always inspect remember-me cookies for encoding and hashing patterns.

> [!WARNING]
> Weak remember-me implementations may completely bypass normal authentication protections.