# Lab 04 – Single-Endpoint Race Conditions

## Lab Overview

### Objective

Exploit a race condition in the email-change functionality to associate an arbitrary email address with your account.

The target email address is:

```text
carlos@ginandjuice.shop
```

Carlos has a pending administrator invitation.

If the address is successfully claimed, the account can inherit administrator privileges.

Credentials:

```text
Username: wiener
Password: peter
```

:contentReference[oaicite:8]{index=8}

---

# Vulnerability

The application stores only one pending email address at a time.

Submitting a new email address replaces the existing pending value.

This creates collision potential when multiple email-change requests are processed concurrently.

---

# Predict the Collision

1. Log in.
2. Change your email to an address such as:

```text
anything@exploit-YOUR-ID.exploit-server.net
```

3. Observe the confirmation email.
4. Complete the confirmation process.

---

# Identify Shared State

Submit two different email addresses sequentially.

For example:

```text
test1@exploit-server
test2@exploit-server
```

Observe that the first confirmation link becomes invalid after submitting the second request.

This indicates that only one pending email address is stored.

Therefore:

```text
New request
    ↓
Overwrite pending email
```

creates collision potential. :contentReference[oaicite:9]{index=9}

---

# Benchmark

1. Send:

```text
POST /my-account/change-email
```

to Repeater.

2. Add it to a request group.

3. Duplicate the request 19 times.

4. Make each email address unique.

Example:

```text
test1@exploit-server
test2@exploit-server
test3@exploit-server
...
```

5. Send the group sequentially over separate connections.

You should receive one confirmation email for each request.

---

# Probe for Clues

Send the same request group in parallel.

Check the confirmation emails.

A clue is when the recipient address does not always match the pending email address.

This suggests that a race window exists between:

```text
Start email-sending task
          ↓
Race Window
          ↓
Retrieve current pending email
          ↓
Render email
```

A concurrent request may change the pending email during this window. :contentReference[oaicite:10]{index=10}

---

# Prove the Concept

Create a new Repeater group with two copies of:

```text
POST /my-account/change-email
```

Set one request to:

```text
anything@exploit-YOUR-ID.exploit-server.net
```

Send the pair in parallel.

Then configure the other request to:

```text
carlos@ginandjuice.shop
```

Send the requests in parallel again.

---

# Verify the Result

Check the email client.

If the confirmation email contains:

```text
carlos@ginandjuice.shop
```

click the confirmation link.

The email address on your account should now be associated with Carlos's pending administrator invitation.

---

# Final Steps

1. Access the admin panel.
2. Delete the user:

```text
carlos
```

The lab is solved.

---

# Why the Attack Works

The application starts an email-sending task and later retrieves the current pending email from the database.

A concurrent request can change that value between these operations.

---

# Key Learnings

- Single-endpoint races can be powerful.
- Different values can be supplied to the same endpoint.
- Email-based functionality is particularly interesting because email processing may occur in background threads.
- Shared state and temporary sub-states are important indicators.