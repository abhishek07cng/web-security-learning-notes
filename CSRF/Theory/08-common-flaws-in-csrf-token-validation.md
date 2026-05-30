# Common Flaws in CSRF Token Validation

## Overview

CSRF vulnerabilities often exist even when applications implement CSRF tokens.

The problem is usually not the token itself, but flaws in how the token is validated.

This file covers common CSRF token validation weaknesses and how attackers exploit them.

---

# Flaw 1: Validation Depends on Request Method

Some applications validate CSRF tokens only for:

```http
POST
```

requests.

When the request is converted to:

```http
GET
```

token validation is skipped.

---

## Example

Protected POST request:

```http
POST /email/change

csrf=token123
```

---

Unprotected GET request:

```http
GET /email/change?email=attacker@evil.com
```

---

## Exploitation

```text
Convert POST
        ↓
Change To GET
        ↓
Token Validation Bypassed
```

---

## Related Lab

```text
lab02-csrf-where-token-validation-depends-on-request-method.md
```

---

# Flaw 2: Validation Depends on Token Presence

Some applications validate tokens only if they exist.

---

## Example

Request with invalid token:

```http
csrf=fake123
```

Rejected.

---

Request without token:

```http
email=attacker@evil.com
```

Accepted.

---

## Exploitation

```text
Remove Token Parameter
        ↓
Validation Skipped
        ↓
Request Accepted
```

---

## Related Lab

```text
lab03-csrf-where-token-validation-depends-on-token-being-present.md
```

---

# Flaw 3: Token Not Tied To User Session

Some applications maintain a global pool of tokens.

Any valid token can be used by any user.

---

## Example

Attacker:

```text
Token = ABC123
```

Victim:

```text
Uses Same Token
```

Accepted.

---

## Exploitation

```text
Attacker Obtains Token
        ↓
Token Added To CSRF Payload
        ↓
Victim Uses Attacker Token
        ↓
Request Accepted
```

---

## Related Lab

```text
lab04-csrf-token-not-tied-to-user-session.md
```

---

# Flaw 4: Token Tied To Non-Session Cookie

Some applications bind tokens to:

```http
csrfKey
```

cookie instead of:

```http
session
```

cookie.

---

## Problem

If attackers can inject:

```http
csrfKey
```

they may use their own token.

---

## Exploitation

```text
Inject CSRF Cookie
        ↓
Provide Matching Token
        ↓
Validation Passes
```

---

## Related Lab

```text
lab05-csrf-token-tied-to-non-session-cookie.md
```

---

# Flaw 5: Token Duplicated In Cookie

Also known as:

```text
Double Submit Cookie
```

---

## Example

Cookie:

```http
csrf=token123
```

---

Request:

```http
csrf=token123
```

---

Validation:

```text
Cookie == Parameter
```

If both match:

```text
Request Accepted
```

---

# Why This Is Weak

The server stores no token state.

Attackers only need to set:

```http
csrf=fake
```

cookie and submit:

```http
csrf=fake
```

parameter.

---

## Exploitation

```text
Inject Fake Cookie
        ↓
Submit Matching Parameter
        ↓
Validation Passes
```

---

## Related Lab

```text
lab06-csrf-token-duplicated-in-cookie.md
```

---

# Common Testing Methodology

When testing CSRF tokens:

---

## Test 1

Remove token.

---

## Test 2

Modify token.

---

## Test 3

Switch request method.

---

## Test 4

Swap tokens between users.

---

## Test 5

Swap CSRF cookies.

---

## Test 6

Check double-submit implementation.

---

# CSRF Token Testing Checklist

```text
Remove Token
Change Token
Change Method
Swap User Tokens
Swap Cookies
Check Double Submit
```

---

# Related Payloads

- `csrf-token-analysis-notes.md`
- `csrf-token-bypass-techniques.md`
- `csrf-test-checklist.md`

---

# Related Labs

- `lab02`
- `lab03`
- `lab04`
- `lab05`
- `lab06`

---

# Key Takeaways

- A CSRF token alone does not guarantee protection.
- Validation logic is often flawed.
- Many real-world CSRF vulnerabilities arise from incorrect token implementation.
- Understanding token validation weaknesses is critical for web security testing.

> [!WARNING]
> Always test how a token is validated, not just whether a token exists.