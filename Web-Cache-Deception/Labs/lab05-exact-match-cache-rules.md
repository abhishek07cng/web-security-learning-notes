# Lab 05 — Exploiting Exact-Match Cache Rules

## Objective

Exploit a discrepancy between cache and origin server normalization to make a sensitive dynamic response match an exact-match cache rule.

---

# Core Concept

Some caches use exact file-name rules.

For example:

```text
/index.html
```

may be configured as a cacheable resource.

The attack attempts to make:

```text
Cache
   ↓
Normalize URL
   ↓
Match exact cached file

Origin
   ↓
Interpret URL differently
   ↓
Return sensitive content
```

---

# Basic Methodology

```text
Identify Exact-Match Cached File
        ↓
Confirm Cache Rule
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

# Step 1 — Identify Exact-Match Cache Rule

Look for a commonly cached file.

Examples:

```text
/index.html
/robots.txt
/favicon.ico
```

Send a GET request and inspect:

```text
X-Cache
Cache-Control
Response Time
```

---

# Step 2 — Establish Cache Behavior

Request the known cached resource:

```text
/index.html
```

A possible response is:

```text
X-Cache: miss
```

Repeat the request:

```text
/index.html
```

A possible response is:

```text
X-Cache: hit
```

This establishes that the resource is cached.

---

# Step 3 — Test Origin Normalization

Identify the sensitive endpoint.

For example:

```text
/my-account
```

Test encoded traversal behavior:

```text
/aaa/..%2fmy-account
```

Compare the response with:

```text
/my-account
```

This helps determine how the origin handles:

```text
%2f
```

and:

```text
..
```

---

# Step 4 — Test Cache Normalization

Now construct a URL that contains:

```text
Encoded slash
+
Encoded dot-segments
+
Known cached file name
```

Example:

```text
/profile%2f%2e%2e%2findex.html
```

The cache may normalize this to:

```text
/index.html
```

and therefore match the exact file-name cache rule.

---

# Cache Interpretation

```text
/profile%2f%2e%2e%2findex.html
              │
              ▼
       Cache normalization
              │
              ▼
         /index.html
              │
              ▼
      Exact-match rule
              │
              ▼
       Response cached
```

---

# Origin Interpretation

The origin may process the same URL differently.

Conceptually:

```text
/profile%2f%2e%2e%2findex.html
              │
              ▼
       Origin processing
              │
              ▼
       Different resource
```

The exact behavior depends on the application's routing and normalization logic.

---

# Step 5 — Identify the Discrepancy

The useful condition is:

```text
Cache
   ↓
Resolves encoded dot-segments
   ↓
Matches /index.html

Origin
   ↓
Does not resolve the same sequence
   ↓
Processes another resource
```

This discrepancy can potentially cause a sensitive origin response to be stored under a cacheable file name.

---

# Step 6 — Construct the Malicious URL

Use the discovered normalization behavior.

A general pattern is:

```text
/<path>%2f%2e%2e%2f<cached-file>
```

Example:

```text
/profile%2f%2e%2e%2findex.html
```

The exact payload must be based on the behavior observed in the lab.

---

# Step 7 — Confirm Cache Behavior

Send the crafted request through Burp Repeater.

Inspect:

```text
X-Cache
Cache-Control
Response Body
Response Time
```

A useful sequence is:

```text
X-Cache: miss
```

followed by:

```text
X-Cache: hit
```

when the same cache key is requested again.

---

# Step 8 — Trigger the Victim

Use the lab exploit server to make the victim visit the crafted URL.

The victim's request causes the origin to generate the sensitive response.

The cache then stores the response according to its cache rule.

---

# Step 9 — Retrieve the Cached Response

Request the same malicious URL after the victim has accessed it.

If successful:

```text
Attacker
   ↓
Malicious URL
   ↓
Cache Hit
   ↓
Victim's Sensitive Response
```

The response should contain the sensitive information required by the lab.

---

# Burp Suite Workflow

```text
Identify Cached File
        ↓
Confirm Exact-Match Rule
        ↓
Identify Sensitive Endpoint
        ↓
Test Origin Normalization
        ↓
Test Cache Normalization
        ↓
Construct Payload
        ↓
Send to Repeater
        ↓
Check X-Cache
        ↓
Trigger Victim
        ↓
Request Same URL
        ↓
Retrieve Cached Response
```

---

# Cachebuster Consideration

During investigation, use unique cache keys where appropriate.

For example:

```text
/profile%2f%2e%2e%2findex.html?cb=001
```

Then:

```text
/profile%2f%2e%2e%2findex.html?cb=002
```

However, remember that changing the query string can create a different cache key.

The final victim and attacker requests must therefore use the same cache key when demonstrating the vulnerability.

---

# Detection Conditions

A successful exact-match WCD technique generally requires:

```text
1. Sensitive dynamic endpoint
        +
2. Known exact-match cache rule
        +
3. Cache normalization behavior
        +
4. Origin/cache normalization discrepancy
        +
5. Sensitive response actually cached
        +
6. Cached response accessible to attacker
```

---

# Important Distinction

Finding that:

```text
/profile%2f%2e%2e%2findex.html
```

is normalized to:

```text
/index.html
```

does not automatically prove a vulnerability.

You must also demonstrate that the resulting cached response contains sensitive information and can be retrieved in an unauthorized context.

---

# Key Takeaways

- Exact-match cache rules target specific file names.
- Common examples include `index.html`, `robots.txt`, and `favicon.ico`.
- Encoded path traversal can expose differences in cache and origin normalization.
- The cache may normalize a malicious URL to a known cached file.
- The origin may interpret the same URL differently.
- This discrepancy can potentially cause sensitive content to be cached.
- Confirm the actual cache hit and sensitive response.
- The final exploit must use the same cache key for the victim and attacker.