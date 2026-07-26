# Version Control History

## Overview

Most web applications are developed using version control systems such as Git.

The PortSwigger material explains that exposing the `.git` directory can leak valuable development history.

---

# Exposed Git Repository

If the `.git` directory is publicly accessible, attackers may:

- Download repository data
- Review commit history
- Inspect previous code changes

---

# Why This Is Dangerous

Previous commits may contain:

- Hard-coded passwords
- API keys
- Sensitive configuration
- Removed secrets

Although these values no longer exist in the current code, they remain stored in Git history.

---

# PortSwigger Lab Example

The uploaded lab demonstrates:

1. Browsing to:

```
/.git
```

reveals the Git repository.

2. Downloading the repository allows inspection of commit history.

3. A commit titled:

```
Remove admin password from config
```

shows that a hard-coded administrator password was replaced with an environment variable.

4. The previous password remains visible in the Git diff and can be used to log in as the administrator.

---

# Risks

Version control history may expose:

- Deleted secrets
- Previous configurations
- Sensitive source code
- Internal development practices

---

# Key Takeaways

- Deleting secrets from source code does not remove them from Git history.
- Publicly accessible `.git` directories should never exist in production.
- Commit history can reveal sensitive information long after it has been removed from the application.