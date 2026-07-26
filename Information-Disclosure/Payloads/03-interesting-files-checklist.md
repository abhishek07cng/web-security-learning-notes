# Interesting Files Checklist

Always inspect the following resources during testing.

---

## Standard Files

```
/robots.txt

/sitemap.xml
```

---

## Backup Locations

```
/backup
```

Look for backup source code files such as:

```
*.bak

*~

.old
```

---

## Debug Pages

Example:

```
/cgi-bin/phpinfo.php
```

---

## Version Control

```
/.git
```

---

## Hidden Directories

Check for:

- Administrative resources
- Backup directories
- Development resources

---

## Why These Matter

These locations may reveal:

- Source code
- Credentials
- Environment variables
- Internal endpoints
- Hidden functionality