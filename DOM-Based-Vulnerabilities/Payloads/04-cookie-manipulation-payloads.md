# DOM Cookie Manipulation Payloads

## 1. Purpose

Payloads and test values for investigating whether attacker-controlled DOM data can influence:

```javascript
document.cookie
```

The core flow is:

```text
Source
  ↓
Attacker Input
  ↓
JavaScript
  ↓
document.cookie
  ↓
Cookie
  ↓
Consumer
```

---

# 2. Harmless Marker

Start with:

```text
cookietest123
```

---

# 3. Basic Cookie Value

For:

```javascript
document.cookie = "test=" + value;
```

use:

```text
cookietest123
```

Expected:

```text
test=cookietest123
```

---

# 4. Special Character Testing

Test:

```text
;
```

```text
=
```

```text
&
```

```text
%
```

```text
#
```

```text
?
```

Determine how the application handles each character.

---

# 5. Cookie Attribute Testing

Inspect whether input influences:

```text
Path
Domain
Expires
Max-Age
Secure
SameSite
```

A conceptual test value is:

```text
cookietest123
```

Then inspect the resulting cookie in:

```text
DevTools → Application → Cookies
```

---

# 6. Cookie Name Testing

Determine whether attacker input affects:

```text
Cookie Name
```

or:

```text
Cookie Value
```

Example:

```javascript
document.cookie = name + "=" + value;
```

Trace both:

```text
name
value
```

---

# 7. Cookie Scope Testing

Record:

```text
Domain
Path
```

Test the behavior from:

```text
Current Path
Parent Path
Related Paths
```

where applicable.

---

# 8. JavaScript Cookie Inspection

Use:

```javascript
document.cookie
```

Remember:

```text
HttpOnly cookies
```

are not exposed through:

```javascript
document.cookie
```

---

# 9. HTTP Verification

After modifying a cookie, inspect:

```text
DevTools → Network
```

or:

```text
Burp Suite → HTTP History
```

Look for:

```http
Cookie:
```

---

# 10. Consumer Testing

After creating a controlled cookie, find:

```text
Where is the cookie read?
```

Search for:

```text
document.cookie
Cookies.get()
getCookie()
cookie
```

Then trace:

```text
Cookie
  ↓
Consumer
  ↓
Security-Sensitive Operation
```

---

# 11. DOM XSS Chain Testing

If the application reads a cookie into a DOM sink, trace:

```text
Cookie
  ↓
document.cookie
  ↓
Variable
  ↓
innerHTML
```

Use a harmless marker first.

Only proceed to execution testing in an authorized lab.

---

# 12. Navigation Chain Testing

If a cookie controls navigation:

```text
Cookie
  ↓
Variable
  ↓
location.href
```

test with a controlled domain:

```text
https://example.com
```

---

# 13. Cookie Checklist

```text
☐ document.cookie identified
☐ Source identified
☐ Cookie name identified
☐ Cookie value identified
☐ Marker tested
☐ Special characters tested
☐ Domain checked
☐ Path checked
☐ Secure checked
☐ HttpOnly checked
☐ SameSite checked
☐ HTTP Cookie header checked
☐ Consumer identified
☐ Security impact tested
```

---

# Quick Payload List

```text
cookietest123
```

```text
;
```

```text
=
```

```text
&
```

```text
%
```

---

# Final Rule

```text
DO NOT STOP AT COOKIE CREATION.

SOURCE
  ↓
document.cookie
  ↓
COOKIE
  ↓
CONSUMER
  ↓
IMPACT
```