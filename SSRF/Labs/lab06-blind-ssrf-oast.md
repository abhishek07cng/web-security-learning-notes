# Lab 06: Blind SSRF with Out-of-Band Detection

## Lab Description

This application uses analytics software that automatically requests the URL supplied in the **Referer** header.

The response is never returned to the attacker.

Your objective is to verify the Blind SSRF vulnerability using Burp Collaborator.

---

# Objective

- Trigger a server-side request.
- Observe an Out-of-Band (OAST) interaction.
- Confirm Blind SSRF.

---

# Vulnerability

The analytics component fetches URLs from the `Referer` header.

Because the request occurs in the background, no response is visible to the attacker.

---

# Exploitation Steps

## Step 1

Visit any product page.

Intercept the request.

---

## Step 2

Send the request to **Repeater**.

---

## Step 3

Replace the Referer header with a Burp Collaborator payload.

Example:

```http
Referer: http://xxxx.burpcollaborator.net
```

---

## Step 4

Send the request.

---

## Step 5

Open the **Collaborator** tab.

Click:

```
Poll Now
```

---

## Step 6

Observe DNS and/or HTTP interactions.

This confirms that the application fetched the supplied URL.

The lab is solved.

---

# Burp Workflow

```
Intercept

↓

Repeater

↓

Insert Collaborator Payload

↓

Send Request

↓

Poll Collaborator

↓

DNS / HTTP Interaction
```

---

# Why This Works

Although the server never returns the response to the attacker, it still performs the outbound request.

Burp Collaborator records this interaction, providing proof of Blind SSRF.

---

# DNS vs HTTP

### DNS Only

The application resolved the hostname but could not establish an HTTP connection.

---

### DNS + HTTP

The application successfully connected to the Collaborator server.

---

# Impact

Blind SSRF can lead to:

- Internal network discovery
- Service enumeration
- Vulnerability chaining
- Remote Code Execution in some environments

---

# Mitigation

- Validate all server-side requests.
- Restrict outbound traffic.
- Disable unnecessary URL fetching.
- Monitor unexpected outbound connections.

---

# Bug Bounty Methodology

Test:

- Referer headers
- Callback URLs
- Webhooks
- Analytics features
- URL preview services

Always verify with Burp Collaborator.

---

# Key Learnings

- Blind SSRF does not return responses.
- OAST tools such as Burp Collaborator provide reliable detection.
- DNS interactions alone can still indicate a vulnerability.