# SSRF Against the Local Server

## Overview

One of the most common SSRF attacks targets the server itself.

Instead of requesting an external resource, the attacker causes the application to send an HTTP request back to its own loopback interface.

This often allows access to administrative functionality that is unavailable to external users.

---

# Loopback Interface

Most operating systems provide a loopback interface that points back to the local machine.

Common loopback addresses include:

```
127.0.0.1

localhost
```

Any request sent to these addresses is handled by the local server itself.

---

# Typical Scenario

Consider a shopping application with a stock checking feature.

Normal request:

```http
POST /product/stock HTTP/1.1

stockApi=http://stock.example.com/product/stock/check?productId=6&storeId=1
```

The server requests the backend stock service and returns the stock status.

---

# Exploiting SSRF

An attacker modifies the request:

```http
POST /product/stock HTTP/1.1

stockApi=http://localhost/admin
```

Instead of contacting the stock service, the application requests its own administrative interface.

---

# Why This Works

Many applications trust requests that originate from the local machine.

Examples include:

- Administrative interfaces
- Recovery endpoints
- Internal management APIs
- Services listening only on localhost

These resources are often inaccessible to external users but become reachable through SSRF.

---

# Attack Flow

```
Attacker

↓

Vulnerable Application

↓

localhost

↓

Admin Interface

↓

Sensitive Response

↓

Attacker
```

---

# Common Reasons for Trusting Local Requests

- Access control is enforced by a reverse proxy that is bypassed by local requests.
- Administrative interfaces are intentionally exposed only on localhost.
- Disaster recovery features allow local administrative access without authentication.
- Internal services listen on non-public ports.

---

# Bug Bounty Perspective

Whenever you identify SSRF, immediately test:

```text
http://localhost/

http://127.0.0.1/

http://localhost/admin

http://127.0.0.1/admin
```

Look for:

- Admin panels
- Debug endpoints
- Internal APIs
- Configuration interfaces

---

# Key Learnings

SSRF against localhost exploits the trust placed in requests originating from the local machine. This frequently results in unauthorized access to administrative functionality.