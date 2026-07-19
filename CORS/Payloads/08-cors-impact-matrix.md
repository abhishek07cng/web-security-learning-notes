# CORS Impact Matrix

| Misconfiguration | Typical Impact | Severity |
|------------------|----------------|----------|
| Origin Reflection + Credentials | Account Data Disclosure | High |
| Trusted `null` Origin | Authenticated Data Disclosure | High |
| Trusted HTTP Origin | Data Disclosure | High |
| XSS on Trusted Origin | Account Takeover / Data Theft | High |
| Wildcard ACAO (Public Data Only) | Limited Risk | Low |
| Weak Origin Parsing | Sensitive Data Disclosure | High |
| Internal Services + Wildcard ACAO | Internal Information Disclosure | Medium–High |

---

## Business Impact

Possible consequences include:

- API Key Disclosure
- Personal Data Leakage
- Internal API Exposure
- Session Information Disclosure
- Privacy Violations
- Compliance Issues

---

## Reporting Tips

A strong report should demonstrate:

- The vulnerable CORS configuration
- The affected endpoint
- Whether credentials are included
- The sensitive data exposed
- A working proof of concept
- Clear business impact