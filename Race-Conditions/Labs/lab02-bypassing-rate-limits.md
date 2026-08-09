# Lab 02 – Bypassing Rate Limits via Race Conditions

## Lab Overview

### Objective

Exploit a race condition in the login mechanism to bypass a brute-force protection mechanism.

The goal is to:

1. Bypass the rate limit.
2. Brute-force Carlos's password.
3. Log in as Carlos.
4. Access the admin panel.
5. Delete Carlos.

Credentials for your account:

```text
Username: wiener
Password: peter
```

The lab has a 15-minute time limit and requires Burp Suite 2023.9 or higher with the latest Turbo Intruder. :contentReference[oaicite:2]{index=2}

---

# Vulnerability

The application temporarily blocks an account after more than three failed login attempts.

The counter is associated with the username.

Potential race window:

```text
Login Attempt
      ↓
Check Rate Limit
      ↓
Race Window
      ↓
Increment Failed-Attempt Counter
```

If several requests are processed before the counter is updated, more attempts may be accepted than intended.

---

# Predict the Collision

### Step 1 – Test the Rate Limit

Intentionally submit incorrect passwords for your own account.

After more than three failed attempts, observe that the account becomes temporarily blocked.

---

### Step 2 – Test Another Username

Attempt to log in using another username.

The normal:

```text
Invalid username or password
```

response indicates that the rate limit is enforced per username rather than per session.

This suggests that the failed-attempt count is stored server-side.

---

# Benchmark

1. Find an unsuccessful:

```text
POST /login
```

request in Burp Proxy history.

2. Send it to Repeater.

3. Add it to a request group.

4. Duplicate the request 19 times.

This gives a group of 20 requests.

---

# Sequential Test

Send the group sequentially using separate connections.

Observe that after the expected number of failures, the account is temporarily locked.

This establishes the baseline.

---

# Parallel Test

Send the same group in parallel.

Observe the responses.

Despite triggering the account lock, more than three requests may still receive:

```text
Invalid username or password
```

This is evidence that multiple login attempts are being processed before the rate-limit counter is updated. :contentReference[oaicite:3]{index=3}

---

# Prove the Concept with Turbo Intruder

1. Highlight the password parameter in the login request.

2. Select:

```text
Extensions
→ Turbo Intruder
→ Send to Turbo Intruder
```

3. Use the supplied password list from the lab.

4. Configure the requests so that multiple password attempts are released together.

The objective is to exploit the race window so that multiple password attempts are processed before the rate limit takes effect.

---

# Successful Result

Identify the valid password for:

```text
carlos
```

Then:

1. Log in as Carlos.
2. Access the admin panel.
3. Delete Carlos.

---

# Why the Attack Works

The rate-limit counter is updated after the login attempt.

Concurrent requests can therefore pass the rate-limit check before the counter reflects all previous failures.

---

# Key Learnings

- Rate limits can themselves contain race windows.
- Test whether limits are enforced per session, user, IP, or another identifier.
- Parallel requests can bypass counters that are updated non-atomically.
- Turbo Intruder is useful for repeated race-condition attempts.