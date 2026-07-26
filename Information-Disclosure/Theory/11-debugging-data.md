# Debugging Data

## Overview

During development, applications often generate debugging information to help developers understand the application's behavior.

While useful during development, this information becomes a security risk if it remains accessible in the production environment.

The PortSwigger material highlights debugging data as a common source of Information Disclosure.

---

# What Can Be Exposed?

Debugging pages and messages may reveal:

- Environment variables
- Session variables
- Hostnames
- Back-end credentials
- File paths
- Directory names
- Encryption keys
- Application configuration

These details provide attackers with valuable insight into the application's internal workings.

---

# Debug Logs

Some applications store debugging information in log files.

If these files are publicly accessible, attackers may discover:

- Runtime errors
- Internal configuration
- Sensitive values
- Application state

---

# Debug Pages

Certain applications expose dedicated debugging pages.

Example:

```
/cgi-bin/phpinfo.php
```

Such pages may disclose:

- PHP configuration
- Installed modules
- Environment variables
- Secret keys
- Server information

---

# PortSwigger Lab Example

The uploaded lab demonstrates that an HTML developer comment points to:

```
/cgi-bin/phpinfo.php
```

Accessing this page reveals debugging information, including the application's `SECRET_KEY` environment variable.

---

# Risks

Exposed debugging information can assist attackers by revealing:

- Internal architecture
- Sensitive configuration
- Credentials
- Cryptographic secrets

---

# Key Takeaways

- Debugging features should never remain enabled in production.
- Debug pages often expose highly sensitive information.
- Always inspect comments and hidden pages for debugging endpoints.