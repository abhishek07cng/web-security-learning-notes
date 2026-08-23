# Clickjacking — Quick Revision

## 1. Definition

Clickjacking is an attack where an attacker places a target page inside an iframe and overlays a deceptive interface so that a victim's click is delivered to an unintended target control.

```text
Visible Decoy
      ↓
Victim Click
      ↓
Target iframe
      ↓
Target Control
      ↓
Unintended Action
```

---

# 2. Core Requirement

Remember:

```text
Frameable Page
      +
Sensitive Action
      +
User Interaction
      ↓
Potential Clickjacking
```

A page being frameable alone does not prove a vulnerability.

---

# 3. First Things to Check

Always inspect:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

Specifically:

```text
frame-ancestors
```

---

# 4. X-Frame-Options

### DENY

```http
X-Frame-Options: DENY
```

Intended to prevent framing.

### SAMEORIGIN

```http
X-Frame-Options: SAMEORIGIN
```

Restricts framing to the same origin.

### ALLOW-FROM

```http
X-Frame-Options: ALLOW-FROM https://example.com
```

Historically intended to allow a specified origin; browser support is inconsistent.

---

# 5. CSP frame-ancestors

### Block all framing

```http
Content-Security-Policy: frame-ancestors 'none';
```

### Same-origin framing

```http
Content-Security-Policy: frame-ancestors 'self';
```

### Specific origin

```http
Content-Security-Policy: frame-ancestors trusted-origin.example;
```

---

# 6. Basic iframe

```html
<iframe src="https://TARGET"></iframe>
```

---

# 7. Basic PoC

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

# 8. Alignment

During testing:

```css
opacity: 0.1;
```

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
Decoy
  ↓
Target Control
```

is correctly aligned.

---

# 9. Final Visibility

After successful alignment:

```css
opacity: 0.0001;
```

---

# 10. CSRF + Clickjacking

Important:

```text
CSRF Token
    ≠
Clickjacking Protection
```

A legitimate page can contain a valid CSRF token while still being vulnerable to clickjacking if it can be framed.

---

# 11. Prefilled Form

Check whether URL parameters populate sensitive fields.

Example:

```text
/my-account?email=test@example.com
```

Concept:

```text
URL Parameter
      ↓
Form Field
      ↓
Clickjacking
      ↓
Form Submission
```

---

# 12. Frame-Busting

Look for:

```text
window.top
window.self
top.location
parent.location
```

Concept:

```text
Page Detects iframe
      ↓
Attempts Top-Level Navigation
```

Frame-busting JavaScript should not be treated as equivalent to server-side framing policy.

---

# 13. iframe Sandbox

For the authorized lab technique:

```html
<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

The technique relies on restricting top-level navigation while preserving required form functionality.

---

# 14. DOM XSS + Clickjacking

Possible chain:

```text
Frameable Page
      +
DOM XSS
      +
Required User Interaction
      ↓
Combined Attack
```

Check:

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

---

# 15. Multistep Clickjacking

A workflow can require multiple clicks:

```text
Click 1
   ↓
Action 1
   ↓
Page State Changes
   ↓
Click 2
   ↓
Action 2
```

Important:

```text
Interaction Order
Page State
Target Position
Dynamic Elements
```

---

# 16. Clickbandit

Clickbandit can help generate clickjacking PoCs.

```text
Open Target
    ↓
Clickbandit
    ↓
Record Interaction
    ↓
Generate PoC
    ↓
Review
    ↓
Test
```

A generated PoC still needs verification.

---

# 17. Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target
  ↓
Inspect Response
  ↓
Check X-Frame-Options
  ↓
Check CSP
  ↓
Check frame-ancestors
  ↓
Inspect JavaScript
  ↓
Identify Sensitive Action
  ↓
Create PoC
  ↓
Align Target
  ↓
Verify Interaction
```

---

# 18. Testing Methodology

```text
1. Confirm authorization
2. Identify sensitive functionality
3. Determine authentication requirements
4. Inspect framing headers
5. Test actual frameability
6. Identify sensitive control
7. Review CSRF protection
8. Check URL-prefilled inputs
9. Check frame-busting behavior
10. Check DOM XSS where relevant
11. Identify single/multistep workflow
12. Create iframe
13. Create decoy
14. Align target
15. Test interaction
16. Confirm sensitive action
17. Document impact
18. Recommend remediation
```

---

# 19. What Makes a Strong Finding?

Do not report only:

```text
"The page can be framed."
```

A stronger finding demonstrates:

```text
Frameable Page
      +
Sensitive Action
      +
Victim Interaction
      +
Successful Unintended Action
```

---

# 20. Impact

Consider:

```text
Account Modification
Security Setting Changes
Administrative Actions
Account Deletion
Other Sensitive State Changes
```

Impact depends on:

```text
Sensitivity
Authentication
Required Privileges
User Interaction
Reproducibility
```

---

# 21. Evidence

Capture:

```text
☐ Target URL
☐ Relevant request
☐ Relevant response
☐ X-Frame-Options
☐ CSP
☐ frame-ancestors
☐ PoC
☐ Target control
☐ Successful interaction
☐ Resulting state change
```

---

# 22. Main Defenses

If framing is not required:

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

For trusted external framing, allow only the required trusted origins.

---

# 23. One-Minute Decision Tree

```text
Can I frame the page?
        │
        ├── NO → Document / Stop
        │
        └── YES
             ↓
     Sensitive action?
             │
        ├────┴────┐
        NO        YES
        │          │
        ▼          ▼
     Usually   User interaction?
     low value      │
               ┌────┴────┐
               NO        YES
                │          │
                ▼          ▼
             Assess     Create PoC
             other         │
             paths         ▼
                       Align target
                            │
                            ▼
                       Victim click
                            │
                            ▼
                       Action executes?
                         │       │
                        NO      YES
                         │       │
                         ▼       ▼
                       Debug   Confirm
                               Impact
```

---

# 24. Key Terms

```text
Clickjacking
iframe
Overlay
Decoy
X-Frame-Options
CSP
frame-ancestors
CSRF Token
Frame-Busting
iframe Sandbox
Clickbandit
DOM XSS
Multistep Clickjacking
```

---

# 25. Final Mental Model

```text
CAN I FRAME IT?
       ↓
IS THERE A SENSITIVE ACTION?
       ↓
DOES THE VICTIM NEED TO INTERACT?
       ↓
CAN I ALIGN THE TARGET?
       ↓
DOES THE ACTION EXECUTE?
       ↓
IS IMPACT CONFIRMED?
       ↓
DOCUMENT + REPORT + REMEDIATE
```

---

# Final Revision Checklist

```text
☐ Know what clickjacking is
☐ Know iframe mechanics
☐ Know opacity and positioning
☐ Know z-index
☐ Know X-Frame-Options
☐ Know CSP frame-ancestors
☐ Know CSRF ≠ clickjacking protection
☐ Know prefilled form technique
☐ Know frame-busting
☐ Know sandbox behavior
☐ Know DOM XSS combination
☐ Know multistep clickjacking
☐ Know Clickbandit
☐ Know Burp workflow
☐ Know impact validation
☐ Know remediation
```