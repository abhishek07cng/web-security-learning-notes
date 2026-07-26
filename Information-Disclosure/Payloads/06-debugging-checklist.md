# Debugging Information Checklist

## Goal

Identify debugging features that expose sensitive information.

---

## Debug Pages

Check for exposed debugging pages such as:

```
/cgi-bin/phpinfo.php
```

---

## Environment Variables

Look for exposed values including:

- SECRET_KEY
- Environment variables
- Configuration values

---

## Server Information

Review debugging output for:

- PHP configuration
- Installed modules
- Server software
- Runtime information

---

## Hidden References

Inspect:

- HTML comments
- JavaScript files
- Response headers

These may reveal hidden debugging endpoints.

---

## Burp Workflow

```
Browse Application

↓

Find Comments

↓

Locate Debug Page

↓

Request Debug Resource

↓

Review Output

↓

Extract Sensitive Information
```

---

## Document

Record:

- Debug page URL
- Exposed information
- Security impact
- Screenshots
- Recommended mitigation

---

## Remediation

☐ Remove debugging pages from production.

☐ Disable debugging mode.

☐ Restrict access to diagnostic interfaces.

☐ Review deployment before release.