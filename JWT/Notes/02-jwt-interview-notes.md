# JWT Interview Notes

## What Is JWT?

A JSON Web Token is a compact, URL-safe token used for authentication and authorization.

---

## JWT Structure

```text
Header

↓

Payload

↓

Signature
```

---

## Why Use JWT?

```text
Stateless Authentication

REST APIs

Microservices
```

---

## Common JWT Attacks

```text
Missing Signature Verification

alg=none

Weak Secrets

JWK Injection

JKU Injection

kid Injection

Algorithm Confusion
```

---

## Why Are JWT Attacks Dangerous?

They can lead to:

```text
Authentication Bypass

Privilege Escalation

Account Takeover
```

---

## Best Defense

```text
Verify Every Signature

Pin Algorithms

Trust Only Known Keys

Validate Claims
```