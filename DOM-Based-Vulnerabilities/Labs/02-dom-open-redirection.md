# Lab 02 — DOM-Based Open Redirection

## 1. Lab Overview

DOM-based open redirection occurs when client-side JavaScript takes attacker-controlled data and writes it into a navigation sink.

The basic source-to-sink model is:

```text
Attacker-Controlled Input
        ↓
DOM Source
        ↓
JavaScript Processing
        ↓
Navigation Sink
        ↓
Browser Redirect
        ↓
External Domain
```

The key mental model is:

```text
SOURCE → PROPAGATION → NAVIGATION SINK → REDIRECTION
```

---

# 2. Lab Objective

This lab contains a:

```text
DOM-based open-redirection vulnerability
```

The objective is to:

```text
Exploit the vulnerability
        ↓
Redirect the victim
        ↓
To the exploit server
```

The provided lab material specifies that the vulnerable functionality is the **"Back to Blog"** link on a blog post page. :contentReference[oaicite:2]{index=2}

---

# 3. Vulnerability Overview

The vulnerability occurs because client-side JavaScript extracts a URL from attacker-controlled data and assigns it to a navigation property.

A simplified vulnerable pattern is:

```javascript
let url = /https?:\/\/.+/.exec(location.hash);

if (url) {
    location = url[0];
}
```

The flow is:

```text
location.hash
      ↓
URL Extraction
      ↓
url[0]
      ↓
location
      ↓
Browser Navigation
```

The source material identifies this as a DOM-based open-redirection vulnerability. :contentReference[oaicite:3]{index=3}

---

# 4. What Is Open Redirection?

An open redirect occurs when an application allows an attacker to cause a user to navigate to an arbitrary external destination.

For example:

```text
Trusted Website
      ↓
Attacker-Controlled URL
      ↓
External Website
```

The victim initially visits the legitimate application URL but is subsequently redirected elsewhere.

---

# 5. DOM-Based Open Redirection

The important difference is that the redirection happens through client-side JavaScript.

```text
Attacker-Controlled URL
        ↓
Browser
        ↓
JavaScript
        ↓
Navigation Sink
        ↓
External Site
```

The server does not necessarily need to issue the redirect.

---

# 6. Common Source

The most common source in this example is:

```javascript
location.hash
```

For example:

```text
https://example.com/example#https://evil.example
```

JavaScript can extract:

```text
https://evil.example
```

from the fragment.

---

# 7. Vulnerable Example

Consider:

```javascript
goto = location.hash.slice(1);

if (goto.startsWith('https:')) {
    location = goto;
}
```

The flow is:

```text
URL Fragment
      ↓
location.hash
      ↓
slice(1)
      ↓
goto
      ↓
startsWith('https:')
      ↓
location
      ↓
External Navigation
```

The source material provides this as a basic example of DOM-based open redirection. :contentReference[oaicite:4]{index=4}

---

# 8. Example Attack URL

A conceptual malicious URL is:

```text
https://www.innocent-website.com/example#https://www.evil-user.net
```

The browser loads:

```text
innocent-website.com
```

Then the client-side JavaScript reads:

```text
location.hash
```

and redirects the browser to:

```text
https://www.evil-user.net
```

:contentReference[oaicite:5]{index=5}

---

# 9. Why the Fragment Is Useful

The fragment:

```text
#...
```

is available to client-side JavaScript through:

```javascript
location.hash
```

This makes it useful for testing DOM-based vulnerabilities.

Conceptually:

```text
Attacker-Controlled Fragment
        ↓
location.hash
        ↓
JavaScript
        ↓
Navigation Sink
```

---

# 10. Lab — DOM-Based Open Redirection

## Objective

The specific lab asks you to:

```text
Exploit the DOM-based open redirect
        ↓
Redirect the victim
        ↓
To your exploit server
```

:contentReference[oaicite:6]{index=6}

---

# 11. Step 1 — Open a Blog Post

Open a blog post in the lab.

Locate the:

```text
Back to Blog
```

link.

The link returns the user to the blog home page.

---

# 12. Step 2 — Inspect the Link

Inspect the HTML / JavaScript associated with:

```text
Back to Blog
```

The provided lab notes show the relevant behavior:

```javascript
returnURL = /url=https?:\/\/.+/.exec(location);

if (returnURL)
    location.href = returnURL[1];
else
    location.href = "/";
```

The important parts are:

```text
location
      ↓
Regex
      ↓
returnURL[1]
      ↓
location.href
```

:contentReference[oaicite:7]{index=7}

---

# 13. Step 3 — Identify the Source

The source is:

```javascript
location
```

The application searches the current URL for a:

```text
url=
```

parameter.

Conceptually:

```text
Current URL
      ↓
location
      ↓
Regex
      ↓
url parameter
```

---

# 14. Step 4 — Identify the Sink

The navigation sink is:

```javascript
location.href
```

The flow is:

```text
location
      ↓
returnURL[1]
      ↓
location.href
      ↓
Browser Navigation
```

---

# 15. Step 5 — Understand the Regex

The application uses a pattern equivalent to:

```text
/url=https?:\/\/.+/
```

This looks for:

```text
url=http://...
```

or:

```text
url=https://...
```

The important point is that the destination is taken from attacker-controlled URL data.

---

# 16. Step 6 — Construct the Lab URL

The lab walkthrough provides the following structure:

```text
https://YOUR-LAB-ID.web-security-academy.net/post?postId=4&url=https://YOUR-EXPLOIT-SERVER-ID.exploit-server
```

Replace:

```text
YOUR-LAB-ID
```

with the lab identifier.

Replace:

```text
YOUR-EXPLOIT-SERVER-ID
```

with the exploit server identifier.

:contentReference[oaicite:8]{index=8}

---

# 17. Attack Flow

The complete flow is:

```text
Attacker-Controlled URL
        ↓
url=https://EXPLOIT-SERVER
        ↓
location
        ↓
Regex Extraction
        ↓
returnURL[1]
        ↓
location.href
        ↓
Browser Redirect
        ↓
Exploit Server
```

---

# 18. Why the Attack Works

The application assumes that the `url` parameter contains a legitimate destination.

However, the attacker controls:

```text
url
```

Therefore:

```text
Attacker-Controlled Destination
        ↓
Accepted by JavaScript
        ↓
Assigned to location.href
        ↓
External Navigation
```

---

# 19. Source-to-Sink Diagram

```text
                ATTACKER
                   ↓
             Crafted URL
                   ↓
             url parameter
                   ↓
              location
                   ↓
             Regex Parsing
                   ↓
              returnURL
                   ↓
             location.href
                   ↓
          Browser Navigation
                   ↓
            External Domain
```

---

# 20. What Is the Security Impact?

The primary impact of DOM-based open redirection is that an attacker can cause a victim to navigate from a trusted website to an attacker-controlled website.

This can facilitate:

```text
Phishing
Social Engineering
Credential Theft
Malicious Website Delivery
```

The source material specifically highlights phishing as an important impact. :contentReference[oaicite:9]{index=9}

---

# 21. Why Phishing Is More Convincing

An attacker may send a URL beginning with the legitimate application's domain:

```text
https://trusted.example/...
```

The victim initially sees the trusted domain.

The client-side JavaScript then redirects the browser to:

```text
https://attacker.example
```

The initial trusted URL can make the attack appear more credible.

The source material notes that the legitimate domain and valid TLS certificate can increase the credibility of phishing attacks. :contentReference[oaicite:10]{index=10}

---

# 22. Potential Escalation to JavaScript Injection

The source material also notes that if an attacker can control the beginning of the string passed to the redirection API, the vulnerability may potentially be escalated using the:

```text
javascript:
```

pseudo-protocol.

Conceptually:

```text
Open Redirect
      ↓
Attacker Controls Navigation String
      ↓
javascript: URL
      ↓
Potential JavaScript Execution
```

This requires separate confirmation in the specific application and browser context. :contentReference[oaicite:11]{index=11}

---

# 23. Important Distinction

Do not automatically classify every open redirect as DOM-based.

### Server-Side Open Redirect

```text
HTTP Request
      ↓
Server
      ↓
HTTP 3xx
      ↓
Location Header
      ↓
Browser
```

### DOM-Based Open Redirect

```text
HTTP Response
      ↓
Client-Side JavaScript
      ↓
Source
      ↓
Navigation Sink
      ↓
Browser Redirect
```

This lab focuses on the second case.

---

# 24. Common DOM Open-Redirect Sinks

The provided material identifies these important sinks:

```text
location
location.host
location.hostname
location.href
location.pathname
location.search
location.protocol
location.assign()
location.replace()
open()
element.srcdoc
XMLHttpRequest.open()
XMLHttpRequest.send()
jQuery.ajax()
$.ajax()
```

:contentReference[oaicite:12]{index=12}

Not every sink necessarily results in a conventional browser redirect; analyze the exact behavior of the API.

---

# 25. Common Sources

Potential sources include:

```text
document.URL
document.documentURI
document.URLUnencoded
document.baseURI
location
document.referrer
window.name
history.pushState
history.replaceState
localStorage
sessionStorage
IndexedDB
```

The provided material lists these as potential sources for DOM-based taint-flow vulnerabilities. :contentReference[oaicite:13]{index=13}

---

# 26. Testing Methodology

Use this process when testing DOM open redirects.

```text
START
  ↓
Identify Navigation Functionality
  ↓
Find Client-Side JavaScript
  ↓
Identify Navigation Sink
  ↓
Trace Sink Argument
  ↓
Identify Source
  ↓
Confirm Attacker Control
  ↓
Determine URL Validation
  ↓
Construct Controlled Destination
  ↓
Trigger Navigation
  ↓
Confirm External Redirect
  ↓
Assess Impact
```

---

# 27. Step 1 — Identify Navigation Functionality

Look for:

```text
Back
Next
Continue
Return
Redirect
Open
View
Login
Logout
```

Also inspect:

```text
onclick
JavaScript navigation
```

---

# 28. Step 2 — Search JavaScript

Useful searches include:

```text
location
location.href
location.assign
location.replace
window.open
open(
```

Also search:

```text
returnURL
redirect
url
next
return
destination
```

---

# 29. Step 3 — Identify the Source

Determine where the destination comes from.

Potential sources:

```text
location
location.search
location.hash
document.URL
document.referrer
window.name
localStorage
sessionStorage
```

---

# 30. Step 4 — Trace the Value

For example:

```text
location
   ↓
regex
   ↓
returnURL
   ↓
returnURL[1]
   ↓
location.href
```

The goal is to establish:

```text
SOURCE → PROPAGATION → SINK
```

---

# 31. Step 5 — Analyze Validation

Look for validation such as:

```text
startsWith()
endsWith()
includes()
indexOf()
Regex
URL parsing
Hostname allowlist
Protocol allowlist
```

Do not assume that the presence of validation makes the redirect safe.

Determine exactly what values the validation accepts.

---

# 32. Weak Validation Example

Consider:

```javascript
if (url.startsWith("https:")) {
    location = url;
}
```

The application checks only that the URL begins with:

```text
https:
```

This allows an external HTTPS destination.

Conceptually:

```text
https://trusted.example
```

and:

```text
https://attacker.example
```

both satisfy:

```text
startsWith("https:")
```

---

# 33. Another Weak Validation Example

Consider:

```javascript
if (url.includes("trusted.example")) {
    location.href = url;
}
```

The presence of:

```text
trusted.example
```

inside a string does not necessarily prove that the actual destination host is trusted.

Always inspect the parsed URL components when appropriate.

---

# 34. Browser Testing

Use DevTools to inspect the actual behavior.

```text
DevTools
   ↓
Sources
   ↓
Find Navigation Code
   ↓
Set Breakpoint
   ↓
Trigger Functionality
   ↓
Inspect URL Variable
   ↓
Observe location.href
```

---

# 35. Network Testing

Use:

```text
DevTools
   ↓
Network
```

Then trigger the vulnerable navigation.

Determine:

```text
Initial URL
Final URL
Redirect Sequence
Destination Host
```

For DOM-based navigation, pay particular attention to the client-side transition.

---

# 36. Burp Suite Workflow

```text
Burp Suite
      ↓
Open Lab in Burp Browser
      ↓
HTTP History
      ↓
Identify Blog Post
      ↓
Inspect Response
      ↓
Inspect JavaScript
      ↓
Find Navigation Sink
      ↓
Trace URL Parameter
      ↓
Construct Test URL
      ↓
Confirm Redirect
```

---

# 37. Lab Verification

After constructing the lab URL:

```text
Open URL
      ↓
Load Blog Post
      ↓
Trigger / follow Back to Blog
      ↓
JavaScript extracts url
      ↓
location.href is assigned
      ↓
Browser navigates
      ↓
Exploit Server loads
```

The destination should be your exploit server.

---

# 38. Evidence to Capture

Record:

```text
☐ Vulnerable page
☐ Navigation functionality
☐ Source
☐ URL parameter
☐ JavaScript
☐ Regex / validation
☐ Navigation sink
☐ Crafted URL
☐ Final destination
☐ Browser behavior
```

---

# 39. Common Mistakes

## Mistake 1 — Testing Only Server Redirects

A DOM open redirect may not involve:

```text
HTTP 3xx
```

The redirect can happen entirely through JavaScript.

---

## Mistake 2 — Ignoring the Client-Side Code

Always inspect:

```text
location
location.href
location.assign()
location.replace()
```

---

## Mistake 3 — Assuming a Trusted Starting URL Means a Trusted Destination

The initial URL may belong to the legitimate website while JavaScript subsequently redirects to an external domain.

---

## Mistake 4 — Not Tracing the Parameter

Finding:

```text
url=
```

does not prove a vulnerability.

Trace:

```text
url
 ↓
JavaScript
 ↓
navigation sink
```

---

## Mistake 5 — Ignoring Validation

Determine exactly what validation is performed.

Examples:

```text
Regex
startsWith()
endsWith()
includes()
```

can all have different security properties.

---

# 40. Lab Write-Up

Use the following format for your personal lab notes:

```markdown
# Lab 02 — DOM-Based Open Redirection

## Objective

Exploit the DOM-based open redirect and redirect the victim to the exploit server.

## Source

```text
location / url parameter
```

## Sink

```javascript
location.href
```

## Vulnerable Logic

```javascript
[relevant JavaScript]
```

## Taint Flow

```text
Attacker-Controlled URL
      ↓
url parameter
      ↓
location
      ↓
Regex
      ↓
returnURL[1]
      ↓
location.href
      ↓
External Navigation
```

## Exploit URL

```text
https://YOUR-LAB-ID.web-security-academy.net/post?postId=4&url=https://YOUR-EXPLOIT-SERVER-ID.exploit-server
```

## Result

The browser redirects to the attacker-controlled exploit server.

## Impact

The vulnerability can facilitate phishing and other social-engineering attacks.

## Key Lesson

Always trace attacker-controlled URL data into client-side navigation sinks.
```

---

# 41. Quick Revision

### Definition

```text
DOM-Based Open Redirection =
Attacker-Controlled Source
        ↓
Navigation Sink
        ↓
External Redirect
```

### Common Sources

```text
location
location.hash
location.search
document.URL
document.referrer
window.name
```

### Common Sinks

```text
location
location.href
location.assign()
location.replace()
open()
```

---

# 42. Master Testing Checklist

```text
☐ Navigation functionality identified
☐ Client-side JavaScript inspected
☐ Source identified
☐ URL parameter identified
☐ Attacker control confirmed
☐ URL extraction identified
☐ Regex reviewed
☐ startsWith() reviewed
☐ endsWith() reviewed
☐ includes() reviewed
☐ URL parsing reviewed
☐ Navigation sink identified
☐ Crafted external destination tested
☐ Browser redirect confirmed
☐ Final destination confirmed
☐ Phishing impact considered
☐ JavaScript URL escalation considered where applicable
☐ Evidence captured
☐ Finding documented
```

---

# 43. Final Mental Model

```text
                 ATTACKER
                    ↓
             CRAFTED URL
                    ↓
             URL PARAMETER
                    ↓
              DOM SOURCE
                    ↓
          CLIENT-SIDE JAVASCRIPT
                    ↓
             URL PROCESSING
                    ↓
          NAVIGATION SINK
                    ↓
             location.href
                    ↓
           BROWSER NAVIGATION
                    ↓
            EXTERNAL DOMAIN
```

---

# Final Rule

```text
ATTACKER-CONTROLLED URL
        +
CLIENT-SIDE PROCESSING
        +
NAVIGATION SINK
        +
EXTERNAL DESTINATION
        +
REPRODUCIBLE REDIRECTION
        =
DOM-BASED OPEN REDIRECTION
```