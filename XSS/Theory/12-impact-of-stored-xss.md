# Impact of Stored XSS

## Overview

Stored XSS can perform everything that Reflected XSS can perform.

However, Stored XSS is often significantly more dangerous because the attack is already embedded inside the application.

---

# Why Stored XSS Is More Dangerous

## Reflected XSS

Requires:

```text
Victim Clicks Link
```

---

## Stored XSS

Requires:

```text
Victim Visits Page
```

Only.

---

# Impact Comparison

| Feature | Reflected XSS | Stored XSS |
|----------|----------|----------|
| Requires Link Delivery | Yes | No |
| Persistent | No | Yes |
| Hits Multiple Users | Difficult | Easy |
| Admin Targeting | Possible | Common |
| Severity | Medium-High | High-Critical |

---

# Common Attacker Goals

## Account Takeover

Steal:

```text
Session Data
Credentials
```

---

## Read Sensitive Data

Examples:

```text
Private Messages
Personal Information
Financial Data
```

---

## Perform Actions As Victim

Examples:

```text
Delete Content
Change Passwords
Modify Settings
```

---

## Attack Administrators

Most dangerous scenario:

```text
Attacker
        ↓
Stores Payload
        ↓
Admin Visits Page
        ↓
Admin Session Compromised
```

---

# Timing Advantage

Reflected XSS:

```text
Victim Must Be Logged In
When Link Is Clicked
```

---

Stored XSS:

```text
Payload Waits
Until Victim Visits
```

---

# Persistence Advantage

```text
One Payload
        ↓
Many Victims
```

---

# Critical Scenario

```text
Stored XSS
        ↓
Admin Compromise
        ↓
Privilege Escalation
        ↓
Full Application Control
```

---

# Real World Targets

```text
Admin Dashboards
Support Systems
Ticketing Platforms
Forums
Comments
Messaging Systems
```

---

# Related Lab

- lab02-stored-xss-html-context.md

---

# Key Takeaways

- Stored XSS is usually more severe than Reflected XSS.
- One payload can attack many users.
- Admin users often create critical impact.
- Stored XSS frequently leads to account compromise.