# CORS Testing Methodology

## Phase 1 – Reconnaissance

- Identify API endpoints
- Locate authenticated requests
- Review response headers
- Identify sensitive data

---

## Phase 2 – Header Analysis

Inspect:

- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Allow-Headers
- Access-Control-Allow-Methods

---

## Phase 3 – Origin Manipulation

Test:

```http
Origin: https://evil.com
Origin: null
Origin: https://trusted.com.evil.com
Origin: https://trusted.com@evil.com
Origin: http://trusted.com
```

---

## Phase 4 – Credential Testing

Determine whether:

```http
Access-Control-Allow-Credentials: true
```

is returned.

---

## Phase 5 – Sensitive Data Review

Check whether the response contains:

- API Keys
- JWTs
- Email Addresses
- Profile Information
- Internal IDs
- Account Details

---

## Phase 6 – Trusted Origin Review

Audit:

- Subdomains
- Development servers
- Staging environments
- HTTP origins
- Third-party applications

---

## Phase 7 – Proof of Concept

Develop a minimal HTML/JavaScript exploit demonstrating the issue.

---

## Phase 8 – Reporting

Include:

- Vulnerable endpoint
- Request/response
- PoC
- Business impact
- Recommended mitigation