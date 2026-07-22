# How SSRF Works

## Overview

SSRF occurs when a web application accepts user-controlled input and uses it to make server-side requests without proper validation.

The attacker manipulates the destination of the request.

---

# Typical Workflow

```
User

↓

Application

↓

Backend Request

↓

Response Returned
```

The attacker changes the destination of the backend request.

---

# Normal Request

```http
POST /product/stock HTTP/1.1

stockApi=http://stock.example.com/check
```

The application retrieves stock information from the intended backend service.

---

# Malicious Request

```http
POST /product/stock HTTP/1.1

stockApi=http://localhost/admin
```

The server now requests the administrator interface instead.

---

# Request Flow

```
Attacker

↓

Vulnerable Application

↓

Server Makes HTTP Request

↓

Internal Resource

↓

Response

↓

Attacker
```

---

# Why This Happens

The application trusts user input and forwards it directly to an HTTP client without validating the destination.

Examples include:

- Stock checkers
- Image fetchers
- URL preview generators
- Import features
- Webhook handlers

---

# Common Attack Targets

```
localhost

127.0.0.1

192.168.x.x

10.x.x.x

172.16.x.x
```

---

# SSRF vs Normal HTTP Request

Normal

```
Browser

↓

Server
```

SSRF

```
Browser

↓

Server

↓

Another Server
```

The vulnerable application becomes an intermediary.

---

# Bug Bounty Perspective

When reviewing functionality:

- Does the application accept a URL?
- Does it contact another server?
- Can the destination be modified?
- Are responses returned?

If yes, investigate for SSRF.

---

# Key Learnings

SSRF exploits insecure server-side request functionality by redirecting requests to unintended destinations, often exposing internal services that should never be accessible from the Internet.