# Reflected XSS CheatSheet

## Identification

Input:

```text
test123
```

appears immediately in response.

---

## Attack Flow

```text
Attacker Payload
        ↓
HTTP Request
        ↓
Immediate Reflection
        ↓
Execution
```

---

## Common Targets

```text
Search Bars
Error Messages
Contact Forms
Query Parameters
```

---

## Basic Payload

```html
<script>alert(1)</script>
```

---

## Testing Workflow

```text
Input
        ↓
Reflection
        ↓
Context
        ↓
Payload
        ↓
Execution
```

---

## Related Lab

```text
Lab01
```

---

## Key Reminder

```text
Reflection
≠
XSS

Execution
=
XSS
```