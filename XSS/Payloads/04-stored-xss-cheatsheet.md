# Stored XSS CheatSheet

## Identification

User input:

```text
Saved
```

and appears later.

---

## Attack Flow

```text
Input
        ↓
Storage
        ↓
Later Output
        ↓
Execution
```

---

## Common Targets

```text
Comments
Forums
Profiles
Reviews
Support Tickets
Chat Messages
```

---

## Basic Payload

```html
<script>alert(1)</script>
```

---

## Testing Workflow

```text
Find Storage Point
        ↓
Submit Probe
        ↓
Locate Output
        ↓
Determine Context
        ↓
Execute Payload
```

---

## Related Lab

```text
Lab02
```

---

## Severity Reminder

```text
Reflected XSS
        ↓
One Victim

Stored XSS
        ↓
Many Victims
```

---

## Admin Targeting

Always check whether stored data appears in:

```text
Admin Dashboards
Logs
Moderation Panels
```

because this often turns a medium issue into a critical issue.