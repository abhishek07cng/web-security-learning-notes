# Common Sources of Information Disclosure

## Overview

Information Disclosure can occur in many different places within a web application.

The PortSwigger material highlights several common sources that should always be checked during testing.

---

# robots.txt

The file:

```
/robots.txt
```

may reveal:

- Hidden directories
- Administrative paths
- Sensitive resources

---

# sitemap.xml

The sitemap may list:

- Hidden pages
- Internal endpoints
- Resources not linked elsewhere

---

# Directory Listings

If directory listing is enabled, attackers may discover:

- Temporary files
- Backup files
- Crash dumps
- Sensitive documents

---

# Developer Comments

HTML comments may contain:

- Internal notes
- Hidden endpoints
- TODO items
- Development reminders

---

# Error Messages

Verbose errors often reveal:

- Framework names
- Framework versions
- Database information
- File paths

---

# Debug Pages

Debug pages may expose:

- Environment variables
- Secret keys
- Configuration
- Internal hostnames

---

# Backup Files

Backup files sometimes expose:

- Source code
- Database credentials
- API keys

---

# Version Control History

Exposed Git repositories may reveal:

- Commit history
- Source code changes
- Previously committed secrets

---

# Key Takeaways

Always inspect:

- robots.txt
- sitemap.xml
- Directory listings
- Comments
- Errors
- Debug pages
- Backup files
- Version control directories