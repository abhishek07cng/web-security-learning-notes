# HTTP/2 Request Smuggling

## 1. Core Idea

HTTP request smuggling is fundamentally about:

```text
DISAGREEMENT ABOUT REQUEST LENGTH
```

Classic HTTP/1 attacks exploit ambiguity involving:

```text
Content-Length
Transfer-Encoding
```

HTTP/2 changes how message length is represented.

However:

```text
HTTP/2 Front-End
        ↓
HTTP/1 Back-End
```

can reintroduce request-smuggling vulnerabilities through:

```text
HTTP/2 DOWNGRADING
```

---

# 2. HTTP/2 Message Length

HTTP/2 messages are transmitted as:

```text
FRAMES
```

Each frame has an:

```text
explicit length field
```

Conceptually:

```text
HTTP/2 REQUEST

+------------------+
| Frame Length = A |
| Frame Data       |
+------------------+

+------------------+
| Frame Length = B |
| Frame Data       |
+------------------+

Request Length = A + B
```

This gives HTTP/2 a single robust mechanism for determining request length.

---

# 3. End-to-End HTTP/2

If HTTP/2 is used:

```text
Client
  |
 HTTP/2
  |
  v
Front-End
  |
 HTTP/2
  |
  v
Back-End
```

then the classic HTTP/1 request-length ambiguity does not arise in the same way.

The problem commonly appears when:

```text
HTTP/2
  ↓
HTTP/1
```

conversion occurs.

---

# 4. HTTP/2 Downgrading

Many back-end systems still only support:

```text
HTTP/1
```

Therefore:

```text
Client
  |
  | HTTP/2
  v
Front-End
  |
  | converts request
  v
HTTP/1
  |
  v
Back-End
```

This process is:

```text
HTTP/2 DOWNGRADING
```

The response is converted in the opposite direction:

```text
HTTP/1 Response
      ↓
Front-End
      ↓
HTTP/2 Response
      ↓
Client
```

---

# 5. Why Downgrading Creates Risk

During downgrading, there may effectively be multiple ways to represent request length:

```text
HTTP/2 frame length
Content-Length
Transfer-Encoding
```

So:

```text
        SAME REQUEST
             |
   +---------+---------+
   |         |         |
   v         v         v
HTTP/2      CL        TE
Length
```

If the front end and back end rely on different values:

```text
REQUEST BOUNDARY DISAGREEMENT
             ↓
           DESYNC
```

---

# 6. HTTP/2 Representation in Burp

HTTP/2 is a:

```text
BINARY PROTOCOL
```

The human-readable representation used in Burp and these notes is simplified.

For example:

```text
:method     POST
:path       /example
:authority  vulnerable-website.com
```

HTTP/2 pseudo-headers begin with:

```text
:
```

Examples:

```text
:method
:path
:authority
```

Remember:

> This is a convenient representation. HTTP/2 does not literally look like this on the wire.

---

# 7. H2.CL

```text
H2.CL
```

means:

```text
Front-End → HTTP/2 built-in length

Back-End → Content-Length
```

HTTP/2 does not require a request-length header because its framing already communicates the length.

However, an HTTP/2 request can also contain:

```http
content-length
```

---

# 8. The H2.CL Problem

The HTTP/2 specification requires the supplied:

```http
content-length
```

to match the actual length derived from HTTP/2 framing.

But the source notes that this is not always properly validated before downgrading.

An attacker may therefore supply:

```http
content-length: 0
```

even though the HTTP/2 request actually contains body data.

---

# 9. H2.CL Example

Front-end representation:

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

Front end:

```text
Uses HTTP/2 frame lengths
        ↓
knows body exists
```

After downgrading:

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

Back end:

```text
Content-Length: 0
        ↓
POST ends immediately
        ↓
GET /admin...
becomes another request
```

---

# 10. H2.CL Mental Model

```text
HTTP/2 FRONT-END

Actual body length
determined by frames
       |
       v
[ POST + BODY ]


HTTP/1 BACK-END

Content-Length: 0
       |
       v
[ POST ][ BODY LEFTOVER ]
                |
                v
          Smuggled request
```

---

# 11. Basic H2.CL Probe

The source's H2.CL lab starts with:

```http
POST / HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Content-Length: 0

SMUGGLED
```

If vulnerable:

```text
Front-End
uses HTTP/2 length

Back-End
uses CL = 0
```

so:

```text
SMUGGLED
```

remains available to interfere with the subsequent request.

---

# 12. Confirmation Pattern

The source notes:

```text
Send request repeatedly
        ↓
Every second request returns 404
```

This demonstrates that:

```text
SMUGGLED
+
NEXT REQUEST
```

are being combined by the back end.

---

# 13. Handling Victim Headers

Suppose you smuggle:

```http
GET /admin HTTP/1.1
Host: vulnerable-website.com
```

The victim's request may be appended:

```text
GET /admin HTTP/1.1
Host: vulnerable-website.com
GET / HTTP/1.1
Host: vulnerable-website.com
...
```

This can produce:

```text
duplicate headers
invalid syntax
```

or otherwise interfere with exploitation.

---

# 14. Content-Length Trick

The source demonstrates adding:

```http
Content-Length:
```

to the smuggled prefix.

Example:

```http
GET /resources HTTP/1.1
Host: foo
Content-Length: 5

x=1
```

Using a `Content-Length` slightly longer than the supplied body can cause part of the following request to be consumed as body data.

Conceptually:

```text
Smuggled Body
      +
Beginning of Victim Request
      ↓
Consumed as body
```

This can prevent unwanted victim headers from interfering with the smuggled request.

---

# 15. H2.TE

The second major downgrade variant is:

```text
H2.TE
```

Meaning:

```text
Front-End → HTTP/2 framing

Back-End → Transfer-Encoding
```

The critical header is:

```http
Transfer-Encoding: chunked
```

---

# 16. Chunked Encoding and HTTP/2

Chunked transfer encoding is incompatible with HTTP/2.

Therefore, an HTTP/2:

```http
Transfer-Encoding: chunked
```

header should be:

```text
stripped
```

or the request should be:

```text
blocked
```

If the front end fails to do this, the header may survive HTTP/1 downgrading.

---

# 17. H2.TE Example

HTTP/2 front-end representation:

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

After downgrading:

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

Back end:

```text
Transfer-Encoding: chunked
        ↓
0
        ↓
end of body
        ↓
GET /admin...
        ↓
next request
```

---

# 18. H2.CL vs H2.TE

| Variant | Front-End | Back-End |
|---|---|---|
| `H2.CL` | HTTP/2 framing | Content-Length |
| `H2.TE` | HTTP/2 framing | Transfer-Encoding |

Memory:

```text
H2.CL
      ↓
HTTP/2 vs CL
```

```text
H2.TE
      ↓
HTTP/2 vs TE
```

---

# 19. Hidden HTTP/2 Support

Normally browsers and Burp use HTTP/2 when the server advertises support through:

```text
ALPN
```

during the TLS handshake.

But a server may:

```text
support HTTP/2
```

while failing to advertise it correctly.

Clients then fall back to:

```text
HTTP/1.1
```

This can hide HTTP/2-specific attack surface.

---

# 20. Force HTTP/2 in Burp

The source gives these steps:

```text
Burp Settings
     ↓
Tools
     ↓
Repeater
     ↓
Connections
     ↓
Enable:
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
Protocol
   ↓
HTTP/2
```

Now Burp can attempt HTTP/2 even if the server did not advertise it.

---

# 21. HTTP/2 CRLF Injection

HTTP/2's binary format creates another attack surface:

```text
CRLF INJECTION
```

In HTTP/1:

```text
\r\n
```

has structural meaning.

It separates:

```text
headers
```

and:

```text
\r\n\r\n
```

marks the end of the header section.

HTTP/2 does not use CRLF delimiters to determine individual header boundaries.

---

# 22. Why CRLF Injection Works

Consider an HTTP/2 header value:

```text
foo    bar\r\nTransfer-Encoding: chunked
```

The HTTP/2 front end can treat this as:

```text
ONE HEADER VALUE
```

But after downgrading:

```http
Foo: bar
Transfer-Encoding: chunked
```

The HTTP/1 back end sees:

```text
TWO HEADERS
```

So:

```text
HTTP/2 interpretation
        ≠
HTTP/1 interpretation
```

---

# 23. CRLF Injection Mental Model

```text
HTTP/2

foo = "bar\r\nTransfer-Encoding: chunked"

            ↓

Front-End:
ONE HEADER

            ↓
      DOWNGRADE

            ↓

HTTP/1

Foo: bar
Transfer-Encoding: chunked

            ↓

Back-End:
TWO HEADERS
```

---

# 24. Why This Can Bypass H2.TE Defenses

Suppose the front end blocks a normal:

```http
Transfer-Encoding: chunked
```

HTTP/2 header.

Instead, the attacker may place the string inside another header value:

```text
foo:
bar\r\nTransfer-Encoding: chunked
```

The front end may not identify a separate TE header.

After downgrading:

```text
HTTP/1 Back-End
```

does.

This can recreate an:

```text
H2.TE-style discrepancy
```

even when direct TE injection is filtered.

---

# 25. HTTP/2 Request Splitting

CRLF injection can also be used to insert:

```text
\r\n\r\n
```

This marks the end of an HTTP/1 header section.

Then attacker-controlled bytes can begin:

```text
ANOTHER REQUEST
```

Conceptually:

```text
ONE HTTP/2 REQUEST
        ↓
HTTP/1 DOWNGRADE
        ↓
TWO HTTP/1 REQUESTS
```

This is:

```text
HTTP/2 REQUEST SPLITTING
```

---

# 26. Request Splitting Example

Conceptual HTTP/2 request:

```text
:method     GET
:path       /
:authority  vulnerable-website.com
foo         bar\r\n
            \r\n
            GET /admin HTTP/1.1\r\n
            Host: vulnerable-website.com
```

After HTTP/1 rewriting, the back end may receive:

```http
GET / HTTP/1.1
...

GET /admin HTTP/1.1
Host: vulnerable-website.com
```

The attacker has transformed:

```text
1 HTTP/2 request
```

into:

```text
2 HTTP/1 requests
```

---

# 27. Advantage of Header-Based Splitting

The source notes that this is more versatile than body-based splitting.

You are not dependent on request methods that normally contain a body.

For example:

```http
GET
```

can potentially be used.

This can also help where:

```text
Content-Length is validated
```

or:

```text
Back-End does not support chunked encoding
```

---

# 28. Accounting for Front-End Rewriting

When HTTP/2 is downgraded, pseudo-headers must be converted.

For example:

```text
:authority
```

normally becomes:

```http
Host:
```

The location where the front end inserts this generated header matters.

If your request is split before the generated `Host` header:

```text
Request 1 → no Host

Request 2 → duplicate Host
```

Both can cause problems.

---

# 29. Host Header Positioning

The source demonstrates positioning an injected Host before the split.

Conceptually:

```text
:method     GET
:path       /
:authority  vulnerable-website.com
foo         bar\r\n
            Host: vulnerable-website.com\r\n
            \r\n
            GET /admin HTTP/1.1
```

The goal is for both resulting HTTP/1 requests to remain syntactically valid after the front end performs its rewriting.

The same principle applies to other internal headers inserted during downgrading.

---

# 30. Burp CRLF Input

For the HTTP/2 request-splitting lab, the source notes that newlines can be inserted into an HTTP/2 header through the Inspector.

Use:

```text
Inspector
   ↓
Header value
   ↓
Shift + Return
```

The source notes that this feature is not available when simply double-clicking the header.

---

# 31. Response Queue Poisoning

HTTP/2 request smuggling can also lead to:

```text
RESPONSE QUEUE POISONING
```

The key difference from ordinary prefix smuggling is:

```text
Smuggle a COMPLETE request
```

The front end believes:

```text
1 request
```

was sent.

The back end sees:

```text
2 requests
```

and generates:

```text
2 responses
```

---

# 32. Queue Desynchronization

```text
FRONT-END

Request A
    ↓
expects one response
```

Back end:

```text
Request A → Response A
Request B → Response B
```

Front end:

```text
Response A → Request A
```

But:

```text
Response B
```

has no matching request.

It stays queued.

---

# 33. Next Request Receives Wrong Response

When:

```text
Request C
```

arrives:

```text
Request C
    ↓
Front-End
    ↓
Back-End
```

the first response waiting is:

```text
Response B
```

So:

```text
Request C → Response B
```

while:

```text
Response C
```

becomes the next leftover response.

---

# 34. H2.TE Queue Poisoning Probe

The source uses:

```http
POST / HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked

0

SMUGGLED
```

A pattern where every second request returns:

```text
404
```

confirms that the subsequent request is being appended to the smuggled prefix.

---

# 35. Smuggling a Complete Request

The source then uses:

```http
POST /x HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked

0

GET /x HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net

```

Important:

```text
Terminate the smuggled request with:

\r\n\r\n
```

Using a nonexistent:

```text
/x
```

provides a predictable:

```text
404
```

response.

This makes unexpected responses easier to recognize.

---

# 36. Request Splitting Can Also Poison the Queue

CRLF request splitting can directly create:

```text
2 complete HTTP/1 requests
```

from:

```text
1 HTTP/2 request
```

Therefore:

```text
HTTP/2 Request
       ↓
CRLF Injection
       ↓
HTTP/1 Request Splitting
       ↓
2 Back-End Requests
       ↓
2 Responses
       ↓
Front-End expected 1
       ↓
RESPONSE QUEUE POISONING
```

---

# 37. HTTP Request Tunnelling

Traditional request smuggling often depends on reuse of:

```text
Front-End ↔ Back-End
```

connections.

But some targets:

```text
do not reuse the connection
```

This prevents many classic cross-request attacks.

However, the source shows that:

```text
HTTP REQUEST TUNNELLING
```

can still provide an attack path.

---

# 38. Tunnelling Concept

The goal is:

```text
ONE front-end request
        ↓
TWO back-end requests
```

and potentially:

```text
TWO back-end responses
```

all within one front-end request/response exchange.

Conceptually:

```text
HTTP/2 Client
      |
      | Request A
      v
Front-End
      |
      | rewritten HTTP/1
      v
Back-End
      |
      +---- Request A
      |       ↓
      |    Response A
      |
      +---- Request B
              ↓
           Response B
```

This does not require poisoning a connection for a later user request.

---

# 39. HTTP/2 Makes Tunnelling Easier to Observe

With HTTP/2:

```text
one stream
```

should correspond to:

```text
one request
+
one response
```

If the body unexpectedly contains another complete:

```http
HTTP/1.1 200 OK
```

response, this provides evidence that another back-end request was processed.

Conceptually:

```text
HTTP/2 Response
       |
       +-- Response A
       |
       +-- HTTP/1.1 Response B
```

---

# 40. Tunnelling via :path

The source's tunnelling material demonstrates that HTTP/2-specific inputs such as:

```text
:path
```

can be useful during downgrade attacks.

A conceptual injected value looks like:

```text
:path

/?cachebuster=1 HTTP/1.1\r\n
Foo: bar
```

The goal is to manipulate the HTTP/1 request line and headers generated during downgrading.

---

# 41. HEAD and Tunnelling

The source's tunnelling lab uses:

```http
HEAD
```

for the outer request while injecting another request through `:path`.

Conceptually:

```text
HEAD /outer HTTP/1.1
...

GET /inner HTTP/1.1
...
```

The nested response can then become observable within the response returned for the outer request.

---

# 42. Tunnelling + Web Cache Poisoning

The source also combines:

```text
HTTP Request Tunnelling
        +
Web Cache Poisoning
```

This is especially significant because the relevant lab explicitly states:

```text
Front-End does NOT reuse
the Back-End connection
```

Therefore:

```text
Classic connection poisoning
       X
```

but:

```text
Request Tunnelling
       ✓
```

is still possible.

---

# 43. High-Level Cache Attack Flow

```text
HTTP/2 Request
      ↓
Manipulate downgrade
      ↓
Tunnel second request
      ↓
Nested response returned
      ↓
Front-End associates it
with outer request
      ↓
Cache stores wrong response
```

This demonstrates why:

```text
"No connection reuse"
```

does not automatically eliminate all request-smuggling impact.

---

# 44. HTTP/2 Attack Map

```text
                    HTTP/2
                       |
                       v
                 DOWNGRADING
                       |
          +------------+------------+
          |                         |
          v                         v
        H2.CL                     H2.TE
          |                         |
          |                         |
          +-----------+-------------+
                      |
                      v
                REQUEST SMUGGLING
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
 CRLF Injection   Queue Poisoning  Tunnelling
        |
        v
 Request Splitting
        |
        v
Two HTTP/1 Requests
```

---

# 45. Burp HTTP/2 Workflow

Before testing:

```text
[ ] Send request to Repeater

[ ] Open Inspector

[ ] Expand Request attributes

[ ] Verify Protocol = HTTP/2

[ ] If HTTP/2 appears hidden:
    enable HTTP/2 ALPN override

[ ] Inspect pseudo-headers

[ ] Check :method

[ ] Check :path

[ ] Check :authority

[ ] Test H2.CL where appropriate

[ ] Test H2.TE where appropriate

[ ] Consider HTTP/2 header-value injection

[ ] Account for front-end rewriting
```

---

# 46. HTTP/1 vs HTTP/2 Quick Comparison

| Feature | HTTP/1 | HTTP/2 |
|---|---|---|
| Message representation | Text-oriented | Binary frames |
| Length mechanism | CL / TE | Frame lengths |
| Chunked encoding | Supported | Incompatible |
| Pseudo-headers | No | Yes |
| `:method` | No | Yes |
| `:path` | No | Yes |
| `:authority` | No | Yes |
| Downgrading risk | N/A | Yes |
| H2.CL | No | Yes |
| H2.TE | No | Yes |
| CRLF downgrade attacks | Different context | Important advanced vector |

---

# 47. Variant Memory Table

```text
CL.TE
Front = CL
Back  = TE
```

```text
TE.CL
Front = TE
Back  = CL
```

```text
H2.CL
Front = HTTP/2 framing
Back  = CL
```

```text
H2.TE
Front = HTTP/2 framing
Back  = TE
```

The easy memory rule:

```text
LEFT  = FRONT-END
RIGHT = BACK-END
```

So:

```text
H2.CL
│   │
│   └── Back-End uses CL
│
└────── Front-End uses HTTP/2
```

---

# 48. Prevention

The source's main recommendation is:

```text
USE HTTP/2 END-TO-END
```

where possible.

Architecture:

```text
Client
  |
 HTTP/2
  |
  v
Front-End
  |
 HTTP/2
  |
  v
Back-End
```

This avoids the risky:

```text
HTTP/2 → HTTP/1
```

conversion.

---

# 49. If Downgrading Cannot Be Avoided

The source recommends validating rewritten requests against HTTP/1.1 requirements.

Examples include rejecting requests containing problematic constructs such as:

```text
Newlines in headers
Colons in header names
Spaces in request methods
```

The front end should normalize ambiguous requests, and the back end should reject requests that remain ambiguous.

---

# 50. Final Mental Model

Do not think:

```text
HTTP/2 = request smuggling impossible
```

Instead think:

```text
HTTP/2 END-TO-END
        ↓
robust request-length framing
```

but:

```text
HTTP/2
   ↓
FRONT-END
   ↓
DOWNGRADE
   ↓
HTTP/1
   ↓
BACK-END
```

creates a translation boundary.

At that boundary ask:

```text
Does the HTTP/2 front end
and HTTP/1 back end
interpret the rewritten request
the same way?
```

If:

```text
NO
```

then investigate:

```text
H2.CL
H2.TE
CRLF Injection
Request Splitting
Response Queue Poisoning
Request Tunnelling
```

---

# 51. One-Minute Revision

```text
HTTP/2 LENGTH
= sum of frame lengths
```

```text
DOWNGRADING
HTTP/2 → HTTP/1
```

```text
H2.CL
H2 framing vs Content-Length
```

```text
H2.TE
H2 framing vs Transfer-Encoding
```

```text
CRLF INJECTION
one H2 header
→ multiple H1 headers
```

```text
REQUEST SPLITTING
one H2 request
→ two H1 requests
```

```text
QUEUE POISONING
one expected response
→ two actual responses
```

```text
TUNNELLING
useful even without
front-end/back-end connection reuse
```

---

## Related Labs

```text
Lab-13-H2-CL-Request-Smuggling.md

Lab-14-Response-Queue-Poisoning.md

Lab-15-H2-CRLF-Injection.md

Lab-16-H2-Request-Splitting.md

Lab-17-H2-Request-Tunnelling.md

Lab-18-H2-Tunnelling-Web-Cache-Poisoning.md
```

---

## Notes Section Complete

```text
Notes/
├── Advanced-Request-Smuggling.md
├── Detection-Techniques.md
├── Exploitation-Techniques.md
├── HTTP-Request-Smuggling-Notes.md
└── HTTP2-Request-Smuggling.md
```

## Next Section

Continue with:

```text
Payloads/
```

Start with:

```text
Payloads/CL-TE-Payloads.md
```