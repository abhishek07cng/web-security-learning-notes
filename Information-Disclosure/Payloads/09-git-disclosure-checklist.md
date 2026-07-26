# Git Repository Disclosure Checklist

## Goal

Identify publicly accessible version control repositories.

---

## Check Repository Access

Browse to:

```
/.git
```

---

## If Accessible

Review whether the repository can be downloaded.

Inspect:

- Commit history
- Commit messages
- Previous file versions
- Configuration changes

---

## Look For

- Hard-coded passwords
- API keys
- Database credentials
- Deleted secrets
- Sensitive configuration

---

## Review Commits

Pay special attention to commits mentioning:

- Password removal
- Configuration updates
- Secret removal
- Security fixes

These changes may still expose sensitive information in previous revisions.

---

## Burp / Git Workflow

```
Access /.git

↓

Download Repository

↓

Review Commit History

↓

Inspect Diffs

↓

Recover Sensitive Information
```

---

## Remediation

☐ Prevent public access to `.git`.

☐ Store secrets outside source code.

☐ Audit commit history before deployment.