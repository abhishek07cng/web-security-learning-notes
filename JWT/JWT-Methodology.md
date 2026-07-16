# JWT Testing Methodology

## Step 1

Identify JWT

Locations:

```text
Cookies

Authorization Headers

Local Storage

Session Storage
```

---

## Step 2

Decode

Inspect:

```text
Header

Payload
```

---

## Step 3

Identify Claims

Look For:

```text
sub

role

permissions

isAdmin
```

---

## Step 4

Inspect Header

Check:

```text
alg

kid

jwk

jku
```

---

## Step 5

Determine Algorithm

```text
HS256

RS256

ES256
```

---

## Step 6

Understand Verification

Questions:

```text
How Is The Signature Verified?

Which Key Is Used?

Who Controls That Key?
```

---

## Step 7

Review Key Management

```text
Embedded JWK

Remote JWKS

Filesystem Keys

Weak Secrets
```

---

## Step 8

Assess Impact

```text
Authentication Bypass

Privilege Escalation

JWT Forgery

Account Takeover
```

---

# Personal Formula

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