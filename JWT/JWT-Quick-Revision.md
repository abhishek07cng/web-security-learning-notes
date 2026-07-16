# JWT Quick Revision

## JWT Structure

```text
Header

↓

Payload

↓

Signature
```

---

## Header Parameters

```text
alg

kid

jwk

jku
```

---

## Common Claims

```text
sub

role

isAdmin

permissions

exp

iss

aud
```

---

## Algorithms

### Symmetric

```text
HS256

HS384

HS512
```

### Asymmetric

```text
RS256

ES256
```

---

## Common JWT Attacks

```text
Missing Signature Verification

alg=none

Weak Secret Keys

JWK Injection

JKU Injection

kid Injection

Algorithm Confusion
```

---

## Typical Impact

```text
Authentication Bypass

JWT Forgery

Privilege Escalation

Account Takeover
```

---

# Top Lessons From PortSwigger

1. JWT headers are attacker-controlled.

2. JWT payloads are attacker-controlled until verified.

3. Signature verification is the foundation of JWT security.

4. The server must select the verification algorithm.

5. Verification keys must come from trusted sources.

6. Weak secrets defeat HS256 security.

7. Key management is as important as cryptography.

---

# Personal JWT Formula

```text
Capture JWT

↓

Decode

↓

Claims

↓

Header

↓

Verification

↓

Impact
```