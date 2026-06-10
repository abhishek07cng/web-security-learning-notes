# Impact of Reflected XSS

## Overview

Reflected XSS allows attackers to execute JavaScript inside a victim's browser.

Once code execution is achieved, the attacker gains the same permissions as the victim user within the application.

---

# What Can An Attacker Do?

## Perform User Actions

Examples:

```text
Change Profile
Transfer Funds
Delete Data
Send Messages
```

---

## Read Sensitive Data

Examples:

```text
Personal Information
Private Messages
API Responses
```

---

## Steal Credentials

Attackers can inject:

```text
Fake Login Forms
Credential Harvesters
```

---

## Session Hijacking

Goal:

```text
Steal Session Tokens
```

or

```text
Perform Actions As Victim
```

---

## Attack Other Users

Victim becomes:

```text
Unintentional Attack Platform
```

for further attacks.

---

# Why Reflected XSS Is Less Severe Than Stored XSS

Reflected XSS:

```text
Attacker Must Deliver Payload
```

usually through:

```text
Email
Message
Website Link
Social Engineering
```

---

Stored XSS:

```text
Payload Already Exists
```

inside the application.

---

# Impact Comparison

| Type | Victim Action Needed |
|---------|---------|
| Reflected XSS | Must Click Link |
| Stored XSS | Just Visit Page |

---

# Severity Factors

## Low

```text
Public Website
Anonymous Users
```

---

## High

```text
Sensitive User Data
Authenticated Features
```

---

## Critical

```text
Admin Users
Financial Systems
Healthcare Applications
```

---

# Attack Flow

```text
Victim Clicks Link
        ↓
JavaScript Executes
        ↓
Victim Session Compromised
        ↓
Attacker Gains Access
```

---

# Key Takeaways

- Reflected XSS can fully compromise a victim account.
- Impact depends heavily on victim privileges.
- Admin-targeted XSS is often critical.