# Lab 02: Information Disclosure on Debug Page

## Lab Description

This lab contains a debugging page that exposes sensitive application information.

Your objective is to locate the page, obtain the `SECRET_KEY` environment variable, and submit it.

---

# Objective

- Discover the hidden debug page.
- Access the debugging information.
- Extract the `SECRET_KEY`.

---

# Vulnerability

The application contains an accessible debugging page that should not be exposed in a production environment.

---

# Exploitation Steps

## Step 1

Browse the application's home page.

---

## Step 2

In Burp Suite:

```
Target → Site Map
```

Right-click the application.

Select:

```
Engagement Tools

↓

Find Comments
```

---

## Step 3

Review the extracted HTML comments.

One comment references:

```text
/cgi-bin/phpinfo.php
```

---

## Step 4

Send the request for:

```http
GET /cgi-bin/phpinfo.php
```

to **Burp Repeater**.

---

## Step 5

Send the request.

The page displays PHP debugging information.

---

## Step 6

Locate the environment variable:

```text
SECRET_KEY
```

Copy its value.

---

## Step 7

Submit the `SECRET_KEY`.

The lab is solved.

---

# Why This Works

The application exposes a debugging page containing sensitive configuration information.

Developer comments also reveal the location of this hidden page.

---

# Burp Workflow

```
Browse Homepage

↓

Find Comments

↓

Locate Debug Page

↓

Send to Repeater

↓

Retrieve phpinfo()

↓

Extract SECRET_KEY
```

---

# Impact

Debug pages may expose:

- Environment variables
- Credentials
- Secret keys
- Server configuration
- Installed modules

---

# Mitigation

- Remove debug pages from production.
- Disable debugging features.
- Review HTML comments before deployment.

---

# Bug Bounty Methodology

Always:

- Inspect developer comments.
- Search for debug pages.
- Review hidden endpoints.
- Check for exposed environment variables.

---

# Key Learnings

- HTML comments may reveal hidden functionality.
- Debug pages often disclose highly sensitive information.
- Environment variables should never be publicly accessible.