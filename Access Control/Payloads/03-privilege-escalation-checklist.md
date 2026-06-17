# Privilege Escalation Checklist

## Vertical Escalation

Ask:

```text
Can User Become Admin?
```

---

Check:

```text
Admin URLs
Admin APIs
Admin Functions
```

---

## Horizontal Escalation

Ask:

```text
Can User Access
Other User Data?
```

---

Check:

```text
Profiles
Messages
Orders
Documents
```

---

## Horizontal → Vertical

Ask:

```text
Can Exposed Data
Lead To Admin Access?
```

---

Check:

```text
Passwords
API Keys
Sessions
Tokens
```

---

## Multi-Step Processes

Ask:

```text
Can I Skip Steps?
```

---

## Authorization Formula

```text
Read
        ↓
Modify
        ↓
Delete
        ↓
Escalate
```

---

## Severity Guide

| Impact | Typical Severity |
|----------|----------|
| Data Disclosure | Medium |
| User Data Modification | High |
| Account Takeover | High |
| Admin Access | Critical |