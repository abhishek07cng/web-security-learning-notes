# What is CORS (Cross-Origin Resource Sharing)?

## Overview

Cross-Origin Resource Sharing (CORS) is a browser security mechanism that allows a web application to access resources hosted on a different origin.

It extends the browser's Same-Origin Policy (SOP) by allowing servers to explicitly specify which external origins are permitted to access their resources.

---

# Why Was CORS Introduced?

The Same-Origin Policy blocks JavaScript from reading responses from different origins.

Example:

```
Frontend

https://app.example.com

↓

API

https://api.example.com
```

Without CORS, the browser blocks access to the API response.

CORS provides a controlled way to relax this restriction.

---

# What Is an Origin?

An origin is defined by:

```
Protocol

+

Host

+

Port
```

Example:

```
https://example.com:443
```

Changing any of these creates a different origin.

Examples:

```
https://example.com

http://example.com

https://api.example.com

https://example.com:8080
```

All of the above are different origins.

---

# How CORS Works

Browser

↓

Cross-Origin Request

↓

Server

↓

Access-Control-Allow-Origin

↓

Browser Decides

↓

Allow or Block Response

The browser checks the CORS response headers before making the response available to JavaScript.

---

# Important Point

CORS is enforced by browsers.

It is **not** a server-side access control mechanism.

Attackers using tools like:

- Burp Suite
- curl
- Postman

can send requests regardless of CORS.

---

# CORS Is Not a Security Feature

CORS does **not** protect against:

- CSRF
- Authentication bypass
- Unauthorized requests

Its purpose is to control whether browser JavaScript can read cross-origin responses.

---

# Example

Request:

```http
GET /api/user HTTP/1.1
Host: api.example.com
Origin: https://shop.example.com
```

Response:

```http
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://shop.example.com
```

The browser allows JavaScript running on `shop.example.com` to read the response.

---

# Bug Bounty Perspective

Whenever you encounter CORS, ask:

- Which origins are trusted?
- Is the Origin header reflected?
- Are credentials allowed?
- Can sensitive data be read cross-origin?

---

# Key Learnings

- CORS relaxes the Same-Origin Policy.
- It is enforced by browsers.
- It controls access to responses, not requests.
- Misconfigurations can expose sensitive data.