# MD5 Hashing Notes

## Overview

MD5 is a cryptographic hashing algorithm that produces a:

```text
128-bit hash value
```

It was once widely used for:

- password hashing
- integrity verification
- authentication systems

However, MD5 is now considered insecure.

---

# Example MD5 Hash

## Plaintext

```text
password123
```

---

## MD5 Hash

```text
482c811da5d5b4bc6d497ffa98491e38
```

---

# Why MD5 Is Weak

MD5 is vulnerable because:

- it is computationally fast
- collisions exist
- rainbow tables exist
- GPUs crack MD5 extremely quickly

---

# Common MD5 Risks

| Weakness | Risk |
|---|---|
| Fast Hashing | Easy brute force |
| No Salting | Rainbow table attacks |
| Public Databases | Instant cracking |
| Collision Attacks | Integrity weaknesses |

---

# MD5 in Authentication

Weak applications sometimes use MD5 inside:

- remember-me cookies
- password storage
- session tokens

Example:

```text
base64(username:md5(password))
```

This is insecure.

---

# Common MD5 Identification

MD5 hashes commonly:

- contain 32 hexadecimal characters

Example:

```text
5f4dcc3b5aa765d61d8327deb882cf99
```

---

# Offline Password Cracking

Attackers commonly crack MD5 hashes using:

- Hashcat
- John the Ripper
- online databases
- rainbow tables

---

# Why Offline Cracking Is Dangerous

Offline attacks:

- bypass rate limits
- bypass account lockouts
- run extremely fast

---

# Common Cracking Workflow

```text
Extract Hash
        ↓
Identify Hash Type
        ↓
Load Wordlist
        ↓
Perform Offline Cracking
        ↓
Recover Plaintext Password
```

---

# Common Tools

| Tool | Purpose |
|---|---|
| Hashcat | GPU cracking |
| John the Ripper | Password cracking |
| CrackStation | Online hash lookup |
| CyberChef | Hash analysis |

---

# Common MD5 Indicators

| Indicator | Meaning |
|---|---|
| 32 Hex Characters | Possible MD5 |
| Fast Cracking | Weak hashing |
| No Salt | High risk |

---

# Better Alternatives

Applications should use:

- bcrypt
- Argon2
- PBKDF2

These algorithms are:

- slower
- salted
- resistant to brute force

---

# Key Takeaways

- MD5 is NOT secure for password storage.
- Fast hashing makes brute-force attacks practical.
- Modern applications should avoid MD5 completely.

> [!WARNING]
> MD5 should never be used for password hashing.

> [!IMPORTANT]
> Unsalted MD5 hashes are highly vulnerable to offline cracking attacks.