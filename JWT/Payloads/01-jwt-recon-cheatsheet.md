# JWT Recon Cheat Sheet

## Identify JWTs

Common Locations:

```text
Authorization: Bearer <JWT>

Cookie: session=<JWT>

Local Storage

Session Storage
```

---

## JWT Structure

```text
HEADER.PAYLOAD.SIGNATURE
```

---

## Interesting Header Fields

```text
alg
kid
jwk
jku
typ
cty
```

---

## Interesting Payload Claims

```text
sub
role
isAdmin
username
email
exp
iat
iss
aud
```

---

## Questions To Ask

```text
Can Claims Be Modified?

Does Signature Verification Exist?

What Algorithm Is Used?

Is HS256 Or RS256 Used?

Are Dangerous Header Parameters Present?
```

---

# Key Learnings

Always inspect both the JWT header and payload before testing.