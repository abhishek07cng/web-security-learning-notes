# Single-Endpoint Race Conditions

## Overview

A **single-endpoint race condition** occurs when multiple requests are sent to the same endpoint with different values, causing the requests to interact with shared application state.

Unlike multi-endpoint races, all requests target the same endpoint.

---

# Basic Concept

Consider a password reset mechanism that stores the following information in the user's session:

```text
session['reset-user']
session['reset-token']
```

A vulnerable implementation may process multiple password reset requests concurrently.

---

# Potential Collision

Suppose two requests are sent using the same session:

```text
Request A
username = attacker
```

and:

```text
Request B
username = victim
```

If the operations interleave incorrectly, the session could end up in an inconsistent state.

---

# Example Collision

The PortSwigger material describes a possible final state:

```text
session['reset-user'] = victim
session['reset-token'] = 1234
```

The victim's user ID is stored in the session, while the valid reset token is sent to the attacker.

This can create a powerful account-takeover primitive.

---

# Why It Happens

The individual operations performed by each request may execute in an unexpected order.

For example:

```text
Request A:
Set reset-user
Generate token
Send token

Request B:
Set reset-user
Generate token
Send token
```

The operations can interleave:

```text
A → Set attacker
B → Set victim
A → Generate token
A → Send token to attacker
```

The resulting session state may no longer correspond to the token received by the attacker.

---

# Important Characteristic

The requests target:

```text
Same Endpoint
+
Same Session
+
Different Input
```

This combination can create a collision.

---

# Timing and Reliability

The PortSwigger material notes that the operations must occur in the right order for the attack to succeed.

Therefore:

- Multiple attempts may be required.
- The attack may depend on timing.
- Some luck may be involved.

---

# Good Targets

Email-based operations are particularly interesting.

The supplied material notes that email operations often run in a background thread after the server sends the HTTP response.

This can make them more susceptible to race conditions.

---

# Testing Workflow

```text
Identify Single Endpoint
        ↓
Identify Shared Session State
        ↓
Send Different Values
        ↓
Send Requests in Parallel
        ↓
Observe State Changes
        ↓
Repeat
        ↓
Confirm Collision
```

---

# Key Takeaways

- Single-endpoint races use multiple requests against one endpoint.
- Different inputs can cause the requests to interfere with shared session state.
- Password-reset and email-related functionality can be valuable targets.
- Successful exploitation may require multiple attempts.