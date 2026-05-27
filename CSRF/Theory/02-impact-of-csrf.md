# What is the Impact of a CSRF Attack?

## Overview

The impact of a CSRF attack depends on:

- the vulnerable functionality
- the privileges of the victim
- the sensitivity of the targeted action

In severe cases, CSRF can lead to complete application compromise.

---

# Impact on Regular Users

A CSRF attack against a normal user may allow attackers to:

- change account email addresses
- change passwords
- perform unauthorized transactions
- post content on behalf of the user
- delete or modify user data

---

# Account Takeover Scenario

A common attack flow:

```text
Change Victim Email
        ↓
Trigger Password Reset
        ↓
Reset Link Sent to Attacker
        ↓
Full Account Takeover
```

---

# Financial Impact

CSRF may enable:

- unauthorized money transfers
- fraudulent purchases
- subscription changes
- payment modifications

---

# Impact on Administrative Users

The impact becomes significantly more dangerous when an administrator is targeted.

---

# Possible Admin-Level Consequences

Attackers may:

- create new admin accounts
- delete application data
- modify permissions
- compromise other users
- gain full control over the application

---

# Example Admin CSRF Scenario

```text
Admin visits malicious page
        ↓
Browser submits forged request
        ↓
New administrator account created
        ↓
Attacker gains persistent privileged access
```

---

# Important Characteristic of CSRF

In most CSRF attacks:

```text
The attacker does NOT directly read responses.
```

The goal is to force actions, not steal data directly.

---

# Why CSRF Targets State-Changing Requests

CSRF commonly targets:

```http
POST /change-email
POST /transfer-funds
DELETE /account
```

instead of:

```http
GET /view-profile
```

because the objective is unauthorized action execution.

---

# Privilege Determines Severity

| Victim Type | Impact |
|---|---|
| Regular User | Account compromise |
| Moderator | Content manipulation |
| Administrator | Full application compromise |

---

# Real-World Risks

CSRF vulnerabilities may lead to:

- account takeover
- financial fraud
- privilege escalation
- persistent attacker access
- mass user compromise

---

# Related Theory

- `Theory/01-what-is-csrf.md`
- `Theory/03-how-csrf-works.md`

---

# Related Notes

- `Notes/common-observations.md`

---

# Key Takeaways

- CSRF severity depends heavily on victim privileges.
- Administrative CSRF attacks are extremely dangerous.
- CSRF focuses on unauthorized actions rather than data theft.

> [!WARNING]
> A successful CSRF attack against an administrator may completely compromise an application.