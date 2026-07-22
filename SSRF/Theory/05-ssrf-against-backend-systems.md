# SSRF Against Other Back-End Systems

## Overview

Many web applications communicate with internal services that are not directly accessible from the Internet.

These services usually reside on private networks and often lack strong authentication because they are assumed to be protected by network isolation.

SSRF allows attackers to abuse the vulnerable server to reach these internal systems.

---

# Private Networks

Common private IP ranges include:

```
10.0.0.0/8

172.16.0.0 – 172.31.255.255

192.168.0.0/16
```

These addresses are typically unreachable from outside the organization's network.

---

# Example

An internal administrative interface exists at:

```text
http://192.168.0.68/admin
```

Normal users cannot access it.

However, an attacker submits:

```http
POST /product/stock HTTP/1.1

stockApi=http://192.168.0.68/admin
```

The vulnerable application requests the internal resource and returns the response.

---

# Internal Targets

Potential targets include:

- Internal Admin Panels
- REST APIs
- Databases
- Monitoring Dashboards
- Jenkins
- GitLab
- Kubernetes
- Elasticsearch
- Redis

---

# Internal Network Scanning

If the exact address is unknown, attackers often enumerate private IP ranges.

Example:

```
192.168.0.1

↓

192.168.0.2

↓

192.168.0.3

↓

...

↓

192.168.0.255
```

Responses may reveal:

- Live hosts
- Open ports
- Administrative interfaces

---

# Attack Flow

```
Attacker

↓

Vulnerable Server

↓

Private Network

↓

Internal Service

↓

Response

↓

Attacker
```

---

# Bug Bounty Perspective

Test common private ranges such as:

```text
192.168.0.x

10.0.0.x

172.16.x.x
```

If SSRF exists, determine:

- Which hosts respond
- Which ports are open
- Whether sensitive functionality is exposed

---

# Key Learnings

SSRF can break network isolation by allowing attackers to access internal systems that were never intended to be reachable from the Internet.