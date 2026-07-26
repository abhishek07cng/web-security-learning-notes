# Information Disclosure Impact Matrix

| Information Disclosed | Potential Risk | Possible Follow-on Attack |
|------------------------|----------------|---------------------------|
| Framework version | Identify known vulnerabilities | Exploit vulnerable software |
| Stack trace | Understand application internals | Targeted exploitation |
| File path | Discover server structure | Directory traversal or targeted attacks |
| Database information | Reveal backend technologies | Database-focused attacks |
| Environment variables | Exposure of sensitive configuration | Credential compromise |
| Secret keys | Authentication or cryptographic compromise | Privilege escalation |
| Backup source code | Exposure of business logic and credentials | Source code analysis |
| Debug page | Disclosure of server configuration | Further reconnaissance |
| Custom request headers | Exposure of trust mechanisms | Authentication bypass |
| Git history | Recovery of deleted secrets | Administrative access |

---

## Severity Assessment

### Low

- Minor technical details with no practical exploitation.

### Medium

- Information that assists reconnaissance or improves attack precision.

### High

- Credentials, source code, environment variables, or authentication-related data that directly enable compromise.

---

## Reporting Tips

When reporting Information Disclosure findings, include:

- Exact endpoint
- Steps to reproduce
- Information exposed
- Security impact
- Potential attack scenarios
- Recommended mitigation

This helps demonstrate why the disclosed information is a security concern, even if it does not immediately result in account compromise.