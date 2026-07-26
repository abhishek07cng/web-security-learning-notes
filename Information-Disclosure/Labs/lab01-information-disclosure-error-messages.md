# Lab 01: Information Disclosure in Error Messages

## Lab Description

This lab demonstrates how verbose error messages can unintentionally reveal technical information about an application.

Your objective is to obtain the version number of the vulnerable third-party framework used by the application.

---

# Objective

- Trigger an application error.
- Extract the framework version from the error message.
- Submit the version number to solve the lab.

---

# Vulnerability

The application exposes a detailed stack trace when invalid input is supplied.

Instead of displaying a generic error message, it reveals internal framework information.

---

# Exploitation Steps

## Step 1

Open any product page.

Example request:

```http
GET /product?productId=1
```

---

## Step 2

Intercept the request in Burp Suite.

Send it to **Repeater**.

---

## Step 3

Modify the `productId` parameter by replacing the integer with a string.

Example:

```http
GET /product?productId="example"
```

---

## Step 4

Send the request.

The application throws an exception because it expects an integer.

---

## Step 5

Study the response.

The verbose stack trace reveals the framework and version:

```text
Apache Struts 2 2.3.31
```

---

## Step 6

Submit:

```
2 2.3.31
```

The lab is solved.

---

# Why This Works

The application performs insufficient error handling.

Instead of hiding internal implementation details, it returns a complete exception and stack trace to the user.

---

# Burp Workflow

```
Browse Product

↓

Intercept Request

↓

Send to Repeater

↓

Modify productId

↓

Trigger Exception

↓

Read Stack Trace

↓

Obtain Framework Version
```

---

# Impact

Verbose error messages may reveal:

- Framework names
- Framework versions
- Stack traces
- File paths
- Database details

This information helps attackers identify known vulnerabilities.

---

# Mitigation

- Return generic error messages.
- Disable stack traces in production.
- Log detailed errors internally instead of exposing them to users.

---

# Bug Bounty Methodology

Whenever you find an input parameter:

- Test invalid data types.
- Test malformed input.
- Compare error messages.
- Look for framework names, versions, file paths, or database details.

---

# Key Learnings

- Verbose error messages are a common source of Information Disclosure.
- Framework versions can be used to search for public exploits.
- Error handling should never expose internal implementation details.