# HTTP Request Smuggling — Master Notes

## 1. What Is HTTP Request Smuggling?

HTTP Request Smuggling is a technique for interfering with how a website processes a sequence of HTTP requests.

The central problem is:

```text
Front-End interpretation
          ≠
Back-End interpretation
```

If the two servers disagree about where one request ends and the next begins, part of one request can be interpreted by the back-end as the beginning of another request.

---

# 2. Typical Architecture

Modern applications often use:

```text
Client
  |
  v
+----------------+
|   Front-End    |
| Reverse Proxy  |
| Load Balancer  |
+----------------+
        |
        | reused connection
        v
+----------------+
|    Back-End    |
| Application    |
+----------------+
```

Multiple requests may travel over the same front-end/back-end connection.

Therefore, both servers must agree on:

```text
REQUEST 1 | REQUEST 2 | REQUEST 3
          ^
      exact boundary
```

If they disagree:

```text
DESYNCHRONIZATION
        ↓
REQUEST SMUGGLING
```

---

# 3. Why HTTP/1 Is Vulnerable

HTTP/1 provides two mechanisms that can determine request-body length:

```http
Content-Length
```

and:

```http
Transfer-Encoding: chunked
```

### Content-Length

```http
Content-Length: 11

q=smuggling
```

means:

```text
Read 11 bytes.
```

### Transfer-Encoding

```http
Transfer-Encoding: chunked

b
q=smuggling
0
```

Chunk sizes are expressed in:

```text
HEXADECIMAL
```

and:

```text
0
```

terminates the chunked body.

The problem appears when different servers process these mechanisms differently.

---

# 4. Classic HTTP/1 Variants

Remember:

```text
LEFT  = FRONT-END
RIGHT = BACK-END
```

## CL.TE

```text
Front-End → Content-Length
Back-End  → Transfer-Encoding
```

Example structure:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

Front-end:

```text
Content-Length
      ↓
includes SMUGGLED
```

Back-end:

```text
Transfer-Encoding
      ↓
0 = end of body
      ↓
SMUGGLED remains
```

Result:

```text
SMUGGLED
```

may become the beginning of the next request.

---

## TE.CL

```text
Front-End → Transfer-Encoding
Back-End  → Content-Length
```

This is the reverse of CL.TE.

Memory:

```text
CL.TE → Front CL / Back TE
TE.CL → Front TE / Back CL
```

---

## TE.TE

Both servers support:

```http
Transfer-Encoding
```

but one can be induced not to process it through header obfuscation.

Examples from the source include:

```http
Transfer-Encoding: xchunked
```

```http
Transfer-Encoding : chunked
```

and duplicate variants such as:

```http
Transfer-Encoding: chunked
Transfer-Encoding: x
```

If only one server recognizes the header:

```text
Different parsing
      ↓
DESYNC
```

---

# 5. Important Burp Settings

Classic:

```text
CL.TE
TE.CL
TE.TE
```

techniques use:

```text
HTTP/1
```

When the target supports HTTP/2, check:

```text
Repeater
   ↓
Inspector
   ↓
Request attributes
   ↓
Protocol
```

and switch to HTTP/1 when required.

For requests where you deliberately manipulate `Content-Length`, also pay attention to:

```text
Update Content-Length
```

because automatic recalculation may alter your intended request.

---

# 6. Detecting Request Smuggling

The source covers two major approaches:

```text
Timing techniques
       +
Differential responses
```

---

# 7. Timing Detection — CL.TE

A CL.TE probe from the source:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Transfer-Encoding: chunked
Content-Length: 4

1
A
X
```

Why can this delay?

```text
Front-End uses CL
       ↓
forwards part of request
       ↓
Back-End uses TE
       ↓
expects another chunk
       ↓
WAIT
       ↓
TIME DELAY
```

A noticeable delay can indicate potential:

```text
CL.TE
```

behavior.

---

# 8. Timing Detection — TE.CL

Example from the source:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Transfer-Encoding: chunked
Content-Length: 6

0

X
```

Conceptually:

```text
Front-End uses TE
       ↓
considers chunked body complete

Back-End uses CL
       ↓
expects additional bytes
       ↓
WAIT
       ↓
TIME DELAY
```

This can indicate:

```text
TE.CL
```

---

# 9. Important Testing Order

The source warns that a TE.CL timing probe may interfere with other users if the application is actually vulnerable to CL.TE.

Therefore, for lower disruption:

```text
Test CL.TE first
       ↓
If unsuccessful
       ↓
Test TE.CL
```

---

# 10. Differential Response Confirmation

Timing can suggest a vulnerability.

Next:

```text
Confirm it
```

by causing the smuggled prefix to alter the response to a subsequent request.

Conceptually:

```text
ATTACK REQUEST
      ↓
poisons connection
      ↓
NORMAL REQUEST
      ↓
unexpected response
```

Example idea:

```text
smuggled prefix
      ↓
GET /hopefully404
```

If a following normal request unexpectedly receives:

```text
404
```

that provides stronger evidence of desynchronization.

---

# 11. Important Confirmation Considerations

The source emphasizes several precautions.

### Different Connections

The:

```text
Attack request
```

and:

```text
Normal request
```

should use different network connections when confirming interference with another request.

---

### Similar URLs and Parameters

Keep the attack and normal requests as similar as possible:

```text
Same URL
Same parameter names
```

because applications may route requests to different back-end systems depending on URL or parameters.

---

### Race Conditions

Other traffic may reach the back-end between your requests.

Therefore:

```text
Attack request
      ↓
Normal request IMMEDIATELY
```

may need to be repeated.

---

### Load Balancing

A front-end may distribute requests across different back-end servers.

```text
Attack → Back-End A

Normal → Back-End B
```

means the interference may not occur.

Multiple attempts may therefore be necessary.

---

### Avoid Affecting Other Users

If your test interferes with another user's request instead of your controlled follow-up request, continuing the test may disrupt real users.

Use caution during authorized testing.

---

# 12. Exploitation Categories

Your source covers several ways request smuggling can be exploited:

```text
Bypass front-end security controls

Reveal front-end request rewriting

Capture other users' requests

Deliver reflected XSS

Web cache poisoning

Web cache deception

Response queue poisoning

HTTP request tunnelling
```

---

# 13. Bypassing Front-End Security Controls

Some applications enforce security at the front end.

Example:

```text
User
  |
  | GET /admin
  v
Front-End
  |
  X BLOCKED
```

The back-end may assume:

> Any request reaching me has already passed the front-end security checks.

Request smuggling may bypass that assumption.

Conceptually:

```text
Front-End sees:

GET /allowed
```

while the back-end eventually processes:

```text
GET /admin
```

If the back-end performs no additional authorization check, the restricted endpoint may become reachable.

---

# 14. Revealing Front-End Request Rewriting

Front-end systems may modify requests before forwarding them.

For example, they may add headers containing information about:

```text
Client IP
TLS details
Internal routing
Other request metadata
```

Request smuggling can sometimes help reveal what the rewritten back-end request looks like.

This is useful because a smuggled request may need to reproduce headers automatically added by the front end.

---

# 15. Capturing Other Users' Requests

A smuggled request can sometimes cause another user's request to be incorporated into attacker-controlled data.

Conceptually:

```text
Smuggled request
      +
Victim request
      ↓
Stored / reflected somewhere
      ↓
Attacker retrieves it
```

Depending on the application, captured data may contain sensitive request information.

---

# 16. Delivering Reflected XSS

Request smuggling can also be combined with another vulnerability.

Suppose an application contains:

```text
Reflected XSS
```

but exploitation normally requires the attacker to control a request sent by the victim.

Request smuggling can potentially cause the victim's request to be prefixed with attacker-controlled data.

Conceptually:

```text
Request Smuggling
       +
Reflected XSS
       ↓
Attack delivered to
another user's request
```

---

# 17. Web Cache Poisoning

Request smuggling can potentially interfere with the request that a caching system believes produced a particular response.

Conceptually:

```text
Smuggled request
       ↓
Back-End generates response
       ↓
Front-End/cache associates response
with wrong request
       ↓
Malicious response cached
```

Subsequent users may then receive the poisoned cached response.

---

# 18. Web Cache Deception

The source also covers using request smuggling in connection with:

```text
Web Cache Deception
```

The objective is different from cache poisoning.

Conceptually:

```text
Sensitive response
       ↓
incorrectly cached
       ↓
attacker requests cached resource
       ↓
sensitive information exposed
```

---

# 19. HTTP/2 Request Smuggling

HTTP/2 uses explicit frame lengths.

Conceptually:

```text
HTTP/2 Request
     |
     ├── Frame → length
     ├── Frame → length
     └── Frame → length
```

When HTTP/2 is used end-to-end, the classic HTTP/1 CL/TE ambiguity does not arise in the same way.

The problem reappears when:

```text
HTTP/2
   ↓
Front-End
   ↓
DOWNGRADE
   ↓
HTTP/1
   ↓
Back-End
```

---

# 20. H2.CL

```text
H2.CL

Front-End → HTTP/2 length
Back-End  → Content-Length
```

A misleading HTTP/2:

```http
content-length
```

may be copied into the downgraded HTTP/1 request.

If it does not match the HTTP/2 framing:

```text
Front-End boundary
       ≠
Back-End boundary
```

resulting in a desync.

---

# 21. H2.TE

```text
H2.TE

Front-End → HTTP/2
Back-End  → Transfer-Encoding
```

Chunked transfer encoding is incompatible with HTTP/2.

A front end should strip or reject:

```http
Transfer-Encoding: chunked
```

If it fails to do this and forwards the header during HTTP/1 downgrading:

```text
HTTP/1 Back-End
       ↓
interprets chunked encoding
       ↓
possible desync
```

---

# 22. Response Queue Poisoning

Response queue poisoning occurs when a smuggled **complete request** causes the back-end to generate more responses than the front-end expects.

Conceptually:

```text
Front-End expects:

1 request
↓
1 response
```

but the back-end sees:

```text
Request 1
Request 2
    ↓
Response 1
Response 2
```

The front-end only expected one response.

Therefore:

```text
Response 2
```

remains queued.

---

# 23. Poisoned Response Queue

Now another request arrives:

```text
User Request
     ↓
Front-End
     ↓
Back-End
```

but the front-end already has:

```text
LEFTOVER RESPONSE
```

waiting in the queue.

So the wrong response may be assigned to the new request.

Conceptually:

```text
Request A → Response A
Request B → Response B
Request C → Response C
```

becomes misaligned:

```text
Request B → Response A
Request C → Response B
...
```

This may expose responses intended for other users.

---

# 24. HTTP/2 CRLF Injection

HTTP/2 is binary, so header boundaries are not determined using the same text delimiters as HTTP/1.

This can create unusual behavior during HTTP/2 → HTTP/1 downgrading.

Conceptually, a value containing:

```text
\r\n
```

may exist inside an HTTP/2 header value.

After downgrading to HTTP/1:

```text
\r\n
```

regains its meaning as a header delimiter.

Therefore something conceptually like:

```text
foo: bar\r\nTransfer-Encoding: chunked
```

may become:

```http
Foo: bar
Transfer-Encoding: chunked
```

for the HTTP/1 back-end.

This can introduce a header that the front end did not interpret as a separate header.

---

# 25. HTTP Request Tunnelling

Many traditional request-smuggling attacks rely on:

```text
Front-End ↔ Back-End
connection reuse
```

But the source introduces:

```text
HTTP REQUEST TUNNELLING
```

for cases where connection reuse may not be available.

The idea is to craft a single front-end request that causes the back-end to process additional hidden request data and potentially produce multiple responses.

---

# 26. Why HTTP/2 Helps Identify Tunnelling

In HTTP/1, multiple responses on a persistent connection can be difficult to interpret conclusively.

HTTP/2 is different because each:

```text
stream
```

should correspond to a single request and response.

Therefore, if an HTTP/2 response unexpectedly contains what appears to be an additional:

```text
HTTP/1 response
```

inside its body, this can provide strong evidence that another request was tunneled to the back-end.

---

# 27. CL.0

```text
CL.0

Front-End → Content-Length
Back-End  → ignores body / treats length as 0
```

Conceptually:

```text
Front-End:

[ HEADERS + BODY ]
```

Back-End:

```text
[ HEADERS ][ BODY LEFTOVER ]
```

The leftover body can potentially become another request.

---

# 28. Client-Side Desync

Traditional:

```text
Front-End ↔ Back-End
```

desynchronization is not the only possibility.

A Client-Side Desync poisons:

```text
Browser ↔ Server
```

A vulnerable server may:

```text
respond to POST
       ↓
without reading body
       ↓
keep connection open
       ↓
browser reuses connection
       ↓
leftover body + next request
       ↓
DESYNC
```

This can even affect single-server websites.

---

# 29. Pause-Based Desync

Some vulnerabilities only become visible if the request is paused.

Conceptually:

```text
Send Headers
     ↓
PAUSE
     ↓
Back-End read timeout
     ↓
Back-End responds
     ↓
Connection remains open
     ↓
Send Body
     ↓
Back-End interprets body
as another request
```

This can produce:

```text
CL.0-like behavior
```

---

# 30. Master Variant Table

| Variant | Front-End Interpretation | Back-End Interpretation |
|---|---|---|
| `CL.TE` | Content-Length | Transfer-Encoding |
| `TE.CL` | Transfer-Encoding | Content-Length |
| `TE.TE` | TE parsing differs | TE parsing differs |
| `H2.CL` | HTTP/2 framing | Content-Length |
| `H2.TE` | HTTP/2 framing | Transfer-Encoding |
| `0.CL` | No body | Content-Length |
| `CL.0` | Content-Length | No body |

---

# 31. Master Testing Flow

```text
START
  |
  v
Understand architecture
  |
  v
Determine protocol
  |
  +---------------------+
  |                     |
 HTTP/1                HTTP/2
  |                     |
  v                     v
CL.TE / TE.CL      Check downgrading
TE.TE                   |
  |                 +---+---+
  v                 |       |
Timing tests       H2.CL   H2.TE
  |
  v
Differential confirmation
  |
  v
Identify exact desync
  |
  v
Look for exploitation primitive
```

Also consider:

```text
CL.0
Client-Side Desync
Pause-Based Desync
Request Tunnelling
```

where relevant.

---

# 32. Burp Checklist

Before sending a test:

```text
[ ] Confirm HTTP version
[ ] Check Request attributes
[ ] Check Update Content-Length
[ ] Verify Content-Length manually when required
[ ] Verify chunk sizes
[ ] Verify CRLF placement
[ ] Use correct zero chunk
[ ] Check whether connection reuse matters
[ ] Compare multiple responses
[ ] Repeat only when necessary
```

---

# 33. Fast Memory Sheet

```text
LEFT = FRONT
RIGHT = BACK
```

```text
CL.TE
Front CL
Back TE
```

```text
TE.CL
Front TE
Back CL
```

```text
TE.TE
Different TE parsing
```

```text
H2.CL
Front HTTP/2
Back CL
```

```text
H2.TE
Front HTTP/2
Back TE
```

```text
CL.0
Front CL
Back ignores body
```

```text
CSD
Browser ↔ Server desync
```

```text
Pause-Based
Timeout → response → connection reused
```

---

# 34. Core Principle

No matter how advanced the technique becomes, always return to one question:

> **Do both sides agree about where the request ends?**

If:

```text
YES
 ↓
Normal processing
```

If:

```text
NO
 ↓
DESYNCHRONIZATION
 ↓
Potential Request Smuggling
```

---

# 35. Labs in This Repository

```text
Labs/
├── Lab-01-Basic-CL-TE.md
├── Lab-02-Basic-TE-CL.md
├── Lab-03-TE-Header-Obfuscation.md
├── Lab-04-Confirming-CL-TE.md
├── Lab-05-Confirming-TE-CL.md
├── Lab-06-Bypass-Front-End-Security-CL-TE.md
├── Lab-07-Bypass-Front-End-Security-TE-CL.md
├── Lab-08-Reveal-Front-End-Request-Rewriting.md
├── Lab-09-Capture-Other-Users-Requests.md
├── Lab-10-Deliver-Reflected-XSS.md
├── Lab-11-Web-Cache-Poisoning.md
├── Lab-12-Web-Cache-Deception.md
├── Lab-13-H2-CL-Request-Smuggling.md
├── Lab-14-Response-Queue-Poisoning.md
├── Lab-15-H2-CRLF-Injection.md
├── Lab-16-H2-Request-Splitting.md
├── Lab-17-H2-Request-Tunnelling.md
├── Lab-18-H2-Tunnelling-Web-Cache-Poisoning.md
├── Lab-19-0-CL-Request-Smuggling.md
├── Lab-20-CL-0-Request-Smuggling.md
├── Lab-21-Client-Side-Desync.md
└── Lab-22-Pause-Based-Desync.md
```

---

## Next Note

Continue with:

```text
Notes/Detection-Techniques.md
```

This will contain the detailed workflow for:

```text
Timing detection
Differential response confirmation
CL.TE testing
TE.CL testing
TE obfuscation
HTTP/2 testing
CL.0 testing
CSD testing
Pause-based testing
False positives and confirmation
```