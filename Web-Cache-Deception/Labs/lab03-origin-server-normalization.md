# Lab 03 — Exploiting Origin Server Normalization

## Objective

Exploit a discrepancy in how the origin server and cache server normalize URL paths.

The lab requires obtaining the API key for the victim.

---

# Core Concept

The attack uses encoded path traversal to make the origin and cache interpret the same URL differently.

---

# Methodology

```text
Identify Sensitive Endpoint
        ↓
Test Origin Normalization
        ↓
Test Cache Normalization
        ↓
Identify Discrepancy
        ↓
Construct Malicious URL
        ↓
Trigger Victim Request
        ↓
Retrieve Cached Response
```

---

# Step 1 — Identify Target

Log in to the lab application and identify the sensitive account endpoint.

The relevant endpoint is:

```text
/my-account
```

The response contains sensitive account information.

---

# Step 2 — Test Origin Normalization

Send the request to Repeater.

Add an arbitrary directory and encoded traversal sequence:

```text
/aaa/..%2fmy-account
```

The lab response is:

```text
404 Not Found
```

This indicates that the origin server does not decode the slash and resolve the dot-segment.

---

# Step 3 — Test Cache Normalization

The lab provides a static directory cache rule.

Investigate how the cache handles encoded traversal.

Conceptually:

```text
/static/..%2fprofile
```

can be interpreted differently by cache and origin.

---

# Step 4 — Identify the Discrepancy

The objective is to find a path where:

```text
Origin
   ↓
Processes the encoded path differently

Cache
   ↓
Normalizes the path
   ↓
Matches cache rule
```

---

# Step 5 — Construct Exploit

Use the identified normalization behavior to create a URL that causes:

```text
Origin
   ↓
Returns /my-account
```

while:

```text
Cache
   ↓
Interprets the URL as belonging to a cacheable directory
```

---

# Step 6 — Confirm Caching

Check:

```text
X-Cache: miss
```

Then resend the same request.

A successful cache interaction should produce:

```text
X-Cache: hit
```

---

# Step 7 — Trigger Victim

Use the lab exploit server to make the victim request the crafted URL.

Make sure the URL uses a unique cache key so the victim's response is not replaced by a previously cached response.

---

# Step 8 — Retrieve Cached Response

Request the same URL after the victim has accessed it.

The response should contain the victim's API key.

---

# Key Learning

Normalization discrepancies occur when:

```text
Cache Normalization
        ≠
Origin Normalization
```

Encoded path traversal can expose these differences.

The source material specifically uses encoded slash and dot-segment behavior when demonstrating this class of Web Cache Deception attack.
```