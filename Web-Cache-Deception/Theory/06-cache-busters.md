# Cache Busters

## Overview

A cachebuster is a changing query string that creates a unique cache key for each request.

Cachebusters are useful during Web Cache Deception testing because previously cached responses can otherwise interfere with your results.

---

# Why Cachebusters Are Needed

When testing cache behavior, you may send the same URL multiple times.

If the response from an earlier request has already been cached, a later request may receive that cached response instead of reaching the origin server.

This can make testing results misleading.

```text
Test Request
     ↓
Response Cached
     ↓
Second Test
     ↓
Cached Response
     ↓
Misleading Result
Basic Cachebuster

A simple cachebuster can be added as a query parameter:

?cb=001

For example:

/my-account/abc.js?cb=001

The next request can use:

/my-account/abc.js?cb=002

Then:

/my-account/abc.js?cb=003
Why This Works

The URL path and query parameters are typically included in the cache key.

Therefore:

/my-account/abc.js?cb=001

and:

/my-account/abc.js?cb=002

can generate different cache keys.

Conceptually:

Request 1
   ↓
Cache Key A

Request 2
   ↓
Cache Key B

where:

Cache Key A ≠ Cache Key B
Cachebuster Testing Flow
Request
   ↓
Add Unique Cachebuster
   ↓
Send Request
   ↓
Observe Response
   ↓
Change Cachebuster
   ↓
Send Again
   ↓
Compare Results
Example

Suppose the target endpoint is:

/my-account

First test:

/my-account?cb=001

Second test:

/my-account?cb=002

Third test:

/my-account?cb=003

Each request is intended to use a different cache key.

Cachebuster and Web Cache Deception

During WCD testing, you may test a URL such as:

/my-account/abc.js

If you repeatedly send exactly the same request, the cache state can affect the results.

Instead, during investigation you can use:

/my-account/abc.js?cb=001
/my-account/abc.js?cb=002
/my-account/abc.js?cb=003

This allows you to investigate behavior without unintentionally reusing an earlier cache entry.

Param Miner

The source material recommends using the Param Miner extension to automate dynamic cachebusters.

Workflow:

Param Miner
    ↓
Settings
    ↓
Add dynamic cachebuster

Burp then adds a unique query string to requests.

The generated query strings can be viewed in the Logger tab.

Why Automation Helps

Manual cachebusters require you to continuously change the value:

cb=001
cb=002
cb=003
cb=004
...

Param Miner can automate this process so that each request receives a unique cachebuster.

Cachebuster vs Normal Query Parameter

A cachebuster does not necessarily have application meaning.

For example:

?cb=001

may simply exist to change the cache key.

It is primarily useful for controlling cache state during testing.

Cachebuster and Cache Keys

The relationship is:

Cachebuster
     ↓
Changes Query String
     ↓
Changes Cache Key
     ↓
Prevents Reuse of Previous Cache Entry

This makes cachebusters particularly useful when investigating cache behavior.

Detecting Cache Behavior

Use a cachebuster and inspect the response.

For example:

GET /my-account/abc.js?cb=001

Possible response:

X-Cache: miss

Then repeat the same request:

GET /my-account/abc.js?cb=001

Possible response:

X-Cache: hit

This can indicate that the response associated with that cache key was cached.

Changing the Cachebuster

Now change:

cb=001

to:

cb=002

The cache key may change:

cb=001
   ↓
Cache Key A

cb=002
   ↓
Cache Key B

Therefore, the new request can be tested independently.

Important: Final Exploit URL

Cachebusters are useful during investigation, but remember that changing the query string can also change the cache key.

For example:

/my-account/abc.js?cb=001

and:

/my-account/abc.js?cb=002

may be different cache entries.

Therefore, when demonstrating a WCD vulnerability, make sure the victim and attacker ultimately use the same cache key.

Burp Testing Workflow
Find Sensitive Endpoint
        ↓
Send to Repeater
        ↓
Add Cachebuster
        ↓
Send Request
        ↓
Check X-Cache
        ↓
Change Cachebuster
        ↓
Send Again
        ↓
Compare Responses
        ↓
Identify Cache Behavior
Practical Checklist
☐ Add unique cachebuster
☐ Send request
☐ Record response
☐ Check X-Cache
☐ Check Cache-Control
☐ Record response timing
☐ Change cachebuster
☐ Repeat request
☐ Compare results
☐ Avoid relying on stale cached responses
Key Takeaways
Cachebusters help prevent previous cached responses from affecting tests.
Query parameters are typically part of the cache key.
Changing a cachebuster can therefore create a new cache key.

Example:

?cb=001
?cb=002
?cb=003
Param Miner can automate dynamic cachebusters.
X-Cache and response timing can help determine whether caching occurred.
A cachebuster changes the cache key, so the final victim and attacker requests must use the same cache key when demonstrating the vulnerability.