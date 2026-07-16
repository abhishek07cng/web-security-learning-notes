# Lab07 - JWT Authentication Bypass Via Algorithm Confusion

## Objective

Use the server's RSA public key to forge a valid HS256 token.

Delete:

```text
carlos
```

Credentials:

```text
wiener:peter
```

---

# Vulnerability Overview

The application normally uses:

```text
RS256
```

However, it accepts:

```text
HS256
```

using the server's public key as the HMAC secret.

---

# Attack Flow

```text
Download Public Key
        ↓
Convert To PEM
        ↓
Base64 Encode
        ↓
Create Symmetric Key
        ↓
alg = HS256
        ↓
Sign JWT
```

---

# Step 1

Download the server's public key.

---

# Step 2

Convert it into PEM.

Base64 encode the PEM.

---

# Step 3

Create:

```text
New Symmetric Key
```

Replace:

```text
k
```

with the Base64 PEM.

---

# Step 4

Modify:

```json
{
   "sub":"administrator"
}
```

Change:

```json
{
   "alg":"HS256"
}
```

Sign using the generated symmetric key.

Replay:

```http
GET /admin
```

Delete:

```text
carlos
```

---

# Why It Works

```text
Public Key

↓

Used As HMAC Secret

↓

HS256 Verification

↓

JWT Accepted
```

---

# Personal Analysis

Question:

```text
Does The Server Trust alg?

Can I Switch RS256 → HS256?
```

---

# Bug Bounty Indicators

```text
RS256

Public Key Exposure

Algorithm Switching
```

---

# Impact

```text
JWT Forgery

Authentication Bypass

Privilege Escalation
```

---

# Mitigation

```text
Pin Algorithms

Never Trust alg Header
```

---

# Related Theory

```text
13-algorithm-confusion-attacks.md
```

---

# Key Learnings

The server—not the JWT—must decide which algorithm to use.