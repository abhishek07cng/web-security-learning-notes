# XSS Interview Notes

## What Is XSS?

Cross-Site Scripting (XSS) is a web vulnerability that allows an attacker to inject malicious JavaScript into a web application and execute it in another user's browser.

---

# Why Is XSS Dangerous?

Because the script executes within the context of the vulnerable application.

The browser trusts the code as if it came from the legitimate website.

---

# Main Types Of XSS

## Reflected XSS

Payload comes from:

```text
Current HTTP Request
```

Example:

```text
Search Parameter
```

---

## Stored XSS

Payload comes from:

```text
Database
```

Example:

```text
Comments
Profiles
Reviews
```

---

## DOM XSS

Payload processed entirely by:

```text
Client-Side JavaScript
```

---

# Difference Between Reflected And Stored XSS

| Reflected XSS | Stored XSS |
|---------------|------------|
| Comes from request | Comes from storage |
| Needs victim to click link | Victim only visits page |
| Not persistent | Persistent |
| Usually medium-high severity | Often high-critical severity |

---

# Difference Between XSS And CSRF

## XSS

```text
Inject JavaScript
```

Goal:

```text
Execute Code In Victim Browser
```

---

## CSRF

```text
Force Victim Action
```

Goal:

```text
Perform Unauthorized Request
```

---

# Difference Between XSS And SQL Injection

## XSS

Targets:

```text
Users
```

---

## SQL Injection

Targets:

```text
Database
```

---

# Common XSS Contexts

```text
HTML Context
Attribute Context
JavaScript Context
URL Context
CSS Context
```

---

# Common Interview Question

## Reflection Found. Is It XSS?

Answer:

```text
No

Reflection Alone
≠ XSS

JavaScript Execution
= XSS
```

---

# Common Interview Question

## Why Is Stored XSS More Dangerous?

Answer:

```text
Payload Is Already Stored

Victims Don't Need To Click Links

One Payload Can Affect Many Users
```

---

# Common Interview Question

## What Is The First Thing You Check During XSS Testing?

Answer:

```text
Where Does My Input Appear?
```

because context determines payload selection.

---

# Common Interview Question

## How Do You Test For XSS?

```text
Find Input
        ↓
Inject Probe
        ↓
Locate Reflection
        ↓
Determine Context
        ↓
Craft Payload
        ↓
Verify Execution
```

---

# Common Payloads

HTML:

```html
<script>alert(1)</script>
```

---

Attribute:

```html
" onmouseover="alert(1)
```

---

JavaScript:

```javascript
";alert(1);//
```

---

# Key Interview Takeaways

- Reflection ≠ XSS
- Context determines payload
- Stored XSS is generally more dangerous
- DOM XSS occurs client-side
- XSS targets application users