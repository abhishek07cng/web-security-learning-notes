# Lab 19 — refer to this post : https://medium.com/@sandeep18.privateemail/0-cl-demistified-ft-portswigger-web-security-academy-fb6413089991

> **Scope:** PortSwigger Web Security Academy / authorized lab environment only.

## Lab Notes

-------------------

#CL.0 request smuggling
Request smuggling vulnerabilities are the result of discrepancies in how chained systems determine where each request starts and ends. This is typically due to inconsistent header parsing, leading to one server using a request's Content-Length and the other treating the message as chunked. However, it's possible to perform many of the same attacks without relying on either of these issues.

In some instances, servers can be persuaded to ignore the Content-Length header, meaning they assume that each request finishes at the end of the headers. This is effectively the same as treating the Content-Length as 0.

If the back-end server exhibits this behavior, but the front-end still uses the Content-Length header to determine where the request ends, you can potentially exploit this discrepancy for HTTP request smuggling. We've decided to call this a "CL.0" vulnerability.

PortSwigger Research
The materials and labs in this section are based on Browser-Powered Desync Attacks: A New Frontier in HTTP Request Smuggling by PortSwigger Research.

Testing for CL.0 vulnerabilities
To probe for CL.0 vulnerabilities, first send a request containing another partial request in its body, then send a normal follow-up request. You can then check to see whether the response to the follow-up request was affected by the smuggled prefix.

In the following example, the follow-up request for the home page has received a 404 response. This strongly suggests that the back-end server interpreted the body of the POST request (GET /hopefully404...) as the start of another request.

```http
POST /vulnerable-endpoint HTTP/1.1
Host: vulnerable-website.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 34
```

```http
GET /hopefully404 HTTP/1.1
Foo: xGET / HTTP/1.1
Host: vulnerable-website.com
HTTP/1.1 200 OK
```

HTTP/1.1 404 Not Found
Crucially, notice that we haven't tampered with the headers in any way - the length of the request is specified by a perfectly normal, accurate Content-Length header.

To try this yourself using Burp Repeater:

Create one tab containing the setup request and another containing an arbitrary follow-up request.

Add the two tabs to a group in the correct order.

Using the drop-down menu next to the Send button, change the send mode to Send group in sequence (single connection).

Change the Connection header to keep-alive.

Send the sequence and check the responses.

In the wild, we've mostly observed this behavior on endpoints that simply aren't expecting POST requests, so they implicitly assume that no requests have a body. Endpoints that trigger server-level redirects and requests for static files are prime candidates.

Eliciting CL.0 behavior
If you can't find any endpoints that appear vulnerable, you can try eliciting this behavior instead.

When a request's headers trigger a server error, some servers issue an error response without consuming the request body off the socket. If they don't close the connection afterwards, this can provide an alternative CL.0 desync vector.

You can also try using GET requests with an obfuscated Content-Length header. If you're able to hide this from the back-end server but not the front-end, this also has the potential to cause a desync. We looked at some header obfuscation techniques when we covered TE.TE request smuggling.

Exploiting CL.0 vulnerabilities
You can exploit CL.0 vulnerabilities for the same server-side request smuggling attacks we've covered in our previous request smuggling materials. Try this for yourself with the following lab.
----
