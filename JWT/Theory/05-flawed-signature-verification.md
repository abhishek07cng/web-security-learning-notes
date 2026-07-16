# Flawed Signature Verification

## Overview

JWT security depends on verifying the token's signature before trusting its contents.

If verification is flawed or skipped, attackers can modify claims freely.

---

# Common Mistakes

```text
Using decode() Instead Of verify()
Ignoring Signature Errors
Trusting Header Values
Accepting Invalid Algorithms
```

---

# Example

Original Claim:

```json
{
  "sub":"wiener",
  "role":"user"
}
```

Modified Claim:

```json
{
  "sub":"administrator",
  "role":"admin"
}
```

If the server skips verification, the modified token is accepted.

---

# Attack Flow

```text
Modify Payload
        ↓
Signature Not Verified
        ↓
Server Trusts Claims
        ↓
Authentication Bypass
```

---

# Related Labs

```text
Lab01
Lab02
Lab03
```

---

# Key Takeaways

- Never trust decoded JWTs without verifying the signature.
- Signature verification is the foundation of JWT security.