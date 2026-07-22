# What is SSRF (Server-Side Request Forgery)?

## Overview

Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to make the server-side application send requests to unintended locations.

Instead of communicating only with trusted resources, the vulnerable server can be manipulated into making requests to:

- Internal systems
- Localhost services
- Private network resources
- External systems controlled by the attacker

---

# Why SSRF Is Dangerous

Normally, users can only access resources exposed to the Internet.

With SSRF, the attacker abuses the server itself to access resources that are normally unreachable.

```
Attacker

↓

Vulnerable Web Server

↓

Internal Network

↓

Sensitive Resources
```

The server acts as a proxy for the attacker.

---

# Typical SSRF Scenario

Many web applications accept a URL from the user.

Example:

```
Check Stock

↓

Backend API

↓

Return Inventory
```

The application retrieves information from another server using the supplied URL.

If user input is not properly validated, the attacker can replace the intended URL with another target.

---

# Example

Normal request:

```http
POST /product/stock HTTP/1.1

stockApi=http://stock.example.com/check?product=1
```

Attacker request:

```http
POST /product/stock HTTP/1.1

stockApi=http://localhost/admin
```

Instead of checking stock, the server requests the local administrator interface.

---

# Types of SSRF

## SSRF Against Localhost

```
127.0.0.1

localhost
```

---

## SSRF Against Internal Network

```
192.168.x.x

10.x.x.x

172.16.x.x
```

---

## Blind SSRF

The server makes the request, but the response is not returned to the attacker.

Detection relies on out-of-band techniques.

---

# Common Targets

- Admin Panels
- Internal APIs
- Metadata Services
- Redis
- Elasticsearch
- Jenkins
- Kubernetes
- Docker APIs
- Cloud Metadata Endpoints

---

# Bug Bounty Perspective

Look for parameters containing:

- URLs
- Hostnames
- Images
- PDFs
- Webhooks
- File Imports
- Stock Checkers

These often become SSRF attack surfaces.

---

# Key Learnings

- SSRF abuses server-side requests.
- The attacker uses the server as a proxy.
- Internal systems become reachable.
- SSRF is often a high- or critical-severity vulnerability.