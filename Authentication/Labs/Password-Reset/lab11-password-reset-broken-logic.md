# Lab11 - Password Reset Broken Logic

## Objective

Gain access to the victim account by exploiting flaws in the password reset workflow.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Broken Password Reset Logic
```

The application improperly validates password reset functionality, allowing attackers to manipulate the reset process and reset another user's password.

---

## Understanding the Vulnerability

Password reset workflows are highly sensitive because users are not authenticated during the process.

Applications must securely validate:

- reset tokens
- user identity
- password reset requests

Improper validation may allow attackers to reset arbitrary accounts.

---

## Typical Secure Reset Flow

```text
Request Password Reset
        ↓
Receive Reset Token
        ↓
Validate Token
        ↓
Reset Password
```

---

## Vulnerable Reset Flow

In this lab, the application trusted client-side parameters too heavily.

Attackers could manipulate password reset requests and target another user account.

---

# Reconnaissance

The password reset functionality was analyzed using Burp Suite Proxy.

---

## Initial Observations

The reset process involved:

- reset links
- user parameters
- token validation

However, validation logic appeared weak.

---

# Attack Methodology

The attack focused on manipulating password reset requests to reset the victim's password.

---

# Step 1 - Access Forgot Password Functionality

The password reset feature was accessed.

Example endpoint:

```text
/forgot-password
```

---

## Step 2 - Submit Reset Request

A password reset request was generated for a controlled account.

Example:

```http
POST /forgot-password HTTP/1.1

username=wiener
```

---

## Step 3 - Analyze Reset Workflow

The application generated a reset link containing:

- username references
- reset tokens
- verification parameters

---

## Step 4 - Intercept Reset Request

The password reset request was intercepted using Burp Suite Proxy.

---

## Step 5 - Modify User Parameters

The request parameters were modified to target the victim account.

Example:

```http
username=carlos
```

---

## Step 6 - Submit Manipulated Request

The modified request was forwarded to the server.

---

## Step 7 - Reset Victim Password

The application improperly trusted modified parameters and accepted the password reset request.

The victim password was successfully changed.

---

# Result

The victim account password was reset successfully.

Authenticated access was obtained using the newly assigned password.

---

# Root Cause

The application failed to securely validate password reset ownership server-side.

Instead, it trusted client-controlled parameters during the reset process.

---

# Why This Is Dangerous

Password reset functionality effectively replaces normal authentication.

Weak validation may allow attackers to:

- bypass authentication entirely
- compromise arbitrary accounts
- escalate privileges

---

# Common Testing Methodology

During testing, attackers commonly analyze:

- reset tokens
- hidden parameters
- username references
- token validation logic
- parameter tampering possibilities

---

# Common Weaknesses in Password Reset Systems

| Weakness | Risk |
|---|---|
| Client-Side Trust | Parameter manipulation |
| Weak Token Validation | Unauthorized reset |
| Predictable Tokens | Token brute-force |
| Missing Ownership Checks | Arbitrary password reset |

---

# Mitigation

Applications should:

- validate reset ownership server-side
- use high-entropy reset tokens
- prevent parameter manipulation
- expire tokens quickly
- invalidate tokens after use

---

# Secure Password Reset Principles

Applications should:

- trust only server-side validation
- avoid exposing sensitive identifiers
- validate tokens during every stage
- monitor suspicious reset behavior

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Repeater | Modify reset requests |
| Browser Session | Reset workflow analysis |

---

# Key Learnings

- Learned how weak password reset validation can compromise accounts.
- Practiced parameter manipulation during reset workflows.
- Improved understanding of authentication recovery mechanisms.
- Understood why server-side validation is critical.

---

# Attack Flow Summary

```text
Request Password Reset
        ↓
Intercept Reset Workflow
        ↓
Modify Username Parameters
        ↓
Exploit Weak Validation
        ↓
Reset Victim Password
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Password reset functionality is part of the authentication attack surface.

> [!TIP]
> During testing, always inspect hidden parameters and token validation logic.

> [!WARNING]
> Weak password reset validation may allow complete account takeover.