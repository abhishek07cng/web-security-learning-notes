# JKU Header Injection

## Overview

The `jku` header parameter specifies a URL containing a JSON Web Key Set (JWKS).

The server may fetch public keys from this URL when verifying JWT signatures.

---

# Normal Flow

```text
JWT
        ↓
Trusted JKU URL
        ↓
Fetch Trusted JWKS
        ↓
Verify Signature
```

---

# Vulnerable Flow

```text
Attacker Controls JKU
        ↓
Server Fetches Attacker JWKS
        ↓
Attacker Public Key Loaded
        ↓
Forged JWT Accepted
```

---

# Attack Concept

The attacker:

```text
Generates RSA Key Pair
        ↓
Hosts Public JWK
        ↓
Sets jku To Controlled Location
        ↓
Signs JWT With Private Key
```

---

# Important Header Parameters

```text
jku
kid
alg
```

The `kid` should identify the corresponding key inside the JWK Set.

---

# Indicators

```text
jku Header Present
JWKS Endpoint
RS256
Remote Key Retrieval
```

---

# Related Lab

```text
Lab05
```

---

# Mitigation

- Allowlist trusted JWKS locations.
- Never fetch arbitrary key URLs.
- Validate key origin.
- Pin trusted issuers and keys.

---

# Key Takeaways

The server must never allow an attacker to choose an arbitrary verification key source.