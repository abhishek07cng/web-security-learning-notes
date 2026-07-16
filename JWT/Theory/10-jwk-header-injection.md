# JWK Header Injection

## Overview

The `jwk` header allows a JSON Web Key to be embedded directly inside the JWT.

Some vulnerable applications incorrectly trust this attacker-supplied key.

---

# Attack Concept

Attacker:

```text
Generates Key Pair
        ↓
Signs JWT
        ↓
Embeds Public Key In Header
        ↓
Server Uses Attacker Key
```

---

# Simplified Flow

```text
Attacker Key
        ↓
JWT Header
        ↓
Server Imports Key
        ↓
Signature Accepted
```

---

# Indicators

```text
JWT Authentication
RS256
Embedded JWK
```

---

# Related Lab

```text
Lab04
```

---

# Mitigation

- Ignore user-supplied JWK values.
- Maintain a trusted server-side key store.
- Validate key origin before use.

---

# Key Takeaways

The server should choose the verification key—not the client.