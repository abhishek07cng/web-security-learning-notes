# Information Disclosure Testing Methodology

## Objective

Identify information that is unintentionally exposed by a web application and determine whether it can assist further attacks.

---

# Phase 1 – Initial Reconnaissance

Browse the application normally.

During browsing:

- Observe every page.
- Review HTTP responses.
- Check page source.
- Inspect response headers.
- Note unusual behaviour.

---

# Phase 2 – Trigger Informative Responses

Supply unexpected input to application parameters.

Examples include:

- Invalid values
- Incorrect data types
- Missing parameters

Compare responses for:

- Error messages
- Status codes
- Response length
- Response time

---

# Phase 3 – Search Hidden Resources

Review common locations highlighted in the PortSwigger material:

- /robots.txt
- /sitemap.xml
- Hidden directories
- Backup folders
- Debug pages

---

# Phase 4 – Review Developer Artifacts

Inspect:

- HTML comments
- Debug pages
- Backup files
- Version control repositories

These resources may reveal sensitive implementation details.

---

# Phase 5 – Use Burp Suite

Recommended tools:

- Repeater
- Intruder
- Search
- Find Comments
- Discover Content
- Logger++

Use these tools to automate discovery and compare responses.

---

# Phase 6 – Assess Impact

Determine whether the disclosed information reveals:

- Framework versions
- File paths
- Environment variables
- Credentials
- Source code
- Internal configuration

Consider how the information could support additional attacks.

---

# Phase 7 – Report Findings

Document:

- Affected endpoint
- Steps to reproduce
- Information exposed
- Security impact
- Recommended mitigation

---

# Testing Flow

```
Browse Application
        │
        ▼
Inspect Responses
        │
        ▼
Trigger Errors
        │
        ▼
Search Hidden Resources
        │
        ▼
Review Comments & Debug Pages
        │
        ▼
Inspect Backup Files & Git
        │
        ▼
Assess Impact
        │
        ▼
Report Finding
```

---

# Key Principles

- Examine every response carefully.
- Treat small disclosures as valuable reconnaissance.
- Combine multiple observations to understand the application's security posture.