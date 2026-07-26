# Insecure Configuration

## Overview

Information Disclosure often results from insecure configuration rather than programming mistakes.

The PortSwigger material highlights several configuration issues that expose sensitive information.

---

# Common Misconfigurations

Examples include:

- Debug mode enabled
- Verbose error messages
- Directory listing enabled
- HTTP TRACE enabled
- Debug pages exposed

---

# HTTP TRACE

The HTTP TRACE method is intended for diagnostic purposes.

When enabled, the server echoes the request back to the client.

Although this behavior is often harmless, it may reveal:

- Internal authentication headers
- Reverse proxy headers
- Custom request headers

---

# PortSwigger Lab Example

The uploaded lab demonstrates:

1. The `/admin` page indicates that administrator access is allowed from localhost.
2. Sending a TRACE request reveals the automatically added header:

```
X-Custom-IP-Authorization
```

3. By supplying:

```
X-Custom-IP-Authorization: 127.0.0.1
```

the application treats the request as originating from localhost, allowing access to the admin interface.

---

# Why Configuration Matters

Incorrect configuration can unintentionally expose information that simplifies further attacks.

Examples include:

- Internal headers
- Authentication mechanisms
- Debug features

---

# Key Takeaways

- Configuration mistakes frequently lead to Information Disclosure.
- TRACE responses may reveal internal request headers.
- Production environments should disable unnecessary diagnostic features.