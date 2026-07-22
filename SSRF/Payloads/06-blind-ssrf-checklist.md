# Blind SSRF Checklist

## Test These Features

- Referer
- Webhooks
- Callback URLs
- URL Preview
- Analytics
- Feed Readers
- Image Import
- PDF Generation

---

## Detection

Use:

- Burp Collaborator
- OAST

---

## Observe

- DNS requests
- HTTP requests
- SMTP interactions

---

## Indicators

- Delayed processing
- Background jobs
- Asynchronous requests

---

## Notes

Blind SSRF rarely provides immediate feedback. Out-of-band interaction is the primary detection method.