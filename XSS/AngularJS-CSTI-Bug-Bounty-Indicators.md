# AngularJS & CSTI Bug Bounty Indicators

## Purpose

Connect:

```text
Observation
        ↓
Potential Vulnerability
        ↓
Testing Methodology
        ↓
Related Lab
```

---

# Scenario 1

## Double Curly Braces Present

### Observation

```html
{{ }}
```

---

### Test

```html
{{7*7}}
```

---

### Expected

```text
49
```

---

### Related Labs

```text
Lab24
Lab25
```

---

# Scenario 2

## AngularJS Keywords Found

### Observation

```html
ng-app
ng-controller
ng-model
```

---

### Potential Vulnerability

```text
CSTI
AngularJS XSS
```

---

### Test

```html
{{7*7}}
```

---

# Scenario 3

## orderBy Appears

### Observation

```javascript
orderBy
```

---

### Potential Vulnerability

```text
Sandbox Escape Sink
```

---

### Related Lab

```text
Lab24
```

---

# Scenario 4

## ng-focus Present

### Observation

```html
ng-focus
```

---

### Potential Vulnerability

```text
CSP Bypass
```

---

### Related Lab

```text
Lab25
```

---

# Scenario 5

## CSP Exists

### Observation

```text
Content-Security-Policy
```

header present.

---

### Important

```text
Do NOT Assume XSS Is Impossible
```

---

### Check

```html
ng-focus
ng-click
$event
```

---

### Related Lab

```text
Lab25
```

---

# Scenario 6

## AngularJS Version < 1.6

### Observation

Legacy AngularJS.

---

### Potential Vulnerability

```text
Sandbox Escape
```

---

### Related Lab

```text
Lab24
Lab25
```

---

# Quick Reference

| Observation | Test |
|------------|---------|
| {{ }} | {{7*7}} |
| ng-app | {{7*7}} |
| orderBy | Sandbox Escape |
| ng-focus | CSP Bypass |
| CSP Header | Check Angular Events |

---

# Personal Revision Note

```text
AngularJS Found
        ↓
{{7*7}}
        ↓
49?
        ↓
Sandbox Escape
        ↓
orderBy
        ↓
CSP Bypass
```

These indicators are extremely useful during bug bounty reconnaissance because AngularJS-based CSTI vulnerabilities are often overlooked compared to traditional XSS. 