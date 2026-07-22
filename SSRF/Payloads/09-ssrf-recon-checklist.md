# SSRF Recon Checklist

## Identify Features

- Stock Check
- Image Fetch
- Import by URL
- Webhooks
- Analytics
- PDF Generation
- Feed Readers
- URL Preview

---

## Test

✓ Localhost

✓ Private IPs

✓ Different ports

✓ Redirects

✓ URL encoding

✓ Whitelist bypass

✓ Blind SSRF

---

## Confirm

- HTTP response
- DNS interaction
- Collaborator callback

---

## Reporting

Include:

- Vulnerable parameter
- Payload used
- Impact
- Proof of concept
- Mitigation