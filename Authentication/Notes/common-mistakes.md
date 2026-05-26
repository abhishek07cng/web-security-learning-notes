# Common Mistakes Notes

## Common Authentication Testing Mistakes

---

# 1. Ignoring Response Length

## Problem

Many vulnerabilities only appear through:

- small response size differences
- hidden formatting changes

---

## Result

Missed username enumeration vulnerabilities.

---

# 2. Ignoring Redirects

## Problem

Successful authentication often appears through:

```text
HTTP 302 Redirects
```

instead of visible success messages.

---

# 3. Ignoring Cookies

## Problem

Session cookies often reveal:

- authenticated state
- privilege changes
- session creation

---

# 4. No Enumeration Before Brute Force

## Problem

Brute-forcing without enumeration wastes time.

---

## Better Workflow

```text
Enumerate Users
        ↓
Brute-Force Passwords
```

---

# 5. Only Looking at Error Messages

## Problem

Many applications use generic messages.

Real differences appear in:

- response size
- timing
- redirects
- cookies

---

# 6. Trusting Client-Side Validation

## Problem

Client-side checks can usually be bypassed easily.

Always test server-side behavior.

---

# 7. Not Testing Hidden Parameters

## Problem

Hidden parameters frequently contain:

- usernames
- IDs
- tokens
- privilege values

---

# 8. Ignoring MFA State Handling

## Problem

Some applications create sessions BEFORE MFA validation.

This may allow forced browsing.

---

# 9. No Session Analysis

## Problem

Weak session handling causes:

- session hijacking
- privilege escalation
- authentication bypass

---

# 10. Testing Too Fast

## Problem

Aggressive Intruder attacks may trigger:

- IP bans
- rate limits
- account lockouts

---

# Better Practice

Use:

- resource pools
- slower attack speeds
- controlled automation

---

# 11. Ignoring Business Logic

## Problem

Logic flaws are often more dangerous than injections.

---

# Example

```text
Password Reset Logic
MFA Workflow
Role Switching
```

---

# 12. Weak Documentation

## Problem

Poor notes reduce learning retention.

---

# Better Practice

Document:

- payloads
- methodology
- observations
- mistakes
- response indicators

---

# Key Takeaways

- Small mistakes often hide major vulnerabilities.
- Good methodology is critical.
- Observation skills matter more than tools.

> [!TIP]
> Most beginners miss vulnerabilities because they ignore small behavioral differences.