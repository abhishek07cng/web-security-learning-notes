# Bruteforcing Secret Keys

## Overview

JWTs using symmetric algorithms (such as HS256) rely on a shared secret.

If the secret is weak, attackers may recover it through brute-force attacks.

---

# Attack Flow

```text
Capture JWT
        ↓
Identify Algorithm
        ↓
Guess Secret
        ↓
Recover Key
        ↓
Forge Tokens
```

---

# Weak Secrets

Examples:

```text
secret
password
admin
123456
qwerty
```

---

# After Recovery

An attacker can create arbitrary JWTs.

Example claims:

```json
{
  "sub":"administrator",
  "role":"admin"
}
```

---

# Detection

Questions:

```text
Is HS256 Used?
Is The Secret Weak?
Can New Tokens Be Signed?
```

---

# Related Lab

```text
Lab03
```

---

# Mitigation

- Use long, random secrets.
- Rotate secrets periodically.
- Prefer asymmetric algorithms where appropriate.

---

# Key Takeaways

Weak signing keys completely undermine JWT security.