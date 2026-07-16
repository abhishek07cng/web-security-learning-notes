# Unverified Signatures

## Overview

Some applications decode JWTs but fail to verify the signature before trusting the claims.

This allows attackers to modify the payload without possessing the signing key.

---

# How It Happens

Instead of:

```text
Verify JWT
        ↓
Accept Claims
```

The application performs:

```text
Decode JWT
        ↓
Accept Claims
```

---

# Example

Original Payload:

```json
{
  "sub":"wiener",
  "role":"user"
}
```

Modified Payload:

```json
{
  "sub":"administrator",
  "role":"admin"
}
```

If the server only decodes the JWT, the modified claims are accepted.

---

# Attack Flow

```text
Capture JWT
        ↓
Modify Claims
        ↓
Re-encode Token
        ↓
Server Skips Verification
        ↓
Privilege Escalation
```

---

# Detection

Look for applications that:

```text
Accept Modified Claims
Ignore Signature Changes
Never Return Signature Errors
```

---

# Related Lab

```text
Lab01
```

---

# Key Takeaways

- Decoding is not verification.
- Never trust JWT claims unless the signature has been verified.