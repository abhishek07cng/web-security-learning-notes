# Insecure Configuration Checklist

## Goal

Identify configuration weaknesses that expose sensitive information.

---

## Review Server Configuration

Check whether:

☐ HTTP TRACE is enabled.

☐ Directory listing is enabled.

☐ Debug mode is enabled.

☐ Verbose error messages are returned.

☐ Debug pages remain accessible.

---

## Request Testing

Attempt:

```http
TRACE /
```

Review the response for:

- Request headers
- Custom headers
- Proxy headers

---

## Administrative Access

When admin pages restrict access to localhost:

Check whether leaked headers influence access control.

Examples include custom IP authorization headers disclosed through TRACE.

---

## Record

Document:

- Configuration issue
- Exposed information
- Security impact
- Reproduction steps

---

## Remediation

☐ Disable unnecessary HTTP methods.

☐ Disable verbose errors.

☐ Disable directory listings.

☐ Remove debugging features.

☐ Harden production configuration.