# Source Code Disclosure Checklist

## Goal

Identify publicly accessible source code and backup files.

---

## Hidden Resources

Inspect:

```
/robots.txt
```

Look for references to:

- Backup folders
- Hidden directories
- Development resources

---

## Backup Files

Search for files such as:

```
*.bak

*~

.old
```

---

## Source Code Review

When source code is exposed, inspect it for:

- Database credentials
- API keys
- Hard-coded passwords
- Internal endpoints
- Sensitive configuration

---

## Why It Matters

Source code may reveal:

- Business logic
- Authentication mechanisms
- Database connections
- Hidden functionality

---

## Burp Workflow

```
robots.txt

↓

Backup Directory

↓

Download Source

↓

Review Code

↓

Extract Sensitive Information
```

---

## Remediation

☐ Remove backup files.

☐ Restrict access to development resources.

☐ Perform deployment reviews before publishing applications.