# Bypassing SameSite Restrictions Using On-Site Gadgets

## Overview

Even SameSite=Strict can sometimes be bypassed.

A common technique involves:

```text
Client-Side Redirect Gadget
```

---

# What Is An On-Site Gadget?

An application feature that can be abused to generate a secondary request.

Example:

```text
/post/comment/confirmation
```

---

# Why This Works

Initial request:

```text
evil.com
        ↓
target.com
```

Cookies blocked.

---

Secondary request:

```text
target.com
        ↓
target.com/change-email
```

Cookies sent.

---

# Browser Perspective

The second request appears:

```text
Same-Site
```

therefore:

```text
Cookie Included
```

---

# Client-Side Redirect Example

```javascript
window.location =
"/post/" + postId;
```

If:

```text
postId
```

is attacker-controlled:

```text
Redirect Abuse Possible
```

---

# Attack Flow

```text
Victim Visits Evil Site
        ↓
Redirect Gadget Triggered
        ↓
Secondary Same-Site Request
        ↓
Strict Cookie Sent
        ↓
Action Executed
```

---

# Why Server Redirects Don't Work

Browsers understand:

```text
Cross-Site Redirect Chain
```

and continue enforcing restrictions.

---

# Why Client-Side Redirects Work

Browser treats the second request as:

```text
Fresh Same-Site Request
```

---

# Related Lab

- `lab08-samesite-strict-bypass-via-client-side-redirect.md`

---

# Key Takeaways

- SameSite=Strict is not always sufficient.
- Client-side redirect gadgets are dangerous.
- On-site gadgets can completely bypass SameSite protections. :contentReference[oaicite:4]{index=4}