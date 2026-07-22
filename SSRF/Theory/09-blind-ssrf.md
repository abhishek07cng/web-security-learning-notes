# Blind SSRF

## Overview

Blind SSRF occurs when the server makes a backend request but does not return the response to the attacker.

Unlike traditional SSRF, attackers cannot directly view the contents of the requested resource.

---

# Normal SSRF

```
Attacker

↓

Server

↓

Internal Service

↓

Response Returned

↓

Attacker
```

---

# Blind SSRF

```
Attacker

↓

Server

↓

Internal Service

↓

No Response

↓

Attacker
```

The request still occurs, but the response is hidden.

---

# Why Blind SSRF Is Harder

The attacker cannot directly observe:

- Page contents
- Status codes
- Internal responses
- Error messages

Instead, they must rely on indirect evidence.

---

# Common Blind SSRF Targets

- Analytics Software
- URL Preview Services
- Logging Systems
- Monitoring Tools
- Webhooks

These features often fetch attacker-controlled URLs in the background.

---

# Detecting Blind SSRF

Blind SSRF is commonly detected using Out-of-Band (OAST) techniques.

Instead of targeting an internal resource, the attacker supplies a URL under their control.

If the server makes the request, the attacker observes an interaction.

---

# Typical Workflow

```
Application

↓

Attacker-Controlled Server

↓

DNS Lookup

↓

HTTP Request

↓

Interaction Logged
```

---

# Limitations

Blind SSRF does not immediately expose internal data.

However, it can still be used for:

- Internal Network Discovery
- Service Enumeration
- Chaining into Other Vulnerabilities
- Remote Code Execution (in some environments)

---

# Bug Bounty Perspective

Indicators of Blind SSRF include:

- Webhooks
- Referer-based analytics
- Import features
- Callback URLs
- Background URL fetching

Use Burp Collaborator or another OAST service to verify server-side interactions.

---

# Key Learnings

Blind SSRF is more difficult to exploit because responses are not visible, but it remains a serious vulnerability and is commonly detected using Out-of-Band interaction techniques.