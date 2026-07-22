# SSRF Impact Matrix

| Finding | Impact |
|----------|--------|
| Localhost Access | High |
| Internal Network Access | High |
| Admin Panel Access | Critical |
| Authentication Bypass | Critical |
| Blind SSRF | Medium–High |
| Cloud Metadata Access | Critical |
| Internal Network Enumeration | High |
| Shellshock via SSRF | Critical |
| Open Redirect + SSRF | High |
| Whitelist Bypass | High |

---

## Severity Guide

Low

↓

Medium

↓

High

↓

Critical

---

## Notes

Severity depends on:

- Reachable resources
- Sensitive functionality
- Available trust relationships
- Ability to chain SSRF with additional vulnerabilities