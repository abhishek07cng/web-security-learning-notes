# Lab 01 — Exploiting Path Mapping for Web Cache Deception

## Objective

Exploit a path-mapping discrepancy to retrieve sensitive information from a cached response.

---

# Core Concept

The lab demonstrates how an origin server can abstract additional path segments while the cache treats the URL as a cacheable static resource.

---

# Methodology

```text
Identify Sensitive Endpoint
        ↓
Add Arbitrary Path Segment
        ↓
Confirm Origin Still Returns Sensitive Data
        ↓
Add Static Extension
        ↓
Confirm Cache Behavior
        ↓
Trigger Victim Request
        ↓
Retrieve Cached Response
```

---

# Burp Workflow

## 1. Identify Target

Log in to the lab application and identify a sensitive endpoint.

Inspect the response in Burp.

Look for sensitive information that belongs to the authenticated user.

---

## 2. Send Request to Repeater

In:

```text
Proxy → HTTP history
```

right-click the relevant GET request and select:

```text
Send to Repeater
```

---

## 3. Test Path Mapping

Add an arbitrary path segment.

Example:

```text
/my-account/abc
```

Compare the response with:

```text
/my-account
```

If the origin returns the same sensitive response, the path may be abstracted.

---

## 4. Add Static Extension

Modify the path:

```text
/my-account/abc.js
```

Observe whether the response is cached.

---

## 5. Confirm Cache Behavior

Check:

```text
X-Cache
```

A useful sequence is:

```text
X-Cache: miss
```

followed by:

```text
X-Cache: hit
```

---

## 6. Trigger the Victim Request

The lab requires causing the victim to visit the malicious URL.

Use the lab's exploit server to deliver the crafted URL to the victim.

The URL should be unique so that an earlier cached response does not interfere.

---

## 7. Retrieve Cached Response

Request the same malicious URL after the victim has accessed it.

The response should contain the victim's sensitive information.

---

# Important

Use the exact lab environment and authorized target only.

---

# Key Learning

A path-mapping discrepancy can allow:

```text
Cache
   ↓
Static Resource

Origin
   ↓
Sensitive Dynamic Resource
```

The resulting response can become cached and accessible through the malicious URL.