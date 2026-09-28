# HTTP Request Smuggling — Fundamentals

## What is HTTP Request Smuggling?

HTTP Request Smuggling is a technique for interfering with how a website processes a sequence of HTTP requests.

The vulnerability occurs when different servers in the request chain **disagree about where one HTTP request ends and the next request begins**.

Request smuggling vulnerabilities can be critical because they may allow an attacker to:

- Bypass security controls
- Gain unauthorized access to sensitive data
- Interfere with other users' requests
- Compromise application users

---

## Where Does Request Smuggling Happen?

Modern web applications commonly use multiple HTTP servers.

A typical architecture looks like:

```text
User
  |
  v
Front-End Server
(Load Balancer / Reverse Proxy)
  |
  v
Back-End Server
  |
  v
Application
```

The user normally does not communicate directly with the back-end server.

Instead:

```text
Client
   |
   | HTTP Request
   v
Front-End
   |
   | Forwarded Request
   v
Back-End
```

The front-end server may be:

- A reverse proxy
- A load balancer
- A CDN
- Another gateway/proxy component

---

## Why Does Request Smuggling Occur?

Front-end servers commonly forward multiple HTTP requests over the same back-end connection.

Conceptually:

```text
Request 1
Request 2
Request 3
Request 4
```

The receiving server therefore needs to determine:

```text
Where does Request 1 end?

Where does Request 2 begin?
```

Both the front-end and back-end servers must agree on these boundaries.

If they disagree, a **desynchronization** can occur.

---

## Request Boundary Desynchronization

Imagine an attacker sends an ambiguous request:

```text
Attacker
   |
   v
+----------------+
| Front-End      |
| Interpretation |
+----------------+
        |
        v
+----------------+
| Back-End       |
| Interpretation |
+----------------+
```

The front-end may believe:

```text
[----------- Request 1 -----------]
```

while the back-end may interpret the same bytes as:

```text
[---- Request 1 ----][Request 2...]
```

The extra data left by the first request can then become the beginning of the next request.

This is the basic idea behind **HTTP Request Smuggling**.

---

# HTTP/1 Request Length

Most classic HTTP request smuggling vulnerabilities arise because HTTP/1 provides two ways to specify the end of a request body:

1. `Content-Length`
2. `Transfer-Encoding`

---

## Content-Length

`Content-Length` tells the server the length of the HTTP message body in **bytes**.

Example:

```http
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smuggling
```

Here:

```text
Content-Length: 11
```

means the server expects **11 bytes** in the request body.

---

# Transfer-Encoding

Another way to specify the body is:

```http
Transfer-Encoding: chunked
```

With chunked encoding, the body is divided into chunks.

Example:

```http
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked

b
q=smuggling
0
```

The chunk size is represented in **hexadecimal**.

The final:

```text
0
```

indicates the end of the message.

---

## Important Burp Note

When testing chunked requests, remember:

> Burp Suite may automatically unpack chunked encoding to make messages easier to view and edit.

Also, browsers do not normally use chunked encoding for requests.

This is one reason security testers may be less familiar with chunked request bodies.

---

# The Core Problem

A request can potentially contain both:

```http
Content-Length: ...
```

and:

```http
Transfer-Encoding: chunked
```

For example:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

If both servers interpret the request in exactly the same way, there is no desynchronization.

The vulnerability appears when they **interpret it differently**.

---

# Front-End vs Back-End Disagreement

Suppose:

```text
Front-End
   |
   | Uses Content-Length
   v
Request boundary A

Back-End
   |
   | Uses Transfer-Encoding
   v
Request boundary B
```

The two servers now disagree about the request boundary.

Part of the attacker's request may remain in the back-end connection.

Conceptually:

```text
ATTACKER REQUEST
        |
        v
+--------------------+
| Front-End Server   |
| Request ends here  |
+--------------------+
        |
        v
+--------------------+
| Back-End Server    |
| Request ends here  |
+--------------------+
        |
        v
   SMUGGLED DATA
        |
        v
Next HTTP Request
```

The smuggled data can interfere with the next request processed by the back-end server.

---

# Why Can Servers Disagree?

Problems can arise because:

1. Some servers do not support `Transfer-Encoding` in requests.

2. Some servers support it but can be induced not to process it when the header is obfuscated.

3. Different front-end and back-end implementations may parse unusual requests differently.

For example:

```http
Transfer-Encoding: chunked
```

may be recognized by one server, while an unusual variation may be ignored by another.

This disagreement creates the possibility of request smuggling.

---

# Three Classic HTTP/1 Variants

Classic request smuggling is commonly divided into:

```text
CL.TE
TE.CL
TE.TE
```

## CL.TE

```text
Front-End  → Content-Length
Back-End   → Transfer-Encoding
```

Memory trick:

```text
CL . TE
^     ^
|     |
FE    BE
```

---

## TE.CL

```text
Front-End  → Transfer-Encoding
Back-End   → Content-Length
```

Memory trick:

```text
TE . CL
^     ^
|     |
FE    BE
```

---

## TE.TE

Both servers support `Transfer-Encoding`, but one can be induced to ignore it through some form of header obfuscation.

```text
Front-End → Transfer-Encoding
Back-End  → Transfer-Encoding

BUT

one server ignores the obfuscated TE header
```

The result can behave like either:

```text
CL.TE
```

or:

```text
TE.CL
```

depending on which server ignores the header.

---

# HTTP/1 vs HTTP/2

Classic:

```text
CL.TE
TE.CL
TE.TE
```

techniques rely on HTTP/1 request parsing.

HTTP/2 uses a different mechanism for determining message length.

If HTTP/2 is used **end-to-end**, it avoids the classic `Content-Length` versus `Transfer-Encoding` ambiguity.

However, an important situation is:

```text
Client
   |
 HTTP/2
   |
   v
Front-End
   |
 HTTP/1
   |
   v
Back-End
```

The front-end converts the HTTP/2 request into HTTP/1 before forwarding it.

This is known as:

# HTTP/2 Downgrading

Request smuggling can become possible when the conversion to HTTP/1 introduces parsing discrepancies.

We will cover this separately in:

```text
Theory/04-HTTP2-Downgrading.md
```

---

# Burp Suite Testing Note

When a PortSwigger lab supports HTTP/2 but requires a classic HTTP/1 request-smuggling technique, manually switch the request protocol in **Burp Repeater**.

Look in:

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

For some TE.CL testing, you may also need to prevent Burp from automatically correcting the `Content-Length`.

---

# Quick Mental Model

Remember request smuggling like this:

```text
            HTTP REQUEST
                 |
                 v
        +----------------+
        |   FRONT-END    |
        +----------------+
          thinks request
            ends HERE
                 |
                 v
        +----------------+
        |    BACK-END    |
        +----------------+
          thinks request
          ends somewhere
             ELSE
                 |
                 v
            DESYNC
                 |
                 v
        SMUGGLED REQUEST
```

---

# Key Revision Points

- HTTP request smuggling is fundamentally a **request-boundary/desynchronization problem**.
- Modern applications often have both front-end and back-end HTTP servers.
- Both servers must agree about where each request ends.
- HTTP/1 can use `Content-Length` or `Transfer-Encoding` to determine message length.
- Different interpretation of these mechanisms can create request smuggling.
- The three classic variants are `CL.TE`, `TE.CL`, and `TE.TE`.
- `CL.TE` = front-end uses CL, back-end uses TE.
- `TE.CL` = front-end uses TE, back-end uses CL.
- `TE.TE` relies on different handling of an obfuscated TE header.
- Classic CL/TE attacks require HTTP/1.
- HTTP/2 used end-to-end avoids the classic ambiguity.
- HTTP/2 → HTTP/1 downgrading can introduce new request-smuggling opportunities.

---

## One-Line Definition

> **HTTP Request Smuggling occurs when front-end and back-end servers disagree about HTTP request boundaries, allowing part of one request to be interpreted as the beginning of another request.**

---

## Next

Continue with:

**`02-CL-TE-vs-TE-CL-vs-TE-TE.md`**

There we will break down the three variants visually and analyze exactly what the front-end and back-end see.