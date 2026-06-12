# DOM XSS in jQuery

## Overview

Modern web applications often use third-party JavaScript libraries.

One of the most common libraries is:

```javascript
jQuery
```

Like native JavaScript functions, jQuery also contains dangerous sinks that can lead to DOM-Based XSS vulnerabilities.

---

# Why jQuery Matters

Applications frequently trust:

```javascript
location.search
location.hash
```

and pass them into jQuery functions.

If user-controlled input reaches a dangerous jQuery sink, JavaScript execution may become possible.

---

# Common jQuery Sinks

## .attr()

Changes HTML attributes.

Example:

```javascript
$('#backLink').attr(
'href',
(new URLSearchParams(location.search))
.get('returnUrl')
);
```

---

## .html()

Writes HTML into the DOM.

Example:

```javascript
$('#output').html(
location.hash
);
```

---

## $() Selector

Creates or selects DOM elements.

Example:

```javascript
$(location.hash);
```

---

# Vulnerable Example

```javascript
$(function() {

$('#backLink').attr(
"href",
(new URLSearchParams(
window.location.search
)).get('returnUrl')
);

});
```

---

URL:

```text
?returnUrl=javascript:alert(document.domain)
```

---

Flow

```text
location.search
        ↓
returnUrl
        ↓
.attr("href")
        ↓
User Clicks Link
        ↓
JavaScript Executes
```

---

# Common Sources

```javascript
location.search
location.hash
document.referrer
postMessage
```

---

# Common Sinks

```javascript
.attr()
.html()
$()
```

---

# Testing Methodology

## Step 1

Identify:

```javascript
location.search
location.hash
```

---

## Step 2

Trace data flow.

---

## Step 3

Determine sink.

---

## Step 4

Craft payload.

---

## Step 5

Verify execution.

---

# Related Labs

- lab06-dom-xss-jquery-href-location-search.md
- lab07-dom-xss-jquery-selector-hashchange.md

---

# Key Takeaways

- jQuery introduces additional DOM XSS sinks.
- .attr() and $() are common targets.
- Source → Sink tracing remains critical.
- Third-party libraries expand attack surface.