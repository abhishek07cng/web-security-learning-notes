# HTTP/2 Request-Smuggling Payload Notes

> For authorized training environments only.

HTTP/2 uses explicit frame lengths, so classic HTTP/1 `Content-Length` versus `Transfer-Encoding` ambiguity does not apply end-to-end. The important training scenario is **HTTP/2 downgrading**, where a front end translates HTTP/2 into HTTP/1 for the back end.

## H2.CL concept

A misleading HTTP/2 `content-length` value may survive an HTTP/2 → HTTP/1 downgrade when validation is incorrect.

Conceptual representation:

```text
:method    POST
:path      /example
:authority YOUR-LAB-ID.web-security-academy.net
content-length: <TEST-VALUE>

<REQUEST-BODY>
```

### Mental model

```text
Client --HTTP/2--> Front End --HTTP/1--> Back End
        frame length               Content-Length
```

A discrepancy during downgrade can create a desynchronization.

## H2.TE concept

HTTP/2 normally prohibits `Transfer-Encoding`, but vulnerable downgrade implementations may fail to remove it before creating the HTTP/1 request.

Conceptual representation:

```text
:method    POST
:path      /example
:authority YOUR-LAB-ID.web-security-academy.net
transfer-encoding: chunked

<LAB BODY>
```

## CRLF injection concept

Some HTTP/2 downgrade vulnerabilities involve injecting CRLF characters into a header value so that the resulting HTTP/1 request contains an unintended header or request boundary.

```text
HTTP/2 header value
        ↓ downgrade
HTTP/1 textual headers
        ↓
Unexpected parser interpretation
```

## Burp reminder

HTTP/2 pseudo-headers such as `:method`, `:path`, and `:authority` are easiest to inspect and modify using Burp Repeater's HTTP/2-aware interface.

Keep exact exploit strings with the corresponding authorized lab writeup rather than treating them as universal payloads; behavior depends on the front-end/back-end implementation.
