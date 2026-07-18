# Lab 03 - Forced OAuth Profile Linking

## Lab Information

**Difficulty:** Practitioner

**Category**

- OAuth
- CSRF
- Account Linking
- Authentication
- Account Takeover

---

# Lab Objective

Use a CSRF attack to attach **your own social media account** to the administrator's account.

After linking succeeds:

- Login using your social account
- Become Administrator
- Delete Carlos

---

# Vulnerability

## Missing state Parameter

The OAuth linking flow does not include the mandatory:

```
state
```

parameter.

Because of this, the application cannot determine whether the OAuth callback belongs to the browser that initiated the linking process.

This allows an attacker to complete the linking flow inside another user's authenticated session.

---

# Root Cause

OAuth uses **state** as a CSRF token.

Expected flow:

```
User Starts OAuth

↓

Random state Generated

↓

OAuth Provider

↓

Returns Same state

↓

Server Validates state

↓

Link Account
```

Actual flow:

```
User Starts OAuth

↓

Authorization Code

↓

No state Validation

↓

Anyone Can Complete Callback
```

---

# Why This Is Dangerous

Instead of logging the victim into the attacker's account (Login CSRF),

the application permanently links:

```
Attacker Social Account

↓

Victim Local Account
```

After that,

the attacker simply clicks

```
Login With Social Media
```

and becomes the victim.

---

# Attack Flow

```
Attacker

↓

Starts OAuth Linking

↓

Receives Authorization Code

↓

Intercepts Callback

↓

Drops Request

↓

Creates CSRF

↓

Victim Loads Page

↓

Victim Completes Callback

↓

Attacker Social Account Linked

↓

Attacker Logs In

↓

Victim Account
```

---

# Burp Analysis

Capture:

```
GET /auth
```

Notice:

```
redirect_uri=/oauth-linking
```

More importantly,

observe:

```
NO state PARAMETER
```

---

# Exploitation Walkthrough

## Step 1

Login normally.

```
wiener

peter
```

---

## Step 2

Choose

```
Attach Social Profile
```

---

## Step 3

Authenticate with social account.

```
peter.wiener

hotdog
```

---

## Step 4

Intercept:

```
GET /oauth-linking?code=...
```

---

## Step 5

Copy the URL.

Example

```
https://target.com/oauth-linking?code=ABC123
```

---

## Step 6

Drop the request.

Do **NOT** forward it.

Authorization codes are single-use.

---

## Step 7

Create exploit.

```html
<iframe src="https://target.com/oauth-linking?code=ABC123"></iframe>
```

---

## Step 8

Deliver exploit.

Administrator loads iframe.

Browser automatically sends:

```
Session Cookie

+

Authorization Code
```

The server links:

```
Admin Account

↓

Attacker Social Account
```

---

## Step 9

Login using

```
Login With Social Media
```

You become Administrator.

Delete Carlos.

---

# Visual Attack Diagram

```
Attacker

↓

OAuth Linking

↓

Authorization Code

↓

iframe

↓

Victim Browser

↓

Victim Session Cookie

↓

Server Links Accounts

↓

Attacker Logs In As Victim
```

---

# Why It Works

The callback endpoint assumes:

```
Authorization Code

↓

Must Belong To Current User
```

Without validating:

```
state
```

there is no proof that the callback belongs to the browser that initiated OAuth.

---

# Detection Checklist

During testing ask:

```
Does Authorization Request Include state?

↓

Is state Random?

↓

Is state Bound To Session?

↓

Is state Validated?

↓

Can Callback Be Replayed?
```

---

# Real-World Bug Bounty Cases

Very similar vulnerabilities have appeared on:

- Shopify
- Slack
- Mixmax
- Gratipay

These resulted in:

```
Account Takeover

↓

Permanent Account Linking

↓

Authentication Bypass
```

---

# Impact

```
Account Takeover

Authentication Bypass

Persistent Account Linking

Privilege Escalation
```

CVSS is generally High or Critical depending on the application.

---

# Mitigation

Always:

- Generate a cryptographically random `state`
- Bind `state` to the user's session
- Validate `state` on the callback
- Expire unused authorization codes
- Require re-authentication before linking sensitive accounts

---

# Bug Bounty Methodology

Whenever you find:

```
Connect Google

Connect GitHub

Connect Facebook

Attach Social Account
```

Always inspect:

```
GET /authorize
```

Checklist:

- Is `state` present?
- Is it random?
- Can the callback be replayed?
- Is account linking protected against CSRF?
- Does linking require user confirmation?

---

# Personal Learning

The `state` parameter is **not optional from a security perspective**.

It functions as a CSRF token for OAuth flows.

Missing or improperly validated `state` values can allow attackers to bind their own identity to another user's account, resulting in persistent account takeover.

---

# PortSwigger Skills Learned

- OAuth Account Linking
- OAuth CSRF
- Missing state Exploitation
- Burp Proxy
- Burp Repeater
- Exploit Server
- iframe CSRF
- Account Takeover