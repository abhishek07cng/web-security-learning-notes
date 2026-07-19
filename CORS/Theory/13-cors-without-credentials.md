# CORS Without Credentials (Intranet & Internal Network Attacks)

## Overview

Most discussions about CORS focus on authenticated requests that include cookies or other credentials. However, even when credentials are **not** included, insecure CORS configurations can still introduce significant security risks.

One notable example is exposing internal or intranet resources that should never be accessible from an external website.

---

# Does CORS Always Require Credentials?

No.

A browser can make cross-origin requests without cookies.

Example:

```javascript
fetch("http://192.168.1.1/")
```

Although no credentials are sent, the request is still issued.

If the internal application returns permissive CORS headers, JavaScript may be able to read the response.

---

# Example Scenario

Victim Network

```
192.168.1.1
```

↓

Admin Panel

↓

Permissive CORS

↓

Attacker Website

↓

Reads Internal Data

---

# Example Request

```http
GET / HTTP/1.1
Host: 192.168.1.1
Origin: https://attacker.com
```

---

# Vulnerable Response

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin: *

Content-Type: text/html
```

Since no credentials are required, the browser allows JavaScript to read the response.

---

# Attack Flow

```
Victim Visits Attacker Site

↓

JavaScript Sends Requests

↓

Router

NAS

Printer

Jenkins

GitLab

Internal API

↓

Permissive CORS

↓

Responses Returned

↓

Attacker Learns Internal Information
```

---

# Possible Targets

- Home Routers
- NAS Devices
- Printers
- Jenkins
- Kubernetes Dashboards
- Docker APIs
- Internal Admin Panels
- Development Servers

---

# Why This Matters

Even if authentication is required later, attackers may still obtain:

- Device model
- Firmware version
- Internal IP addresses
- Service banners
- Configuration details
- Software versions

This information can greatly assist further attacks.

---

# Bug Bounty Perspective

When testing CORS:

- Check whether credentials are actually required.
- Inspect public APIs.
- Test internal IP ranges.
- Look for wildcard ACAO responses.
- Examine IoT and management interfaces.

---

# Mitigation

- Do not expose sensitive resources using permissive CORS.
- Restrict trusted origins.
- Avoid wildcard (`*`) responses for internal services.
- Place internal services behind authentication and network segmentation.

---

# Key Learnings

Even without credentials, poorly configured CORS can expose valuable internal information and increase the attack surface for attackers.