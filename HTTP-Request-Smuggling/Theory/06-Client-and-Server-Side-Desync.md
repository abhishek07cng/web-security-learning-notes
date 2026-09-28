# Client-Side and Server-Side Desync

## Overview

HTTP desynchronization is not limited to classic:

```text
CL.TE
TE.CL
TE.TE
```

attacks.

The advanced material introduces two important perspectives:

```text
Server-Side Desync
Client-Side Desync (CSD)
```

and also:

```text
Pause-Based Desync
```

The fundamental concept remains:

> Two parties disagree about where an HTTP request ends.

---

# 1. Server-Side Desync

Traditional HTTP request smuggling normally occurs between:

```text
Client
   |
   v
FRONT-END
   |
   | shared / reused connection
   v
BACK-END
```

The attacker causes the:

```text
Front-End
```

and:

```text
Back-End
```

to disagree about request boundaries.

Conceptually:

```text
Front-End sees:

[ REQUEST 1 ][ REQUEST 2 ]

Back-End sees:

[ REQUEST 1 + PREFIX ][ REQUEST 2 ... ]
```

This is a:

```text
SERVER-SIDE DESYNC
```

because the desynchronized connection is between server-side components.

---

# 2. Classic Server-Side Request Smuggling

Examples include:

```text
CL.TE
TE.CL
TE.TE
H2.CL
H2.TE
CL.0
```

Although their exact mechanisms differ, they can all result in:

```text
Front-End
    |
    | poisoned connection
    v
Back-End
```

The attacker attempts to leave bytes on the back-end connection that affect a subsequent request.

---

# 3. Basic Server-Side Mental Model

```text
ATTACKER
   |
   | malicious request
   v
+----------------+
|   FRONT-END    |
+----------------+
        |
        | interprets boundary A
        v
+----------------+
|    BACK-END    |
+----------------+
        |
        | interprets boundary B
        v

Boundary A ≠ Boundary B
        |
        v
      DESYNC
```

---

# 4. Client-Side Desync

A **Client-Side Desync (CSD)** is different.

Instead of poisoning:

```text
Front-End ↔ Back-End
```

the attack desynchronizes:

```text
Victim Browser ↔ Web Server
```

Your source defines CSD as an attack that causes the victim's browser to desynchronize its own connection to the vulnerable website.

---

# 5. Why Client-Side Desync Is Important

Classic request smuggling commonly relies on deliberately malformed requests.

Ordinary browsers normally will not send many of these malformed requests.

For example, an attacker using Burp can precisely manipulate:

```text
Content-Length
Transfer-Encoding
Raw HTTP formatting
```

A normal browser gives the attacker much less control.

However, CL.0-style behavior demonstrated that a desync may sometimes be triggered using a request that is compatible with normal browser behavior.

This enables:

```text
CLIENT-SIDE DESYNC
```

attacks.

---

# 6. Root Cause of CSD

Your source explains that some web servers can be encouraged to:

```text
Respond to a POST request
BEFORE
reading its entire body
```

Then the server may keep the connection open.

Consider:

```text
Browser sends:

POST /endpoint HTTP/1.1
Content-Length: 40

[40-byte body]
```

But the server effectively behaves like:

```text
POST /endpoint
      |
      v
Respond immediately
      |
      v
Do not consume body
```

The remaining body bytes stay on the connection.

If that connection is reused:

```text
LEFTOVER BODY
      +
NEXT BROWSER REQUEST
```

may be interpreted together.

---

# 7. CSD Attack Flow

Your notes describe the high-level process as:

```text
1. Victim visits attacker-controlled page

              ↓

2. Malicious JavaScript causes the browser
   to send a request to the vulnerable site

              ↓

3. Request body contains an
   attacker-controlled request prefix

              ↓

4. Vulnerable server responds without
   consuming the complete body

              ↓

5. Prefix remains on the TCP/TLS connection

              ↓

6. Browser reuses the connection

              ↓

7. Follow-up request is appended
   to the leftover prefix

              ↓

8. Connection is desynchronized
```

---

# 8. CSD Visualization

```text
VICTIM BROWSER
      |
      | POST
      | Content-Length: ...
      |
      | [malicious prefix]
      v
+-----------------------+
|   VULNERABLE SERVER   |
+-----------------------+
      |
      | responds early
      v

Malicious prefix remains
on connection

      ↓

Browser sends next request

      ↓

PREFIX + NEXT REQUEST

      ↓

DESYNCHRONIZATION
```

---

# 9. Important Difference From Traditional Smuggling

Traditional request smuggling:

```text
Browser/Attacker
       |
       v
Front-End
       X  ← DESYNC
       v
Back-End
```

Client-side desync:

```text
Victim Browser
       X  ← DESYNC
       v
Web Server
```

This means CSD does not necessarily require:

```text
Front-End + Back-End
```

architecture.

Your notes explicitly state that even:

```text
single-server websites
```

may potentially be vulnerable.

---

# 10. HTTP/1.1 Requirement

An important condition from the source is that client-side desync relies on:

```text
HTTP/1.1 connection reuse
```

Browsers generally prefer:

```text
HTTP/2
```

when the target supports it.

Therefore, the target normally needs to operate over HTTP/1.1 for this browser-powered technique.

Your source also mentions a possible exception where the victim accesses the target through a forward proxy that only supports HTTP/1.1.

---

# 11. Testing Workflow for CSD

Your source recommends testing methodically.

The workflow is:

```text
1. Probe for potential desync vectors in Burp

2. Confirm the desync vector in Burp

3. Build a browser proof of concept

4. Identify an exploitable gadget

5. Construct the working exploit in Burp

6. Replicate the exploit in the browser
```

Do not immediately jump from:

```text
"Interesting response"
```

to:

```text
"Browser exploitable"
```

Each stage should be confirmed separately.

---

# 12. Probing for CSD

The first goal is to find a request where the server appears to ignore:

```http
Content-Length
```

A simple probe is to specify a `Content-Length` that is larger than the body actually sent.

Conceptually:

```http
POST /candidate-endpoint HTTP/1.1
Host: vulnerable-website.com
Content-Length: 100

x
```

The server was told to expect more bytes.

Now observe what happens.

---

# 13. Interpreting the Probe

## Server Waits

If the request:

```text
hangs
```

or:

```text
times out
```

the server may be waiting for the remaining bytes.

Conceptually:

```text
Content-Length says 100
        |
        v
Server received less
        |
        v
WAIT
```

This does not demonstrate the desired CSD behavior.

---

## Server Responds Immediately

If the server responds immediately despite not receiving the full body:

```text
Content-Length says more data exists
        |
        v
Server responds anyway
```

then you may have found a potential:

```text
CSD VECTOR
```

This requires further confirmation.

---

# 14. Likely Candidate Endpoints

Your source notes that promising candidates are similar to those used when testing CL.0.

Examples include endpoints that are not normally expected to receive POST bodies, such as:

```text
Static resources
Server-level redirects
```

Server errors may also sometimes produce interesting behavior.

---

# 15. Confirming the Desync

Once a candidate is found, the next step is to determine whether leftover body data actually affects the next request on the same connection.

Conceptually:

```text
REQUEST 1

POST /candidate HTTP/1.1
Content-Length: CORRECT

GET /hopefully404 HTTP/1.1
Foo: x
```

followed on the same connection by:

```text
REQUEST 2

GET / HTTP/1.1
Host: vulnerable-website.com
```

If the server ignored the body of Request 1:

```text
GET /hopefully404...
```

may remain on the connection.

The following request can then be appended to it.

A response corresponding to:

```text
/hopefully404
```

provides evidence of the desync.

---

# 16. Why Connection Reuse Matters

CSD depends on:

```text
Connection reuse
```

If the connection closes immediately after the first response:

```text
Leftover prefix
       |
       v
Connection closed
       |
       X
Cannot poison next request
```

But if it stays open:

```text
Leftover prefix
       |
       v
Connection reused
       |
       v
Next request appended
```

the desync may be exploitable.

---

# 17. Browser Delivery

Once the behavior has been confirmed in Burp, the next challenge is reproducing it from a browser.

The source describes using browser-compatible cross-domain requests generated by JavaScript.

The conceptual flow is:

```text
Attacker-controlled page
        |
        v
Victim browser
        |
        | cross-domain request
        v
Vulnerable website
        |
        | responds early
        v
Connection poisoned
        |
        v
Follow-up browser request
```

---

# 18. Server-Side vs Client-Side

| Characteristic | Server-Side Desync | Client-Side Desync |
|---|---|---|
| Desynchronized connection | Front-end ↔ Back-end | Browser ↔ Server |
| Browser directly performs attack? | Usually no | Yes |
| Can affect single-server site? | Traditional attacks generally rely on multiple server components | Yes |
| Connection reuse important? | Yes | Yes |
| HTTP/1.1 important? | Often | Yes for CSD described here |
| Can involve ignored request body? | Yes | Yes |

---

# 19. Pause-Based Desync

Your advanced notes also introduce:

```text
PAUSE-BASED DESYNC
```

Some websites that initially appear safe may behave differently if the request is deliberately paused partway through transmission.

---

# 20. Why Pausing Matters

Servers commonly implement:

```text
READ TIMEOUTS
```

A server expects more request data:

```text
Content-Length: N
```

but no additional data arrives.

Eventually:

```text
READ TIMEOUT
```

may occur.

Some servers may then:

```text
issue a response
```

without consuming the complete request.

The dangerous behavior occurs if the server also:

```text
keeps the connection open
```

for reuse.

---

# 21. Pause-Based CL.0

Your notes explain that pause-based behavior can produce something similar to:

```text
CL.0
```

even when an ordinary CL.0 probe does not initially work.

Example structure from the source:

```http
POST /example HTTP/1.1
Host: vulnerable-website.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 34

GET /hopefully404 HTTP/1.1
Foo: x
```

Instead of sending everything immediately:

```text
Send Headers
      ↓
PAUSE
      ↓
Send Body
```

---

# 22. What Happens During the Pause?

The sequence described in your source is:

```text
1. Front-end receives request headers.

2. Front-end forwards the headers
   to the back-end.

3. Front-end waits for the body promised
   by Content-Length.

4. Back-end also waits.

5. Back-end reaches its read timeout.

6. Back-end sends a response despite not
   receiving the complete request.

7. Back-end leaves the connection open.

8. Attacker finally sends the body.

9. Front-end thinks these bytes are still
   part of the original request.

10. Back-end already finished Request 1.

11. Back-end therefore interprets the
    newly arriving body as another request.
```

Result:

```text
PAUSE-BASED CL.0 DESYNC
```

---

# 23. Pause-Based Visualization

```text
ATTACKER
   |
   | HEADERS
   v
FRONT-END
   |
   | HEADERS
   v
BACK-END
   |
   | waiting...
   |
   | READ TIMEOUT
   v
BACK-END SENDS RESPONSE
   |
   | connection remains open
   |
   v

ATTACKER SENDS BODY
   |
   v
FRONT-END
"Still part of Request 1"
   |
   v
BACK-END
"Request 1 already finished"
   |
   v
BODY interpreted as
NEW REQUEST
   |
   v
DESYNC
```

---

# 24. Conditions for Server-Side Pause-Based Desync

Your source specifies three important conditions.

### Condition 1

The front-end must forward request bytes to the back-end as they arrive rather than waiting for the complete request.

```text
Client
  ↓
Front-End
  ↓ immediately
Back-End
```

### Condition 2

The front-end must not time out before the back-end.

Otherwise, the attack will be terminated before the required back-end behavior occurs.

### Condition 3

After the back-end read timeout:

```text
connection must remain open
```

for reuse.

Without this:

```text
timeout
   ↓
connection closed
   ↓
no poisoned reusable connection
```

---

# 25. Testing Pause-Based Desync

Your notes recommend:

```text
Turbo Intruder
```

because some pause-based vulnerabilities cannot be reliably tested using Burp's core tools alone.

The relevant idea is:

```text
Send part of request
       ↓
Pause
       ↓
Allow back-end timeout
       ↓
Resume sending
```

---

# 26. Turbo Intruder Configuration

The source uses a single connection:

```python
engine = RequestEngine(
    endpoint=target.endpoint,
    concurrentConnections=1,
    requestsPerConnection=100,
    pipeline=False
)
```

The important settings are:

```text
concurrentConnections = 1
pipeline = False
```

This helps ensure that the requests interact with the same connection in the intended order.

---

# 27. Adding a Pause

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
Find:
\r\n\r\n

      ↓

Pause after headers

      ↓

Wait 60000 ms

      ↓

60 seconds
```

---

# 28. Follow-Up Request

A follow-up request can then be queued:

```python
followUp = 'GET / HTTP/1.1\r\nHost: vulnerable-website.com\r\n\r\n'
engine.queue(followUp)
```

The responses are recorded with:

```python
def handleResponse(req, interesting):
    table.add(req)
```

The goal is to determine whether the second response corresponds to the smuggled request prefix.

---

# 29. Client-Side Pause-Based Desync

Your notes also discuss a theoretical client-side version.

The problem is:

```text
How do you make a normal browser
pause halfway through a request?
```

The material states that there is not a reliable direct method for making the browser pause mid-request.

It describes a possible workaround involving an:

```text
ACTIVE MITM
```

that delays TCP packets.

The idea is:

```text
Browser
   |
   | packet 1
   | packet 2
   |
   | [delay final packet]
   v
Server
```

The server may time out and respond before the delayed packet arrives.

The delayed data could then potentially contribute to desynchronizing the connection.

---

# 30. Server-Side vs Client-Side vs Pause-Based

```text
HTTP DESYNC
     |
     +-----------------------+
     |                       |
     v                       v
SERVER-SIDE             CLIENT-SIDE
     |                       |
Front-End                 Browser
   ↕                         ↕
Back-End                  Server
     |
     v
Can also use
pause-based behavior
```

Pause-based behavior is therefore better thought of as another **technique/vector**, rather than simply a completely separate request-smuggling family.

---

# 31. Prevention Notes From the Source

Your material gives several high-level defensive measures.

Use:

```text
HTTP/2 end-to-end
```

and disable HTTP downgrading where possible.

If downgrading cannot be avoided, rewritten HTTP/1 requests should be validated.

---

Ambiguous requests should be:

```text
normalized by the front-end
```

and any remaining ambiguous requests should be:

```text
rejected by the back-end
```

with the connection closed.

---

The source also emphasizes:

> Never assume that requests will not have a body.

This is particularly important because such assumptions are the fundamental cause of:

```text
CL.0
```

and:

```text
Client-Side Desync
```

behavior.

---

# 32. Final Comparison

```text
CLASSIC SERVER-SIDE

Attacker
   ↓
Front-End
   X ← DESYNC
Back-End
```

```text
CLIENT-SIDE

Malicious Page
      ↓
Victim Browser
      X ← DESYNC
Web Server
```

```text
PAUSE-BASED SERVER-SIDE

Attacker
   ↓
Front-End
   ↓
Back-End waits
   ↓
TIMEOUT
   ↓
Back-End responds
   ↓
Connection stays open
   ↓
Remaining body arrives
   ↓
Interpreted as new request
```

---

# 33. One-Minute Revision

### Server-Side Desync

```text
Front-End ↔ Back-End
```

become desynchronized.

### Client-Side Desync

```text
Browser ↔ Server
```

become desynchronized.

### CSD Root Behavior

```text
Server responds
WITHOUT consuming body
        +
Connection reused
        =
Possible client-side desync
```

### Pause-Based Desync

```text
Send headers
    ↓
PAUSE
    ↓
Back-end timeout
    ↓
Response sent
    ↓
Connection remains open
    ↓
Send remaining body
    ↓
Possible CL.0-like desync
```

---

# Master Memory Map

```text
HTTP REQUEST SMUGGLING / DESYNC
│
├── Classic HTTP/1
│   ├── CL.TE
│   ├── TE.CL
│   └── TE.TE
│
├── HTTP/2 Downgrading
│   ├── H2.CL
│   └── H2.TE
│
├── Body Handling
│   ├── 0.CL
│   └── CL.0
│
├── Client-Side Desync
│   └── Browser ↔ Server
│
└── Pause-Based Desync
    └── Timeout creates CL.0-like behavior
```

---

## Theory Section Complete

You have now completed:

```text
Theory/
├── 01-Request-Smuggling-Fundamentals.md
├── 02-CL-TE-vs-TE-CL-vs-TE-TE.md
├── 03-Content-Length-and-Transfer-Encoding.md
├── 04-HTTP2-Downgrading.md
├── 05-0-CL-and-CL-0.md
└── 06-Client-and-Server-Side-Desync.md
```

## Next Section

Next move to:

```text
Notes/
```

starting with:

```text
Notes/HTTP-Request-Smuggling-Notes.md
```