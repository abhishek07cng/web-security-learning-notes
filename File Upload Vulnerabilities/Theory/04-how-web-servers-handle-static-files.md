# How Web Servers Handle Static Files

## Static Files

Examples:

```text
Images
CSS
JavaScript
PDF
HTML
```

---

# Request Flow

```text
Request
        ↓
Server Parses Extension
        ↓
Maps MIME Type
        ↓
Handles File
```

---

# Non-Executable Files

Example:

```text
image.jpg
```

Server returns contents directly.

---

# Executable Files

Example:

```text
Server-side scripts
```

The server interprets the file before sending a response.

---

# Misconfigurations

Sometimes source code may be exposed instead of executed.

This can leak:

```text
Source Code
Credentials
Secrets
Configuration Data
```

---

# Key Takeaways

File execution behavior depends on:

```text
Server Configuration
```