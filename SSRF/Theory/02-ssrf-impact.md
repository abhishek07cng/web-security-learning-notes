# Impact of SSRF

## Overview

The impact of SSRF depends on which systems the vulnerable application can access.

Because the requests originate from a trusted server, SSRF often bypasses network restrictions that prevent direct external access.

---

# Common Impacts

## 1. Access Internal Services

The server may communicate with:

```
Admin Panels

↓

Internal APIs

↓

Private Databases
```

These systems are normally inaccessible to attackers.

---

## 2. Authentication Bypass

Some administrative interfaces trust requests originating from the local machine.

Example:

```
localhost

↓

Admin Interface

↓

No Login Required
```

SSRF can exploit this trust relationship.

---

## 3. Sensitive Data Disclosure

Possible information exposed:

- User Details
- Configuration Files
- Internal APIs
- API Keys
- Tokens
- Server Metadata

---

## 4. Internal Network Reconnaissance

Attackers may discover:

- Live Hosts
- Open Ports
- Internal Services
- Hidden Applications

---

## 5. Remote Code Execution

Some internal services expose dangerous functionality.

If reachable through SSRF, they may lead to command execution.

---

## 6. Cloud Metadata Access

Cloud providers expose metadata endpoints that contain sensitive credentials.

If accessible through SSRF, attackers may retrieve:

- Temporary credentials
- IAM roles
- Access tokens

---

# Trust Relationships

```
Internet User

↓

Web Server

↓

Trusted Internal Network

↓

Sensitive Services
```

The attacker abuses the trust placed in the web server.

---

# Bug Bounty Perspective

Always assess:

- What can the server reach?
- Can localhost be accessed?
- Can private IPs be reached?
- Is metadata exposed?
- Is sensitive functionality available?

---

# Key Learnings

The severity of SSRF depends on the reachable resources. Even a simple SSRF can become critical if it provides access to internal administrative functionality or cloud credentials.