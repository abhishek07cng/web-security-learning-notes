# Clickjacking — Methodology

## Purpose

This methodology provides a structured approach for testing clickjacking during authorized web application security assessments.

The process moves from reconnaissance and framing analysis to proof-of-concept creation, impact validation, and reporting.

---

# 1. Define the Scope

Before testing:

```text
☐ Confirm authorization
☐ Identify allowed application
☐ Identify allowed functionality
☐ Identify test accounts
☐ Avoid unauthorized targets
```

---

# 2. Identify Sensitive Functionality

Start by identifying pages containing meaningful user actions.

Prioritize:

```text
Account Settings
Email Changes
Password Changes
Profile Changes
Account Deletion
Administrative Functions
Security Settings
Other State-Changing Actions
```

Record:

```text
Target:
____________________________

Functionality:
____________________________

Sensitive Action:
____________________________
```

---

# 3. Determine Authentication Requirements

Establish whether the target action requires authentication.

```text
Unauthenticated
      ↓
Test normally
```

or:

```text
Authenticated
      ↓
Determine required victim session
      ↓
Test using authorized account
```

Record:

```text
Authentication Required:
YES / NO

Required Role:
____________________________
```

---

# 4. Inspect Response Headers

Capture the target response using Burp Suite.

Navigate to:

```text
Proxy
  ↓
HTTP history
  ↓
Target response
```

Inspect:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

Specifically search for:

```text
frame-ancestors
```

---

# 5. Analyze X-Frame-Options

Record the configured policy.

Possible values:

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

```http
X-Frame-Options: ALLOW-FROM ...
```

For each policy:

```text
☐ Record value
☐ Understand intended restriction
☐ Test actual browser behavior
```

---

# 6. Analyze CSP frame-ancestors

Search the CSP header for:

```text
frame-ancestors
```

Examples:

```http
Content-Security-Policy: frame-ancestors 'none';
```

```http
Content-Security-Policy: frame-ancestors 'self';
```

or a list of explicitly trusted origins.

Record:

```text
frame-ancestors:
____________________________
```

---

# 7. Test Actual Frameability

Do not rely only on header inspection.

Create an authorized test page:

```html
<!DOCTYPE html>
<html>
<body>

<iframe
    src="https://TARGET"
    width="700"
    height="500">
</iframe>

</body>
</html>
```

Observe:

```text
☐ Target loads
☐ Target remains inside iframe
☐ Browser blocks framing
☐ Target redirects
☐ Target displays an error
```

---

# 8. Decision Point — Can It Be Framed?

```text
Target can be framed?
        │
    ┌───┴───┐
    │       │
   NO      YES
    │       │
    ▼       ▼
Document  Continue
result    testing
```

A frameable page is only a candidate.

```text
Frameable
    ≠
Automatically Vulnerable
```

---

# 9. Identify the Sensitive Control

Locate the control that performs the meaningful action.

Examples:

```text
Button
Form Submission
Link
Checkbox
Administrative Control
```

Record:

```text
Target Control:
____________________________

Expected Action:
____________________________
```

---

# 10. Understand the Request

Use Burp Suite to inspect the action.

Determine:

```text
HTTP Method
Endpoint
Parameters
Cookies
CSRF Token
Response
```

Example workflow:

```text
GET /account
      ↓
User Interaction
      ↓
POST /account/change
      ↓
State Change
```

---

# 11. Review CSRF Protection

Determine whether the action contains:

```text
CSRF Token
SameSite Cookie
Other CSRF Controls
```

Important:

```text
CSRF Protection
      ≠
Clickjacking Protection
```

A legitimate page can contain a valid CSRF token while still being frameable.

---

# 12. Test URL-Prefilled Inputs

Check whether URL parameters influence form fields.

Example:

```text
/my-account?email=test@example.com
```

Determine:

```text
☐ Parameter accepted
☐ Parameter reflected
☐ Form field populated
☐ Value survives inside iframe
☐ Sensitive form can be submitted
```

---

# 13. Inspect Frame-Busting JavaScript

Review client-side JavaScript for:

```text
window.top
window.self
top.location
parent.location
```

Determine:

```text
☐ Frame-busting exists
☐ Target detects iframe
☐ Target attempts top-level navigation
☐ Navigation succeeds
☐ Navigation is restricted
```

---

# 14. Analyze iframe Sandbox Behavior

For the authorized lab technique involving client-side frame-busting, test sandbox behavior where appropriate.

Example:

```html
<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

The specific technique relies on restricting top-level navigation while preserving form functionality.

---

# 15. Check for DOM XSS Where Relevant

If the target contains client-side functionality that may be relevant, inspect:

### Sources

```text
document.URL
document.location
document.referrer
window.name
URL parameters
```

### Sinks

```text
innerHTML
outerHTML
document.write()
eval()
```

Determine:

```text
Source
   ↓
Processing
   ↓
Sink
```

If a user interaction is required, determine whether clickjacking can trigger it.

---

# 16. Determine Attack Type

Classify the candidate.

```text
Single-Step
      ↓
One target interaction
```

```text
Prefilled Form
      ↓
URL parameter
      +
Target interaction
```

```text
Multistep
      ↓
Interaction 1
      ↓
State change
      ↓
Interaction 2
```

```text
DOM XSS Combination
      ↓
Frameable page
      +
DOM XSS
      +
Required interaction
```

---

# 17. Create the Initial PoC

Start with a partially visible iframe.

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

# 18. Align the Target

Use:

```css
opacity: 0.1;
```

during development.

Adjust:

```text
top
left
width
height
z-index
```

until:

```text
Visible Decoy
      ↓
Target Control
```

are correctly aligned.

---

# 19. Test the Interaction

Click the visible decoy.

Determine:

```text
Does the target receive the click?
        │
    ┌───┴───┐
    │       │
   NO      YES
    │       │
    ▼       ▼
Adjust    Continue
position
```

---

# 20. Validate the Sensitive Action

Do not stop after confirming that the target receives a click.

Confirm:

```text
Click
  ↓
Target Control
  ↓
Target Request
  ↓
State Change
```

The complete action must be demonstrated.

---

# 21. Test Multistep Workflows

If multiple interactions are required:

```text
Interaction 1
      ↓
Page State Change
      ↓
Interaction 2
      ↓
Page State Change
      ↓
Final Action
```

Test each step independently.

Document:

```text
Step 1:
____________________________

Step 2:
____________________________

Final Result:
____________________________
```

---

# 22. Hide the Target Interface

Once alignment is confirmed:

```css
opacity: 0.0001;
```

Retest the complete interaction.

The goal is:

```text
Victim sees decoy
      ↓
Victim clicks normally
      ↓
Hidden target receives interaction
      ↓
Sensitive action executes
```

---

# 23. Validate Impact

Confirm:

```text
☐ Victim interaction is required
☐ Victim is authenticated where necessary
☐ Target control receives interaction
☐ Sensitive action executes
☐ Result is reproducible
☐ Security impact is understood
```

---

# 24. Capture Evidence

Record:

```text
Target URL
HTTP Request
HTTP Response
X-Frame-Options
CSP
frame-ancestors
PoC
Target Control
Successful Interaction
Resulting State Change
```

Screenshots can include:

```text
☐ Original target
☐ Partially visible iframe
☐ Aligned overlay
☐ Final PoC
☐ Resulting action
```

---

# 25. Determine Severity

Consider:

```text
Impact
+
Authentication Requirement
+
Sensitivity of Action
+
Required User Interaction
+
Privileges
+
Reproducibility
```

Higher-impact examples may involve:

```text
Account Modification
Security Setting Changes
Administrative Actions
Account Deletion
```

---

# 26. Report Construction

Use the following structure:

```text
Title
  ↓
Affected Endpoint
  ↓
Description
  ↓
Prerequisites
  ↓
Reproduction Steps
  ↓
Proof of Concept
  ↓
Observed Result
  ↓
Security Impact
  ↓
Remediation
```

---

# 27. Remediation

Where framing is not legitimately required:

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

For legitimate external framing, restrict the policy to the minimum required trusted origins.

---

# 28. Complete Methodology

```text
START
  ↓
Define Scope
  ↓
Identify Sensitive Functionality
  ↓
Determine Authentication
  ↓
Inspect Response Headers
  ↓
Check X-Frame-Options
  ↓
Check CSP frame-ancestors
  ↓
Test Actual Frameability
  ↓
Can Target Be Framed?
  │
  ├── NO → Document / Stop
  │
  └── YES
        ↓
Identify Sensitive Control
        ↓
Inspect Request
        ↓
Review CSRF Protection
        ↓
Check URL-Prefilled Inputs
        ↓
Check Frame-Busting
        ↓
Check DOM XSS Where Relevant
        ↓
Identify Single/Multi-Step Workflow
        ↓
Create PoC
        ↓
Align Overlay
        ↓
Test Interaction
        ↓
Sensitive Action Executes?
        │
        ├── NO → Debug
        │
        └── YES
              ↓
        Confirm Impact
              ↓
        Capture Evidence
              ↓
        Document Finding
              ↓
        Recommend Remediation
```

---

# 29. Final Testing Checklist

```text
☐ Scope confirmed
☐ Target identified
☐ Sensitive action identified
☐ Authentication identified
☐ X-Frame-Options checked
☐ CSP checked
☐ frame-ancestors checked
☐ Actual frameability verified
☐ CSRF controls reviewed
☐ URL-prefilled input reviewed
☐ Frame-busting reviewed
☐ DOM XSS reviewed where relevant
☐ Workflow classified
☐ iframe created
☐ Decoy created
☐ Target aligned
☐ Interaction verified
☐ Sensitive action verified
☐ Final PoC tested
☐ Impact confirmed
☐ Evidence captured
☐ Remediation documented
☐ Report prepared
```

---

# Core Methodology

The complete testing model is:

```text
CAN I FRAME IT?
       ↓
IS THERE A SENSITIVE ACTION?
       ↓
DOES THE VICTIM NEED TO INTERACT?
       ↓
CAN I ALIGN THE TARGET CONTROL?
       ↓
DOES THE INTERACTION EXECUTE THE ACTION?
       ↓
WHAT IS THE SECURITY IMPACT?
       ↓
DOCUMENT + REPORT + REMEDIATE
```