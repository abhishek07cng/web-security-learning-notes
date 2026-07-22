# SSRF Quick Revision

## Definition

Server-Side Request Forgery (SSRF) allows an attacker to make a vulnerable application send requests to unintended destinations, such as localhost, internal services, or external systems.

---

## Common Targets

- localhost
- 127.0.0.1
- Internal Networks
- Admin Panels
- Internal APIs
- Cloud Metadata
- Debug Endpoints

---

## Private IP Ranges

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

---

## Common Bypass Techniques

- Alternative IP formats
- URL Encoding
- Double URL Encoding
- Embedded Credentials (`@`)
- URL Fragments (`#`)
- Nested Hostnames
- Open Redirects

---

## Blind SSRF

Detection relies on:

- Burp Collaborator
- DNS Interactions
- HTTP Interactions

---

## Typical Workflow

```
Find URL Fetching

↓

Confirm SSRF

↓

Test Localhost

↓

Test Internal Network

↓

Bypass Filters

↓

Test Blind SSRF

↓

Assess Impact

↓

Report
```

---

## Severity

| Finding | Severity |
|----------|----------|
| Localhost Access | High |
| Internal Network Access | High |
| Admin Panel Access | Critical |
| Blind SSRF | Medium–High |
| Cloud Metadata | Critical |
| Command Execution | Critical |

---

## One-Minute Interview Answer

> SSRF is a vulnerability where an attacker tricks a server into making unintended requests. This can expose internal services, administrative interfaces, private networks, or cloud metadata. Common testing involves localhost, private IP ranges, filter bypasses, and Blind SSRF detection using Burp Collaborator. Proper mitigation includes strict allowlists, secure URL validation, outbound network restrictions, and authentication for internal services.