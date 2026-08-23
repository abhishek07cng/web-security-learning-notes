# Clickbandit

## Overview

Clickbandit is a Burp Suite tool that helps create clickjacking proof-of-concept attacks.

Instead of manually constructing the iframe, overlay, positioning, and interaction sequence from scratch, Clickbandit can record interactions with a target page and generate an HTML proof of concept.

---

# Purpose

Clickbandit is useful for:

```text
Identifying Frameable Pages
        ↓
Recording Target Interaction
        ↓
Generating Clickjacking Overlay
        ↓
Creating Proof of Concept
```

---

# Basic Workflow

```text
Open Target Page
       ↓
Start Clickbandit
       ↓
Perform Target Interaction
       ↓
Stop / Generate PoC
       ↓
Review Generated HTML
       ↓
Host PoC on Exploit Server
```

---

# Starting Clickbandit

In Burp Suite:

```text
Proxy
   ↓
HTTP history
   ↓
Select target request
   ↓
Open in Clickbandit
```

The exact interface may vary depending on the Burp Suite version.

---

# Target Page

The target must be capable of being loaded inside a frame.

Before using Clickbandit, inspect the response for:

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

# Recording an Interaction

Clickbandit allows the tester to interact with the target page.

For example:

```text
Target Page
     ↓
Click account action
     ↓
Clickbandit records interaction
```

The recorded interaction becomes part of the generated proof of concept.

---

# Generated Overlay

The resulting proof of concept can contain:

```text
Target iframe
      +
Transparent overlay
      +
Positioned interaction
```

Conceptually:

```html
<iframe src="TARGET"></iframe>

<div class="decoy">
    Click me
</div>
```

The generated HTML and CSS depend on the interaction being recorded.

---

# Manual vs Clickbandit

## Manual Construction

```text
Create iframe
      ↓
Set dimensions
      ↓
Set opacity
      ↓
Position iframe
      ↓
Create decoy
      ↓
Position decoy
      ↓
Test alignment
```

---

## Clickbandit

```text
Open target
      ↓
Perform interaction
      ↓
Generate PoC
```

Clickbandit can reduce the amount of manual positioning required.

---

# Testing Workflow

```text
1. Identify a potentially vulnerable page.
2. Confirm the page can be framed.
3. Open the page through Clickbandit.
4. Start recording.
5. Perform the target action.
6. Generate the proof of concept.
7. Review the generated HTML.
8. Host it in an authorized environment.
9. Test the generated interaction.
```

---

# Example Target Action

A target page might contain:

```text
Delete account
```

The tester can use Clickbandit to record the interaction.

The generated PoC attempts to place the target interaction beneath an attacker-controlled visible element.

The victim sees something like:

```text
Click me
```

while the actual target control is underneath.

---

# Alignment

Clickbandit assists with positioning, but the generated PoC should still be reviewed.

Check:

```text
Iframe position
Iframe dimensions
Target control position
Decoy position
Opacity
Interaction sequence
```

---

# Opacity

A generated PoC may use an opacity value that makes the target interface effectively invisible.

During debugging, increasing the opacity can help visualize the target.

For example:

```css
opacity: 0.1;
```

After alignment:

```css
opacity: 0.0001;
```

may be used for testing.

---

# Clickbandit and Multistep Actions

Clickbandit can also be useful when the target workflow contains multiple interactions.

Conceptually:

```text
Interaction 1
      ↓
Interaction 2
      ↓
Interaction 3
```

The generated PoC can then be reviewed to determine whether the sequence is reproducible.

---

# Clickbandit and CSRF

Clickbandit can be useful for testing actions protected by CSRF tokens when the legitimate target page is loaded inside the victim's authenticated session.

The important point is:

```text
Target Form
      ↓
Victim Session
      ↓
Valid CSRF Token
      ↓
Victim Interaction
```

The attacker does not necessarily need to know the token.

---

# Clickbandit and DOM XSS

If a target page contains a DOM XSS vulnerability that requires a user interaction, clickjacking can potentially be used as the interaction mechanism.

The workflow can be:

```text
DOM XSS
   +
Frameable Page
   +
Clickbandit
   ↓
Clickjacking PoC
```

The complete attack must still be verified.

---

# Limitations

Clickbandit does not automatically mean that a target is vulnerable.

A generated PoC may fail because:

```text
Page is not frameable
Target changes dynamically
Element positions change
Authentication expires
Browser protections interfere
CSP prevents framing
X-Frame-Options prevents framing
```

Therefore, the generated PoC must be tested.

---

# Verification Checklist

```text
☐ Target page identified
☐ Target page can be framed
☐ X-Frame-Options checked
☐ CSP checked
☐ Clickbandit opened
☐ Target interaction recorded
☐ PoC generated
☐ Generated HTML reviewed
☐ Iframe position verified
☐ Decoy position verified
☐ Target action verified
☐ PoC tested in authorized environment
```

---

# Burp Workflow

```text
Burp Suite
    ↓
Proxy / HTTP History
    ↓
Target Page
    ↓
Clickbandit
    ↓
Record Interaction
    ↓
Generate HTML
    ↓
Review PoC
    ↓
Exploit Server
    ↓
Deliver to Authorized Victim
    ↓
Verify Result
```

---

# Key Takeaways

- Clickbandit is a Burp Suite tool for creating clickjacking proof of concepts.
- It can reduce the manual work involved in positioning overlays.
- The tester records the target interaction and generates an HTML PoC.
- The generated PoC should always be reviewed and tested.
- Clickbandit does not bypass server-side framing protections automatically.
- `X-Frame-Options` and CSP `frame-ancestors` should be checked first.
- Clickbandit can be useful when testing clickjacking involving CSRF-protected actions or interaction-triggered DOM XSS.