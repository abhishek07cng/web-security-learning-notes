# CL.TE vs TE.CL vs TE.TE

## Overview

Classic HTTP/1 request smuggling occurs when the **front-end server** and **back-end server** disagree about how to determine the end of an HTTP request.

The two important headers are:

```http
Content-Length
Transfer-Encoding
```

The three classic request-smuggling variants are:

| Variant | Front-End Uses | Back-End Uses |
|---|---|---|
| `CL.TE` | Content-Length | Transfer-Encoding |
| `TE.CL` | Transfer-Encoding | Content-Length |
| `TE.TE` | Transfer-Encoding | Transfer-Encoding, but one server ignores an obfuscated TE header |

---

# 1. CL.TE

## Meaning

```text
CL.TE
│   │
│   └── Back-End → Transfer-Encoding
│
└────── Front-End → Content-Length
```

So:

```text
Front-End = Content-Length
Back-End  = Transfer-Encoding
```

---

## Basic CL.TE Request

Example:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

The important part is that the request contains **both**:

```http
Content-Length: 13
```

and:

```http
Transfer-Encoding: chunked
```

But the two servers interpret them differently.

---

## What the Front-End Sees

The front-end uses:

```http
Content-Length: 13
```

Therefore, it considers the request body to contain all 13 bytes.

Conceptually:

```text
FRONT-END VIEW

POST / HTTP/1.1
...
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
^^^^^^^^^^^^^
Entire body according to Content-Length
```

The front-end forwards this request to the back-end.

---

## What the Back-End Sees

The back-end ignores `Content-Length` and processes:

```http
Transfer-Encoding: chunked
```

The body begins:

```text
0
```

In chunked encoding:

```text
0 = end of request body
```

Therefore, the back-end considers the request finished here:

```text
0

--- BACK-END REQUEST ENDS ---
```

The remaining bytes:

```text
SMUGGLED
```

are left unprocessed.

---

## Result

The back-end may interpret:

```text
SMUGGLED
```

as the beginning of the **next HTTP request**.

Conceptually:

```text
Front-End:

[ 0 + SMUGGLED ]

        ↓ forwarded

Back-End:

[ 0 ][ SMUGGLED ]
  ↑       ↑
END      left over
         for next request
```

This is the desynchronization.

---

# CL.TE Memory Trick

Remember:

```text
CL.TE

Front → CL
Back  → TE
```

or:

```text
CLIENT
   |
   v
FRONT-END
   |
   | Content-Length
   v
BACK-END
   |
   | Transfer-Encoding
   v
SMUGGLED DATA
```

---

# 2. TE.CL

## Meaning

```text
TE.CL
│   │
│   └── Back-End → Content-Length
│
└────── Front-End → Transfer-Encoding
```

So:

```text
Front-End = Transfer-Encoding
Back-End  = Content-Length
```

This is the **opposite of CL.TE**.

---

## Basic TE.CL Request

Example:

```http
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```

---

# What the Front-End Sees

The front-end uses:

```http
Transfer-Encoding: chunked
```

Therefore, it interprets:

```text
8
SMUGGLED
0
```

as a chunked message.

Conceptually:

```text
8
SMUGGLED
0
```

The final:

```text
0
```

terminates the chunked body.

The front-end therefore forwards the complete request.

---

# What the Back-End Sees

The back-end ignores `Transfer-Encoding` and instead uses:

```http
Content-Length: 3
```

Therefore, it believes that the body contains only the number of bytes specified by `Content-Length`.

The remaining bytes are left in the back-end connection.

These leftover bytes can then become part of the next HTTP request.

---

# TE.CL Visualization

```text
                REQUEST
                   |
                   v

        +--------------------+
        |     FRONT-END      |
        | Transfer-Encoding  |
        +--------------------+
                   |
             reads chunks
                   |
                   v
        +--------------------+
        |      BACK-END      |
        |   Content-Length   |
        +--------------------+
                   |
          reads fewer bytes
                   |
                   v
           LEFTOVER DATA
                   |
                   v
             NEXT REQUEST
```

---

# Important Burp Setting for TE.CL

When manually testing TE.CL in Burp Repeater, the source notes that you may need to disable:

```text
Update Content-Length
```

Otherwise, Burp may automatically change the `Content-Length` value and break the deliberately malformed request.

In Burp Repeater:

```text
Repeater
   ↓
Menu
   ↓
Update Content-Length
   ↓
UNCHECK
```

Also remember that the final zero chunk needs the appropriate trailing CRLF sequence.

Conceptually:

```text
0\r\n\r\n
```

---

# TE.CL Memory Trick

```text
TE.CL

Front → TE
Back  → CL
```

Compare:

```text
CL.TE = Front CL / Back TE

TE.CL = Front TE / Back CL
```

---

# 3. TE.TE

## Meaning

TE.TE is different.

Both the front-end and back-end normally support:

```http
Transfer-Encoding
```

However, one server can sometimes be induced to **ignore the Transfer-Encoding header** if the header is obfuscated.

---

# Normal Situation

Both servers understand:

```http
Transfer-Encoding: chunked
```

Therefore:

```text
Front-End → TE
Back-End  → TE
```

No disagreement:

```text
Same interpretation
        ↓
No desynchronization
```

---

# Obfuscating Transfer-Encoding

Different HTTP server implementations may tolerate malformed or unusual headers differently.

Examples from the source material include variations such as:

```http
Transfer-Encoding: xchunked
```

or:

```http
Transfer-Encoding : chunked
```

or duplicate headers:

```http
Transfer-Encoding: chunked
Transfer-Encoding: x
```

Other variations may involve whitespace or unusual formatting.

---

# Why Does This Matter?

Imagine:

```text
Front-End
     ↓
recognizes obfuscated TE

Back-End
     ↓
does NOT recognize obfuscated TE
```

Now the servers disagree.

Alternatively:

```text
Front-End
     ↓
ignores obfuscated TE

Back-End
     ↓
recognizes TE
```

Again, they disagree.

---

# TE.TE Can Become CL.TE or TE.CL

Once one server ignores the obfuscated `Transfer-Encoding` header, the resulting behavior may effectively become:

```text
CL.TE
```

or:

```text
TE.CL
```

depending on which server ignores the TE header.

---

# TE.TE Visualization

```text
Request
   |
   | Content-Length
   | Transfer-Encoding: [obfuscated]
   |
   v
+------------------+
|    FRONT-END     |
+------------------+
       |
       | recognizes TE?
       |
       v
+------------------+
|     BACK-END     |
+------------------+
       |
       | recognizes TE?
       |
       v

If answers differ
       ↓
DESYNCHRONIZATION
```

---

# Why TE.TE Exists

Real-world HTTP implementations do not always interpret unusual syntax identically.

One server may accept:

```text
slightly malformed TE header
```

while another server rejects or ignores it.

That parser disagreement can create the request-boundary ambiguity required for request smuggling.

---

# Quick Comparison

## CL.TE

```text
FRONT-END
Content-Length
     |
     v
BACK-END
Transfer-Encoding
```

Think:

```text
CL → TE
```

---

## TE.CL

```text
FRONT-END
Transfer-Encoding
     |
     v
BACK-END
Content-Length
```

Think:

```text
TE → CL
```

---

## TE.TE

```text
FRONT-END
Transfer-Encoding
     |
different parsing
     |
     v
BACK-END
Transfer-Encoding

One server ignores
the obfuscated TE header
```

---

# Fast Identification Table

| Question | CL.TE | TE.CL | TE.TE |
|---|---|---|---|
| Front-end uses CL? | ✅ | ❌ | Depends on obfuscation |
| Front-end uses TE? | ❌ | ✅ | Usually |
| Back-end uses CL? | ❌ | ✅ | Depends on obfuscation |
| Back-end uses TE? | ✅ | ❌ | Usually |
| TE obfuscation central? | ❌ | ❌ | ✅ |
| HTTP/1 classic technique? | ✅ | ✅ | ✅ |

---

# Exam / Interview Memory Trick

Do not try to memorize the whole attack first.

Just remember:

```text
LEFT = FRONT
RIGHT = BACK
```

Therefore:

```text
CL.TE
│   │
│   └── BACK = TE
└────── FRONT = CL
```

and:

```text
TE.CL
│   │
│   └── BACK = CL
└────── FRONT = TE
```

So if someone asks:

> In a CL.TE vulnerability, which server uses Content-Length?

Answer:

```text
Front-end server.
```

If they ask:

> Which server uses Transfer-Encoding?

Answer:

```text
Back-end server.
```

---

# How the Desync Happens

The overall logic for all variants is:

```text
1. Attacker sends ambiguous HTTP request

                    ↓

2. Front-end determines request boundary

                    ↓

3. Back-end determines a DIFFERENT boundary

                    ↓

4. Extra bytes remain in back-end connection

                    ↓

5. Back-end interprets leftover bytes as part
   of the next request

                    ↓

6. HTTP REQUEST SMUGGLING
```

---

# Key Revision Points

### CL.TE

```text
Front-End = Content-Length
Back-End  = Transfer-Encoding
```

### TE.CL

```text
Front-End = Transfer-Encoding
Back-End  = Content-Length
```

### TE.TE

```text
Both support Transfer-Encoding,
but header obfuscation makes one server ignore it.
```

### Most Important Concept

```text
Request Smuggling
        =
Front-End Parsing
        ≠
Back-End Parsing
```

---

# One-Minute Revision

```text
CL.TE
Front = CL
Back  = TE

TE.CL
Front = TE
Back  = CL

TE.TE
Both understand TE
BUT
one ignores an obfuscated TE header
```

---

## Next File

Continue to:

`03-Content-Length-and-Transfer-Encoding.md`

That file will focus specifically on:

- `Content-Length`
- Chunked encoding
- Hexadecimal chunk sizes
- Zero chunk
- CRLF
- Conflicting CL/TE headers
- Why different parsers create ambiguity
- Burp behavior when working with these headers