# Reflected XSS - Frequently Asked Questions

## What Is The Difference Between Reflected XSS And Stored XSS?

### Reflected XSS

```text
Payload Comes From Request
```

Example:

```text
Search Parameter
```

---

### Stored XSS

```text
Payload Comes From Database
```

Example:

```text
Comments
Profiles
Messages
```

---

# What Is Self-XSS?

Self-XSS occurs when:

```text
Victim Must Enter Payload Themselves
```

Example:

```text
Paste This In Browser Console
```

---

Why it is usually low severity:

```text
Requires User Interaction
No Direct Delivery Mechanism
```

---

# Why Is Reflected XSS Less Dangerous Than Stored XSS?

Reflected XSS:

```text
Victim Must Click Link
```

Stored XSS:

```text
Victim Only Needs To Visit Page
```

---

# Can Reflected XSS Lead To Account Takeover?

Yes.

Possible scenarios:

```text
Session Theft
Credential Theft
Admin Actions
Sensitive Data Access
```

---

# Is alert(1) A Real Attack?

No.

It is only:

```text
Proof Of Concept
```

used to verify JavaScript execution.

---

# What Should I Look For During Bug Bounty Testing?

```text
Search Parameters
Error Messages
Reflected User Input
Login Pages
Headers
```

---

# Quick Revision

```text
Reflected XSS
        ↓
Input From Request
        ↓
Immediate Reflection
        ↓
JavaScript Execution
```

---

# Related Lab

- lab01-reflected-xss-html-context.md

---

# Key Takeaways

- Reflected XSS requires a delivery mechanism.
- Stored XSS is generally more severe.
- Self-XSS is usually low impact.
- Context determines payload selection.