# Lab 05 – Partial Construction Race Conditions

## Lab Overview

### Objective

Exploit a race condition in the registration process to bypass email verification and register using an arbitrary email address.

After creating the account:

1. Log in.
2. Access the admin panel.
3. Delete Carlos.

The lab requires Burp Suite 2023.9 or higher and the latest Turbo Intruder. :contentReference[oaicite:11]{index=11}

---

# Vulnerability

The application creates a user in multiple stages.

During a temporary state:

```text
User exists
+
Registration token not initialized
```

the application may temporarily treat an uninitialized token as valid.

---

# Predict the Collision

The registration system normally requires:

```text
@ginandjuice.shop
```

email addresses.

A confirmation link is sent to complete registration.

Because you do not have access to such an email address, investigate the registration workflow.

---

# Discover the Confirmation Endpoint

Review the application's JavaScript through Burp Proxy history.

The JavaScript reveals that the confirmation form submits to:

```text
POST /confirm
```

with the registration token supplied as a query parameter.

---

# Test the Token Parameter

Create a request such as:

```http
POST /confirm?token=1
```

Observe the responses for different token states.

### Arbitrary token

```text
Incorrect token
```

### Missing parameter

```text
Missing parameter
```

### Empty token

```text
Forbidden
```

---

# Important Clue

The forbidden response for an empty token suggests that developers may have specifically attempted to prevent exploitation of an uninitialized token.

Consider a race window between:

```text
Register User
      ↓
Generate / store registration token
```

During the temporary state, the token may not yet be initialized.

---

# Test Null-Like Input

The source demonstrates an empty array representation:

```text
POST /confirm?token[]=
```

This produces an:

```text
Invalid token: Array
```

response.

This confirms that an empty array can be passed as the parameter value and may be useful when targeting the uninitialized state. :contentReference[oaicite:12]{index=12}

---

# Benchmark

1. Send the registration request to Repeater.
2. Create a separate Repeater request for:

```text
POST /confirm?token[]=
```

3. Add both requests to a group.
4. Send them sequentially and in parallel.
5. Use a different username for each attempt to avoid the separate:

```text
Account already exists
```

condition.

---

# Prove the Race

For reliable testing, use Turbo Intruder.

The supplied methodology queues:

```text
1 registration request
+
50 confirmation requests
```

under the same gate.

This allows the confirmation requests to collide with the registration request during the temporary construction state. :contentReference[oaicite:13]{index=13}

---

# Example Attack Structure

```text
Registration Request
        │
        ├───────────────┐
        │               │
        ▼               ▼
User Creation       50 Confirmation Requests
        │               │
        └──── Race ─────┘
             Window
```

---

# Identify Successful Attempt

Launch the attack.

Sort the results by:

```text
Length
```

A successful confirmation request should return a:

```text
200
```

response containing:

```text
Account registration for user <USERNAME> successful
```

Make a note of the successful username.

---

# Complete the Lab

1. Log in using the successful username.
2. Use the static password supplied during registration.
3. Access the admin panel.
4. Delete:

```text
carlos
```

---

# Why the Attack Works

The application creates the user before fully initializing the registration token.

A concurrent confirmation request can therefore interact with the partially constructed account.

---

# Key Learnings

- Partial construction races target temporary object states.
- Uninitialized values can become security-relevant.
- Non-string input structures such as arrays can sometimes interact differently with application logic.
- Turbo Intruder is useful when a very short race window requires many concurrent requests.