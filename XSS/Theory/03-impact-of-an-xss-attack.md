# Impact of an XSS Attack

## Overview

The impact of XSS depends on:

- Application functionality
- Sensitive data available
- Victim privileges
- Business context

---

# What Can An Attacker Do?

## Account Takeover

```javascript
document.cookie
```

may expose session information.

---

## Read Sensitive Data

Examples:

```text
Emails
Personal Information
Financial Data
Healthcare Records
```

---

## Perform Actions As Victim

Examples:

```text
Change Password
Transfer Funds
Modify Profile
Delete Data
```

---

## Steal Credentials

Attackers can create fake:

```text
Login Forms
Password Prompts
```

---

## Website Defacement

Example:

```javascript
document.body.innerHTML =
"<h1>Hacked</h1>";
```

---

## Deliver Further Attacks

Victims may unknowingly attack:

```text
Other Users
Administrators
Internal Systems
```

---

# Impact By Application Type

## Public Website

```text
Low Impact
```

---

## Banking Application

```text
Critical Impact
```

---

## Admin Portal

```text
Critical Impact
```

---

# Privilege Escalation Scenario

```text
Admin Visits Vulnerable Page
        ↓
Malicious Script Executes
        ↓
Attacker Gains Admin Actions
        ↓
Full Application Compromise
```

---

# Related Theory

- 01-what-is-xss.md
- 06-reflected-xss.md
- 11-stored-xss.md

---

# Key Takeaways

- XSS can be far more serious than an alert popup.
- Impact depends heavily on victim privileges.
- Admin-targeted XSS often becomes critical.