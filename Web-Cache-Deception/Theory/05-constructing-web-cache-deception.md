# Constructing a Web Cache Deception Attack

## Overview

A basic Web Cache Deception attack involves finding a discrepancy between how the cache server and origin server interpret a URL.

The attacker uses this discrepancy to make the cache store a dynamic response containing sensitive information. The attacker can then request the same URL and retrieve the cached response.

---

# Core Attack Flow

```text
Identify Sensitive Endpoint
          ↓
Find Cache / Origin Discrepancy
          ↓
Craft Malicious URL
          ↓
Victim Requests URL
          ↓
Origin Returns Sensitive Data
          ↓
Cache Stores Response
          ↓
Attacker Requests Same URL
          ↓
Cached Sensitive Data
Step 1 — Identify a Target Endpoint

First identify an endpoint that returns a dynamic response containing sensitive information.

Examples may include:

/my-account
/profile
/orders

The important characteristic is that the response contains information specific to the authenticated user.

Review Burp Responses

Sensitive information may not be visible on the rendered web page.

Therefore, inspect the actual HTTP responses in Burp Suite.

Look for:

API Keys
Account Information
Personal Data
Session-Related Information
Other Sensitive Data
Prefer Safe HTTP Methods

Focus on endpoints supporting:

GET
HEAD
OPTIONS

Requests that modify the application's state are generally not cached.

For example:

GET /my-account

is a better candidate than a request that performs a state-changing action.

Step 2 — Identify a Cache / Origin Discrepancy

The next step is to determine whether the cache and origin server interpret the URL differently.

The source material identifies three major categories:

Path Mapping
Delimiter Processing
Path Normalization
Path Mapping

The origin and cache may map URL paths to resources differently.

For example:

/my-account/abc

may be interpreted by the origin as:

/my-account

while the cache may treat the entire path literally.

Adding a static extension can then produce:

/my-account/abc.js

The origin may still return:

/my-account

while the cache sees:

/my-account/abc.js

and applies a .js cache rule.

Delimiter Processing

The cache and origin may disagree about the meaning of special delimiter characters.

Conceptually:

URL
 ↓
Cache interpretation
      ≠
Origin interpretation

If the discrepancy causes the origin to return sensitive content while the cache considers the URL cacheable, this can potentially lead to Web Cache Deception.

Path Normalization

The cache and origin may also normalize paths differently.

Examples of normalization-related differences can involve:

Dot segments
Encoded characters
Path separators
URL decoding

A URL may therefore represent different logical resources to the cache and origin.

Step 3 — Craft the Malicious URL

Once a discrepancy is identified, construct a URL that satisfies both conditions:

Origin
  ↓
Returns sensitive dynamic content

and:

Cache
  ↓
Treats the request as cacheable

For a static-extension technique, the general pattern is:

/<dynamic-endpoint>/<arbitrary-segment>.js

For example:

/my-account/wcd.js

The exact URL depends on the behavior discovered during testing.

Step 4 — Use a Cachebuster During Testing

Each test request should normally have a different cache key.

Otherwise, an earlier cached response can affect the result.

Example:

/my-account/abc.js?cb=001
/my-account/abc.js?cb=002
/my-account/abc.js?cb=003

This creates different cache keys when query parameters are included in the cache key.

Param Miner

Burp Suite's Param Miner extension can automate dynamic cachebusters.

The source workflow is:

Param Miner
    ↓
Settings
    ↓
Add dynamic cachebuster

Burp then adds a unique query string to requests.

The generated cachebusters can be viewed in the Logger tab.

Step 5 — Detect Whether the Response Is Cached

Inspect response headers and timing.

A common indicator is:

X-Cache: miss

The first request may produce:

X-Cache: miss

Send the same request again.

If it becomes:

X-Cache: hit

this indicates that the response was served from the cache.

Other Indicators

Also inspect:

Cache-Control

For example:

Cache-Control: public, max-age=30

A positive max-age suggests that the response may be cacheable.

However:

Cache-Control
      ≠
Proof of actual caching

The cache can sometimes override the header.

Response Timing

Response time can provide additional evidence.

For example:

First request  → slower
Second request → significantly faster

The faster response may have been served from the cache.

Timing should be treated as supporting evidence rather than definitive proof.

Step 6 — Confirm the Attack

Once the malicious URL is constructed:

Victim
  ↓
Requests malicious URL
  ↓
Origin returns victim's sensitive response
  ↓
Cache stores response

The attacker can then request the same URL:

Attacker
  ↓
Same malicious URL
  ↓
Cache Hit
  ↓
Victim's cached response

This demonstrates the security impact.

Important Burp Workflow

Use Burp to verify the behavior rather than relying solely on the browser.

A useful workflow is:

Identify Endpoint
      ↓
Send to Repeater
      ↓
Baseline Request
      ↓
Add Path Segment
      ↓
Check Origin Behavior
      ↓
Add Cacheable Pattern
      ↓
Check X-Cache
      ↓
Use Cachebuster
      ↓
Repeat Request
      ↓
Confirm Cache Hit

The source material specifically recommends using Burp to retrieve the cached response during testing.

Why Not Rely Only on the Browser?

Some applications may:

Redirect unauthenticated users
Invalidate local data
Change behavior based on browser state

These behaviors can hide or complicate the vulnerability.

Burp Repeater provides more direct control over the request and response.

Example: Path Mapping Technique

Suppose the sensitive endpoint is:

/my-account
Baseline
/my-account

Returns sensitive account information.

Add Arbitrary Segment
/my-account/abc

If the same sensitive response is returned, the origin may be abstracting the path.

Add Static Extension
/my-account/abc.js

If the response becomes cached:

X-Cache: miss

followed by:

X-Cache: hit

the cache may be applying a .js cache rule while the origin still treats the request as /my-account.

Complete Example
Sensitive Endpoint
      │
      ▼
/my-account
      │
      ▼
Add arbitrary segment
      │
      ▼
/my-account/abc
      │
      ▼
Origin still returns account data
      │
      ▼
Add static extension
      │
      ▼
/my-account/abc.js
      │
      ├───────────────┐
      ▼               ▼
   Origin            Cache
      │               │
      ▼               ▼
/my-account       *.js rule
      │               │
      ▼               ▼
Sensitive data    Cache response
      │               │
      └───────┬───────┘
              ▼
       Sensitive data
          is cached
              │
              ▼
          Attacker
              │
              ▼
       Retrieves cache
Attack Requirements

A successful Web Cache Deception attack generally requires:

1. Sensitive dynamic endpoint
        +
2. Cacheable interpretation
        +
3. Origin/cache URL discrepancy
        +
4. Victim request
        +
5. Cached response accessible to attacker
Important Limitation

A discrepancy does not automatically mean that every endpoint is vulnerable.

The source material notes that path-mapping attacks can be limited to the specific endpoint tested because different endpoints may have different abstraction rules.

Therefore:

One vulnerable endpoint
      ≠
Entire application vulnerable

Test each relevant endpoint independently.

Testing Checklist
☐ Find sensitive dynamic endpoint
☐ Inspect actual HTTP response
☐ Prefer GET / HEAD / OPTIONS
☐ Establish baseline
☐ Test arbitrary path segment
☐ Check origin interpretation
☐ Test static extensions
☐ Test delimiters
☐ Test normalization
☐ Use unique cachebusters
☐ Inspect X-Cache
☐ Inspect Cache-Control
☐ Compare response timing
☐ Confirm cache hit
☐ Verify cached response
☐ Assess impact
☐ Document minimal reproduction
Final Methodology
IDENTIFY
   ↓
Sensitive Dynamic Endpoint
   ↓
BASELINE
   ↓
Find Origin Behavior
   ↓
Find Cache Behavior
   ↓
Identify Discrepancy
   ↓
Craft Cacheable URL
   ↓
Use Cachebuster
   ↓
Confirm Cache Miss
   ↓
Trigger Victim Request
   ↓
Confirm Cache Hit
   ↓
Retrieve Cached Response
   ↓
Document Impact
Key Takeaways
Start with a dynamic endpoint containing sensitive information.
Prefer GET, HEAD, or OPTIONS endpoints.
Look for discrepancies in path mapping, delimiter processing, or normalization.
Make the cache interpret the request as cacheable while the origin returns sensitive content.
Use unique cachebusters during testing.
X-Cache: miss followed by X-Cache: hit is useful evidence of caching.
Use Burp Repeater to inspect and retrieve cached responses.
Confirm the actual security impact instead of assuming that a discrepancy is exploitable.