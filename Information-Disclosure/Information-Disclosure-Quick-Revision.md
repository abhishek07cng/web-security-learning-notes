# Information Disclosure - Quick Revision

## Definition

Information Disclosure occurs when an application unintentionally exposes information that should not be available to users.

---

# Common Sources

- Error messages
- Debug pages
- Developer comments
- robots.txt
- Backup files
- Version control repositories
- Insecure configuration

---

# Burp Tools

- Repeater
- Intruder
- Search
- Find Comments
- Discover Content
- Logger++

---

# Things to Test

✔ Trigger errors

✔ Compare responses

✔ Inspect HTML comments

✔ Review robots.txt

✔ Search for backup files

✔ Test HTTP TRACE

✔ Check debug pages

✔ Look for exposed Git repositories

---

# Valuable Information

- Framework versions
- Stack traces
- File paths
- Environment variables
- Source code
- Credentials
- Secret keys
- Request headers

---

# Common Lab Techniques

### Error Messages

→ Trigger exceptions using invalid input.

### Debug Pages

→ Locate hidden debug endpoints through developer comments.

### Backup Files

→ Retrieve exposed source code from backup directories.

### HTTP TRACE

→ Identify custom request headers used for authentication decisions.

### Git History

→ Recover deleted secrets from previous commits.

---

# Prevention

- Use generic error messages.
- Disable debug mode.
- Remove backup files.
- Protect version control data.
- Remove developer comments.
- Harden production configuration.

---

# One-Minute Interview Summary

**What is Information Disclosure?**

The unintended exposure of technical, business, or sensitive information by a web application.

**Common causes:**

- Verbose errors
- Debug pages
- Backup files
- Developer comments
- Insecure configuration
- Exposed Git repositories

**Why is it dangerous?**

Because attackers can use the leaked information to identify vulnerabilities, recover secrets, bypass protections, or launch more targeted attacks.

---

# Final Checklist

- ✔ Observe every response.
- ✔ Trigger unexpected behaviour.
- ✔ Search hidden resources.
- ✔ Review developer artefacts.
- ✔ Assess the impact of every disclosure.