# Content Security Policy

## Overview

Content Security Policy (CSP) is a security mechanism that can be used to control how web content is loaded and executed.

In the context of clickjacking, the important CSP directive is:

```text
frame-ancestors
```

This directive controls which origins are permitted to embed a page.

---

# Basic Concept

```text
Target Response
       ↓
Content-Security-Policy
       ↓
frame-ancestors
       ↓
Browser Determines
Whether Framing Is Allowed
```

---

# Prevent All Framing

A page that should never be framed can use:

```http
Content-Security-Policy: frame-ancestors 'none';
```

Conceptually:

```text
Attacker Page
      ↓
Attempts iframe
      ↓
Browser checks CSP
      ↓
frame-ancestors 'none'
      ↓
Framing blocked
```

---

# Allow Same-Origin Framing

A policy can allow framing by the same origin:

```http
Content-Security-Policy: frame-ancestors 'self';
```

Conceptually:

```text
Same Origin
     ↓
Allowed

Different Origin
     ↓
Blocked
```

---

# Allow Specific Origins

The policy can specify trusted origins.

Example:

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

This allows the specified origin to frame the page.

---

# frame-ancestors

The relevant directive is:

```text
frame-ancestors
```

It controls the origins that are permitted to embed the protected resource.

Common policies include:

```http
Content-Security-Policy: frame-ancestors 'none';
```

```http
Content-Security-Policy: frame-ancestors 'self';
```

and:

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

---

# Clickjacking Protection

Basic clickjacking requires:

```text
Attacker Page
      ↓
iframe
      ↓
Target Page
```

A restrictive CSP can prevent this:

```text
Attacker Page
      ↓
iframe
      X
Target Page
```

Therefore:

```text
frame-ancestors
        ↓
Controls framing
        ↓
Helps prevent clickjacking
```

---

# Checking CSP in Burp Suite

Open:

```text
Proxy → HTTP history
```

Select the target response.

Inspect:

```http
Content-Security-Policy
```

Search for:

```text
frame-ancestors
```

---

# Example Response

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Security-Policy: frame-ancestors 'none';
```

This indicates that the page should not be embedded in a frame.

---

# Same-Origin Example

```http
Content-Security-Policy: frame-ancestors 'self';
```

This allows framing by the same origin while restricting other origins.

---

# Specific-Origin Example

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

This allows the specified origin to frame the page.

---

# CSP and X-Frame-Options

A site can use both:

```http
X-Frame-Options: DENY
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

The supplied material discusses using both mechanisms as layered protection.

---

# Testing Workflow

```text
Identify Sensitive Page
        ↓
Inspect Response
        ↓
Find Content-Security-Policy
        ↓
Find frame-ancestors
        ↓
Determine Allowed Origins
        ↓
Test Actual Framing
        ↓
Document Result
```

---

# CSP During Clickjacking Testing

Before constructing a PoC:

```text
Check X-Frame-Options
        ↓
Check CSP
        ↓
Check frame-ancestors
        ↓
Determine whether target can be framed
```

If:

```http
Content-Security-Policy: frame-ancestors 'none';
```

is present, the target is intended to prevent framing.

---

# Important Distinction

CSP contains many directives.

For clickjacking testing, the relevant directive is:

```text
frame-ancestors
```

Do not confuse it with directives such as:

```text
script-src
default-src
img-src
style-src
```

Those directives control other resource or execution behavior.

---

# CSP and DOM XSS

The supplied material also discusses CSP in relation to a clickjacking + DOM XSS lab.

In that context, inspect the policy for weaknesses affecting script execution.

For example:

```text
Content-Security-Policy
        ↓
script-src
        ↓
Determine permitted script sources
```

However, the clickjacking framing control remains:

```text
frame-ancestors
```

---

# Security Review Checklist

```text
☐ Inspect Content-Security-Policy
☐ Locate frame-ancestors
☐ Check for 'none'
☐ Check for 'self'
☐ Identify explicitly allowed origins
☐ Determine whether target can actually be framed
☐ Check X-Frame-Options
☐ Document framing behavior
```

---

# Defensive Examples

## Prevent Framing

```http
Content-Security-Policy: frame-ancestors 'none';
```

---

## Same-Origin Framing

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

## Specific Trusted Origin

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

---

# Key Takeaways

- CSP is a security mechanism that controls browser behavior.
- For clickjacking, `frame-ancestors` is the important directive.
- `frame-ancestors 'none'` prevents framing.
- `frame-ancestors 'self'` allows same-origin framing.
- Specific trusted origins can also be allowed.
- Check CSP response headers when assessing clickjacking.
- CSP can be used alongside `X-Frame-Options`.
- The `frame-ancestors` directive should not be confused with CSP directives that control scripts or other resources.