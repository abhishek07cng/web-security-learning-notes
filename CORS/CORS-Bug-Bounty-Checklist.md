# CORS Bug Bounty Checklist

## Discovery

- Identify API endpoints
- Inspect CORS headers
- Check for sensitive responses

---

## Origin Testing

- Arbitrary Origin
- `null`
- Prefix bypass
- Suffix bypass
- Username (`@`) bypass
- Localhost
- IP addresses

---

## Credentials

- ACAC enabled?
- Cookies included?
- Authenticated endpoint?

---

## Trusted Origins

- HTTP?
- Staging?
- Development?
- Legacy?
- Third-party?

---

## Exploitation

- Build PoC
- Verify browser access
- Confirm sensitive data exposure

---

## Report

Include:

- Vulnerability description
- Steps to reproduce
- Evidence
- Business impact
- Mitigation