# Clickjacking — Decision Tree

## Purpose

A practical decision tree for identifying, testing, validating, and documenting potential clickjacking vulnerabilities during authorized security testing.

---

# 1. Start — Identify a Target

```text
Start
  ↓
Identify Web Application
  ↓
Identify Sensitive Page
  ↓
Identify Sensitive Action
```

Look for actions involving:

```text
Account Settings
Email Changes
Password Changes
Profile Changes
Account Deletion
Administrative Actions
Other State-Changing Operations
```

---

# 2. Does the Page Require Authentication?

```text
Does the target require authentication?
          │
     ┌────┴────┐
     │         │
    YES        NO
     │         │
     ▼         ▼
Determine    Continue
victim       testing
session
     │
     └──────────┐
                ▼
          Check Framing
```

If authentication is required, determine whether the action would execute using the victim's authenticated session.

---

# 3. Check X-Frame-Options

Inspect the target response for:

```http
X-Frame-Options
```

### Is it present?

```text
X-Frame-Options?
       │
   ┌───┴───┐
   │       │
  YES      NO
   │       │
   ▼       ▼
Evaluate  Check
value     CSP
```

---

# 4. Evaluate X-Frame-Options

### `DENY`

```http
X-Frame-Options: DENY
```

Decision:

```text
Framing intended to be prevented
        ↓
Test actual browser behavior
        ↓
Document result
```

---

### `SAMEORIGIN`

```http
X-Frame-Options: SAMEORIGIN
```

Decision:

```text
Same-origin framing may be permitted
        ↓
Determine framing origin
        ↓
Check whether attacker origin satisfies policy
```

---

### `ALLOW-FROM`

```http
X-Frame-Options: ALLOW-FROM ...
```

Decision:

```text
Browser support is inconsistent
        ↓
Check CSP
        ↓
Test actual framing behavior
```

---

# 5. Check Content Security Policy

Inspect:

```http
Content-Security-Policy
```

Specifically search for:

```text
frame-ancestors
```

Decision:

```text
CSP present?
      │
  ┌───┴───┐
  │       │
 YES      NO
  │       │
  ▼       ▼
Check    Test
frame-   actual
ancestors framing
```

---

# 6. Evaluate frame-ancestors

### `'none'`

```http
Content-Security-Policy: frame-ancestors 'none';
```

Decision:

```text
Framing intended to be prevented
        ↓
Verify actual browser behavior
        ↓
Document result
```

---

### `'self'`

```http
Content-Security-Policy: frame-ancestors 'self';
```

Decision:

```text
Same-origin framing permitted
        ↓
Determine framing origin
        ↓
Test whether attacker origin is allowed
```

---

### Specific Origin

Example:

```http
Content-Security-Policy: frame-ancestors trusted-origin.example;
```

Decision:

```text
Identify allowed origin
        ↓
Compare with testing origin
        ↓
Determine whether framing is permitted
```

---

# 7. Can the Target Actually Be Framed?

Create an authorized test iframe:

```html
<iframe src="https://TARGET"></iframe>
```

Then determine:

```text
Can target be rendered?
        │
   ┌────┴────┐
   │         │
  NO        YES
   │         │
   ▼         ▼
Stop /    Continue
Document
```

If the page cannot be framed, the basic clickjacking technique cannot proceed.

---

# 8. Is There a Sensitive Interaction?

```text
Sensitive control available?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
No clear   Continue
impact
```

Identify:

```text
Button
Form
Link
Checkbox
Administrative Control
State-Changing Action
```

---

# 9. Does the Action Require User Interaction?

```text
User interaction required?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Clickjacking  Assess
may be        other
relevant      behavior
```

Clickjacking is particularly relevant when the sensitive functionality requires a user interaction.

---

# 10. Check for URL-Prefilled Inputs

Determine whether URL parameters can populate form fields.

Example:

```text
/my-account?email=test@example.com
```

Decision:

```text
Does parameter populate form?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Consider    Continue
prefilled   normal
form        testing
```

Conceptually:

```text
URL Parameter
      ↓
Form Field
      ↓
Clickjacking
      ↓
Submission
```

---

# 11. Check for Frame-Busting JavaScript

Inspect client-side JavaScript for:

```text
window.top
window.self
top.location
parent.location
```

Decision:

```text
Frame-busting present?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Analyze     Continue
behavior
```

Determine whether the target successfully escapes the iframe.

---

# 12. Frame-Busting Behavior

```text
Target attempts to escape?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Analyze     Continue
sandbox /
browser
behavior
```

For the authorized lab technique involving sandbox behavior, the relevant structure is:

```html
<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

The specific lab technique relies on restricting top-level navigation while preserving required form functionality.

---

# 13. Check for DOM XSS

If relevant, inspect:

```text
Client-Side JavaScript
        ↓
Source
        ↓
Processing
        ↓
Sink
```

Potential sources:

```text
document.URL
document.location
document.referrer
window.name
URL parameters
```

Potential sinks:

```text
innerHTML
outerHTML
document.write()
eval()
```

Decision:

```text
DOM XSS present?
       │
   ┌───┴───┐
   │       │
  YES      NO
   │       │
   ▼       ▼
Determine Continue
required  normal
interaction
```

---

# 14. Can Clickjacking Trigger the DOM XSS?

```text
DOM XSS
   +
Required User Interaction
   +
Frameable Page
        │
     ┌──┴──┐
     │     │
    YES    NO
     │     │
     ▼     ▼
Potential  Separate
combined   issues
attack
```

The complete chain must be verified.

---

# 15. Is the Workflow Multistep?

```text
Single interaction?
        │
    ┌───┴───┐
    │       │
   YES      NO
    │       │
    ▼       ▼
Basic      Identify
overlay    all steps
              │
              ▼
       Multistep testing
```

For multistep workflows:

```text
Interaction 1
      ↓
State Change
      ↓
Interaction 2
      ↓
State Change
      ↓
Final Action
```

---

# 16. Create the PoC

Once the target is confirmed to be frameable and a sensitive interaction has been identified:

```text
Create iframe
      ↓
Create decoy
      ↓
Position decoy
      ↓
Use opacity = 0.1
      ↓
Align target control
```

Basic structure:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# 17. Does the Click Reach the Target?

```text
Victim clicks decoy
        ↓
Target receives interaction?
        │
    ┌───┴───┐
    │       │
   YES      NO
    │       │
    ▼       ▼
Continue   Adjust
           position
           / z-index
```

Check:

```text
top
left
width
height
z-index
opacity
```

---

# 18. Does the Sensitive Action Execute?

```text
Target receives click
        ↓
Sensitive action executes?
        │
    ┌───┴───┐
    │       │
   YES      NO
    │       │
    ▼       ▼
Impact     Continue
confirmed  debugging
```

Do not report a clickjacking vulnerability solely because the page is frameable.

Confirm the complete interaction and impact.

---

# 19. Final PoC

After successful alignment:

```css
opacity: 0.0001;
```

Then retest:

```text
Visible Decoy
      ↓
Victim Click
      ↓
Hidden Target Control
      ↓
Sensitive Action
```

---

# 20. Validate the Complete Chain

```text
Frameable
    +
Sensitive Action
    +
Correct Positioning
    +
Victim Interaction
    +
Successful Action
        ↓
Confirmed Clickjacking Impact
```

---

# 21. Document Evidence

Record:

```text
Target URL:
____________________________

Sensitive Action:
____________________________

X-Frame-Options:
____________________________

Content-Security-Policy:
____________________________

frame-ancestors:
____________________________

Authentication Required:
YES / NO

Frameable:
YES / NO

Interaction:
____________________________

Observed Impact:
____________________________
```

---

# 22. Remediation Decision

If unauthorized framing is possible, recommend an appropriate framing policy.

For pages that should never be framed:

```http
X-Frame-Options: DENY
```

and/or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

For same-origin framing:

```http
X-Frame-Options: SAMEORIGIN
```

and/or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

For legitimate external framing, restrict the policy to the minimum trusted origins.

---

# Complete Clickjacking Decision Tree

```text
START
  │
  ▼
Identify Sensitive Page
  │
  ▼
Authentication Required?
  │
  ├── YES → Determine Victim Session
  │
  └── NO
  │
  ▼
Check X-Frame-Options
  │
  ▼
Check CSP frame-ancestors
  │
  ▼
Can Target Be Framed?
  │
  ├── NO → Document / Stop
  │
  └── YES
       │
       ▼
Identify Sensitive Action
       │
       ▼
User Interaction Required?
       │
       ├── NO → Assess Other Attack Paths
       │
       └── YES
            │
            ▼
       Check URL-Prefilled Inputs
            │
            ▼
       Check Frame-Busting JS
            │
            ▼
       Check DOM XSS Where Relevant
            │
            ▼
       Single-Step or Multistep?
            │
       ┌────┴────┐
       │         │
   Single      Multi
       │         │
       ▼         ▼
    Basic     Multiple
    Overlay   Decoys
       │         │
       └────┬────┘
            ▼
      Create iframe
            │
            ▼
       Create decoy
            │
            ▼
       Align target
            │
            ▼
      Test opacity 0.1
            │
            ▼
       Victim click
            │
            ▼
    Action Executes?
        │       │
       NO      YES
        │       │
        ▼       ▼
     Debug    Confirm
              Impact
                │
                ▼
          Document Result
                │
                ▼
           Recommend
           Remediation
```

---

# Final Mental Model

```text
CAN I FRAME IT?
       ↓
IS THERE A SENSITIVE ACTION?
       ↓
DOES IT REQUIRE USER INTERACTION?
       ↓
CAN I ALIGN THE TARGET CONTROL?
       ↓
DOES THE VICTIM'S CLICK TRIGGER IT?
       ↓
IS THE IMPACT CONFIRMED?
       ↓
DOCUMENT + REPORT + REMEDIATE
```

---

# Final Checklist

```text
☐ Sensitive target identified
☐ Authentication requirement identified
☐ X-Frame-Options checked
☐ CSP checked
☐ frame-ancestors checked
☐ Actual framing tested
☐ Sensitive interaction identified
☐ URL-prefilled input checked
☐ Frame-busting behavior checked
☐ DOM XSS checked where relevant
☐ Multistep workflow checked
☐ iframe created
☐ Decoy created
☐ Target aligned
☐ Interaction verified
☐ Sensitive action confirmed
☐ Impact documented
☐ Remediation documented
```