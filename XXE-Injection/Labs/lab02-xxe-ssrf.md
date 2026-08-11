# Lab 02 – Exploiting XXE to Perform SSRF

## Objective

Exploit an XXE vulnerability to perform a server-side request to the internal application.

The lab requires accessing an internal administration interface and deleting:

```text
carlos
```

---

## Vulnerability

The XML parser resolves external entities.

Instead of referencing a local file, the external entity can reference a URL.

This causes the vulnerable server to make the request.

---

## Attack Flow

```text
Attacker
   ↓
Malicious XML
   ↓
External Entity
   ↓
Internal URL
   ↓
Vulnerable Server
   ↓
Internal Application
```

---

## Step 1 — Identify XML Input

Intercept the application's XML request using Burp Suite.

Send it to:

```text
Burp Repeater
```

---

## Step 2 — Test SSRF

Define an external entity referencing an internal resource.

Conceptual structure:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "http://internal-resource">
]>
```

Reference the entity somewhere in the XML body:

```xml
&xxe;
```

---

## Step 3 — Identify Internal Response

Observe whether the response contains information from the internal resource.

The goal is to determine the internal administration interface and identify the endpoint used to delete Carlos.

---

## Step 4 — Access the Internal Admin Interface

Use the SSRF primitive to interact with the internal administration functionality.

Conceptually:

```text
XXE
 ↓
SSRF
 ↓
Internal Admin Panel
 ↓
Delete Carlos
```

---

## Why It Works

The attacker cannot directly access the internal application.

However:

```text
Attacker
   ↓
Vulnerable Application
   ↓
Internal Application
```

allows the vulnerable server to make the request on the attacker's behalf.

---

## Key Learning

XXE can become an SSRF primitive when external entities are allowed to reference URLs.

---

## Testing Checklist

```text
☐ Identify XML endpoint
☐ Confirm external entity processing
☐ Test controlled URL
☐ Identify internal resource
☐ Map internal functionality
☐ Determine administrative endpoint
☐ Demonstrate security impact
```