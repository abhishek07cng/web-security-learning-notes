# Same-Origin Policy (SOP)

## Overview

The Same-Origin Policy (SOP) is a browser security mechanism that prevents JavaScript from reading responses from a different origin.

It is one of the most important security features in modern browsers.

---

# Why SOP Exists

Without SOP, a malicious website could read:

- Banking data
- Email
- Internal applications
- Social media accounts

simply because the victim is logged in.

---

# Origin Definition

Two pages have the same origin only if all three match:

```
Protocol

Host

Port
```

Example:

```
https://example.com
```

Same Origin

```
https://example.com
```

Different Origins

```
http://example.com

https://api.example.com

https://example.com:8080
```

---

# What SOP Blocks

JavaScript cannot read:

```
https://bank.com

↓

XMLHttpRequest

↓

Response
```

from

```
https://evil.com
```

---

# What SOP Allows

The browser still permits cross-origin requests such as:

- Images
- Scripts
- Stylesheets
- Forms

However, JavaScript generally cannot read the response.

---

# SOP Example

```javascript
fetch("https://bank.com/account")
```

The request may be sent.

The browser blocks JavaScript from accessing the response unless CORS permits it.

---

# SOP vs CORS

SOP

```
Default

↓

Block Response
```

CORS

```
Server Permission

↓

Allow Response
```

---

# Bug Bounty Perspective

When testing cross-origin functionality:

- Does the application rely on CORS?
- Is SOP intentionally relaxed?
- Are sensitive endpoints exposed?

---

# Key Learnings

- SOP protects users from cross-origin data theft.
- Requests may still be sent.
- Reading responses requires CORS approval.