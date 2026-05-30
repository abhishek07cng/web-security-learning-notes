# Real World Impact Notes

## Why CSRF Matters

CSRF can perform actions using a victim's authenticated session.

---

# Common Real-World Impacts

## Email Change

```text
Email Changed
        ↓
Password Reset
        ↓
Account Takeover
```

---

## Password Change

User loses account access.

---

## Fund Transfer

Unauthorized financial transactions.

---

## Account Deletion

Permanent loss of user data.

---

## Permission Changes

Unauthorized privilege escalation.

---

## Admin Actions

Most dangerous scenario.

---

### Example

```text
Admin Visits Malicious Page
        ↓
Create New Admin User
        ↓
Attacker Gains Access
```

---

# Business Impact

- Financial Loss
- Data Loss
- Account Takeover
- Reputation Damage
- Compliance Issues

---

# Why Admin CSRF Is Critical

The impact of CSRF depends on the victim's privileges.

```text
Normal User
        ↓
Moderate Impact

Administrator
        ↓
Critical Impact
```

---

# Key Takeaway

The real danger of CSRF comes from what action is being performed, not from the vulnerability itself.