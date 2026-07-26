# Lab 04: Authentication Bypass via Information Disclosure

## Lab Description

This lab demonstrates how information disclosure can reveal implementation details that enable an authentication bypass.

The administration interface is protected, but the application leaks the name of a custom HTTP header that is used to determine whether a request originates from the localhost IP address.

Your objective is to obtain the custom header, bypass the authentication mechanism, access the administrator interface, and delete the user **carlos**.

---

# Objective

- Discover the custom authentication header.
- Bypass localhost-only access restrictions.
- Access the admin panel.
- Delete the user **carlos**.

---

# Vulnerability

The application exposes internal authentication logic through the HTTP TRACE method.

The TRACE response reveals a custom request header that the front-end automatically adds to requests.

By supplying this header manually, an attacker can impersonate localhost.

---

# Exploitation Steps

## Step 1

Log in using the provided credentials:

```
Username: wiener

Password: peter
```

---

## Step 2

Browse to:

```http
GET /admin
```

The response states that the admin panel is accessible only if:

- Logged in as an administrator, or
- The request originates from localhost.

---

## Step 3

Send the request to **Burp Repeater**.

Change the request method:

```http
TRACE /admin
```

Send the request.

---

## Step 4

Study the response.

The echoed request reveals a custom header similar to:

```http
X-Custom-IP-Authorization: <your-ip-address>
```

This header is automatically added by the front-end.

---

## Step 5

Configure Burp Proxy.

Navigate to:

```
Proxy

↓

Match and Replace

↓

Add Rule
```

Create a **Request Header** rule.

Leave the **Match** field empty.

Set the replacement header to:

```http
X-Custom-IP-Authorization: 127.0.0.1
```

Save the rule.

---

## Step 6

Browse the application again.

Because Burp now adds the custom header to every request, the application believes the request originates from localhost.

---

## Step 7

Open:

```text
/admin
```

The administrator interface is now accessible.

Delete:

```
carlos
```

The lab is solved.

---

# Burp Workflow

```
Browse Admin

↓

TRACE Request

↓

Read Echoed Headers

↓

Identify X-Custom-IP-Authorization

↓

Configure Match & Replace

↓

Inject Localhost Header

↓

Access Admin Panel

↓

Delete Carlos
```

---

# Why This Works

The application trusts a custom HTTP header to determine whether a request originates from localhost.

Because the header value can be supplied by the client, an attacker can spoof the localhost address and bypass authentication.

The TRACE method unintentionally reveals the header name, making the attack possible.

---

# Impact

This vulnerability may lead to:

- Authentication bypass
- Administrative access
- Privilege escalation
- Unauthorized modification of application data

---

# Mitigation

- Disable HTTP TRACE in production.
- Never trust client-controlled headers for authentication decisions.
- Validate requests using trusted server-side mechanisms.
- Restrict access to administrative interfaces using robust authentication and authorization.

---

# Bug Bounty Methodology

When testing Information Disclosure:

- Check whether HTTP TRACE is enabled.
- Look for custom request headers.
- Identify headers added by proxies or front-end servers.
- Determine whether leaked headers influence authentication or authorization.

---

# Key Learnings

- HTTP TRACE may disclose internal request headers.
- Client-controlled headers should never determine trust.
- Information Disclosure can directly enable authentication bypass.