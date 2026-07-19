# Access-Control-Allow-Credentials (ACAC)

## Overview

`Access-Control-Allow-Credentials` is a CORS response header that tells the browser whether it may include user credentials in a cross-origin request.

Credentials include:

- Cookies
- HTTP Authentication
- TLS Client Certificates

Without this header, browsers refuse to expose authenticated responses to JavaScript.

---

# Example

Request

```http
GET /accountDetails HTTP/1.1
Host: api.example.com
Origin: https://shop.example.com
Cookie: session=abc123
```

Response

```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://shop.example.com
Access-Control-Allow-Credentials: true
```

The browser allows JavaScript running on `shop.example.com` to read the authenticated response.

---

# Browser Workflow

```
Cross-Origin Request

↓

Cookies Included

↓

Server

↓

ACAC: true

↓

Browser

↓

JavaScript Can Read Response
```

---

# JavaScript Example

```javascript
var req = new XMLHttpRequest();

req.open("GET","https://api.example.com/accountDetails");

req.withCredentials = true;

req.send();
```

The browser only exposes the response if the server returns:

```http
Access-Control-Allow-Credentials: true
```

---

# Common Misconfiguration

Many vulnerable applications return:

```http
Access-Control-Allow-Origin:
https://evil.com

Access-Control-Allow-Credentials:
true
```

If the origin is attacker-controlled, sensitive authenticated data becomes accessible.

---

# Important Restriction

Browsers reject:

```http
Access-Control-Allow-Origin: *

Access-Control-Allow-Credentials: true
```

The wildcard (`*`) cannot be combined with credentialed requests.

---

# Bug Bounty Perspective

Whenever you see:

```http
Access-Control-Allow-Credentials: true
```

Ask:

- Is the Origin reflected?
- Is sensitive data returned?
- Are session cookies included?
- Can the response be read cross-origin?

---

# Impact

Misconfigured ACAC may expose:

- User profiles
- API keys
- CSRF tokens
- Personal information
- Internal APIs

---

# Key Learnings

`Access-Control-Allow-Credentials` is not dangerous by itself.

It becomes dangerous when combined with weak origin validation.