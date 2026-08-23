# Clickjacking — Bug Bounty Checklist

## 1. Target Reconnaissance

```text
☐ Identify the target application
☐ Identify sensitive pages
☐ Identify authenticated functionality
☐ Identify state-changing actions
☐ Identify forms and important buttons
☐ Determine whether the action requires user interaction
```

---

# 2. Authentication

Determine whether the target functionality requires an authenticated session.

```text
☐ Authentication required?
☐ Victim must be logged in?
☐ Action executes within victim's session?
☐ Session state remains active when target is framed?
```

Document:

```text
Authentication:
YES / NO

Required Role:
____________________________
```

---

# 3. Framing Protection

Inspect every relevant response for:

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

Checklist:

```text
☐ X-Frame-Options checked
☐ CSP checked
☐ frame-ancestors checked
☐ Allowed framing origins identified
☐ Actual iframe behavior tested
```

---

# 4. X-Frame-Options

Check for:

```http
X-Frame-Options: DENY
```

```http
X-Frame-Options: SAMEORIGIN
```

```http
X-Frame-Options: ALLOW-FROM ...
```

Record:

```text
Value:
____________________________

Observed Behavior:
____________________________
```

---

# 5. CSP frame-ancestors

Check for:

```http
Content-Security-Policy: frame-ancestors 'none';
```

```http
Content-Security-Policy: frame-ancestors 'self';
```

or explicitly allowed origins.

Record:

```text
frame-ancestors:
____________________________
```

---

# 6. Actual Frameability Test

Do not rely only on the presence or absence of a header.

Test the page in an authorized environment:

```html
<iframe src="https://TARGET"></iframe>
```

Check:

```text
☐ Page loads
☐ Page remains inside iframe
☐ Browser does not block framing
☐ Target controls are accessible
```

---

# 7. Sensitive Functionality

Look for:

```text
☐ Change email
☐ Change password
☐ Change profile information
☐ Account settings
☐ Account deletion
☐ Administrative actions
☐ Permission changes
☐ Other security-sensitive state changes
```

Record:

```text
Target Action:
____________________________
```

---

# 8. State-Changing Action

Prioritize actions that modify application state.

```text
GET /page
     ↓
Display Information
```

is generally less significant than:

```text
POST /change
     ↓
State Change
```

Record:

```text
Action:
____________________________

HTTP Method:
____________________________
```

---

# 9. CSRF Protection

Inspect the target action for:

```text
☐ CSRF token
☐ SameSite cookie behavior
☐ Other CSRF controls
```

Important:

```text
CSRF Protection
      ≠
Clickjacking Protection
```

A frameable page may remain vulnerable to clickjacking even when its form contains a CSRF token.

---

# 10. URL-Prefilled Inputs

Check whether URL parameters populate sensitive form fields.

Example:

```text
/my-account?email=test@example.com
```

Test:

```text
☐ Parameter identified
☐ Parameter accepted
☐ Form field populated
☐ Value remains populated inside iframe
☐ Target action can submit the value
```

Record:

```text
Parameter:
____________________________

Field:
____________________________
```

---

# 11. Frame-Busting JavaScript

Inspect JavaScript for:

```text
☐ window.top
☐ window.self
☐ top.location
☐ parent.location
☐ Frame detection
☐ Top-level navigation
```

Record:

```text
Frame-busting:
YES / NO

Behavior:
____________________________
```

---

# 12. DOM XSS Combination

Where relevant, check for:

```text
☐ DOM XSS source
☐ DOM XSS sink
☐ Required interaction
☐ CSP restrictions
☐ Frameability
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

Only consider the combined attack confirmed when the complete chain works.

---

# 13. Clickbandit

Where appropriate:

```text
☐ Open target with Clickbandit
☐ Record interaction
☐ Generate PoC
☐ Review generated HTML
☐ Verify iframe positioning
☐ Verify target control positioning
☐ Test PoC
```

---

# 14. Basic PoC

Create:

```html
<iframe src="https://TARGET"></iframe>
```

Then add:

```text
☐ Decoy element
☐ Positioning
☐ z-index
☐ Partial opacity
☐ Target alignment
```

---

# 15. Alignment Testing

During development:

```css
opacity: 0.1;
```

Verify:

```text
☐ Target control visible
☐ Decoy visible
☐ Decoy correctly positioned
☐ Click reaches target control
```

Adjust:

```text
top
left
width
height
z-index
```

---

# 16. Final PoC

After alignment:

```css
opacity: 0.0001;
```

Verify:

```text
☐ Target is effectively invisible
☐ Decoy remains visible
☐ Victim can interact naturally
☐ Target receives the interaction
☐ Sensitive action executes
```

---

# 17. Multistep Clickjacking

If the target requires multiple interactions:

```text
☐ Identify Step 1
☐ Identify Step 2
☐ Identify additional steps
☐ Record page state changes
☐ Create multiple decoys
☐ Align each control
☐ Test interaction order
☐ Verify complete sequence
```

Mental model:

```text
Click 1
   ↓
State Change
   ↓
Click 2
   ↓
State Change
   ↓
Final Action
```

---

# 18. Impact Validation

Do not report only:

```text
"Page can be framed."
```

Confirm:

```text
☐ Victim interaction reaches target
☐ Sensitive action is triggered
☐ Action occurs in victim session
☐ Result can be reproduced
☐ Security impact is understood
```

---

# 19. Evidence Collection

Capture:

```text
☐ Target URL
☐ Relevant request
☐ Relevant response
☐ X-Frame-Options
☐ Content-Security-Policy
☐ frame-ancestors
☐ Screenshot of target action
☐ Screenshot of PoC
☐ Successful interaction
☐ Resulting state change
```

---

# 20. Reproduction Steps

Document:

```text
1. Log in to the target application.
2. Navigate to the affected functionality.
3. Identify the sensitive action.
4. Confirm the page can be framed.
5. Create the authorized clickjacking PoC.
6. Align the target control.
7. Trigger the interaction.
8. Observe the resulting action.
```

---

# 21. Severity Considerations

Consider:

```text
Impact
+
Authentication Requirement
+
Required User Interaction
+
Sensitivity of Action
+
Privileges Required
+
Reproducibility
```

Higher-impact examples may involve:

```text
Account Modification
Administrative Actions
Security Setting Changes
Account Deletion
```

---

# 22. Remediation

Where framing is not legitimately required, recommend:

```http
X-Frame-Options: DENY
```

and/or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

For same-origin framing requirements:

```http
X-Frame-Options: SAMEORIGIN
```

and/or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

For trusted external framing, restrict the policy to only the required trusted origins.

---

# 23. Final Bug Bounty Decision

```text
Can target be framed?
        │
   ┌────┴────┐
   │         │
  NO        YES
   │         │
   ▼         ▼
Usually    Sensitive
not        action?
vulnerable    │
              ▼
        User interaction?
              │
              ▼
        Can action execute?
              │
         ┌────┴────┐
         │         │
        NO        YES
         │         │
         ▼         ▼
      Further    Validate
      testing    impact
                    │
                    ▼
               Document
                    │
                    ▼
                Report
```

---

# Final Reporting Template

```text
Title:
Clickjacking on [Affected Functionality]

Affected Endpoint:
____________________________

Authentication:
____________________________

Sensitive Action:
____________________________

X-Frame-Options:
____________________________

Content-Security-Policy:
____________________________

frame-ancestors:
____________________________

Reproduction:
____________________________

Impact:
____________________________

Proof of Concept:
____________________________

Recommended Remediation:
____________________________
```

---

# Final Checklist

```text
☐ Target identified
☐ Sensitive action identified
☐ Authentication requirement identified
☐ X-Frame-Options checked
☐ CSP checked
☐ frame-ancestors checked
☐ Actual frameability tested
☐ CSRF controls reviewed
☐ URL-prefilled input checked
☐ Frame-busting checked
☐ DOM XSS checked where relevant
☐ Multistep workflow checked
☐ PoC created
☐ Alignment verified
☐ Victim interaction verified
☐ Sensitive action confirmed
☐ Impact documented
☐ Evidence captured
☐ Remediation documented
☐ Report prepared
```

---

# Core Bug Bounty Principle

```text
Frameable Page
      ≠
Automatically Vulnerable
```

The finding becomes meaningful when:

```text
Frameable Page
      +
Sensitive Action
      +
Victim Interaction
      +
Successful Unintended Action
      ↓
Demonstrated Clickjacking Impact
```