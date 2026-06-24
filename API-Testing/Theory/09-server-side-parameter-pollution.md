# Server-Side Parameter Pollution

## Overview

Server-side parameter pollution (SSPP) occurs when user-controlled input influences internal API requests.

---

# Typical Flow

```text
External Request
        ↓
Backend API Request
        ↓
Unexpected Parameter Injection
```

---

# Attack Goals

```text
Override Parameters
Inject New Parameters
Modify Internal Requests
```

---

# Common Targets

```text
Internal APIs
Search Functions
Password Reset
Profile Updates
```

---

# Related Labs

```text
Lab04
Lab05
```

---

# Key Takeaways

Backend APIs often trust user input too much.