# 0.CL and CL.0 Request Smuggling

## Overview

Not all request smuggling vulnerabilities depend on the classic:

```text
CL.TE
TE.CL
TE.TE
```

patterns.

Another class of desynchronization occurs when the front-end and back-end disagree about **whether a request has a body at all**.

Two important variants are:

```text
0.CL
CL.0
```

The basic idea remains the same:

```text
Front-End interpretation
          ≠
Back-End interpretation
          ↓
DESYNCHRONIZATION
```

---

# 1. Understanding the Names

As with the classic request-smuggling notation:

```text
LEFT  = Front-End
RIGHT = Back-End
```

Therefore:

```text
0.CL
```

means:

```text
Front-End → assumes body length is 0
Back-End  → uses Content-Length
```

While:

```text
CL.0
```

means:

```text
Front-End → uses Content-Length
Back-End  → assumes body length is 0
```

---

# 2. 0.CL Desynchronization

## Meaning

```text
0.CL

Front-End = 0
Back-End  = Content-Length
```

The front-end effectively treats the request as having:

```text
NO BODY
```

while the back-end expects a body based on:

```http
Content-Length
```

---

# 3. 0.CL Mental Model

Imagine:

```text
             REQUEST
                |
                v
       +----------------+
       |   FRONT-END    |
       | Body length: 0 |
       +----------------+
                |
                v
       +----------------+
       |    BACK-END    |
       | Content-Length |
       +----------------+
                |
                v
       Back-end expects
         more bytes
```

The front-end believes the first request is complete.

The back-end does not.

This means data from a subsequent request may be consumed as part of the body of the previous request.

---

# 4. 0.CL Visualization

Conceptually:

```text
Front-End sees:

[ REQUEST 1 ][ REQUEST 2 ]
      ↑            ↑
   complete      separate
```

But the back-end may see:

```text
[ REQUEST 1 + part of REQUEST 2 ]
```

because it is still waiting for the body length indicated by:

```http
Content-Length
```

This difference causes:

```text
DESYNC
```

---

# 5. Why 0.CL Can Be Tricky

With classic CL.TE or TE.CL attacks, the ambiguity is usually visible inside a single specially crafted request.

0.CL can involve the interaction between:

```text
Request 1
+
Request 2
```

on a reused connection.

The front-end thinks:

```text
Request 1 finished.
Send Request 2.
```

while the back-end thinks:

```text
I'm still reading Request 1.
```

Therefore, bytes from Request 2 may be interpreted as belonging to Request 1.

---

# 6. 0.CL Connection State

Think of the connection like this:

```text
FRONT-END

Request 1
─────────────── END

Request 2
─────────────── END
```

But:

```text
BACK-END

Request 1
──────────────────────────────
             ↑
       still waiting
       for body bytes
```

When Request 2 arrives:

```text
Request 2 bytes
      ↓
may satisfy the body
expected for Request 1
```

This puts the two servers out of sync.

---

# 7. CL.0 Desynchronization

Now reverse the situation.

```text
CL.0
```

means:

```text
Front-End = Content-Length
Back-End  = 0
```

The front-end believes the request contains a body.

The back-end effectively treats the request as having:

```text
NO BODY
```

---

# 8. CL.0 Mental Model

```text
             REQUEST
                |
                v
       +----------------+
       |   FRONT-END    |
       | Content-Length |
       +----------------+
                |
                v
       +----------------+
       |    BACK-END    |
       | Body length: 0 |
       +----------------+
                |
                v
         BODY BYTES
         LEFT OVER
```

The front-end forwards the request including the body.

But if the back-end ignores the body:

```text
Body bytes
    ↓
remain on the connection
    ↓
may be interpreted as
another HTTP request
```

---

# 9. CL.0 Visualization

Front-end interpretation:

```text
[ HEADERS + BODY ]
```

Back-end interpretation:

```text
[ HEADERS ][ BODY ]
     ↑         ↑
 Request 1   leftover
```

If the body contains something that resembles another HTTP request:

```http
GET /something HTTP/1.1
Host: example
```

the back-end may interpret those bytes separately.

---

# 10. Why Would a Back-End Ignore the Body?

Your notes describe CL.0 behavior in situations where certain back-end endpoints simply do not expect or process request bodies.

Potential candidates include requests for:

```text
Static resources
Server-level redirects
Certain special endpoints
```

The key question is:

> Does the back-end ignore the body even though the front-end forwards it according to Content-Length?

If yes, the body may remain on the connection.

---

# 11. CL.0 Example Structure

Conceptually:

```http
POST /some-endpoint HTTP/1.1
Host: vulnerable-website.com
Content-Length: [BODY-LENGTH]

GET /hopefully404 HTTP/1.1
Foo: x
```

Front-end:

```text
Content-Length says:

GET /hopefully404...
is the BODY
```

So the front-end sees:

```text
ONE REQUEST
```

But if the back-end ignores that body:

```text
POST /some-endpoint
        ↓
Back-end considers
request complete
        ↓
GET /hopefully404...
        ↓
remains in connection
        ↓
interpreted separately
```

This creates:

```text
CL.0
```

---

# 12. Detecting CL.0 Behavior

The general strategy in your notes is to identify endpoints where the back-end may ignore the request body.

A useful conceptual test is:

```text
1. Find a candidate endpoint.

2. Send a request with a Content-Length body.

3. Put a recognizable request-like prefix in the body.

4. Send another request over the same connection.

5. Observe whether the next request is affected.
```

A recognizable path such as:

```text
/hopefully404
```

can make unexpected back-end processing easier to notice.

---

# 13. Why Use a Nonexistent Path?

Suppose the smuggled prefix contains:

```http
GET /hopefully404 HTTP/1.1
```

If the back-end processes this separately, you may observe:

```text
404 Not Found
```

This gives you a recognizable signal that the body was interpreted as another request.

Conceptually:

```text
Normal second request
        ↓
Expected response: 200

But receive:
        ↓
404
        ↓
possible desynchronization
```

---

# 14. CL.0 and Connection Reuse

These attacks depend heavily on connection behavior.

Conceptually:

```text
Front-End
    |
    | persistent connection
    v
Back-End
```

If the connection is reused:

```text
Attack Request
      ↓
leftover bytes
      ↓
same connection
      ↓
Next Request
```

the leftover bytes can influence subsequent processing.

If every request used a completely new back-end connection, this kind of desynchronization would be much harder to exploit in the same way.

---

# 15. Compare 0.CL and CL.0

| Variant | Front-End | Back-End |
|---|---|---|
| `0.CL` | Assumes no body | Uses Content-Length |
| `CL.0` | Uses Content-Length | Assumes no body |

The easiest way to remember them:

```text
LEFT  = FRONT
RIGHT = BACK
```

So:

```text
0.CL

Front → 0
Back  → CL
```

and:

```text
CL.0

Front → CL
Back  → 0
```

---

# 16. Direction of the Problem

## 0.CL

Back-end expects **more data** than the front-end expects.

```text
Front-End:
Request ends EARLY

Back-End:
Request ends LATER
```

Conceptually:

```text
FRONT: [ REQUEST 1 ][ REQUEST 2 ]

BACK:  [ REQUEST 1 + ... ]
```

---

## CL.0

Back-end expects **less data** than the front-end expects.

```text
Front-End:
Request ends LATER

Back-End:
Request ends EARLY
```

Conceptually:

```text
FRONT: [ REQUEST 1 + BODY ]

BACK:  [ REQUEST 1 ][ BODY... ]
```

The body may therefore become the beginning of another request.

---

# 17. Compare With CL.TE

Do not confuse:

```text
CL.0
```

with:

```text
CL.TE
```

In CL.TE:

```text
Front-End → Content-Length
Back-End  → Transfer-Encoding
```

In CL.0:

```text
Front-End → Content-Length
Back-End  → ignores / expects no body
```

So:

```text
CL.TE

CL → TE
```

versus:

```text
CL.0

CL → NO BODY
```

---

# 18. Compare With H2.CL

Also do not confuse:

```text
0.CL
```

with:

```text
H2.CL
```

They mean different things.

### H2.CL

```text
Front-End → HTTP/2 framing
Back-End  → Content-Length
```

### 0.CL

```text
Front-End → assumes zero-length body
Back-End  → Content-Length
```

---

# 19. Full Variant Comparison

```text
CL.TE
Front = Content-Length
Back  = Transfer-Encoding

TE.CL
Front = Transfer-Encoding
Back  = Content-Length

TE.TE
One server ignores obfuscated TE

H2.CL
Front = HTTP/2 framing
Back  = Content-Length

H2.TE
Front = HTTP/2 framing
Back  = Transfer-Encoding

0.CL
Front = no body
Back  = Content-Length

CL.0
Front = Content-Length
Back  = no body
```

---

# 20. Visual Comparison

```text
                 REQUEST SMUGGLING
                        |
        +---------------+---------------+
        |                               |
        v                               v
Classic HTTP/1                    Other Desync
        |                               |
  +-----+-----+                  +------+------+
  |     |     |                  |             |
  v     v     v                  v             v
CL.TE TE.CL TE.TE              0.CL           CL.0
```

Alongside HTTP/2 downgrade attacks:

```text
HTTP/2 Downgrade
       |
   +---+---+
   |       |
   v       v
 H2.CL   H2.TE
```

---

# 21. Testing Mindset

When looking for request smuggling, don't only ask:

> Does this server support CL.TE or TE.CL?

Also think:

```text
Does the front-end think this request has a body?

Does the back-end think this request has a body?

Do both servers agree about its length?

Does the back-end ignore bodies on this endpoint?

Is the back-end connection reused?

Can leftover bytes affect the next request?
```

The core question always remains:

```text
Do both servers agree
where the request ends?
```

---

# 22. Quick Revision

## 0.CL

```text
FRONT = 0
BACK  = CL

Front-end thinks:
"No body."

Back-end thinks:
"I need Content-Length bytes."
```

Result:

```text
Back-end may consume bytes
from the next request.
```

---

## CL.0

```text
FRONT = CL
BACK  = 0

Front-end thinks:
"This request has a body."

Back-end thinks:
"No body."
```

Result:

```text
Body bytes may remain
and become another request.
```

---

# 23. Memory Trick

Always read the notation:

```text
FRONT . BACK
```

Therefore:

```text
0.CL
0   → Front
CL  → Back
```

and:

```text
CL.0
CL  → Front
0   → Back
```

---

# Final Mental Model

```text
                    FRONT-END
                        |
              "Where does this
               request end?"
                        |
                        v
                    BACK-END
                        |
              "Where do I think
               it ends?"
                        |
                        v

               SAME ANSWER?
                /       \
              YES        NO
               |          |
               v          v
             NORMAL     DESYNC
                           |
                           v
                 REQUEST SMUGGLING
```

The mechanism changes:

```text
CL vs TE
H2 vs CL
H2 vs TE
0 vs CL
CL vs 0
```

but the underlying issue remains:

> **The front-end and back-end disagree about the request boundary.**

---

## Next

Continue to:

`06-Client-and-Server-Side-Desync.md`