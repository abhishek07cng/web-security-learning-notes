# Lab13 - Password Brute-Force via Password Change

## Objective

Gain access to the victim account by exploiting flaws in the password change functionality to brute-force valid credentials.

---

## Lab Difficulty

```text
Practitioner
```

---

## Vulnerability Overview

This lab is vulnerable to:

```text
Password Enumeration via Password Change Functionality
```

The application exposes valid credentials through inconsistent password change responses.

Attackers can abuse these differences to brute-force passwords for another user account.

---

## Understanding the Vulnerability

Password change functionality commonly requires:

1. Current password
2. New password
3. Password confirmation

If applications handle validation inconsistently, attackers may distinguish between:

- valid current passwords
- invalid current passwords

This enables password brute-forcing.

---

## Example Vulnerable Behavior

### Invalid Current Password

```text
Current password is incorrect
```

### Valid Current Password + Mismatched New Passwords

```text
New passwords do not match
```

This difference confirms that the supplied current password is valid.

---

# Reconnaissance

The password change functionality was analyzed using Burp Suite Proxy.

### Password Change Endpoint

```http
POST /my-account/change-password HTTP/1.1
```

---

## Initial Observations

The application responded differently depending on whether:

- the current password was correct
- the new passwords matched

This created a password enumeration vulnerability.

---

# Attack Methodology

The attack abused inconsistent password change responses to brute-force the victim’s current password.

---

# Step 1 - Login with Valid User Account

Authenticated access was obtained using a known user account.

Example:

```http
username=wiener
password=peter
```

---

## Step 2 - Access Password Change Functionality

The password change request was intercepted using Burp Suite Proxy.

---

## Step 3 - Analyze Request Structure

The request contained parameters such as:

```http
username=carlos
current-password=test
new-password-1=password123
new-password-2=password456
```

---

## Step 4 - Identify Response Differences

Testing revealed:

| Condition | Response |
|---|---|
| Invalid Current Password | Current password incorrect |
| Valid Current Password + Mismatched New Passwords | Passwords do not match |

This allowed password enumeration.

---

# Step 5 - Configure Burp Intruder

The request was sent to:

```text
Burp Suite → Intruder
```

The payload position was configured on:

```http
current-password=§payload§
```

---

## Step 6 - Intentionally Mismatch New Passwords

The new password fields were deliberately configured differently.

Example:

```http
new-password-1=test123
new-password-2=test456
```

This ensured the application would reveal when the current password was valid.

---

## Step 7 - Load Password Wordlist

A password wordlist was loaded into Intruder.

---

## Step 8 - Launch Brute-Force Attack

The attack was started and responses were analyzed carefully.

---

## Step 9 - Identify Valid Password

One request returned:

```text
Passwords do not match
```

instead of:

```text
Current password incorrect
```

This confirmed the current password was valid.

---

# Result

The victim’s valid password was successfully identified through password enumeration.

Authenticated access to the target account was obtained.

---

# Burp Intruder Configuration

## Attack Type

```text
Sniper Attack
```

---

## Payload Position

```http
current-password=§payload§
```

---

## Response Analysis

Responses were filtered using:

- response content
- response length
- authentication behavior

---

# Root Cause

The application exposed password validity through inconsistent error handling inside the password change workflow.

This allowed attackers to distinguish valid passwords from invalid ones.

---

# Why This Is Dangerous

Password change functionality is highly sensitive because:

- users are already authenticated
- attackers may abuse trust assumptions
- inconsistent responses leak credential validity

---

# Real-World Risks

Weak password change implementations may allow attackers to:

- brute-force passwords
- compromise accounts
- escalate privileges
- bypass authentication protections

---

# Common Testing Methodology

During testing, attackers commonly analyze:

- password validation behavior
- hidden parameters
- response inconsistencies
- brute-force protections
- session validation

---

# Mitigation

Applications should:

- use generic error messages
- normalize validation responses
- implement rate limiting
- require re-authentication for sensitive actions
- monitor suspicious password change attempts

---

# Secure Error Handling Example

## Insecure

```text
Current password incorrect
```

## Secure

```text
Unable to change password
```

---

# Secure Authentication Principles

Applications should:

- avoid exposing validation state
- use consistent responses
- prevent brute-force attacks
- validate authentication securely server-side

---

# Tools Used

| Tool | Purpose |
|---|---|
| Burp Suite Proxy | Intercept requests |
| Burp Intruder | Automate brute force |
| Wordlists | Password guessing |

---

# Key Learnings

- Learned how password change functionality may expose credential validity.
- Practiced password brute-forcing using response analysis.
- Improved Burp Intruder automation skills.
- Understood why consistent validation responses are critical.

---

# Attack Flow Summary

```text
Authenticate as Valid User
        ↓
Access Password Change Feature
        ↓
Analyze Validation Responses
        ↓
Configure Intruder Payloads
        ↓
Brute-Force Current Password
        ↓
Identify Valid Credentials
        ↓
Gain Account Access
```

---

> [!IMPORTANT]
> Sensitive account actions should never reveal credential validation state.

> [!TIP]
> During testing, intentionally mismatch confirmation fields to expose hidden validation logic.

> [!WARNING]
> Inconsistent password validation responses may allow credential brute-forcing.