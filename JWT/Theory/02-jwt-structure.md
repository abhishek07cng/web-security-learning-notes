# JWT Structure

## Overview

A JWT consists of three parts separated by dots:

```text
Header
.
Payload
.
Signature
```

Example:

```text
xxxxx.yyyyy.zzzzz
```

---

# Header

Contains metadata about the token.

Example fields:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Common parameters:

```text
alg
typ
kid
jwk
jku
```

---

# Payload

Contains user claims.

Example:

```json
{
  "sub":"wiener",
  "role":"user",
  "exp":1711111111
}
```

Common claims:

```text
sub
iss
aud
exp
iat
nbf
role
email
```

---

# Signature

Generated using:

```text
Header
+
Payload
+
Secret / Private Key
```

The server verifies the signature before trusting the token.

---

# Visual Flow

```text
Header
        ↓
Payload
        ↓
Signature
        ↓
JWT
```

---

# Key Takeaways

Only the signature protects the integrity of the token.