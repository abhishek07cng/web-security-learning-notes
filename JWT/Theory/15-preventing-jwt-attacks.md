# Preventing JWT Attacks

## Principle 1 - Verify Every Signature

Never:

```text
Decode
        ↓
Trust Claims
```

Always:

```text
Verify
        ↓
Trust Claims
```

---

## Principle 2 - Allowlist Algorithms

Explicitly define:

```text
Expected Algorithm
```

Example concept:

```text
Only RS256
```

Reject unexpected algorithms.

---

## Principle 3 - Reject Unsigned Tokens

Never accept:

```text
alg = none
```

unless unsigned tokens are explicitly required by design.

---

## Principle 4 - Use Strong Secrets

For HMAC algorithms:

```text
Long
Random
High Entropy
```

Avoid:

```text
Default Secrets
Placeholder Secrets
Hardcoded Example Keys
```

---

## Principle 5 - Do Not Trust JWT Headers

Treat as untrusted:

```text
alg
jwk
jku
kid
cty
x5c
```

---

## Principle 6 - Use Trusted Keys

Verification keys should come from:

```text
Trusted Key Store
Trusted Issuer
Allowlisted JWKS Endpoint
```

---

## Principle 7 - Validate Claims

Validate:

```text
iss
aud
exp
nbf
sub
```

---

## Principle 8 - Keep Libraries Updated

Use maintained JWT libraries and secure verification APIs.

---

# Defense Formula

```text
Verify Signature
        +
Pin Algorithm
        +
Trust Known Keys
        +
Validate Claims
```

---

# Key Takeaways

JWT security depends on strict verification and trusted key management.

The client should never control how the server decides whether a token is trustworthy.