# JWT Attack Observations

## Observation 1

JWTs are **encoded**, not encrypted.

Anyone possessing a JWT can read its header and payload.

---

## Observation 2

JWT security depends entirely on proper signature verification.

Without verification:

```text
Claims Cannot Be Trusted
```

---

## Observation 3

The JWT Header Is Attacker Controlled

Never trust:

```text
alg
kid
jwk
jku
```

---

## Observation 4

The Payload Is Also Attacker Controlled

Never trust:

```text
role
sub
isAdmin
permissions
email
```

until the signature has been successfully verified.

---

## Observation 5

Symmetric JWTs

```text
HS256
HS384
HS512
```

are only as secure as the signing secret.

Weak secrets allow complete JWT forgery.

---

## Observation 6

Asymmetric JWTs

```text
RS256
ES256
```

can introduce:

```text
Algorithm Confusion

JWK Injection

JKU Injection
```

when implemented incorrectly.

---

## Observation 7

The Most Important Question

Never ask:

```text
Can I Read This JWT?
```

Ask:

```text
How Does The Server Decide To Trust This JWT?
```

---

# Personal Formula

```text
Capture JWT
        ↓
Decode
        ↓
Inspect Header
        ↓
Inspect Claims
        ↓
Understand Verification
        ↓
Assess Impact
```