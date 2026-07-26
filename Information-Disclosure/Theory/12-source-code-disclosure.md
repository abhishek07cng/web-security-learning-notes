# Source Code Disclosure

## Overview

Source code provides attackers with a detailed understanding of how an application works.

The PortSwigger material explains that source code is sometimes unintentionally exposed through backup files.

---

# Why Source Code Matters

Access to source code allows attackers to:

- Understand application logic
- Identify vulnerabilities
- Discover hard-coded secrets
- Locate sensitive endpoints

---

# Backup Files

Many text editors create temporary backup files while editing.

Examples include:

```
file.php~

file.java.bak

config.old
```

If these files are accessible through the web server, attackers may download the application's source code.

---

# Information Commonly Found

Source code may reveal:

- API keys
- Database credentials
- Internal URLs
- Secret values
- Business logic

---

# PortSwigger Lab Example

The uploaded lab demonstrates:

1. `robots.txt` reveals the existence of a `/backup` directory.
2. The directory contains:

```
ProductTemplate.java.bak
```

3. The backup file exposes the application's source code.
4. The source code contains a hard-coded PostgreSQL database password.

---

# Why It Is Dangerous

Source code often exposes implementation details that cannot normally be observed from outside the application.

Attackers can use this information to identify and exploit additional vulnerabilities.

---

# Key Takeaways

- Backup files frequently expose source code.
- Source code may contain credentials and sensitive configuration.
- Always inspect hidden directories and backup files during testing.