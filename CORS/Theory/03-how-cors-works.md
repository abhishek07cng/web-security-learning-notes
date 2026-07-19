# How CORS Works

## Overview

CORS works through an exchange of HTTP headers between the browser and the server.

The browser sends an `Origin` header, and the server responds with CORS headers indicating whether the request is allowed.

---

# Basic Flow

```
Browser

↓

Origin Header

↓

Server

↓

CORS Headers

↓

Browser Validation

↓

Allow or Block
```

---

# Step 1 — Browser Sends Origin

Example request:

```http
GET /api/profile HTTP/1.1
Host: api.example.com
Origin: https://shop.example.com
```

The `Origin` header identifies the website making the request.

---

# Step 2 — Server Responds

Example:

```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://shop.example.com
```

The server tells the browser that this origin is allowed.

---

# Step 3 — Browser Validates

If the `Access-Control-Allow-Origin` value matches the requesting origin, the browser allows JavaScript to read the response.

Otherwise, access is blocked.

---

# Credentialed Requests

If cookies or HTTP authentication are included, the server must also return:

```http
Access-Control-Allow-Credentials: true
```

Without this header, the browser blocks access to credentialed responses.

---

# Common CORS Headers

- Origin
- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers

---

# Simple Workflow

```
JavaScript

↓

Cross-Origin Request

↓

Origin Header

↓

Server

↓

ACAO Header

↓

Browser

↓

Response Allowed
```

---

# Bug Bounty Perspective

During testing:

- Inspect the `Origin` header.
- Observe `Access-Control-Allow-Origin`.
- Check whether credentials are allowed.
- Test whether arbitrary origins are accepted.

---

# Key Learnings

- Browsers enforce CORS.
- Servers decide which origins are trusted.
- Misconfigured headers can expose sensitive information to attacker-controlled websites.