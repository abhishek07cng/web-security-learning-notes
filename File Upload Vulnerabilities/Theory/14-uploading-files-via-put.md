# Uploading Files Via PUT

## Overview

Some servers support:

```http
PUT
```

requests.

This may allow direct file uploads without a dedicated upload form.

---

# Attack Flow

```text
PUT Request
        ↓
File Stored
        ↓
File Accessed
        ↓
Possible Execution
```

---

# Why Dangerous?

No upload page is required.

---

# Common Servers

```text
Apache
Tomcat
WebDAV
IIS
```

---

# Testing Methodology

Send:

```http
OPTIONS /
```

Look for:

```http
Allow:
GET, POST, PUT
```

---

# Bug Bounty Mental Model

Whenever:

```http
PUT
```

is enabled ask:

```text
Can Arbitrary Files Be Uploaded?
```

---

# Key Takeaways

- PUT support increases attack surface.
- WebDAV misconfigurations are common.