# Lab04 - JWT Authentication Bypass Via JWK Header Injection

## Objective

Create and sign a modified JWT that grants access to:

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

The server supports the JWT `jwk` header parameter.

The `jwk` parameter can contain a public verification key directly inside the JWT.

The vulnerable server fails to verify whether the embedded key comes from a trusted source.

---

# Vulnerable Flow

```text
Attacker Creates RSA Key Pair
        ↓
Attacker Signs JWT
        ↓
Public Key Embedded In jwk
        ↓
Server Trusts Embedded Key
        ↓
Signature Accepted
```

---

# Analysis & Exploitation Steps

## Step 1 - Install JWT Editor

In Burp Suite:

```text
BApp Store
        ↓
JWT Editor
```

Load the extension.

---

## Step 2 - Capture The JWT

Log in:

```text
wiener:peter
```

Send:

```http
GET /my-account
```

to Burp Repeater.

---

## Step 3 - Test Admin Access

Change the path:

```http
GET /admin
```

Send the request.

Admin access is denied.

---

## Step 4 - Open JWT Editor Keys

Go to:

```text
JWT Editor Keys
```

---

## Step 5 - Generate RSA Key

Click:

```text
New RSA Key
```

Then:

```text
Generate
```

Burp automatically generates an RSA key pair.

Click:

```text
OK
```

to save the key.

---

## Step 6 - Modify The JWT Payload

Return to the `/admin` request.

Open:

```text
JSON Web Token
```

Change the `sub` claim.

Original:

```json
{
  "sub": "wiener"
}
```

Modified:

```json
{
  "sub": "administrator"
}
```

---

## Step 7 - Perform Embedded JWK Attack

At the bottom of the JWT editor, click:

```text
Attack
        ↓
Embedded JWK
```

Select the RSA key generated earlier.

Click:

```text
OK
```

---

## Step 8 - Inspect The JWT Header

Burp adds a `jwk` parameter.

Conceptual structure:

```json
{
  "alg": "RS256",
  "jwk": {
    "kty": "RSA",
    "e": "AQAB",
    "kid": "ATTACKER-KEY-ID",
    "n": "ATTACKER-PUBLIC-KEY"
  }
}
```

The JWT is signed using the attacker's private key.

The matching public key is embedded in the JWT.

---

## Step 9 - Send The Forged JWT

Send:

```http
GET /admin
```

The server uses the attacker-controlled JWK to verify the signature.

The signature is valid for the embedded public key.

Admin access is granted.

---

## Step 10 - Delete Carlos

Find:

```http
/admin/delete?username=carlos
```

Send the request.

Lab solved.

---

# Why The Attack Works

The server accepts arbitrary public keys embedded in JWT headers.

```text
Attacker Private Key
        ↓
Signs JWT
        ↓
Attacker Public Key In jwk
        ↓
Server Trusts jwk
        ↓
JWT Verified
```

The cryptographic signature is valid.

The problem is:

```text
THE SERVER TRUSTS THE WRONG KEY
```

---

# Personal Analysis & Testing Process

This lab changed how I think about JWT signatures.

A valid signature does not automatically mean:

```text
Trusted Token
```

The real question is:

```text
Which Key Verified The Signature?
```

My testing logic:

```text
JWT Uses RS256
        ↓
Inspect JOSE Headers
        ↓
Check jwk Support
        ↓
Generate Own RSA Key
        ↓
Embed Public Key
        ↓
Sign With Private Key
```

---

# Bug Bounty Indicators

Look for JWT headers containing:

```text
jwk
kid
jku
```

Ask:

```text
Can I Influence The Verification Key?
```

Interesting behavior:

```text
Server Accepts Embedded JWK
Unknown kid Accepted
Attacker Key Accepted
```

---

# Impact

```text
JWT Forgery
Authentication Bypass
Privilege Escalation
Administrator Impersonation
Potential Account Takeover
```

---

# Mitigation

The server should:

```text
Use Trusted Verification Keys Only
```

It should not trust arbitrary keys embedded in JWT headers.

Use:

```text
Trusted Key Store
Key Allowlist
Trusted Issuer Validation
```

---

# Related Theory

```text
09-jwt-header-parameter-injection.md
10-jwk-header-injection.md
```

---

# Key Learnings

- `jwk` is attacker-controlled header data.
- A valid signature is meaningless if an attacker chooses the verification key.
- Verification keys must come from trusted server-side configuration.
- Always investigate how the application selects JWT verification keys.