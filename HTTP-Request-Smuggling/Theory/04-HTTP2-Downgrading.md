# HTTP/2 Downgrading and Request Smuggling

## 1. Why HTTP/2 Changes Request Smuggling

Classic HTTP/1 request smuggling relies on disagreement about the length of a request.

For example:

```text
Content-Length
       vs
Transfer-Encoding
```

HTTP/2 handles message length differently.

HTTP/2 messages are transmitted as a series of:

```text
FRAMES
```

Each frame has an explicit length.

Conceptually:

```text
HTTP/2 Request
     |
     ├── Frame 1 → explicit length
     ├── Frame 2 → explicit length
     └── Frame 3 → explicit length
```

Therefore:

```text
Request Length
      =
Sum of Frame Lengths
```

This provides a much less ambiguous way of determining where a request ends.

---

# 2. HTTP/2 End-to-End

Consider:

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

Both sides communicate using HTTP/2.

There is no need to translate the request into HTTP/1.

Therefore, the classic HTTP/1:

```text
Content-Length
       vs
Transfer-Encoding
```

ambiguity does not apply in the same way.

---

# 3. The Real Problem — HTTP/2 Downgrading

Many applications do NOT use HTTP/2 end-to-end.

Instead:

```text
CLIENT
   |
   | HTTP/2
   v
+----------------+
|   FRONT-END    |
| HTTP/2 capable |
+----------------+
        |
        | HTTP/1
        v
+----------------+
|    BACK-END    |
|   HTTP/1 only  |
+----------------+
```

The front-end must convert the HTTP/2 request into an HTTP/1 request.

This process is called:

# HTTP/2 Downgrading

---

# 4. Definition

HTTP/2 downgrading is the process of:

```text
HTTP/2 Request
       ↓
Front-End Rewrites Request
       ↓
HTTP/1 Request
       ↓
Back-End
```

The front-end creates an HTTP/1 equivalent of the HTTP/2 request.

The back-end processes the resulting HTTP/1 message.

When the back-end responds, the front-end can convert the response back into the form expected by the HTTP/2 client.

---

# 5. Why Downgrading Exists

A site may want to support HTTP/2 for modern clients while still using older infrastructure internally.

For example:

```text
Browser
   |
   | HTTP/2
   v
CDN / Reverse Proxy
   |
   | HTTP/1
   v
Legacy Application Server
```

So the front-end effectively acts as a translator.

---

# 6. HTTP/2 vs HTTP/1 Representation

HTTP/2 is a binary protocol.

The human-readable representation shown in Burp is therefore not exactly what is transmitted over the network.

For learning purposes, an HTTP/2 request may appear similar to:

```text
:method    POST
:path      /example
:authority vulnerable-website.com
content-type application/x-www-form-urlencoded
```

HTTP/2 uses special:

```text
pseudo-headers
```

such as:

```text
:method
:path
:authority
```

The `:` helps distinguish pseudo-headers from normal headers.

---

# 7. Mapping HTTP/2 to HTTP/1

An HTTP/2 request such as:

```text
:method     POST
:path       /example
:authority  vulnerable-website.com
```

may be rewritten approximately as:

```http
POST /example HTTP/1.1
Host: vulnerable-website.com
```

Conceptually:

```text
HTTP/2                         HTTP/1

:method POST       ────────>   POST
:path /example     ────────>   /example
:authority site    ────────>   Host: site
```

The problem is not simply that translation occurs.

The security issue appears when the translated HTTP/1 request is interpreted differently by the back-end than the original HTTP/2 request was interpreted by the front-end.

---

# 8. Where the Desynchronization Appears

The front-end understands:

```text
HTTP/2 framing
```

while the back-end understands:

```text
HTTP/1 request syntax
```

Therefore:

```text
HTTP/2
interpretation
     |
     v
FRONT-END
     |
     | downgrade
     v
HTTP/1
     |
     v
BACK-END
     |
     v
HTTP/1 interpretation
```

If the generated HTTP/1 request has an ambiguous length:

```text
Front-End Boundary
        ≠
Back-End Boundary
```

then:

```text
DESYNCHRONIZATION
```

may occur.

---

# 9. Three Possible Length Mechanisms

Your notes highlight an important consequence of HTTP/2 downgrading.

HTTP/2 already has:

```text
built-in frame lengths
```

but the resulting HTTP/1 request may also involve:

```http
Content-Length
```

or:

```http
Transfer-Encoding
```

Conceptually:

```text
          REQUEST LENGTH

               |
     +---------+---------+
     |         |         |
     v         v         v

 HTTP/2     Content-   Transfer-
 Frames     Length     Encoding
```

A discrepancy during conversion can therefore introduce new request-smuggling opportunities.

---

# 10. H2.CL

One important HTTP/2 request-smuggling variant is:

```text
H2.CL
```

Meaning:

```text
Front-End → HTTP/2 built-in length
Back-End  → Content-Length
```

Memory trick:

```text
H2.CL
│   │
│   └── Back-End = Content-Length
│
└────── Front-End = HTTP/2
```

---

# 11. How H2.CL Happens

HTTP/2 requests do not need a `Content-Length` header to determine their actual length because the protocol already knows the size from its frames.

However, an HTTP/2 request can contain:

```http
content-length
```

During HTTP/2 → HTTP/1 downgrading, some front ends may reuse this supplied value in the resulting HTTP/1 request.

If the value does not match the actual HTTP/2 body length and the front end fails to validate this properly, a discrepancy can occur.

---

# 12. H2.CL Concept

Imagine the front-end receives an HTTP/2 request containing:

```text
content-length: 0
```

while the actual HTTP/2 body contains additional data.

The front-end knows the real request length from HTTP/2 framing.

So it receives:

```text
HTTP/2 Request
+-----------------------+
| Headers               |
| content-length: 0     |
|                       |
| Additional Body Data  |
+-----------------------+
```

The front-end may still know that the additional body belongs to this HTTP/2 request.

But after downgrading, the HTTP/1 back-end receives:

```http
Content-Length: 0
```

The back-end interprets:

```text
Body Length = 0
```

Therefore:

```text
Additional data
      ↓
not considered part
of the first body
      ↓
can become another request
```

---

# 13. H2.CL Example

Your notes illustrate the concept with an HTTP/2 request equivalent to:

```text
:method     POST
:path       /example
:authority  vulnerable-website.com
content-type application/x-www-form-urlencoded
content-length 0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Content-Length: 10

x=1
```

The downgraded HTTP/1 request can look conceptually like:

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

The important concept is:

```text
Front-End
uses HTTP/2 framing
       |
       v
sees one HTTP/2 request

BUT

Back-End
uses Content-Length: 0
       |
       v
first request has no body
       |
       v
remaining bytes may become
another HTTP/1 request
```

That is:

```text
H2.CL
```

---

# 14. H2.TE

Another downgrade-based variant is:

```text
H2.TE
```

Meaning conceptually:

```text
Front-End → HTTP/2
Back-End  → Transfer-Encoding
```

---

# 15. Why H2.TE Is Interesting

Chunked transfer encoding is incompatible with HTTP/2.

Therefore, an HTTP/2 request should not normally be able to pass:

```http
Transfer-Encoding: chunked
```

through the front-end in a way that becomes meaningful to an HTTP/1 back-end.

The front-end should strip or reject this kind of header.

But if it fails to do so and then downgrades the request:

```text
HTTP/2
  |
  | transfer-encoding: chunked
  v
Front-End
  |
  | fails to remove it
  v
HTTP/1 Back-End
```

the HTTP/1 back-end may interpret the body as chunked.

---

# 16. H2.TE Example

Conceptually, the HTTP/2 front-end receives:

```text
:method     POST
:path       /example
:authority  vulnerable-website.com
content-type application/x-www-form-urlencoded
transfer-encoding chunked

0

GET /admin HTTP/1.1
Host: vulnerable-website.com
Foo: bar
```

After downgrading, the HTTP/1 back-end may receive:

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

The back-end sees:

```text
0
```

and interprets it as:

```text
END OF CHUNKED BODY
```

The following:

```http
GET /admin HTTP/1.1
```

can then be interpreted as another request.

---

# 17. H2.CL vs H2.TE

| Variant | Front-End | Back-End |
|---|---|---|
| `H2.CL` | HTTP/2 framing | Content-Length |
| `H2.TE` | HTTP/2 framing | Transfer-Encoding |

Memory:

```text
LEFT = FRONT-END
RIGHT = BACK-END
```

Therefore:

```text
H2.CL
Front = HTTP/2
Back  = Content-Length
```

and:

```text
H2.TE
Front = HTTP/2
Back  = Transfer-Encoding
```

---

# 18. Compare With Classic Request Smuggling

Classic HTTP/1:

```text
CL.TE
TE.CL
TE.TE
```

HTTP/2 downgrade-based:

```text
H2.CL
H2.TE
```

Comparison:

```text
CL.TE
Front → CL
Back  → TE

TE.CL
Front → TE
Back  → CL

H2.CL
Front → HTTP/2
Back  → CL

H2.TE
Front → HTTP/2
Back  → TE
```

---

# 19. Hidden HTTP/2 Support

Your notes also describe an important testing issue:

A server may support HTTP/2 but fail to advertise that support correctly.

Normally clients negotiate HTTP/2 using:

```text
ALPN
```

during the TLS handshake.

Conceptually:

```text
Client
   |
   | "Do you support HTTP/2?"
   v
Server
```

If HTTP/2 is not advertised, clients may fall back to:

```text
HTTP/1.1
```

even though the server actually supports HTTP/2.

This can hide HTTP/2-specific attack surface during testing.

---

# 20. Testing Hidden HTTP/2 Support in Burp

Your notes give the following Burp workflow:

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

Then inside Repeater:

```text
Inspector
   ↓
Request attributes
   ↓
Protocol
   ↓
HTTP/2
```

This allows Repeater to attempt HTTP/2 even when the server does not advertise it normally.

---

# 21. Important Burp Reminder

For an HTTP/2 request-smuggling test, always verify the protocol in:

```text
Repeater
   ↓
Inspector
   ↓
Request attributes
```

For H2-based labs you generally want:

```text
Protocol = HTTP/2
```

This is the opposite of the earlier classic CL.TE / TE.CL labs where the intended technique required HTTP/1.

---

# 22. Don't Confuse the Two Situations

## Classic HTTP/1 Testing

```text
CL.TE
TE.CL
TE.TE

→ HTTP/1
```

## HTTP/2 Downgrade Testing

```text
H2.CL
H2.TE

→ HTTP/2 request to front-end
→ downgraded to HTTP/1 internally
```

---

# 23. Quick Attack-Surface Mental Model

```text
Does the application use HTTP/2?
             |
             v
            YES
             |
             v
Is HTTP/2 used end-to-end?
       /           \
     YES            NO
      |              |
      v              v
Classic CL/TE     HTTP/2 may be
ambiguity not     downgraded
introduced this       |
way                    v
                   HTTP/1 back-end
                        |
                        v
                 Check downgrade
                 discrepancies
                        |
                  +-----+-----+
                  |           |
                  v           v
                H2.CL       H2.TE
```

---

# 24. Key Revision Points

- HTTP/2 messages are transmitted using frames.
- Frames contain explicit lengths.
- The request length is derived from the HTTP/2 frame structure.
- HTTP/2 used end-to-end avoids the classic HTTP/1 CL/TE ambiguity.
- Many front ends accept HTTP/2 but communicate with HTTP/1 back ends.
- Converting HTTP/2 into HTTP/1 is called **HTTP/2 downgrading**.
- Downgrading can reintroduce request-boundary discrepancies.
- `H2.CL` means the front end uses HTTP/2 framing while the HTTP/1 back end relies on `Content-Length`.
- `H2.TE` means the front end uses HTTP/2 while the downgraded back-end request is interpreted using `Transfer-Encoding`.
- HTTP/2 `Transfer-Encoding: chunked` should normally be stripped or rejected.
- Hidden HTTP/2 support can exist when the server does not advertise HTTP/2 correctly through ALPN.
- Burp Repeater can be configured to test hidden HTTP/2 support.

---

# 25. One-Minute Revision

```text
HTTP/2 end-to-end
        ↓
Explicit frame lengths
        ↓
No classic CL/TE ambiguity
```

But:

```text
HTTP/2 Client
      ↓
HTTP/2 Front-End
      ↓
   DOWNGRADE
      ↓
HTTP/1 Back-End
      ↓
Possible parsing disagreement
```

Remember:

```text
H2.CL
Front = HTTP/2
Back  = Content-Length

H2.TE
Front = HTTP/2
Back  = Transfer-Encoding
```

---

# Final Mental Model

```text
             CLIENT
                |
             HTTP/2
                |
                v
        +---------------+
        |   FRONT-END   |
        | HTTP/2 parser |
        +---------------+
                |
                | DOWNGRADE
                v
        +---------------+
        |   HTTP/1      |
        |   REQUEST     |
        +---------------+
                |
                v
        +---------------+
        |   BACK-END    |
        | HTTP/1 parser |
        +---------------+
                |
                v

If front-end and back-end
interpret the request length
differently:

          DESYNC
             ↓
    REQUEST SMUGGLING
```

---

## Next

Continue to:

`05-0-CL-and-CL-0.md`