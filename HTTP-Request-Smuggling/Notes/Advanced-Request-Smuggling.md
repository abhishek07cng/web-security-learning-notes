# Advanced HTTP Request Smuggling

## Overview

Advanced request smuggling extends beyond the classic:

```text
CL.TE
TE.CL
TE.TE
```

techniques.

The advanced attack surface in these notes includes:

```text
HTTP/2 Downgrading
├── H2.CL
├── H2.TE
├── CRLF Injection
└── HTTP/2 Request Splitting

Response Queue Poisoning

HTTP Request Tunnelling

CL.0 / 0.CL

Client-Side Desync

Pause-Based Desync
```

The core principle remains:

```text
Different components
interpret the same HTTP traffic
differently
        ↓
DESYNCHRONIZATION
```

---

# 1. HTTP/2 Downgrading

HTTP/2 itself has a robust built-in mechanism for determining request length.

However, many architectures look like:

```text
CLIENT
   |
   | HTTP/2
   v
+----------------+
|   FRONT-END    |
+----------------+
        |
        | HTTP/1
        v
+----------------+
|    BACK-END    |
+----------------+
```

The front end rewrites:

```text
HTTP/2
   ↓
HTTP/1
```

before forwarding the request.

This is:

```text
HTTP/2 DOWNGRADING
```

When the HTTP/1 back-end responds, the front end converts the response back for the HTTP/2 client.

---

# 2. Why Downgrading Is Dangerous

With HTTP/2 downgrading, request length may potentially be represented in three different ways:

```text
HTTP/2 built-in length

Content-Length

Transfer-Encoding
```

Conceptually:

```text
             REQUEST LENGTH
                   |
        +----------+----------+
        |          |          |
        v          v          v
      HTTP/2      CL          TE
      framing
```

If the front end and back end rely on different mechanisms:

```text
DESYNC
```

can occur.

---

# 3. H2.CL

```text
H2.CL
```

means:

```text
Front-End → HTTP/2 built-in length
Back-End  → Content-Length
```

HTTP/2 requests do not need to specify their length using a header.

During downgrading, the front end may generate:

```http
Content-Length
```

for the HTTP/1 back-end.

However, HTTP/2 requests can also contain their own:

```http
content-length
```

header.

The specification requires this value to match the length derived from HTTP/2 framing, but the source notes that some implementations fail to validate this correctly before downgrading.

---

# 4. H2.CL Desynchronization

Conceptual HTTP/2 request:

```text
:method        POST
:path          /example
:authority     vulnerable-website.com
content-type   application/x-www-form-urlencoded
content-length 0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Content-Length: 10

x=1
```

The HTTP/2 front end knows the actual request length from HTTP/2.

But the downgraded HTTP/1 request may become:

```http
POST /example HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Content-Length: 10

x=1
```

Back-end:

```text
Content-Length: 0
        ↓
POST body ends immediately
        ↓
GET /admin...
        ↓
interpreted separately
```

Result:

```text
H2.CL DESYNC
```

---

# 5. Handling the Victim's Request

The source highlights an important problem.

The victim's request may be appended to the smuggled prefix.

Its headers can interfere with the attack and cause problems such as:

```text
Duplicate headers
Invalid syntax
Unexpected parsing
```

One technique is to include:

```http
Content-Length:
```

inside the smuggled request and make it slightly longer than the supplied body.

Conceptually:

```text
Smuggled request body
        +
Beginning of victim request
        ↓
consumed as body
```

while the victim's headers can be truncated before they interfere with the intended request structure.

---

# 6. H2.CL Detection Pattern

The source's H2.CL lab begins with:

```http
POST / HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Content-Length: 0

SMUGGLED
```

Repeated requests produce:

```text
Every second request
        ↓
404
```

This confirms that:

```text
SMUGGLED
+
subsequent request
```

are being combined at the back end.

---

# 7. H2.TE

Another downgrade vulnerability is:

```text
H2.TE
```

Meaning:

```text
Front-End → HTTP/2
Back-End  → Transfer-Encoding
```

HTTP/2 does not use chunked transfer encoding in the same way as HTTP/1.

Therefore, a front end should not allow an HTTP/2:

```http
Transfer-Encoding: chunked
```

header to create chunked semantics after downgrading.

If the front end fails to remove it:

```text
HTTP/2 Request
       ↓
Front-End
       ↓
Downgrade
       ↓
Transfer-Encoding survives
       ↓
HTTP/1 Back-End
       ↓
interprets chunked body
```

A desync can occur.

---

# 8. H2.TE Example

Front-end representation:

```text
:method            POST
:path              /example
:authority         vulnerable-website.com
content-type       application/x-www-form-urlencoded
transfer-encoding  chunked

0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Foo: bar
```

Downgraded request:

```http
POST /example HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Foo: bar
```

Back-end interprets:

```text
0
↓
end of chunked body
```

Therefore:

```http
GET /admin HTTP/1.1
```

can become another request.

---

# 9. Hidden HTTP/2 Support

HTTP/2 is normally negotiated using:

```text
ALPN
```

during TLS negotiation.

Some servers support HTTP/2 but fail to advertise it correctly.

Clients then fall back to:

```text
HTTP/1.1
```

and testers may miss the HTTP/2 attack surface.

---

# 10. Forcing HTTP/2 in Burp

The source gives this procedure:

```text
Settings
   ↓
Tools
   ↓
Repeater
   ↓
Connections
   ↓
Allow HTTP/2 ALPN override
```

Then:

```text
Repeater
   ↓
Inspector
   ↓
Request attributes
   ↓
Protocol = HTTP/2
```

This lets Repeater attempt HTTP/2 even when the server does not advertise it normally.

---

# 11. Response Queue Poisoning

Response queue poisoning is more powerful than simply smuggling a prefix.

The attacker smuggles:

```text
A COMPLETE REQUEST
```

so that:

```text
Front-End thinks:
1 request

Back-End sees:
2 requests
```

Therefore:

```text
Front-End expects:
1 response

Back-End generates:
2 responses
```

---

# 12. How the Queue Becomes Poisoned

Initially:

```text
FRONT-END
Request A
    ↓
expects Response A
```

Back-end:

```text
Request A
Request B
    ↓
Response A
Response B
```

The front end forwards:

```text
Response A
```

normally.

But:

```text
Response B
```

has no matching front-end request.

It remains queued on the connection.

---

# 13. Persistent Response Misalignment

When another request arrives:

```text
Request C
```

the front end forwards it normally.

But the first response in the queue is:

```text
Response B
```

Therefore:

```text
Request C → Response B
```

The actual:

```text
Response C
```

then remains queued.

Result:

```text
Request C → Response B
Request D → Response C
Request E → Response D
```

The response queue remains:

```text
DESYNCHRONIZED
```

---

# 14. Requirements for Response Queue Poisoning

The source gives three requirements:

```text
1. Front-end/back-end TCP connection
   must be reused.

2. Attacker must successfully smuggle
   a complete standalone request.

3. Neither server should close
   the connection after the attack.
```

If the connection closes:

```text
Queue state lost
```

---

# 15. Prefix vs Complete Request

Normal request smuggling often uses:

```text
PARTIAL REQUEST
```

such as:

```http
GET /something HTTP/1.1
Foo: x
```

The next request completes it.

For response queue poisoning, the goal is instead:

```text
COMPLETE REQUEST
```

such as:

```http
GET /anything HTTP/1.1
Host: vulnerable-website.com

```

This lets the back end immediately generate a second response.

---

# 16. Avoid Invalid Leftover Data

If the attack leaves malformed bytes behind:

```text
Request 1
Request 2
garbage
```

the server may:

```text
return error
      ↓
close connection
```

This destroys the poisoned state.

The source therefore emphasizes carefully smuggling exactly two valid requests where possible.

---

# 17. H2.TE Response Queue Poisoning

The source's H2.TE example begins:

```http
POST / HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked

0

SMUGGLED
```

Repeated requests returning:

```text
404 on every second request
```

confirm the desync.

A complete request can then be smuggled:

```http
POST /x HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked

0

GET /x HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net

```

The smuggled request must end with:

```text
\r\n\r\n
```

---

# 18. Recognizing Captured Responses

The source deliberately uses:

```text
/x
```

as a nonexistent endpoint.

Expected response:

```text
404
```

Therefore:

```text
404
↓
probably own expected response

Different status
↓
possibly another queued response
```

This makes unexpected responses easier to recognize.

---

# 19. Request Smuggling via CRLF Injection

Even when basic:

```text
H2.CL
```

and:

```text
H2.TE
```

are prevented, HTTP/2's binary representation can introduce other downgrade discrepancies.

The source specifically discusses:

```text
CRLF INJECTION
```

---

# 20. Why HTTP/2 Changes Header Injection

In HTTP/1, headers are text-based and:

```text
\r\n
```

terminates a header.

HTTP/2 is binary.

Its header boundaries are determined by:

```text
explicit predetermined offsets
```

rather than CRLF delimiters.

Therefore, a value containing:

```text
\r\n
```

can potentially be interpreted as:

```text
ordinary header value data
```

by the HTTP/2 front end.

But after HTTP/1 downgrading:

```text
\r\n
```

regains its delimiter meaning.

---

# 21. CRLF Injection Concept

Suppose an HTTP/2 header contains something conceptually like:

```text
foo: bar\r\nTransfer-Encoding: chunked
```

HTTP/2 front-end:

```text
ONE header
```

After downgrading:

```http
Foo: bar
Transfer-Encoding: chunked
```

HTTP/1 back-end:

```text
TWO headers
```

This can bypass front-end validation that only inspected the HTTP/2 header structure.

---

# 22. HTTP/2 Request Splitting

CRLF injection can go beyond injecting one header.

It can potentially inject:

```text
\r\n\r\n
```

which represents the end of HTTP/1 headers.

Then an attacker-controlled value can introduce:

```text
ANOTHER HTTP/1 REQUEST
```

This is:

```text
HTTP/2 REQUEST SPLITTING
```

---

# 23. Request Splitting Example

Conceptually:

```text
:method     GET
:path       /
:authority  vulnerable-website.com
foo         bar\r\n
            \r\n
            GET /admin HTTP/1.1\r\n
            Host: vulnerable-website.com
```

HTTP/2 front end sees:

```text
ONE HTTP/2 REQUEST
```

After downgrading, the HTTP/1 back-end may see:

```http
GET / HTTP/1.1
...

GET /admin HTTP/1.1
Host: vulnerable-website.com
```

Result:

```text
ONE HTTP/2 REQUEST
        ↓
TWO HTTP/1 REQUESTS
```

---

# 24. Why Header Splitting Is Versatile

The source notes that request splitting inside headers is more versatile than relying on a request body.

You are not limited to methods that normally carry a body.

For example:

```text
GET
```

can potentially be used.

This is also useful where:

```text
Content-Length is validated
```

and the back-end does not support:

```text
chunked encoding
```

---

# 25. Accounting for Front-End Rewriting

Request splitting creates another problem.

Both resulting HTTP/1 requests may need mandatory headers such as:

```http
Host:
```

During HTTP/2 downgrading:

```text
:authority
```

is typically converted into:

```http
Host:
```

But different front ends may insert the generated Host header in different locations.

Therefore, the location of your injected:

```http
Host:
```

may need to account for how the front end performs the rewrite.

---

# 26. Example Rewriting Problem

Suppose:

```text
:method     GET
:path       /
:authority  vulnerable-website.com
foo         bar\r\n
            \r\n
            GET /admin HTTP/1.1\r\n
            Host: vulnerable-website.com
```

If the front end appends its generated:

```http
Host:
```

after the injected header, the split may result in:

```text
First request:
NO Host

Second request:
TWO Host headers
```

This may break the attack.

---

# 27. Positioning the Host Header

The source shows that the injected Host header can instead be positioned before the split:

```text
:method     GET
:path       /
:authority  vulnerable-website.com
foo         bar\r\n
            Host: vulnerable-website.com\r\n
            \r\n
            GET /admin HTTP/1.1
```

Now the first request can receive the required:

```http
Host:
```

while the front end's rewritten Host can potentially belong to the second request.

The same principle applies to other internally generated headers.

---

# 28. Request Splitting → Response Queue Poisoning

If request splitting creates:

```text
TWO complete HTTP/1 requests
```

the back end generates:

```text
TWO responses
```

while the HTTP/2 front end expected:

```text
ONE response
```

This can poison the response queue.

Conceptually:

```text
HTTP/2 request
      ↓
CRLF injection
      ↓
HTTP/1 request split
      ↓
Back-End sees 2 requests
      ↓
Back-End sends 2 responses
      ↓
Front-End expects 1
      ↓
RESPONSE QUEUE POISONING
```

---

# 29. HTTP Request Tunnelling

Classic request smuggling often depends on:

```text
Front-End ↔ Back-End
connection reuse
```

But some architectures:

```text
do not reuse connections
```

or only allow reuse for:

```text
same client
same IP
```

This makes it difficult to influence another user's request through classic connection poisoning.

The source introduces:

```text
HTTP REQUEST TUNNELLING
```

for this situation.

---

# 30. Tunnelling Without Connection Reuse

Even without connection reuse, an attacker may still cause:

```text
ONE front-end request
```

to produce:

```text
TWO back-end requests
```

and:

```text
TWO back-end responses
```

Conceptually:

```text
ATTACKER
   |
   | one request
   v
FRONT-END
   |
   | one request expected
   v
BACK-END
   |
   +---- Request A
   |       ↓
   |    Response A
   |
   +---- Request B
           ↓
        Response B
```

This may allow the second request and response to be hidden from the front end.

---

# 31. Why HTTP/2 Helps Detect Tunnelling

In HTTP/1, persistent connections naturally contain multiple:

```text
requests
responses
```

Therefore, observing multiple responses is not necessarily definitive.

HTTP/2 is different.

Each:

```text
STREAM
```

should contain:

```text
ONE REQUEST
ONE RESPONSE
```

Therefore, if an HTTP/2 response contains what appears to be:

```http
HTTP/1.1 200 OK
```

inside its body:

```text
HTTP/2 RESPONSE
      |
      +-- normal response
      |
      +-- embedded HTTP/1 response
```

the source says this provides strong evidence that a second request was successfully tunneled.

---

# 32. CL.0

Another advanced desync variant is:

```text
CL.0
```

Conceptually:

```text
Front-End → respects Content-Length
Back-End  → ignores the body
```

The front end sees:

```text
[ HEADERS + BODY ]
```

while the back end sees:

```text
[ HEADERS ][ LEFTOVER BODY ]
```

The body may then be interpreted as:

```text
another request
```

---

# 33. Client-Side Desync

Traditional request smuggling poisons:

```text
Front-End ↔ Back-End
```

Client-side desync instead targets:

```text
Browser ↔ Server
```

A vulnerable server may:

```text
Receive POST headers
        ↓
Respond without consuming body
        ↓
Leave connection open
        ↓
Browser sends remaining data
        ↓
Connection reused
        ↓
Next browser request affected
```

The source emphasizes that the underlying dangerous assumption is:

```text
"This endpoint won't have a body."
```

---

# 34. Client-Side Desync Mental Model

```text
Victim Browser
      |
      | POST + body
      v
Web Server
      |
      | responds early
      v

BODY BYTES REMAIN
      |
      v

Browser reuses connection
      |
      v

LEFTOVER BODY
+
NEXT REQUEST
      |
      v
DESYNC
```

Unlike classic server-side smuggling, this can potentially affect:

```text
single-server websites
```

because a front-end/back-end pair is not inherently required for the browser/server desync itself.

---

# 35. Pause-Based Desync

Some desync vulnerabilities only appear when transmission is intentionally paused.

Conceptually:

```text
Send request headers
        ↓
PAUSE
        ↓
Back-End waits for body
        ↓
Read timeout
        ↓
Back-End sends response
        ↓
Connection remains open
        ↓
Send remaining body
```

The key problem:

```text
Front-End:
"These bytes are still Request 1."

Back-End:
"Request 1 already finished."
```

Result:

```text
PAUSE-BASED DESYNC
```

---

# 36. Pause-Based CL.0

The behavior resembles:

```text
CL.0
```

because the front end believes the request has a body according to:

```http
Content-Length
```

while the back end eventually responds without consuming that body.

After the timeout:

```text
remaining body
```

can be interpreted by the back end as a new request.

---

# 37. Conditions for Pause-Based Server Desync

The source identifies three important conditions.

### 1. Streaming

The front end must forward request data to the back end as it arrives.

```text
Client
  ↓
Front-End
  ↓ immediately
Back-End
```

---

### 2. Timeout Ordering

The front end must not terminate the request before the back-end timeout behavior occurs.

Conceptually:

```text
Back-End timeout
must become relevant
before Front-End kills flow
```

---

### 3. Connection Reuse

After the back end times out and responds:

```text
connection must remain open
```

Otherwise:

```text
Timeout
   ↓
Connection closed
   ↓
No reusable desynchronized connection
```

---

# 38. Turbo Intruder for Pause-Based Testing

The source uses:

```text
Turbo Intruder
```

for precise pause control.

Example configuration:

```python
engine = RequestEngine(
    endpoint=target.endpoint,
    concurrentConnections=1,
    requestsPerConnection=100,
    pipeline=False
)
```

Important values:

```text
concurrentConnections = 1
pipeline = False
```

---

# 39. Pause Marker

The source uses:

```python
engine.queue(
    target.req,
    pauseMarker=['\r\n\r\n'],
    pauseTime=60000
)
```

Meaning:

```text
Send through end of headers
        ↓
PAUSE
        ↓
60000 ms
        ↓
60 seconds
        ↓
Continue request
```

The source also notes that instead of string matching with `pauseMarker`, an offset can be used with:

```text
pauseBefore
```

For example, pausing before a 34-byte body can be expressed as:

```text
pauseBefore=-34
```

---

# 40. Client-Side Pause-Based Desync

The source states that there is not currently a reliable direct method to make a normal browser intentionally pause in the middle of a request.

It describes a theoretical workaround involving:

```text
ACTIVE MITM
```

The MITM would not need to decrypt the TLS traffic merely to delay selected TCP packets.

Conceptually:

```text
Browser
   |
   | packet
   | packet
   |
   | final packet ← DELAY
   |
   v
Server
   |
   | timeout
   | response
   v
Delayed packet arrives
```

The source presents this as a possible/theoretical client-side variation rather than a reliable browser technique.

---

# 41. Advanced Attack Relationships

```text
HTTP/2 DOWNGRADING
        |
   +----+----+
   |         |
   v         v
 H2.CL     H2.TE
             |
             v
       Complete Request
             |
             v
   Response Queue Poisoning
```

Another route:

```text
HTTP/2
   ↓
CRLF Injection
   ↓
Request Splitting
   ↓
Two HTTP/1 Requests
   ↓
Two Responses
   ↓
Response Queue Poisoning
```

Another:

```text
No Connection Reuse
        ↓
Request Tunnelling
```

And:

```text
Body ignored / timeout behavior
        ↓
       CL.0
        ↓
Client-Side or Pause-Based Desync
```

---

# 42. Advanced Variant Summary

| Technique | Core Discrepancy |
|---|---|
| H2.CL | HTTP/2 length vs Content-Length |
| H2.TE | HTTP/2 framing vs Transfer-Encoding |
| CRLF injection | HTTP/2 header boundaries vs HTTP/1 delimiters |
| Request splitting | One HTTP/2 request becomes multiple HTTP/1 requests |
| Response queue poisoning | Front end expects fewer responses than back end produces |
| Request tunnelling | Hidden back-end request/response without relying on connection reuse |
| CL.0 | Front end expects body; back end ignores it |
| Client-side desync | Browser/server connection becomes desynchronized |
| Pause-based desync | Timeout changes when back end considers request complete |

---

# 43. Prevention Notes From the Source

The source recommends:

```text
Use HTTP/2 end-to-end
```

and:

```text
Disable HTTP downgrading
where possible
```

If downgrading is necessary, validate the rewritten HTTP/1 request.

Examples of malformed input to reject include:

```text
Newlines in headers

Colons in header names

Spaces in request methods
```

---

# 44. Normalize or Reject Ambiguity

The source also recommends:

```text
Front-End
   ↓
normalize ambiguous requests

Back-End
   ↓
reject anything still ambiguous
   ↓
close TCP connection
```

The goal is to prevent different parsers from making independent interpretations of the same ambiguous message.

---

# 45. Never Assume Requests Have No Body

This is especially important for:

```text
CL.0
```

and:

```text
Client-Side Desync
```

The source explicitly identifies the assumption:

```text
"This request won't have a body."
```

as a fundamental cause of these vulnerabilities.

---

# 46. Exception Handling

The source also recommends:

```text
Server-level exception
       ↓
discard connection
```

rather than keeping a potentially desynchronized connection alive.

---

# 47. Master Advanced Map

```text
              ADVANCED REQUEST SMUGGLING
                         |
       +-----------------+------------------+
       |                 |                  |
       v                 v                  v
 HTTP/2 Downgrade    Body Handling      Connection State
       |                 |                  |
   +---+---+          +--+--+          +----+------+
   |       |          |     |          |           |
 H2.CL   H2.TE      CL.0  CSD       Queue       Pause
   |       |                         Poisoning    Desync
   |       |
   |       +---- CRLF Injection
   |                |
   |                v
   |        Request Splitting
   |                |
   +----------------+
                    |
                    v
          Response Queue Poisoning

No connection reuse?
        |
        v
HTTP Request Tunnelling
```

---

# 48. Fast Revision

```text
H2.CL
HTTP/2 → Content-Length discrepancy
```

```text
H2.TE
HTTP/2 → Transfer-Encoding discrepancy
```

```text
CRLF Injection
One HTTP/2 header
→ multiple HTTP/1 headers
```

```text
Request Splitting
One HTTP/2 request
→ two HTTP/1 requests
```

```text
Response Queue Poisoning
Front expects 1 response
Back sends 2
```

```text
Request Tunnelling
Useful even without connection reuse
```

```text
CL.0
Front expects body
Back ignores body
```

```text
Client-Side Desync
Browser ↔ Server poisoned
```

```text
Pause-Based Desync
Pause → timeout → early response
→ remaining bytes interpreted differently
```

---

# Final Mental Model

Don't memorize advanced request smuggling as unrelated attacks.

Think:

```text
             SAME BYTES
                 |
        +--------+--------+
        |                 |
        v                 v
Component A          Component B
interprets as        interprets as
     X                    Y
        \                 /
         \               /
          v             v
          DISAGREEMENT
               |
               v
             DESYNC
               |
        +------+------+
        |             |
        v             v
Request Effects   Response Effects
        |             |
        v             v
Smuggling       Queue Poisoning
Splitting       Data Exposure
Tunnelling
```

The protocol and technique change.

The fundamental weakness remains:

> **Two components disagree about the boundaries or meaning of the same HTTP traffic.**

---

## Next Note

Continue to:

```text
Notes/HTTP2-Request-Smuggling.md
```

This will isolate the HTTP/2-specific material for fast revision:

```text
HTTP/2 framing
Pseudo-headers
HTTP/2 downgrading
H2.CL
H2.TE
Hidden HTTP/2
CRLF injection
Request splitting
Request tunnelling
Response queue poisoning
Burp HTTP/2 workflow
```