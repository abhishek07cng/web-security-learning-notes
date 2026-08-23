# Clickjacking — Key Learnings

## 1. Core Concept

Clickjacking tricks a victim into interacting with a target page that is loaded inside an iframe.

The visible interface belongs to the attacker-controlled page, while the actual interaction occurs with the framed target.

```text
Visible Decoy
      ↓
Victim Click
      ↓
Transparent Target iframe
      ↓
Target Control
      ↓
Unintended Action
```

---

# 2. Framing Is the Fundamental Requirement

A basic clickjacking attack requires the target page to be frameable.

Therefore, the first checks should be:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

especially:

```text
frame-ancestors
```

---

# 3. iframe Is the Core Mechanism

Basic structure:

```html
<iframe src="TARGET"></iframe>
```

The attacker controls the surrounding page and can position other elements around the iframe.

---

# 4. Opacity Helps With Alignment

During testing:

```css
opacity: 0.1;
```

makes the target partially visible.

This helps with positioning.

After alignment:

```css
opacity: 0.0001;
```

can make the iframe effectively invisible.

---

# 5. Positioning Is Critical

The decoy must be aligned with the actual target control.

Important CSS properties include:

```text
position
top
left
width
height
z-index
opacity
```

---

# 6. z-index Controls the Interaction Layer

The iframe should be positioned so that the browser receives the interaction through the target interface.

Conceptually:

```text
Higher Layer
    ↓
Target iframe

Lower Layer
    ↓
Visible decoy
```

The victim sees the decoy but interacts with the target.

---

# 7. Authentication Can Increase Impact

If the victim is already authenticated:

```text
Victim Session
      ↓
Target Page
      ↓
Framed Interface
      ↓
Victim Interaction
      ↓
Authenticated Action
```

This can make state-changing actions particularly significant.

---

# 8. CSRF Tokens Do Not Equal Clickjacking Protection

A key distinction:

```text
CSRF Protection
      ≠
Framing Protection
```

A target page can contain a valid CSRF token and still be vulnerable to clickjacking if it can be framed.

---

# 9. Prefilled Form Inputs

URL parameters can sometimes prepopulate sensitive form fields.

Conceptually:

```text
URL Parameter
      ↓
Form Field
      ↓
Attacker-Controlled Value
      ↓
Clickjacking
      ↓
Form Submission
```

This can reduce the amount of interaction required from the victim.

---

# 10. Frame-Busting Scripts

Client-side JavaScript may attempt to detect framing.

Common concepts include:

```text
window.top
window.self
top.location
parent.location
```

The important lesson is:

```text
Frame-Busting JavaScript
        ≠
Guaranteed Protection
```

---

# 11. iframe Sandbox

The material demonstrates that iframe sandbox restrictions can affect frame-busting behavior.

Example:

```html
<iframe
    src="TARGET"
    sandbox="allow-forms">
</iframe>
```

The relevant concept is restricting top-level navigation while preserving required form functionality.

---

# 12. Clickjacking + DOM XSS

Clickjacking can sometimes be combined with DOM XSS.

The chain is:

```text
Frameable Page
      +
DOM XSS
      +
Required User Interaction
      ↓
Combined Attack
```

The complete chain must be demonstrated.

---

# 13. Multistep Clickjacking

A clickjacking attack can involve multiple interactions.

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

Testing therefore needs to account for page state and interaction order.

---

# 14. Clickbandit

Clickbandit can help generate clickjacking proof-of-concept pages.

Basic workflow:

```text
Target Page
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

Generated PoCs should still be manually reviewed and verified.

---

# 15. X-Frame-Options

Important values:

```http
X-Frame-Options: DENY
```

Prevents framing.

```http
X-Frame-Options: SAMEORIGIN
```

Restricts framing to the same origin.

---

# 16. CSP frame-ancestors

Important policies:

```http
Content-Security-Policy: frame-ancestors 'none';
```

Prevents framing.

```http
Content-Security-Policy: frame-ancestors 'self';
```

Allows same-origin framing.

Specific trusted origins can also be allowed.

---

# 17. Layered Protection

The material discusses using both:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy: frame-ancestors
```

as layered framing protection.

---

# 18. Testing Mental Model

When testing an authorized target, think:

```text
Can I frame it?
       ↓
Is there a sensitive action?
       ↓
Does authentication matter?
       ↓
Can I align the target control?
       ↓
Can I trigger the action?
       ↓
What is the demonstrated impact?
```

---

# 19. Important Headers

Always inspect:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

Then specifically inspect:

```text
frame-ancestors
```

---

# 20. Final Mental Model

The entire topic can be reduced to:

```text
Framing
   +
Positioning
   +
User Interaction
   +
Application State
   ↓
Potential Clickjacking
```

The primary defensive goal is:

```text
Prevent Unauthorized Framing
```

using appropriate framing policies.

---

# Final Checklist

```text
☐ Understand iframe-based framing
☐ Understand transparent overlays
☐ Understand positioning
☐ Understand opacity
☐ Understand z-index
☐ Check authentication
☐ Check CSRF behavior
☐ Check URL-prefilled inputs
☐ Check frame-busting scripts
☐ Understand sandbox behavior
☐ Understand DOM XSS combinations
☐ Understand multistep attacks
☐ Know Clickbandit
☐ Know X-Frame-Options
☐ Know CSP frame-ancestors
☐ Verify complete impact
```