# How to Construct a CSRF Attack

## Overview

A CSRF attack is commonly constructed using hidden HTML forms that automatically submit requests to a vulnerable application.

The attacker hosts this malicious HTML on a website under their control.

---

# Basic CSRF Attack Workflow

```text
Capture Legitimate Request
        ↓
Recreate Request in HTML Form
        ↓
Auto-Submit Form with JavaScript
        ↓
Host Payload on Attacker Site
        ↓
Victim Visits Malicious Page
        ↓
Browser Sends Authenticated Request
```

---

# Step 1 - Capture Legitimate Request

The attacker first captures a legitimate request using:

- Burp Suite Proxy
- Browser Developer Tools
- Repeater

---

# Example Vulnerable Request

```http
POST /email/change HTTP/1.1
Cookie: session=abc123

email=victim@example.com
```

---

# Step 2 - Convert Request Into HTML Form

The attacker recreates the request using a hidden HTML form.

---

# Example CSRF Payload

```html
<html>
  <body>
    <form action="https://vulnerable-website.com/email/change" method="POST">
      <input type="hidden" name="email" value="attacker@evil.com">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

# Purpose of Each Component

| Element | Purpose |
|---|---|
| Hidden Input | Invisible parameter submission |
| Action URL | Targets vulnerable application |
| Auto-Submit Script | Executes attack automatically |

---

# Why Cookies Are Not Included

The attacker does NOT manually add cookies.

The browser automatically attaches:

```http
Cookie: session=abc123
```

during request execution.

---

# Step 3 - Host the Payload

The malicious HTML is hosted on:

- attacker-controlled servers
- exploit servers
- malicious websites

---

# Step 4 - Victim Visits the Page

Once the victim visits the malicious page:

- the form auto-submits
- cookies are attached automatically
- the server processes the request

---

# Burp Suite CSRF PoC Generator

Burp Suite Professional provides automatic PoC generation.

---

# Workflow

```text
Right Click Request
        ↓
Engagement Tools
        ↓
Generate CSRF PoC
        ↓
Copy Generated HTML
```

---

# Why Burp PoC Generator Is Useful

It automatically:

- creates hidden forms
- handles parameters
- generates auto-submit JavaScript
- speeds up exploitation

---

# Common CSRF Delivery Methods

Attackers commonly deliver CSRF payloads through:

- phishing emails
- malicious links
- compromised websites
- advertisements

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Related Payloads

- `Payloads/csrf-html-poc-templates.md`
- `Payloads/auto-submit-form-payloads.md`

---

# Related Notes

- `Notes/burp-workflow.md`

---

# Key Takeaways

- CSRF payloads are usually simple HTML forms.
- The browser automatically attaches authentication cookies.
- Burp Suite can automatically generate CSRF proof-of-concepts.

> [!TIP]
> During testing, always verify whether cookies are automatically attached to forged requests.