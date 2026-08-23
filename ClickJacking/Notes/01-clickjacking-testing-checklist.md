# Clickjacking Testing Checklist

## Reconnaissance

```text
☐ Identify sensitive pages
☐ Identify sensitive account actions
☐ Identify administrative actions
☐ Identify forms and buttons
☐ Determine whether authentication is required
```

---

## Frameability

```text
☐ Check X-Frame-Options
☐ Check Content-Security-Policy
☐ Check frame-ancestors
☐ Determine whether the target page can be framed
☐ Test actual iframe behavior
```

---

## Basic Clickjacking

```text
☐ Create target iframe
☐ Create visible decoy
☐ Set iframe position
☐ Set iframe dimensions
☐ Set iframe z-index
☐ Set decoy z-index
☐ Use partial opacity during testing
☐ Align decoy with target control
☐ Verify click reaches target
☐ Reduce iframe opacity
```

---

## Sensitive Actions

Check whether the framed page contains actions such as:

```text
☐ Change email
☐ Change account settings
☐ Delete account
☐ Update profile
☐ Administrative actions
☐ Other sensitive state-changing actions
```

---

## CSRF-Protected Actions

```text
☐ Identify CSRF token
☐ Confirm target action uses CSRF protection
☐ Confirm page can still be framed
☐ Determine whether victim authentication is required
☐ Test interaction through framed target
```

Remember:

```text
CSRF Protection
       ≠
Clickjacking Protection
```

---

## Prefilled Form Input

```text
☐ Identify GET parameters
☐ Test whether parameters populate form fields
☐ Confirm attacker-controlled value is reflected
☐ Load target page with parameter inside iframe
☐ Align target submission button
☐ Verify form submission
```

---

## Frame-Busting Scripts

Inspect client-side JavaScript for:

```text
☐ window.top
☐ window.self
☐ top.location
☐ parent.location
☐ Frame detection logic
☐ Top-level navigation
```

Then determine:

```text
☐ Does the page attempt to escape the iframe?
☐ Does the frame-busting script succeed?
☐ Does iframe sandbox behavior affect it?
```

---

## iframe Sandbox

For authorized testing:

```text
☐ Test sandbox behavior
☐ Understand allow-forms
☐ Check whether allow-top-navigation is absent
☐ Observe top-level navigation behavior
```

Example:

```html
<iframe
    src="TARGET"
    sandbox="allow-forms">
</iframe>
```

---

## DOM XSS Combination

```text
☐ Identify DOM XSS source
☐ Identify DOM XSS sink
☐ Confirm attacker-controlled data reaches sink
☐ Determine required user interaction
☐ Check CSP
☐ Check frameability
☐ Determine whether clickjacking can trigger the vulnerable interaction
```

---

## Multistep Clickjacking

```text
☐ Identify complete workflow
☐ Identify first target control
☐ Identify second target control
☐ Record target state changes
☐ Create multiple decoys
☐ Align first interaction
☐ Align subsequent interactions
☐ Verify interaction order
☐ Test complete sequence
```

---

## Clickbandit

```text
☐ Identify frameable target
☐ Open target with Clickbandit
☐ Record target interaction
☐ Generate PoC
☐ Review generated HTML
☐ Check iframe positioning
☐ Check decoy positioning
☐ Test generated PoC
```

---

## Response Headers

Always inspect:

```http
X-Frame-Options
Content-Security-Policy
```

For CSP, specifically inspect:

```text
frame-ancestors
```

Possible policies include:

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

```http
Content-Security-Policy: frame-ancestors 'none';
```

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

## Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target
  ↓
Inspect Response
  ↓
Check Framing Headers
  ↓
Inspect JavaScript
  ↓
Identify Sensitive Action
  ↓
Create iframe
  ↓
Create Overlay
  ↓
Align Target
  ↓
Test Interaction
  ↓
Document Result
```

---

## Exploit Page Checklist

```text
☐ Correct target URL
☐ Correct iframe dimensions
☐ Correct iframe position
☐ Correct opacity
☐ Correct z-index
☐ Correct decoy position
☐ Correct target action
☐ Correct interaction sequence
```

---

## Final Verification

```text
☐ Target page loads
☐ Target remains framed
☐ Decoy is correctly positioned
☐ Victim interaction reaches target
☐ Sensitive action executes
☐ Impact is confirmed
☐ Evidence is captured
☐ Reproduction steps documented
```

---

# Reporting Checklist

```text
☐ Vulnerable endpoint
☐ Vulnerability type
☐ Attack prerequisites
☐ Authentication requirement
☐ Exploit HTML
☐ Relevant response headers
☐ Reproduction steps
☐ Observed behavior
☐ Security impact
☐ Recommended remediation
```

---

# Remediation

Where appropriate, recommend:

```http
X-Frame-Options: DENY
```

or:

```http
X-Frame-Options: SAMEORIGIN
```

and/or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

Use an appropriate restrictive policy based on the application's legitimate framing requirements.

---

# Final Checklist

```text
☐ Recon complete
☐ Frameability checked
☐ Sensitive action identified
☐ CSRF behavior checked
☐ Prefilled input checked
☐ Frame-busting behavior checked
☐ DOM XSS checked where relevant
☐ Multistep workflow checked
☐ Clickbandit considered
☐ Headers documented
☐ PoC tested
☐ Impact confirmed
☐ Remediation documented
```