# Web Cache Deception — Burp Suite Workflow

## Objective

Use Burp Suite to identify discrepancies between cache and origin server behavior and verify whether sensitive dynamic content can be cached.

---

# 1. Capture Target Request

Open:

```text
Proxy → HTTP history
```

Find a request to a sensitive endpoint.

Example:

```http
GET /my-account
```

Send it to:

```text
Repeater
```

---

# 2. Establish Baseline

Send the request without modification.

Record:

```text
Status Code
Response Body
X-Cache
Cache-Control
Response Time
```

---

# 3. Test Path Mapping

Change:

```text
/my-account
```

to:

```text
/my-account/abc
```

Send the request.

Compare the response with the baseline.

Then test:

```text
/my-accountabc
```

This provides a useful reference when identifying delimiters.

---

# 4. Identify Delimiters with Intruder

Right-click the request and select:

```text
Send to Intruder
```

Use:

```text
/my-account§§abc
```

Select:

```text
Sniper
```

Add a list of possible delimiter characters.

Under:

```text
Payloads → Payload encoding
```

disable URL encoding when required.

Start the attack.

---

# 5. Analyze Intruder Results

Sort by:

```text
Status Code
```

Compare the responses.

If a character produces the same sensitive response as:

```text
/my-account
```

while the arbitrary-string reference produces a different response, the character may be an origin delimiter.

---

# 6. Test Static Extensions

Return to Repeater.

Append an extension to the modified path.

Examples:

```text
/my-account;abc.js
/my-account;abc.css
/my-account;abc.ico
```

Inspect:

```text
X-Cache
```

---

# 7. Test Cache Behavior

A typical sequence:

```text
First Request
      ↓
X-Cache: miss
      ↓
Origin processes request
      ↓
Response potentially cached
```

Repeat:

```text
Second Request
      ↓
X-Cache: hit
```

---

# 8. Test Cache Normalization

Identify cached static resources in:

```text
Proxy → HTTP history
```

Look for prefixes such as:

```text
/assets
/static
/resources
```

Test a traversal sequence.

Example:

```text
/aaa/..%2fassets/js/stockCheck.js
```

Compare cache behavior.

---

# 9. Test Static Directory Cache Rules

If the response remains cached, determine whether another rule is responsible.

Replace the resource after the directory prefix with an arbitrary string:

```text
/assets/aaa
```

If it remains cached, this supports the presence of an `/assets` prefix-based cache rule.

---

# 10. Test Exact File-Name Rules

Identify a commonly cached file.

Example:

```text
/robots.txt
```

Send:

```text
/robots.txt
```

Observe:

```text
X-Cache: miss
```

Resend:

```text
X-Cache: hit
```

This indicates caching based on the file name.

---

# 11. Test Cache Normalization

Try:

```text
/aaa/..%2frobots.txt
```

If this receives cached behavior, the cache may be normalizing the path to:

```text
/robots.txt
```

---

# 12. Test Origin Normalization

Use a dynamic endpoint and test:

```text
/aaa/..%2fmy-account
```

If the origin returns 404 instead of the `/my-account` response, it may not be decoding and resolving the encoded traversal sequence.

---

# 13. Combine Discrepancies

A WCD payload may combine:

```text
Dynamic Endpoint
        +
Origin Delimiter
        +
Encoded Traversal
        +
Static Directory / File Rule
```

Example pattern:

```text
/my-account;%2f%2e%2e%2frobots.txt
```

---

# 14. Use Cachebuster

Add a unique query parameter:

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd001
```

When testing again:

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd002
```

---

# 15. Verify Cached Response

After the victim accesses the crafted URL, request the same cache key in Burp Repeater.

Check:

```text
X-Cache
Response Body
Sensitive Information
```

---

# 16. Browser Limitation

Do not rely exclusively on the browser when testing WCD.

Some applications may:

```text
Redirect unauthenticated requests
Invalidate local data
Change behavior based on session state
```

Use Burp Repeater to inspect the actual response.

---

# Complete Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Sensitive Endpoint
  ↓
Repeater
  ↓
Baseline
  ↓
Path Mapping
  ↓
Intruder Delimiter Testing
  ↓
Static Extension Testing
  ↓
Normalization Testing
  ↓
Static Directory Testing
  ↓
File Name Testing
  ↓
Cache Confirmation
  ↓
Victim Request
  ↓
Cached Response
```

---

# Key Burp Tools

```text
Proxy
→ Capture requests

Repeater
→ Manually modify and compare requests

Intruder
→ Test delimiter characters

Logger
→ View requests and dynamic cachebusters

Param Miner
→ Automate cachebusters
```

---

# Practical Notes

```text
Always establish a baseline.

Always compare modified responses.

Check both cache headers and response bodies.

Use unique cache keys during investigation.

Do not assume Cache-Control proves caching.

Confirm X-Cache behavior when available.

Use Repeater for final response verification.
```