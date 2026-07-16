# What Are JWTs?

## Overview

A JSON Web Token (JWT) is a compact, URL-safe format used to securely transfer claims between two parties.

JWTs are commonly used for:

```text
Authentication
Session Management
Access Control
Authorization
Identity Propagation
```

Unlike traditional server-side sessions, JWTs store user information inside the token itself.

---

# Why JWTs Are Popular

JWTs are:

```text
Stateless
Compact
Portable
Scalable
```

This makes them ideal for:

```text
REST APIs
Microservices
Distributed Systems
```

---

# What Can JWTs Contain?

JWT payloads contain claims such as:

```text
Username
User ID
Role
Email
Expiration Time
Issuer
Audience
```

---

# Common Use Cases

```text
Login Sessions
Single Sign-On (SSO)
OAuth
API Authentication
```

---

# Security Note

JWT payloads are **Base64URL encoded**, not encrypted.

Anyone with the token can read its contents.

---

# Key Takeaways

- JWTs are self-contained tokens.
- Security relies on proper signature verification.
- Sensitive data should not be stored in plaintext claims.