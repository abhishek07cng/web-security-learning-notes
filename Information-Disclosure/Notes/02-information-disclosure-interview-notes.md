# Information Disclosure - Interview Notes

## What is Information Disclosure?

Information Disclosure occurs when an application unintentionally exposes information that should not be accessible to users.

The disclosed information may be:

- Technical
- Business-related
- User-related

---

## Common Causes

- Verbose error messages
- Debug pages
- Backup files
- Developer comments
- Version control exposure
- Insecure configuration

---

## Common Examples

- Framework versions
- Stack traces
- File paths
- Database information
- Environment variables
- Source code
- Git repositories

---

## How Do You Test for Information Disclosure?

Typical process:

1. Browse the application.
2. Observe every response.
3. Trigger errors.
4. Compare responses.
5. Search hidden resources.
6. Inspect developer comments.
7. Use Burp engagement tools.
8. Document findings.

---

## Which Burp Tools Are Useful?

According to the PortSwigger material:

- Repeater
- Intruder
- Search
- Find Comments
- Discover Content
- Logger++

---

## Why Are Verbose Errors Dangerous?

Verbose errors may expose:

- Framework versions
- File paths
- Stack traces
- Database details

This information can help attackers identify additional vulnerabilities.

---

## Why Are Backup Files Dangerous?

Backup files may expose:

- Source code
- Database credentials
- API keys
- Business logic

---

## Why Is an Exposed Git Repository Dangerous?

Git history may contain:

- Deleted passwords
- API keys
- Previous configuration
- Sensitive commits

Even if secrets have been removed from the current code, they may still exist in historical commits.

---

## Best Practices

- Remove debug pages.
- Disable verbose errors.
- Remove backup files.
- Protect version control data.
- Review deployment configurations.
- Use generic error messages.

---

## Quick Interview Questions

### Q. What is Information Disclosure?

Unintentional exposure of sensitive information by a web application.

---

### Q. Name common sources.

- Error messages
- Debug pages
- Backup files
- robots.txt
- Developer comments
- Version control history

---

### Q. Why is Information Disclosure dangerous?

Because leaked information often enables further attacks.

---

### Q. Which HTTP method was highlighted in the labs?

TRACE.

---

### Q. Which Burp tools are useful?

- Repeater
- Intruder
- Search
- Find Comments
- Discover Content
- Logger++

---

## One-Line Summary

Information Disclosure vulnerabilities expose technical or sensitive information that can significantly improve an attacker's ability to identify and exploit other weaknesses.