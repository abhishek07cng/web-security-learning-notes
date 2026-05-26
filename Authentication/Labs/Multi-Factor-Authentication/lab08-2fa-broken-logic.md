# Lab08 - 2FA Broken Logic

## Objective

Gain access to the victim account by exploiting flawed Two-Factor Authentication (2FA) logic.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Broken 2FA Authentication Logic
```

The application improperly handles authentication state during the MFA process.

As a result, attackers can bypass 2FA protections and gain unauthorized access.

---

## Understanding the Vulnerability

Two-Factor Authentication should require users to complete:

1. Username/password verification
2. MFA verification

before access is granted.

However, flawed implementations may:

- create authenticated sessions too early
- trust client-side behavior
- fail to validate MFA completion properly

---

## Intended Authentication Flow

```text
Username + Password
        ↓
MFA Verification
        ↓
Authenticated Session
```

---

## Vulnerable Authentication Flow

```text
Username + Password
        ↓
Authenticated Session Created
        ↓
MFA Page Displayed
```

In this vulnerable design, attackers may bypass the second authentication step entirely.

---

# Reconnaissance

The login functionality was analyzed using Burp Suite Proxy.

---

## Initial Observations

After entering valid credentials:

- the application redirected to a 2FA verification page
- session cookies were already generated
- authenticated functionality appeared partially accessible

This indicated weak authentication state handling.

---

# Attack Methodology

The attack focused on bypassing MFA verification by abusing flawed session logic.

---

# Step 1 - Login with Valid Credentials

Valid credentials were submitted.

Example:

```http
POST /login HTTP/1.1

username=wiener&password=peter
```

---

## Step 2 - Intercept Authentication Flow

The MFA verification process was intercepted using Burp Suite Proxy.

The application redirected to:

```text
/login2
```

---

## Step 3 - Analyze Session State

After password verification:

- session cookies were already issued
- partial authentication state existed

This suggested the application trusted authentication too early.

---

## Step 4 - Attempt Forced Browsing

Instead of completing MFA verification, authenticated pages were requested directly.

Example:

```text
/my-account
```

---

## Step 5 - Observe Application Behavior

The application granted access without validating MFA completion.

This confirmed a broken authentication workflow.

---

# Alternative Logic Weakness

Some vulnerable applications include user references inside requests such as:

```http
verify=carlos
```

Attackers may manipulate these parameters and target other accounts.

---

# Response Analysis

Successful bypass indicators included:

| Indicator | Purpose |
|---|---|
| Access to Internal Pages | Authentication bypass |
| Session Cookies | Premature session creation |
| Missing MFA Validation | Broken access control |
| HTTP 200 Responses | Unauthorized access |

---

# Result

The attacker successfully bypassed MFA verification and gained authenticated access without supplying the second authentication factor.

---

# Root Cause

The application created an authenticated session before fully validating MFA completion.

Access control checks failed to verify whether:

```text
MFA verification was completed successfully
```

---

# Why This Is Dangerous

Broken MFA logic may completely undermine additional authentication protections.

Even if passwords are stolen, MFA should prevent unauthorized access.

Improper implementation removes this security benefit entirely.

---

# Real-World Risks

Weak MFA implementations may allow attackers to:

- bypass MFA protections
- compromise sensitive accounts
- escalate privileges
- maintain persistent access

---

# Common Testing Methodology

During testing, attackers commonly analyze:

- session cookies
- redirect behavior
- authentication state
- forced browsing possibilities
- hidden parameters

---

# Mitigation

Applications should:

- validate MFA server-side
- prevent premature session creation
- enforce authentication state properly
- verify MFA completion before granting access
- use secure session handling

---

# Secure Authentication Principle

Applications should NEVER grant authenticated access until:

```text
ALL authentication steps are fully completed
```

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Repeater | Manual request testing |
| Browser Session Analysis | Authentication state testing |

---

# Key Learnings

- Learned how broken MFA logic may bypass authentication entirely.
- Improved understanding of session state handling.
- Practiced forced browsing techniques.
- Understood why server-side validation is critical.

---

# Attack Flow Summary

```text
Submit Valid Credentials
        ↓
Receive Premature Session
        ↓
Skip MFA Verification
        ↓
Directly Access Protected Pages
        ↓
Gain Authenticated Access
```

---

> [!IMPORTANT]
> MFA is only effective when authentication state is validated correctly server-side.

> [!TIP]
> During testing, always analyze whether session cookies are created before MFA completion.

> [!WARNING]
> Broken MFA logic may provide almost no additional protection over password-only authentication.