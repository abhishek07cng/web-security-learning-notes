# Lab 01 – Detecting NoSQL Injection

## Lab Overview

**Objective**

Identify and exploit a NoSQL injection vulnerability in the product category filter to display unreleased products.

The application uses a MongoDB database and is vulnerable to NoSQL syntax injection.

---

# Vulnerability

The product category filter accepts user-controlled input and incorporates it into a MongoDB query without sufficient sanitization.

This enables an attacker to manipulate the server-side query logic.

---

# Reconnaissance

1. Open the lab in Burp's browser.
2. Click any product category.
3. Intercept the request using **Burp Suite**.
4. Send the request to **Repeater**.

Locate the vulnerable parameter:

```text
category
```

---

# Exploitation

### Step 1 – Trigger a Syntax Error

Replace the category value with:

```text
'
```

URL-encode the payload.

A JavaScript syntax error indicates that user input is affecting the MongoDB query.

---

### Step 2 – Confirm Injection

Submit:

```text
Gifts'+'
```

URL-encode the payload.

The request no longer produces a syntax error, suggesting that server-side injection is occurring.

---

### Step 3 – Test Boolean Conditions

False condition:

```text
Gifts' && 0 && 'x
```

No products are returned.

---

True condition:

```text
Gifts' && 1 && 'x
```

Products from the Gifts category are returned.

---

### Step 4 – Override the Query

Submit:

```text
Gifts'||1||'
```

URL-encode the payload.

Display the response in Burp's browser.

---

# Successful Result

The response now includes **unreleased products**, confirming successful NoSQL injection.

---

# Why It Works

The injected condition always evaluates to true.

As a result, the MongoDB query returns additional records that would normally remain hidden.

---

# Impact

Successful exploitation may expose:

- Hidden products
- Unreleased data
- Restricted application content

---

# Mitigation

- Validate user input.
- Use parameterized queries.
- Prevent user-controlled query manipulation.

---

# Bug Bounty Methodology

1. Intercept the request.
2. Trigger a syntax error.
3. Confirm injection using valid syntax.
4. Test boolean conditions.
5. Inject an always-true condition.
6. Verify that restricted data becomes accessible.

---

# Key Learnings

- Syntax errors help identify vulnerable parameters.
- Boolean testing confirms server-side query manipulation.
- Always-true conditions may expose hidden data.