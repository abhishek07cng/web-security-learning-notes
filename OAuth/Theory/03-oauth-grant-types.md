# OAuth Grant Types

## Definition

A grant type defines **how a client obtains an access token**.

Different applications require different OAuth flows.

---

# Common Grant Types

```text
Authorization Code

Implicit

Client Credentials

Resource Owner Password

Device Code

Refresh Token
```

---

# Authorization Code

Most secure.

Used by:

```text
Traditional Web Applications
```

Flow:

```text
User

↓

Authorization Code

↓

Access Token
```

---

# Implicit

Designed for browser-based applications.

Flow:

```text
User

↓

Access Token
```

No authorization code is exchanged.

Less secure because the token is exposed in the browser.

---

# Client Credentials

Machine-to-machine authentication.

Example:

```text
Backend Service

↓

API
```

No user interaction.

---

# Resource Owner Password

User gives credentials directly to the client.

Rarely recommended today.

---

# Device Code

Used by:

```text
Smart TVs

Gaming Consoles

IoT Devices
```

---

# Refresh Token

Obtains a new access token without requiring the user to log in again.

---

# Which Grant Types Matter Most?

For PortSwigger labs:

```text
Authorization Code

Implicit
```

---

# Bug Bounty Focus

Always identify:

```text
Which Grant Type Is Being Used?
```

This determines:

- Attack surface
- Token exposure
- Validation logic
- Exploitation techniques

---

# Key Learnings

Different grant types have different security properties, and understanding the active flow is essential for identifying OAuth vulnerabilities.