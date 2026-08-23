# Web Cache Deception — Bug Bounty Checklist

## Target Discovery

- [ ] Identify authenticated endpoints.
- [ ] Look for endpoints returning user-specific information.
- [ ] Check `/my-account`, `/profile`, `/orders`, `/settings`, and similar endpoints.
- [ ] Inspect the actual HTTP response in Burp Suite.
- [ ] Identify sensitive information in the response.
- [ ] Prefer GET requests when investigating cache behavior.

---

# Baseline Testing

- [ ] Send the original request to Burp Repeater.
- [ ] Record the normal status code.
- [ ] Record the response body.
- [ ] Record relevant response headers.
- [ ] Check `X-Cache`.
- [ ] Check `Cache-Control`.
- [ ] Record response timing.
- [ ] Establish the normal behavior before modifying the URL.

---

# Path Mapping Testing

- [ ] Add an arbitrary path segment.

Example:

```text
/my-account/abc
```

- [ ] Compare the response with the original endpoint.
- [ ] Check whether the origin still returns the same sensitive response.
- [ ] Try adding a static extension.

Example:

```text
/my-account/abc.js
```

- [ ] Test multiple static extensions.

```text
.js
.css
.ico
.exe
```

- [ ] Determine which extensions trigger caching behavior.

---

# Delimiter Testing

- [ ] Test possible path delimiters.
- [ ] Compare the response against a reference request.
- [ ] Determine whether the origin treats a character as a delimiter.
- [ ] Determine whether the cache treats the same character as a delimiter.
- [ ] Look for differences between the two interpretations.

Example:

```text
/my-account;abc.js
```

---

# Delimiter Decoding Testing

- [ ] Test encoded versions of relevant delimiters.
- [ ] Compare cache and origin behavior.
- [ ] Test encoded characters such as:

```text
%23
%3f
%00
%0A
%09
```

- [ ] Determine whether decoding happens before or after cache-rule processing.
- [ ] Check whether an encoded delimiter allows a static extension to be recognized by the cache.

---

# Normalization Testing

- [ ] Test encoded slashes.
- [ ] Test dot-segments.
- [ ] Test encoded dot-segments.
- [ ] Compare origin normalization with cache normalization.

Useful representations include:

```text
%2f
%2e
..
```

---

# Static Directory Testing

Identify possible static directories:

```text
/static
/assets
/scripts
/images
```

Then:

- [ ] Confirm whether the cache uses the directory as a cache rule.
- [ ] Test encoded traversal sequences.
- [ ] Compare cache and origin interpretation.

Example:

```text
/static/..%2fprofile
```

- [ ] Determine whether the origin interprets the path as the sensitive endpoint.
- [ ] Determine whether the cache still considers the request part of the static directory.
- [ ] Confirm whether the sensitive response is cached.

---

# Exact File-Name Testing

Identify commonly cached file names:

```text
/index.html
/robots.txt
/favicon.ico
```

- [ ] Confirm that the file is actually cached.
- [ ] Test normalization around the file name.
- [ ] Test encoded traversal sequences.

Example:

```text
/profile%2f%2e%2e%2findex.html
```

- [ ] Determine whether the cache normalizes the URL to the exact cached file.
- [ ] Determine whether the origin interprets the URL differently.

---

# Cache Detection

Check:

```text
X-Cache
Cache-Control
Response Time
Response Body
```

Look for:

```http
X-Cache: miss
```

followed by:

```http
X-Cache: hit
```

- [ ] Confirm the response was actually cached.
- [ ] Do not rely only on `Cache-Control`.
- [ ] Compare the response body before and after caching.

---

# Cachebuster Testing

Use unique cachebusters during investigation:

```text
?cb=001
?cb=002
?cb=003
```

Example:

```text
/my-account/abc.js?cb=001
```

- [ ] Use a new cachebuster when starting an independent test.
- [ ] Avoid allowing an earlier cached response to contaminate the test.
- [ ] Remember that changing the cachebuster can create a different cache key.

---

# Victim Interaction

When testing an authorized lab or bug-bounty target:

- [ ] Confirm the crafted URL first.
- [ ] Ensure the URL causes the origin to return sensitive content.
- [ ] Ensure the cache considers the response cacheable.
- [ ] Trigger the authorized victim interaction.
- [ ] Wait for the response to become cached.
- [ ] Request the same cache key.
- [ ] Confirm whether the cached response contains the victim's information.

---

# Impact Verification

- [ ] Confirm that sensitive information is present.
- [ ] Confirm that the response was stored by the cache.
- [ ] Confirm that the same URL can return the cached response.
- [ ] Confirm that the information belongs to another user.
- [ ] Demonstrate unauthorized retrieval where permitted by the testing program.

---

# Evidence Collection

Record:

```text
Target URL
Original Request
Modified Request
HTTP Method
Status Code
Response Body
X-Cache
Cache-Control
Response Time
Cachebuster
Cache Key Behavior
Origin Interpretation
Cache Interpretation
```

Take screenshots where useful.

Save the relevant Burp requests and responses.

---

# Burp Suite Checklist

```text
☐ Proxy → HTTP history
☐ Identify sensitive request
☐ Send to Repeater
☐ Establish baseline
☐ Modify path
☐ Test extensions
☐ Test delimiters
☐ Test encoded delimiters
☐ Test normalization
☐ Check cache headers
☐ Repeat request
☐ Confirm cache hit
☐ Document response
```

---

# Vulnerability Confirmation

A strong Web Cache Deception finding should demonstrate:

```text
Sensitive Dynamic Endpoint
          +
Cache / Origin Discrepancy
          +
Cacheable Interpretation
          +
Actual Cached Response
          +
Sensitive Data
          +
Unauthorized Retrieval
```

---

# Important Distinctions

```text
Cacheable
   ≠
Actually Cached
```

```text
Actually Cached
   ≠
Vulnerable
```

A discrepancy alone is not enough.

The security impact must be demonstrated.

---

# Final Checklist

```text
[ ] Sensitive endpoint identified
[ ] Baseline established
[ ] Origin behavior understood
[ ] Cache behavior understood
[ ] Path mapping tested
[ ] Static extensions tested
[ ] Delimiters tested
[ ] Encoded delimiters tested
[ ] Normalization tested
[ ] Static directory rules tested
[ ] Exact file-name rules tested
[ ] Cachebuster used
[ ] Cache miss observed
[ ] Cache hit observed
[ ] Sensitive response confirmed
[ ] Unauthorized retrieval demonstrated
[ ] Evidence collected
[ ] Minimal reproduction documented
```

---

# Key Takeaways

- Start with sensitive dynamic content.
- Understand both origin and cache behavior.
- Test path mapping, delimiters, decoding, and normalization.
- Investigate static extensions, directories, and exact file-name rules.
- Use unique cachebusters during investigation.
- Confirm actual cache behavior.
- Confirm that sensitive information is stored.
- Demonstrate unauthorized retrieval before considering the issue confirmed.