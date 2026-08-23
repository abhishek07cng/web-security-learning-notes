# Clickjacking — Personal Analysis

## What I Understood

Clickjacking is an interface-based attack where a target page is loaded inside an iframe and the attacker positions a visible decoy over a target control.

The victim believes they are interacting with the visible attacker-controlled element, while the browser actually delivers the interaction to the framed target page.

---

# Attack Model

```text
Attacker-Controlled Page
        ↓
Target Page in iframe
        ↓
Transparent / Nearly Invisible iframe
        ↓
Visible Decoy
        ↓
Victim Click
        ↓
Target Control
        ↓
Unintended Action
```

---

# Important Conditions

From the labs and theory, I understand that a useful clickjacking candidate generally requires:

```text
Frameable Target Page
        +
Sensitive User Action
        +
Victim Authentication
        +
Clickable Target Control
```

If the page cannot be framed, the basic clickjacking technique cannot be constructed.

---

# How I Would Test a Target

My testing process:

```text
1. Identify sensitive endpoint
2. Identify sensitive action
3. Inspect response headers
4. Check X-Frame-Options
5. Check CSP frame-ancestors
6. Test whether page can be framed
7. Identify target control
8. Create iframe
9. Create visible decoy
10. Align target control
11. Test with partial opacity
12. Hide iframe
13. Verify interaction
14. Document result
```

---

# Understanding the iframe

The iframe is the core component of a basic clickjacking attack.

Example:

```html
<iframe src="TARGET"></iframe>
```

The target page is loaded inside the iframe while the attacker controls the surrounding page.

---

# Understanding Opacity

During testing, I should not immediately make the iframe completely invisible.

Instead:

```css
opacity: 0.1;
```

helps me see the target page and correctly align the decoy.

After alignment:

```css
opacity: 0.0001;
```

can be used for the final proof of concept.

---

# Understanding z-index

The iframe and decoy need to be positioned correctly.

Conceptually:

```text
Higher z-index
      ↓
Target iframe
```

```text
Lower z-index
      ↓
Visible decoy
```

The victim sees the decoy while the iframe remains capable of receiving the interaction.

---

# Clickjacking and Authentication

Authentication can make clickjacking significant.

The flow is:

```text
Victim Logs Into Target
        ↓
Victim Opens Attacker Page
        ↓
Target Page Loaded in iframe
        ↓
Victim's Existing Session Used
        ↓
Victim Interaction
        ↓
Authenticated Action
```

The attacker may therefore be able to cause an action within the victim's authenticated session.

---

# Clickjacking and CSRF Tokens

One of the most important lessons is:

```text
CSRF Token
      ≠
Clickjacking Protection
```

A legitimate target page can contain a valid CSRF token while still being vulnerable to clickjacking if the page can be framed.

The victim's browser loads the legitimate page and performs the interaction.

---

# Prefilled Form Input

Another important technique is identifying URL parameters that populate form fields.

Conceptually:

```text
URL Parameter
      ↓
Form Field
      ↓
Attacker-Controlled Initial Value
      ↓
Clickjacking
      ↓
Form Submission
```

This can remove the need for the victim to manually enter the value.

---

# Frame-Busting

Some applications use JavaScript to detect whether they are inside an iframe.

I should inspect for logic involving:

```text
window.top
window.self
top.location
parent.location
```

The important lesson is:

```text
Frame-Busting Script
        ≠
Guaranteed Clickjacking Protection
```

The supplied lab demonstrates that iframe sandbox behavior can affect this type of defense.

---

# Clickjacking + DOM XSS

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

The presence of both vulnerabilities does not automatically prove that the combined attack works.

The complete chain must be demonstrated.

---

# Multistep Clickjacking

Clickjacking does not always involve a single click.

A workflow can require:

```text
Click 1
   ↓
Target Action 1
   ↓
Page State Changes
   ↓
Click 2
   ↓
Target Action 2
```

Therefore, testing should account for:

```text
Interaction Order
Target Position
Page State
Dynamic Elements
```

---

# Clickbandit

Clickbandit can help generate clickjacking proof-of-concept pages.

The workflow is:

```text
Open Target
      ↓
Start Clickbandit
      ↓
Perform Interaction
      ↓
Generate PoC
      ↓
Review Generated HTML
      ↓
Test PoC
```

I should still manually review the generated PoC rather than assuming that generation means the target is vulnerable.

---

# Headers I Should Always Check

For clickjacking testing:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

For CSP, specifically:

```text
frame-ancestors
```

---

# Important Defensive Controls

The main protections covered are:

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

# My Testing Mental Model

I can summarize the entire topic as:

```text
Can I frame it?
       ↓
Is there a sensitive action?
       ↓
Is the victim authenticated?
       ↓
Can I align the target control?
       ↓
Can I trigger the action?
       ↓
What is the impact?
```

---

# Common Mistakes to Avoid

```text
☐ Assuming every frameable page is vulnerable
☐ Ignoring X-Frame-Options
☐ Ignoring CSP
☐ Assuming CSRF tokens prevent clickjacking
☐ Making iframe completely invisible before alignment
☐ Forgetting z-index
☐ Ignoring page state changes
☐ Assuming frame-busting always works
☐ Assuming DOM XSS + clickjacking automatically works
☐ Reporting without confirming the final action
```

---

# Key Learning

The most important concept I learned is that clickjacking is fundamentally about:

```text
Controlling the visual interface
        ↓
While the browser interacts with
a different underlying interface
```

The attack therefore depends heavily on:

```text
Framing
+
Positioning
+
User Interaction
+
Application State
```

The strongest prevention is to restrict framing using appropriate server-side policies such as:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy: frame-ancestors
```