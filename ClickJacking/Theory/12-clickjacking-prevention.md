# Clickjacking Prevention

## Overview

Clickjacking prevention focuses on preventing an attacker-controlled website from embedding a sensitive page and positioning the target interface underneath a deceptive overlay.

The primary protections covered in the material are:

```text
X-Frame-Options
        +
Content Security Policy
        ↓
frame-ancestors
```

---

# 1. Prevent Framing

The most direct defense is to prevent sensitive pages from being framed.

Use:

```http
X-Frame-Options: DENY
```

This instructs the browser not to render the page inside a frame.

---

# 2. Same-Origin Framing

If the application requires framing by pages from the same origin, use:

```http
X-Frame-Options: SAMEORIGIN
```

This restricts framing to the same origin.

---

# 3. Content Security Policy

CSP provides a more flexible framing policy.

To prevent all framing:

```http
Content-Security-Policy: frame-ancestors 'none';
```

---

# 4. Same-Origin CSP Policy

If same-origin framing is required:

```http
Content-Security-Policy: frame-ancestors 'self';
```

This allows the page to be framed by the same origin.

---

# 5. Trusted Origins

If the application genuinely needs to be framed by another trusted website, explicitly specify the allowed origin.

Example:

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

Only trusted framing origins should be permitted.

---

# 6. Layered Protection

The supplied material recommends using both:

```http
X-Frame-Options: DENY
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

This provides layered protection against framing.

---

# 7. Why Framing Protection Works

A basic clickjacking attack requires:

```text
Attacker Page
      ↓
iframe
      ↓
Target Page
```

If the browser blocks the target from being framed:

```text
Attacker Page
      ↓
iframe
      X
Target Page
```

the attacker cannot position the target interface beneath a decoy.

---

# 8. Frame-Busting Scripts

Some applications use JavaScript to detect framing.

Conceptually:

```javascript
if (window.top !== window.self) {
    // Attempt to escape the frame
}
```

The source material discusses frame-busting scripts as a client-side defense.

However, client-side frame-busting should not be relied upon as the primary protection when server-side framing controls can be used.

---

# 9. iframe Sandbox Consideration

The material also discusses the HTML5 iframe sandbox mechanism.

Example:

```html
<iframe
    src="https://victim-website.com"
    sandbox="allow-forms">
</iframe>
```

The sandbox can restrict actions available to the framed page.

The material specifically discusses omitting:

```text
allow-top-navigation
```

while permitting:

```text
allow-forms
```

as part of the frame-busting discussion.

---

# 10. Protect Sensitive Pages

Pages containing sensitive actions should receive appropriate framing protection.

Examples include:

```text
Account Settings
Email Changes
Password Changes
Account Deletion
Administrative Actions
```

---

# 11. Review Response Headers

During a security review, inspect:

```text
X-Frame-Options
Content-Security-Policy
```

For CSP, specifically inspect:

```text
frame-ancestors
```

---

# 12. Security Review Workflow

```text
Identify Sensitive Page
        ↓
Inspect Response Headers
        ↓
Check X-Frame-Options
        ↓
Check Content-Security-Policy
        ↓
Check frame-ancestors
        ↓
Determine Allowed Framing Origins
        ↓
Test Actual Framing Behavior
        ↓
Document Result
```

---

# 13. Recommended Policies

## Page Must Never Be Framed

```http
X-Frame-Options: DENY
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

---

## Same-Origin Framing Required

```http
X-Frame-Options: SAMEORIGIN
```

and:

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

## Trusted External Framing Required

Use a restrictive CSP policy specifying only the required trusted origin:

```http
Content-Security-Policy: frame-ancestors trusted-origin.example;
```

---

# 14. Testing Checklist

```text
☐ Identify sensitive pages
☐ Check X-Frame-Options
☐ Check CSP
☐ Check frame-ancestors
☐ Identify allowed framing origins
☐ Check for frame-busting JavaScript
☐ Test actual iframe behavior
☐ Confirm sensitive pages cannot be framed
☐ Document security headers
```

---

# 15. Defense Comparison

```text
X-Frame-Options
       ↓
Basic framing restriction
```

```text
CSP frame-ancestors
       ↓
Flexible framing policy
```

```text
Frame-Busting JavaScript
       ↓
Client-side framing detection
```

The strongest approach discussed in the material is to use server-side framing restrictions rather than relying solely on JavaScript frame-busting.

---

# Final Security Model

```text
Sensitive Page
      ↓
Should it be frameable?
      │
   ┌──┴──┐
  NO    YES
  │       │
  ▼       ▼
DENY    Restrict
Frame   Trusted Origins
  │       │
  ▼       ▼
XFO/CSP  frame-ancestors
```

---

# Key Takeaways

- Prevent framing of sensitive pages whenever possible.
- `X-Frame-Options: DENY` prevents framing.
- `X-Frame-Options: SAMEORIGIN` restricts framing to the same origin.
- CSP `frame-ancestors 'none'` prevents framing.
- CSP `frame-ancestors 'self'` allows same-origin framing.
- Explicitly allow only trusted external framing origins when required.
- `frame-ancestors` is the key CSP directive for clickjacking protection.
- Frame-busting scripts are client-side defenses and should not be the sole protection.
- Sensitive account and administrative pages should receive appropriate framing controls.