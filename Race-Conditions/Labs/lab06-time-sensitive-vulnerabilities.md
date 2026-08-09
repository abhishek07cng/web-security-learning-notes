# Lab 06 – Exploiting Time-Sensitive Vulnerabilities

## Lab Overview

### Important Note

This lab **does not actually contain a race condition**.

Instead, it demonstrates how precise request timing can expose another vulnerability: predictable password-reset tokens.

:contentReference[oaicite:14]{index=14}

---

# Objective

1. Identify the weakness in password-reset token generation.
2. Obtain a valid reset token for Carlos.
3. Reset Carlos's password.
4. Log in as Carlos.
5. Access the admin panel.
6. Delete Carlos.

Credentials:

```text
Username: wiener
Password: peter
```

---

# Vulnerability

The password-reset token appears to be generated using predictable internal state.

The source suggests that a timestamp is one of the inputs used to generate the token.

Conceptually:

```text
Token = Hash(Predictable Timestamp + Other Data)
```

If two requests are processed during the same timestamp window, they may receive the same token.

---

# Step 1 – Study Normal Behavior

Submit a password-reset request for your own account.

Observe that the reset email contains:

```text
Username
+
Token
```

---

# Step 2 – Repeat the Request

Send:

```text
POST /forgot-password
```

multiple times.

Observe that:

- The token has a consistent length.
- Each request normally receives a different token.

---

# Step 3 – Consider the Token Generation

A fixed-length token that changes between requests could be:

- Randomly generated.
- A hash of internal state.
- Based on a counter.
- Based on a timestamp.

The source identifies timestamp-based generation as the relevant weakness.

---

# Step 4 – Test Parallel Requests

Duplicate the password-reset request.

Add both requests to a Repeater group.

Send them in parallel.

If they still show significantly different response timing, the requests may still be processed sequentially.

---

# Step 5 – Bypass Per-Session Locking

The application appears to use a PHP backend.

PHP session handling can process requests sequentially for the same session.

To avoid this:

1. Send:

```text
GET /forgot-password
```

without the session cookie.

2. Obtain the newly issued session cookie and CSRF token.

3. Use these values in one of the reset requests.

You now have two reset requests using different sessions.

---

# Step 6 – Send Parallel Requests

Send the two password-reset requests in parallel.

Observe the response times.

When the processing times become identical or closely aligned, check the confirmation emails.

If both emails contain the same token, this confirms that a timestamp is involved in token generation. :contentReference[oaicite:15]{index=15}

---

# Step 7 – Target Carlos

The separate username parameter suggests that the username may not be included in the token calculation.

Modify one of the parallel requests so that:

```text
username=carlos
```

Keep the other request associated with your own account.

Send both requests in parallel.

---

# Step 8 – Obtain the Token

Check your inbox.

You should receive your own confirmation email.

The corresponding request for Carlos should have used the same token.

Copy your reset URL and change the username in the query string to:

```text
carlos
```

---

# Step 9 – Reset the Password

Open the modified reset URL.

You should reach the password-reset form.

Set a new password.

---

# Step 10 – Log In

Log in as:

```text
carlos
```

using the password you just created.

---

# Final Step

Access the admin panel and delete:

```text
carlos
```

The lab is solved.

---

# Why the Attack Works

The reset token is based partly on predictable timing information.

By carefully aligning two reset requests, both requests can generate the same token.

If the username is not incorporated into the token generation, a token generated for one account can potentially be reused against another account.

---

# Key Learnings

- Precise timing techniques are useful beyond race conditions.
- Predictable timestamps should never replace cryptographically secure randomness.
- Per-session request locking can mask concurrency issues.
- Different sessions can reveal whether processing is actually concurrent.
- Always distinguish a genuine race condition from a time-sensitive cryptographic weakness.