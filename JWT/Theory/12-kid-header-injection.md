# KID Header Injection

## Overview

The `kid` parameter means:

```text
Key ID
```

It helps the server select the correct verification key.

However, insecure implementations may use `kid` directly when accessing a file or database.

---

# Vulnerable Flow

```text
JWT kid
        ↓
Filesystem Lookup
        ↓
Attacker Manipulates Path
        ↓
Unexpected Key Selected
```

---

# Path Manipulation Concept

Example pattern:

```text
../../path/to/predictable-file
```

If a predictable file is used as the verification key, an attacker may be able to reproduce the signing secret.

---

# Why Predictable Files Matter

The attacker wants a file whose contents are known.

Conceptually:

```text
Known File Contents
        ↓
Known Verification Key
        ↓
Token Can Be Re-Signed
```

---

# Indicators

```text
kid Header
Filesystem Key Storage
Different kid Values
Key Selection Errors
```

---

# Related Lab

```text
Lab06
```

---

# Personal Testing Question

Whenever I see:

```text
kid
```

I ask:

```text
How Does The Server Resolve This Key ID?
```

---

# Mitigation

- Map key IDs to trusted keys.
- Never treat `kid` as a filesystem path.
- Reject unknown key identifiers.

---

# Key Takeaways

Key identifiers are attacker-controlled input and require strict validation.