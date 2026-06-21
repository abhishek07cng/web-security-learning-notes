# Insufficient Blacklisting

## Overview

Many applications block dangerous extensions using blacklists.

Example:

```text
.php
.jsp
.aspx
```

---

# Problem

Attackers use alternative extensions.

Examples:

```text
.php5
.phtml
.phar
.pHp
```

---

# Example

Blocked:

```text
shell.php
```

Allowed:

```text
shell.phtml
```

---

# Why Blacklists Fail

Developers cannot enumerate:

```text
Every Possible Extension
```

---

# Better Approach

Use:

```text
Whitelists
```

Allow only:

```text
.jpg
.png
.gif
```

---

# Attack Flow

```text
Blacklist
        ↓
Extension Variation
        ↓
Upload Success
```

---

# Related Lab

```text
Lab04
```

---

# Key Takeaways

- Blacklists are fragile.
- Whitelisting is safer.