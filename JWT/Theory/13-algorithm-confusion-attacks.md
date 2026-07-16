# Algorithm Confusion Attacks

## Overview

Algorithm confusion occurs when an attacker forces a server to verify a JWT using a different algorithm than intended.

Also known as:

```text
Key Confusion Attack
```

---

# Symmetric Algorithms

Example:

```text
HS256
```

Uses:

```text
Secret Key
        ↓
Sign
And
Verify
```

---

# Asymmetric Algorithms

Example:

```text
RS256
```

Uses:

```text
Private Key → Sign
Public Key  → Verify
```

---

# Vulnerability Concept

Expected:

```text
RS256
+
RSA Public Key
```

Attacker changes:

```text
alg = HS256
```

A vulnerable implementation may treat the RSA public key as an HMAC secret.

---

# Attack Flow

```text
Obtain Public Key
        ↓
Change Algorithm
        ↓
Use Public Key As Symmetric Secret
        ↓
Modify Claims
        ↓
Sign JWT
        ↓
Server Accepts Token
```

---

# Root Cause

```text
Server Trusts alg Header
+
Algorithm-Agnostic Verification
```

---

# Indicators

```text
RS256 Tokens
Public Key Available
User-Controlled alg Header
JWT Library Misconfiguration
```

---

# Related Lab

```text
Lab07
```

---

# Key Takeaways

The server should determine the expected algorithm, not the JWT.