# Web Cache Deception — Testing Checklist

## Target Identification

- [ ] Identify authenticated endpoints.
- [ ] Look for endpoints returning sensitive, user-specific information.
- [ ] Inspect HTTP responses in Burp Suite.
- [ ] Prefer endpoints using GET, HEAD, or OPTIONS.
- [ ] Record the normal response before modifying the request.

---

## Baseline

Record:

```text
HTTP Method
URL
Status Code
Response Body
Response Headers
X-Cache
Cache-Control
Response Time
```

Example:

```http
GET /my-account
```

---

## Path Mapping

Test an arbitrary path segment:

```text
/my-account/abc
```

Compare it with:

```text
/my-account
```

Ask:

```text
Does the origin still return the same response?
```

If yes, investigate whether the origin uses REST-style URL mapping or another form of path abstraction.

---

## Static Extension Testing

Test common static extensions:

```text
.js
.css
.ico
.exe
```

Example:

```text
/my-account/abc.js
```

Check whether the response becomes cached.

A cached response may indicate:

```text
Origin → ignores /abc.js
Cache  → recognizes .js
```

---

## Delimiter Testing

Start with an arbitrary string:

```text
/my-accountabc
```

Then insert possible delimiter characters:

```text
/my-account;abc
/my-account?abc
```

Compare the responses.

If a delimiter produces the same response as:

```text
/my-account
```

the origin may interpret that character as a delimiter.

---

## Burp Intruder

Use:

```text
/my-account§§abc
```

Test a list of possible delimiter characters.

Under:

```text
Payloads → Payload encoding
```

disable automatic URL encoding when necessary so that delimiters are sent as intended.

---

## Encoded Delimiters

Test encoded representations where relevant:

```text
%23
%3f
```

Also investigate other encoded characters if the application behavior suggests they may be relevant.

---

## Normalization Testing

Investigate:

```text
Encoded slash
Encoded dot
Dot-segments
Encoded dot-segments
```

Examples:

```text
%2f
%2e
..
```

Example:

```text
/aaa/..%2fmy-account
```

Compare the response with:

```text
/my-account
```

---

## Static Directory Rules

Look for common static prefixes:

```text
/static
/assets
/scripts
/images
/resources
```

Identify requests that appear to be cached.

Then test whether the cache rule is based on the directory prefix.

Example:

```text
/assets/aaa
```

If the response is still cached despite the arbitrary resource name, this can indicate a directory-prefix cache rule.

---

## File Name Rules

Look for commonly cached files:

```text
/robots.txt
/index.html
/favicon.ico
```

Confirm caching by checking:

```text
X-Cache: miss
```

and then:

```text
X-Cache: hit
```

---

## Cachebusters

Use a different cache key for each independent test.

Examples:

```text
?wcd=001
?wcd=002
?wcd=003
```

Param Miner can automate dynamic cachebusters.

---

## Detecting Cached Responses

Check:

```text
X-Cache
Cache-Control
Response Time
```

Important values:

```text
X-Cache: hit
X-Cache: miss
X-Cache: dynamic
X-Cache: refresh
```

Interpretation:

```text
hit
↓
Served from cache

miss
↓
Not currently cached

dynamic
↓
Generally not suitable for caching

refresh
↓
Cached response refreshed/revalidated
```

---

## Final Vulnerability Conditions

A strong WCD finding requires:

```text
Sensitive Dynamic Endpoint
        +
Cache / Origin Discrepancy
        +
Cacheable Interpretation
        +
Actual Cached Response
        +
Sensitive Information
        +
Unauthorized Retrieval
```

---

## Evidence to Record

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
Origin Interpretation
Cache Interpretation
```

---

## Final Checklist

```text
☐ Sensitive endpoint identified
☐ Baseline established
☐ Path mapping tested
☐ Static extensions tested
☐ Delimiters tested
☐ Encoded delimiters tested
☐ Normalization tested
☐ Static directory rules tested
☐ File-name rules tested
☐ Cachebuster used
☐ Cache miss observed
☐ Cache hit observed
☐ Sensitive response confirmed
☐ Unauthorized retrieval verified
☐ Evidence documented
```