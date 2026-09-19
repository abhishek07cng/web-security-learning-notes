# CSRF — Practical Testing Workflow (CTF / Bug Bounty)

> The actual sequence to run on a box or a live target — ordered cheapest-check-first,
> weirder-bypass-last. Only test targets you're authorized to test.

---

## Step 0: Figure out if CSRF is even possible

Check the auth model in Burp/DevTools before touching payloads:

- Cookie-based session (`Cookie: session=...`) → CSRF is on the table.
- `Authorization: Bearer <token>` set by JS, stored in memory/localStorage → **not
  CSRF-able**. Skip it, don't waste time here.
- Mixed apps (cookie session + custom header like `X-CSRF-Token` required for AJAX) →
  still worth checking — the header requirement is often inconsistently enforced
  across endpoints.

---

## Step 1: Build your target list, not just one endpoint

Log in twice if possible (a "victim" account and an "attacker" account). Walk every
page that changes something — profile, security settings, admin panel, checkout,
invite/team management, API key generation. Dump every `POST`/`PUT`/`PATCH`/`DELETE`
into a list.

Most testers only check password-change and stop. That's exactly why the good
findings sit elsewhere: invite-a-user, add-webhook, change-notification-email,
disable-2FA, add-payment-method.

---

## Step 2: The 30-second triage on each request

For each request:

1. Is there a token field/header? Where does it live (body, header, cookie)?
2. What's `SameSite` on the session cookie?
   ```bash
   curl -sv <login-url> 2>&1 | grep -i set-cookie
   ```
3. Repeat the exact request with the token stripped out entirely. If it still `200`s
   → done, you have CSRF, move straight to the PoC.

This alone catches most real-world CSRF bugs, because most broken implementations
only validate the token **if it's present at all**.

---

## Step 3: If token validation actually works — go deeper

This is where most people stop. Don't.

- **Reuse a token from a second account** in the request. Many apps validate "is this
  a real-looking token" against a global pool, not "does this token belong to this
  session."
- **Swap the token's transport.** If it's normally a POST body param, try sending it
  as a header instead (or vice versa) — some middleware only inspects one location.
- **Decode the token.** Base64/hex decode it. If it's `user_id:timestamp` or similar,
  it's forgeable without ever seeing a legitimate one.
- **Method confusion.** If POST is protected, try the same action via GET, PUT, or a
  method-override header (`X-HTTP-Method-Override: POST`). CSRF middleware is
  sometimes only wired to specific verbs.

---

## Step 4: Attack SameSite even when it's set "correctly"

Most people see `SameSite=Lax` and write the endpoint off. Don't.

- **Hunt for state-changing GET endpoints.** `Lax` still sends cookies on top-level
  navigation. `/api/user/delete-account?confirm=1` as a GET is fully exploitable via
  a plain `<a>` link or `<meta http-equiv="refresh">` — no image/iframe trickery
  needed.
- **The Chrome Lax+POST two-minute window.** If there's any flow that resets the
  session cookie (SSO redirect, "remember me" re-auth, OAuth callback), a POST-based
  CSRF fired within ~2 minutes of that cookie being (re)set still goes through even
  under Lax. Worth testing specifically right after any login/redirect chain.
- **Cookie `Domain` scope.** If `Domain=.target.com` and you find XSS or a
  cookie-setting bug on any subdomain (dev., staging., blog.), you can plant your own
  value for a double-submit cookie and it will be accepted as same-site.

---

## Step 5: When the app "requires JSON" — the trick almost nobody checks

Devs assume `Content-Type: application/json` alone kills CSRF, since HTML forms can't
natively send JSON. Test it anyway:

```html
<form action="https://target/api/action" method="POST" enctype="text/plain">
  <input name='{"amount":"1000","x":"' value='y"}' type="hidden">
</form>
<script>document.forms[0].submit()</script>
```

If the backend parses the body as JSON regardless of the declared Content-Type (very
common — Express with a lenient body-parser, Flask's `request.get_json(force=True)`),
this sails straight through. Check this on every "JSON-only" API before writing it
off.

If the endpoint is fetch-only and never form-submittable, the only remaining path is a
CORS misconfig: `Access-Control-Allow-Origin: <reflects your origin>` combined with
`Access-Control-Allow-Credentials: true`. Check this explicitly — most testers assume
strict CORS means "safe" and never actually verify it.

---

## Step 6: Turn a "meh" finding into a real one — chaining

A single low-impact CSRF (change display name) triages low. The move that separates
good reports from mediocre ones is asking: *"what can I do once this specific field is
under my control?"*

- Email-change CSRF alone = medium/high. Email-change CSRF **chained into "forgot
  password"** = full account takeover = critical.
- Add-API-key / add-SSH-key CSRF often has zero token protection, because devs treat
  it as an "advanced feature" rather than "account settings." Check it specifically.
- **Login CSRF** — force the victim into *your* account, not theirs. They unknowingly
  enter sensitive data into an account you control. Almost nobody checks this,
  including experienced testers, because login forms feel "pre-auth, nothing to
  protect."

---

## Step 7: Verify fast with curl before ever writing HTML

```bash
# Baseline: works without a token at all?
curl -X POST "https://target/action" -H "Cookie: session=<sess>" -d "param=value"

# GET-as-state-change under SameSite=Lax
curl "https://target/action?param=value" -H "Cookie: session=<sess>"

# Is Origin actually validated, or just checked for presence?
curl -X POST "https://target/action" \
  -H "Cookie: session=<sess>" \
  -H "Origin: https://evil.com" \
  -d "param=value"
```

Only once curl confirms it, build the iframe / auto-submit HTML PoC for the report or
CTF flag.

---

## The mental checklist, compressed

```
No token?
  → done, exploit it.
Token present but unbound to session?
  → forge/reuse it.
SameSite set?
  → find a GET endpoint, or hit the Lax+POST window.
JSON-only endpoint?
  → try text/plain smuggling, then check CORS.
Nothing works standalone?
  → chain it into something that actually matters (takeover, funds, privilege).
```

That ordering — cheapest check first, weirder bypass last — is what separates people
who find CSRF fast from people who spend an hour building a PoC for an endpoint that
was never vulnerable in the first place.
