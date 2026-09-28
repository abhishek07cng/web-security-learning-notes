# Content-Length and Transfer-Encoding

## Why These Headers Matter

HTTP Request Smuggling is fundamentally about:

> **Where does one HTTP request end and the next request begin?**

In HTTP/1, two important mechanisms can determine the length of a request body:

```http
Content-Length
```

and:

```http
Transfer-Encoding: chunked
```

If a front-end server and back-end server interpret these differently, they may disagree about the request boundary.

That disagreement can create HTTP Request Smuggling.

---

# 1. Content-Length

## What is Content-Length?

The `Content-Length` header tells the server exactly how many **bytes** are contained in the HTTP message body.

Example:

```http
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smuggling
```

The important header is:

```http
Content-Length: 11
```

This tells the server:

```text
Read 11 bytes as the request body.
```

---

# Content-Length Mental Model

Think of `Content-Length` as:

```text
Content-Length: N
        |
        v
Read exactly N bytes
        |
        v
Request body ends
```

For example:

```http
Content-Length: 5

HELLO
```

Conceptually:

```text
H E L L O
1 2 3 4 5
```

The server expects five bytes.

---

# 2. Transfer-Encoding

Instead of specifying the complete body length, HTTP/1 can use:

```http
Transfer-Encoding: chunked
```

This means the body is sent as one or more **chunks**.

---

# Chunked Encoding Structure

Each chunk contains:

```text
Chunk Size
    ↓
Chunk Data
    ↓
Next Chunk
```

The chunk size is represented in:

```text
HEXADECIMAL
```

The message ends with a chunk of size:

```text
0
```

---

# Example from the Notes

```http
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked

b
q=smuggling
0
```

Here:

```text
b
```

is hexadecimal.

Hexadecimal:

```text
b = 11 decimal
```

Therefore:

```text
b
q=smuggling
```

means that the chunk contains 11 bytes.

The final:

```text
0
```

means:

```text
No more chunks.
End of body.
```

---

# Chunked Encoding Mental Model

```text
Transfer-Encoding: chunked

        ↓

Chunk Size (HEX)

        ↓

Chunk Data

        ↓

Next Chunk Size

        ↓

Chunk Data

        ↓

0

        ↓

END
```

---

# Example With Multiple Chunks

Conceptually:

```http
Transfer-Encoding: chunked

4
TEST
3
ABC
0
```

Read it as:

```text
4
↓
Read 4 bytes
↓
TEST

3
↓
Read 3 bytes
↓
ABC

0
↓
END
```

The important idea is that the body length is determined by the **chunk structure**, rather than one overall `Content-Length`.

---

# 3. Content-Length vs Transfer-Encoding

The difference is simple:

## Content-Length

```text
Content-Length: 100
```

means:

```text
Read 100 bytes.
```

## Transfer-Encoding

```text
Transfer-Encoding: chunked
```

means:

```text
Read each chunk according
to its hexadecimal chunk size
until the zero-size chunk.
```

---

# Comparison

| Feature | Content-Length | Transfer-Encoding: chunked |
|---|---|---|
| Determines body size | Yes | Yes |
| Overall body size specified directly | Yes | No |
| Uses chunks | No | Yes |
| Chunk sizes hexadecimal | N/A | Yes |
| Ends with zero chunk | No | Yes |

---

# 4. What Happens if Both Headers Are Present?

Now we reach the important request-smuggling concept.

Imagine:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

This request contains:

```http
Content-Length: 13
```

AND:

```http
Transfer-Encoding: chunked
```

This creates the possibility of different interpretations.

---

# Interpretation A — Content-Length

A server that processes:

```http
Content-Length: 13
```

determines the body length using the number of bytes.

Conceptually:

```text
Content-Length
      |
      v
Read N bytes
      |
      v
Request ends
```

---

# Interpretation B — Transfer-Encoding

A server that processes:

```http
Transfer-Encoding: chunked
```

sees:

```text
0
```

and treats this as the end of the chunked body.

Conceptually:

```text
Transfer-Encoding
        |
        v
Read chunk sizes
        |
        v
0
        |
        v
Request ends
```

Anything after that may remain unprocessed by that server.

---

# The Parsing Disagreement

Now imagine:

```text
FRONT-END
     |
     | uses Content-Length
     v

BACK-END
     |
     | uses Transfer-Encoding
     v
```

The front-end and back-end can determine different request boundaries.

This gives us:

```text
CL.TE
```

The opposite situation:

```text
FRONT-END
     |
     | uses Transfer-Encoding
     v

BACK-END
     |
     | uses Content-Length
     v
```

gives us:

```text
TE.CL
```

---

# 5. What Does the HTTP Specification Say?

Your notes explain that when both:

```http
Content-Length
```

and:

```http
Transfer-Encoding
```

are present, the specification attempts to prevent ambiguity by saying that `Content-Length` should be ignored.

But problems can still arise when multiple servers are chained together.

For example:

```text
Browser
   |
   v
Front-End
   |
   v
Back-End
```

because the servers may not implement or interpret the request identically.

---

# 6. Why Servers May Disagree

Your notes identify two important reasons.

## Reason 1 — TE Not Supported

Some servers may not support:

```http
Transfer-Encoding
```

in requests.

Therefore:

```text
Server A → understands TE
Server B → does not
```

---

## Reason 2 — TE Header Obfuscation

A server may normally understand:

```http
Transfer-Encoding: chunked
```

but fail to recognize an unusual or obfuscated version.

For example, the notes show variants such as:

```http
Transfer-Encoding: xchunked
```

or:

```http
Transfer-Encoding : chunked
```

or:

```http
Transfer-Encoding: chunked
Transfer-Encoding: x
```

Different implementations may process these differently.

That is the basis of:

```text
TE.TE
```

behavior.

---

# 7. CRLF

When working with raw HTTP messages, line endings matter.

HTTP/1 messages conventionally use:

```text
\r\n
```

where:

```text
\r = Carriage Return
\n = Line Feed
```

Together:

```text
\r\n = CRLF
```

A blank line separating headers from the body is therefore represented conceptually as:

```text
\r\n\r\n
```

---

# Why CRLF Matters in Request Smuggling

Request smuggling depends heavily on exact request formatting.

For example, your TE.CL notes specifically warn that the final zero chunk requires the trailing sequence:

```text
\r\n\r\n
```

So small formatting changes can alter how the request is parsed.

---

# 8. Burp Suite and Content-Length

Burp Suite tries to make normal HTTP editing easier.

But request-smuggling testing deliberately creates abnormal or ambiguous requests.

For TE.CL testing, your notes instruct you to ensure that:

```text
Update Content-Length
```

is unchecked.

Otherwise, Burp may automatically recalculate the header.

Conceptually:

```text
You deliberately set:

Content-Length: 4

        ↓

Burp recalculates it

        ↓

Content-Length changes

        ↓

Your intended parsing discrepancy
may disappear
```

So during relevant labs:

```text
Burp Repeater
      ↓
Repeater menu
      ↓
Update Content-Length
      ↓
UNCHECK
```

---

# 9. Burp and Chunked Encoding

Another important point from the notes:

Burp Suite may automatically unpack chunked encoding to make messages easier to view and edit.

Also, browsers normally do not use chunked encoding in requests.

This means chunked **request** bodies may look unfamiliar even if you have already seen chunked encoding in HTTP responses.

---

# 10. Why HTTP/1 Is Important

Classic:

```text
CL.TE
TE.CL
TE.TE
```

request-smuggling techniques rely on HTTP/1 request parsing.

The fundamental problem is:

```text
Two possible message-length mechanisms

Content-Length
        +
Transfer-Encoding
        ↓
Different server interpretation
        ↓
Different request boundaries
        ↓
DESYNC
```

---

# 11. HTTP/2 Difference

Your notes state that HTTP/2 used **end-to-end** has a single robust mechanism for specifying request length.

Therefore, the classic:

```text
Content-Length vs Transfer-Encoding
```

ambiguity does not occur in the same way.

However:

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

creates another important situation.

The front-end has to convert the HTTP/2 request into HTTP/1.

This process is:

```text
HTTP/2 DOWNGRADING
```

and is the subject of the next theory file.

---

# Quick Revision

## Content-Length

```http
Content-Length: N
```

means:

```text
Read N bytes.
```

---

## Transfer-Encoding

```http
Transfer-Encoding: chunked
```

means:

```text
Read chunk size
      ↓
Read chunk data
      ↓
Repeat
      ↓
0
      ↓
END
```

---

## Chunk Sizes

Chunk sizes are:

```text
HEXADECIMAL
```

Example:

```text
b hex = 11 decimal
```

---

## Zero Chunk

```text
0
```

means:

```text
End of chunked body.
```

---

## CRLF

```text
\r\n
```

means:

```text
Carriage Return + Line Feed
```

and:

```text
\r\n\r\n
```

represents the blank-line separation used in HTTP message formatting.

---

# Most Important Concept

Remember:

```text
Content-Length
       vs
Transfer-Encoding
       ↓
Different interpretations
       ↓
Different request boundaries
       ↓
HTTP REQUEST SMUGGLING
```

---

# Memory Trick

```text
CL = COUNT bytes

TE = CHUNKS
```

So:

```text
Content-Length
→ "How many bytes?"

Transfer-Encoding
→ "How are the chunks structured?"
```

---

# Final Revision Diagram

```text
                 HTTP/1 REQUEST
                       |
             +---------+---------+
             |                   |
             v                   v
      Content-Length      Transfer-Encoding
             |                   |
             v                   v
       Count bytes          Read chunks
                                 |
                                 v
                            Zero chunk
                                 |
                                 v
                                END

             If servers disagree
                     ↓
                   DESYNC
                     ↓
          HTTP REQUEST SMUGGLING
```

---

## Next

Continue to:

`04-HTTP2-Downgrading.md`