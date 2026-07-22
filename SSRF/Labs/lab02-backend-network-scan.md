# Lab 02: Basic SSRF Against Another Back-End System

## Lab Description

The application contains a stock checker that communicates with an internal backend service.

The exact IP address of the administrator interface is unknown.

Your objective is to use SSRF to scan the internal network, locate the admin interface, and delete the user **carlos**.

---

# Objective

- Discover the internal admin server.
- Access the administrator interface.
- Delete the user `carlos`.

---

# Vulnerability

The application forwards the supplied URL directly to an internal HTTP client.

This enables the attacker to scan private IP ranges.

---

# Exploitation Steps

## Step 1

Open a product.

---

## Step 2

Click **Check Stock**.

Intercept the request.

---

## Step 3

Send the request to **Burp Intruder**.

---

## Step 4

Modify the parameter:

```text
http://192.168.0.1:8080/admin
```

Highlight the last octet:

```
192.168.0.§1§:8080
```

---

## Step 5

Configure Intruder.

Payload Type:

```
Numbers
```

Values:

```
From: 1

To: 255

Step: 1
```

---

## Step 6

Start the attack.

Burp scans every address in the subnet.

---

## Step 7

Sort responses by Status Code.

Find the request returning:

```
200 OK
```

This host contains the administrator interface.

---

## Step 8

Send that request to Repeater.

Modify:

```text
/admin
```

to

```text
/admin/delete?username=carlos
```

---

## Step 9

Send the request.

Carlos is deleted.

Lab solved.

---

# Burp Workflow

```
Intercept

↓

Intruder

↓

192.168.0.1–255

↓

Find 200 OK

↓

Repeater

↓

Delete Carlos
```

---

# Why This Works

Internal services are protected only by the network.

The vulnerable application has direct access to the private network.

SSRF abuses this trust relationship.

---

# Impact

Attackers can:

- Scan internal hosts
- Discover hidden services
- Reach internal admin panels
- Enumerate network infrastructure

---

# Mitigation

- Block requests to private IP ranges.
- Restrict outbound connections.
- Validate destinations using strict allowlists.
- Segment internal services.

---

# Bug Bounty Methodology

Whenever SSRF exists:

Scan:

```text
192.168.x.x

10.x.x.x

172.16.x.x
```

Look for:

- 200 responses
- Login pages
- Admin dashboards
- API endpoints

---

# Key Learnings

- SSRF enables internal network reconnaissance.
- Private IP ranges are common attack targets.
- Burp Intruder is effective for host discovery.