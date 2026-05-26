# Attack Methodology Notes

## Standard Web Application Testing Workflow

```text
Reconnaissance
        ↓
Attack Surface Mapping
        ↓
Authentication Testing
        ↓
Authorization Testing
        ↓
Input Validation Testing
        ↓
Business Logic Testing
        ↓
Exploitation
        ↓
Post Exploitation
        ↓
Reporting
```

---

# 1. Reconnaissance

## Goals

Identify:

- endpoints
- technologies
- parameters
- authentication flows
- cookies
- APIs

---

# Common Recon Targets

```text
/login
/admin
/api
/graphql
/reset-password
```

---

# 2. Authentication Testing

## Analyze

- login behavior
- MFA implementation
- password reset logic
- session management
- remember-me functionality

---

# Common Authentication Tests

| Test | Purpose |
|---|---|
| Username Enumeration | Identify users |
| Brute Force | Guess credentials |
| MFA Bypass | Skip verification |
| Session Analysis | Cookie weaknesses |

---

# 3. Authorization Testing

## Analyze

- horizontal privilege escalation
- vertical privilege escalation
- IDOR vulnerabilities
- access controls

---

# 4. Input Validation Testing

## Common Targets

- SQL Injection
- XSS
- SSTI
- Command Injection
- XXE

---

# 5. Business Logic Testing

## Analyze

- workflow assumptions
- pricing manipulation
- race conditions
- hidden functionality

---

# 6. Exploitation

## Goals

- gain access
- escalate privileges
- compromise accounts
- demonstrate impact

---

# 7. Post Exploitation

## Analyze

- sensitive data exposure
- admin access
- persistence
- internal functionality

---

# 8. Reporting

## Include

- vulnerability summary
- impact
- reproduction steps
- mitigation
- screenshots
- payloads

---

# Common Testing Principles

- Never trust client-side validation
- Analyze all responses carefully
- Compare response lengths
- Watch redirects and cookies
- Test hidden parameters

---

# Common Response Indicators

| Indicator | Meaning |
|---|---|
| HTTP 302 | Redirect |
| Set-Cookie | Session creation |
| Response Length Changes | Behavioral difference |
| Timing Difference | Backend validation |

---

# Common Burp Workflow

```text
Proxy
        ↓
Repeater
        ↓
Intruder
        ↓
Comparer
        ↓
Decoder
```

---

# Common Pentesting Mindset

- Think like an attacker
- Test assumptions
- Analyze logic flaws
- Observe small differences
- Break workflows

---

# Key Takeaways

- Methodology is more important than tools.
- Small observations often reveal major vulnerabilities.
- Logic flaws are extremely powerful.

> [!TIP]
> Good pentesters analyze application behavior more than payloads.