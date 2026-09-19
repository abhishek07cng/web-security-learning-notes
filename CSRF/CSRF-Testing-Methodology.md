# CSRF Testing Methodology & Checklist

> Personal reference for Cross-Site Request Forgery (CSRF) testing across bug bounty
> programs and CTFs. Only use these techniques against targets you are explicitly
> authorized to test (in-scope bug bounty assets, your own labs, or CTF instances).

---

## 1. What CSRF Actually Exploits

CSRF abuses the fact that browsers attach cookies to *any* request sent to a domain,
regardless of which page triggered that request. The server has no way to tell "the
user clicked this on my site" apart from "a hidden form on some other site fired this
at me while the user happened to be logged in."

Two things make an endpoint a CSRF candidate:

- It **changes state** (create / update / delete something).
- It authenticates the request using something the browser sends **automatically**
  (session cookies). Bearer tokens sent manually via `Authorization` headers by JS are
  *not* CSRF-able, because an attacker's page can't read or set that header cross-origin
  without CORS explicitly allowing it.

---

## 2. Recon Phase — Finding Candidate Endpoints

Before touching payloads, map the attack surface.

1. **Crawl authenticated flows.** Log in, and click through every settings page,
   profile page, admin panel, and checkout/payment flow while capturing traffic in
   Burp Suite / ZAP.
2. **List every state-changing request.** Grep your Burp history for `POST`, `PUT`,
   `PATCH`, `DELETE`, and any `GET` that looks like it mutates data
   (`?action=delete`, `?id=5&confirm=1`).
3. **Group endpoints by impact**, since this drives severity later:
   - Account takeover surface: email change, password change, password reset request,
     2FA disable, add/change recovery email, add SSH/API key.
   - Financial surface: transfer funds, add payee, change payout address, apply coupon,
     modify cart/checkout.
   - Privilege surface: change role, add admin, invite user, change org ownership.
   - Low-impact surface: theme, notification preferences, display name.
4. **Note the auth mechanism per endpoint.** Cookie-only? Cookie + custom header?
   Bearer token in `Authorization`? Only cookie-only (or cookie + weakly-checked header)
   endpoints are in scope for CSRF.

---

## 3. Step-by-Step: Basic → Advanced

### Level 1 — Baseline checks (do this for every endpoint)

1. Capture the legitimate request in Burp.
2. Check for a CSRF token parameter (`csrf_token`, `authenticity_token`, `_token`,
   `X-CSRF-Token` header, etc.). Note where it lives: body, header, or cookie.
3. Check the `Set-Cookie` response header for the session cookie's `SameSite` value:
   ```
   curl -sv https://target.example/login 2>&1 | grep -i set-cookie
   ```
   - `SameSite=Strict` → cross-site CSRF blocked in modern browsers. Still worth
     checking bypass paths (see Level 3).
   - `SameSite=Lax` → cross-site POST blocked, but **top-level GET navigations still
     send the cookie**. Look for state-changing GET endpoints.
   - `SameSite=None` or missing → no browser-level protection at all.
4. Replay the request with Burp's **Engagement Tools → Generate CSRF PoC**, host it,
   and open it in a browser session that's logged into the target.

### Level 2 — Token bypasses (when a token is present)

Test each of these independently, one variable at a time:

| # | Bypass technique | Why it works |
|---|---|---|
| 1 | Remove the token parameter entirely | Many implementations only validate *if* the field is present |
| 2 | Send an empty token value (`csrf_token=`) | Same root cause — empty is treated as "not checked" |
| 3 | Reuse a token from a different session/account | Token isn't bound to the session, just checked for "does it look like a valid token" |
| 4 | Switch HTTP method (POST → GET, or vice versa) | Token validation middleware sometimes only hooks one verb |
| 5 | Move the token from body to a header, or header to body | Validator reads from one location only |
| 6 | Double-submit cookie pattern: set your own cookie value via XSS/subdomain and match it in the form | Cookie isn't tied to server-side session state |
| 7 | Check if the token is static/predictable across requests (timestamp, sequential, base64 of user id) | Can be forged without ever seeing a valid one |

### Level 3 — SameSite bypasses

- **GET-based state changes under `Lax`.** If `/delete?id=5` or `/unsubscribe?email=x`
  mutates data via GET, an `<img>` or `<iframe>` still fires it under Lax.
- **The Chrome "Lax + POST" 2-minute window.** For ~2 minutes after a cookie is set,
  Chrome sends it on cross-site POSTs to accommodate OAuth/SSO redirects. If you can
  trigger a fresh login/cookie-set on the victim (e.g., via a forced re-auth flow) and
  land your CSRF POST inside that window, Lax offers no protection.
- **Missing `Secure` flag / mixed HTTP-HTTPS.** If the app is reachable over plain
  HTTP anywhere, cookies without `Secure` can be forced onto the wire via network MITM
  or a same-network attacker, sidestepping SameSite entirely in edge cases.
- **Subdomain takeover / XSS on a sibling subdomain** when cookies are scoped with
  `Domain=.example.com` — lets you set the double-submit cookie value from an
  in-scope-cookie-domain origin, which browsers treat as same-site.

### Level 4 — Content-Type tricks for "CSRF-proof" JSON APIs

A dev who requires `Content-Type: application/json` assumes they're safe, because
HTML forms can only natively send:
- `application/x-www-form-urlencoded`
- `multipart/form-data`
- `text/plain`

If the backend parses the body as JSON regardless of the declared Content-Type (common
in lenient frameworks), you can smuggle JSON through a form using `enctype="text/plain"`:

```html
<form id="f" action="https://target.example/api/account" method="POST" enctype="text/plain">
  <input name='{"email":"attacker@evil.example","x":"' value='y"}' type="hidden">
</form>
<script>document.getElementById('f').submit();</script>
```

The submitted body becomes `{"email":"attacker@evil.example","x":"=y"}` — valid JSON
if the extra `x` field is ignored server-side.

If the endpoint is only reachable via `fetch()`/`XHR` with credentials, it additionally
requires a **misconfigured CORS policy** — specifically
`Access-Control-Allow-Origin: <attacker-controlled or reflected origin>` combined with
`Access-Control-Allow-Credentials: true`. Check this explicitly; it's rare but exists.

### Level 5 — Chaining for maximum impact

Single low-impact CSRF findings get triaged low. Chains get triaged high/critical:

- **Email change → Password reset.** CSRF the account's email to one you control,
  then trigger "forgot password" — the reset link lands in your inbox.
- **Add SSH/API key → Full API access**, if the key-management endpoint lacks CSRF
  protection.
- **Disable 2FA → Credential stuffing / session takeover.**
- **Login CSRF.** Force the victim to log into *your* attacker-controlled account
  without realizing it. They then enter sensitive data (payment info, PII, searches)
  believing they're using their own session; you retrieve it by logging back in
  yourself later. Login forms need CSRF protection too, even pre-authentication.
- **Multi-step chains via sequential hidden iframes** with `setTimeout` delays to
  respect app-side rate limits or ordering requirements (e.g., change email, wait 2s,
  request password reset).

---

## 4. PoC Payload Templates

```html
<!-- GET via image tag (works even under Lax on top-level nav; img tag itself is a subresource so verify) -->
<img src="https://target.example/action?param=value" style="display:none">

<!-- GET via top-level navigation (bypasses Lax restrictions on subresources) -->
<meta http-equiv="refresh" content="0; url=https://target.example/action?param=value">

<!-- POST auto-submit, visible redirect -->
<form id="f" action="https://target.example/action" method="POST">
  <input type="hidden" name="param" value="value">
</form>
<script>document.getElementById('f').submit();</script>

<!-- POST into hidden iframe (victim never leaves your page) -->
<iframe name="x" style="display:none"></iframe>
<form id="f" action="https://target.example/action" method="POST" target="x">
  <input type="hidden" name="param" value="value">
</form>
<script>document.getElementById('f').submit();</script>

<!-- Multipart/form-data variant (needed for some file-handling or lenient endpoints) -->
<form id="f" action="https://target.example/action" method="POST" enctype="multipart/form-data">
  <input type="hidden" name="param" value="value">
</form>
<script>document.getElementById('f').submit();</script>
```

For AJAX-only targets with permissive CORS:

```html
<script>
fetch("https://target.example/api/action", {
  method: "POST",
  credentials: "include",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({param: "value"})
});
</script>
```

---

## 5. Verifying With curl Before Building HTML

Faster than spinning up a browser PoC every time:

```bash
# Baseline: does it work with a valid session and no CSRF token?
curl -X POST "https://target.example/account/settings" \
  -H "Cookie: session=<victim_or_your_session>" \
  -d "email=test@example.com&confirm=yes"

# Does a state-changing action work over GET?
curl "https://target.example/account/settings?email=test@example.com&confirm=yes" \
  -H "Cookie: session=<session>"

# Is Origin actually validated?
curl -X POST "https://target.example/account/settings" \
  -H "Cookie: session=<session>" \
  -H "Origin: https://evil.example" \
  -d "email=test@example.com"
```

If the app rejects the forged `Origin`/`Referer` but there's no other check, test
whether stripping the header entirely (some privacy extensions/older browsers do this)
gets treated as "fail open."

---

## 6. Full Checklist

### Recon
- [ ] Full authenticated crawl completed
- [ ] Every state-changing endpoint (POST/PUT/PATCH/DELETE + GET-that-mutates) listed
- [ ] Auth mechanism identified per endpoint (cookie vs bearer token)
- [ ] Endpoints grouped by impact (account/financial/privilege/low)

### Baseline
- [ ] `SameSite` attribute checked on every session cookie
- [ ] `Secure` and `HttpOnly` flags checked
- [ ] CSRF token presence checked per endpoint
- [ ] Token location noted (body / header / cookie)

### Token bypass attempts
- [ ] Token parameter removed entirely
- [ ] Empty token value sent
- [ ] Token reused from a different session
- [ ] HTTP method switched (GET ↔ POST)
- [ ] Token moved between header and body
- [ ] Token checked for predictability (timestamp/sequential/decodable)
- [ ] Double-submit cookie pattern checked for session binding

### SameSite / browser-level
- [ ] GET-based state changes tested under `Lax`
- [ ] Top-level navigation vs subresource behavior tested separately
- [ ] Lax 2-minute POST window considered if a fresh-login flow exists
- [ ] Cookie `Domain` scope checked for subdomain cookie-tossing risk

### Content-Type / CORS
- [ ] Confirmed whether the endpoint strictly rejects non-JSON content types
- [ ] `text/plain` JSON-smuggling form tested if lenient
- [ ] CORS policy checked for `Allow-Origin: *` + `Allow-Credentials: true` combo

### Special cases
- [ ] Login CSRF tested (forcing victim into attacker's account)
- [ ] Multipart/form-data variant tried where urlencoded fails
- [ ] Chained impact explored (email change → password reset, etc.)
- [ ] Origin/Referer header validation tested (missing, spoofed, stripped)

### Reporting (bug bounty / CTF write-up)
- [ ] Vulnerable endpoint + method documented
- [ ] Token behavior documented (absent / bypassed / how)
- [ ] SameSite configuration documented
- [ ] Full working HTML PoC included
- [ ] Screenshot/video of before-and-after account state
- [ ] Impact chain clearly explained, not just the isolated bug
- [ ] Severity justified against the impact table below

---

## 7. Impact / Severity Reference

| Severity | Example endpoint |
|---|---|
| Critical | Fund transfer, admin account creation, API key generation with full scope |
| High | Email change (chains into password reset), role/privilege modification |
| Medium | Password change (still requires current password), profile edits |
| Low | Theme preference, notification settings, display name |
| Informational / Out of scope | Logout, language selection, non-sensitive toggles |

Most programs explicitly list "CSRF on logout" as out of scope — check the policy
before reporting.

---

## 8. Common Pitfalls to Avoid

- Assuming `SameSite=Lax` (the modern default) means CSRF is dead — it only blocks
  cross-site POST, not GET-based state changes.
- Assuming a strict CORS policy means the endpoint can't be CSRF'd — CORS blocks
  *reading* the response, not *sending* the request. Forms don't trigger CORS
  preflights at all.
- Stopping after testing the password-change form. Test every state-changing
  endpoint individually — notification settings, API keys, and invitations are
  frequently unprotected even when the "obvious" forms are locked down.
- Forgetting the social-engineering half of the attack. A convincing pretext
  (shipping notice, calendar invite, doc-share link) matters as much as the payload.
- Treating a single low-severity CSRF as the whole finding when it chains into
  something higher-impact.

---

## 9. Practice Targets

- **DVWA** — dedicated CSRF module at low/medium/high difficulty
- **WebGoat** — CSRF lessons with guided walkthroughs
- **PortSwigger Web Security Academy** — CSRF labs covering token validation flaws,
  SameSite bypasses, and Referer validation flaws
- Spin up your own minimal Flask/Express app with cookie sessions and no CSRF
  middleware to practice payload crafting with full visibility into the server side

---

## 10. References

- OWASP CSRF Prevention Cheat Sheet
- PortSwigger Web Security Academy — CSRF topic
- web.dev — SameSite cookies explained
- Historical case studies: Gmail contact/filter CSRF (2007), Netflix account CSRF
  (2006), ING Direct funds-transfer CSRF (2008) — useful precedent for severity
  arguments in reports
