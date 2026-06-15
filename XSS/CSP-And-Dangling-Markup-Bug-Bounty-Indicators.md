# CSP And Dangling Markup Bug Bounty Indicators

## Purpose

Connect:

```text
Observation
        ↓
Potential Vulnerability
        ↓
Testing Strategy
```

---

# Scenario 1

## CSP Present

### Observation

```http
Content-Security-Policy
```

header exists.

---

### Do Not Assume

```text
XSS Impossible
```

---

### Check

```text
Weak Directives
Policy Injection
Trusted Domains
```

---

# Scenario 2

## User Input Appears In CSP Header

### Observation

```http
report-uri=
USER_INPUT
```

---

### Potential Vulnerability

```text
Policy Injection
```

---

### Test

```text
;script-src-elem 'unsafe-inline'
```

---

### Related Lab

```text
Lab30
```

---

# Scenario 3

## Reflection But Scripts Blocked

### Observation

```html
<script>
```

fails.

---

### Test

```text
Dangling Markup
```

---

### Related Lab

```text
Lab29
```

---

# Scenario 4

## form-action Missing

### Observation

No:

```http
form-action
```

directive.

---

### Potential Impact

```text
Form Hijacking
```

---

# Scenario 5

## frame-ancestors Missing

### Observation

No:

```http
frame-ancestors
```

---

### Potential Impact

```text
Clickjacking
```

---

# Scenario 6

## unsafe-inline Present

### Observation

```http
script-src 'unsafe-inline'
```

---

### Impact

```text
Higher XSS Risk
```

---

# Quick CSP Review Checklist

```text
unsafe-inline?
unsafe-eval?
Wildcards?
User Input?
Trusted Domains?
frame-ancestors?
form-action?
```

---

# Personal Revision Note

When testing CSP:

```text
Don't Ask
"Is CSP Present?"
```

Ask:

```text
"Is CSP Secure?"
```