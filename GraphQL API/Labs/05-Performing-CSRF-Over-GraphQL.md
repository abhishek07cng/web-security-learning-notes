# Lab 05 — Performing CSRF Exploits Over GraphQL

**Goal:** Use a CSRF attack to change the viewer's email address.

Credentials supplied by the source:

```text
wiener:peter
```

## Source-based steps

1. Open the lab in Burp's browser.
2. Log in.
3. Enter a new email address.
4. Click **Update email**.
5. Inspect the request in Burp HTTP history.
6. Confirm that the email change is a GraphQL mutation.
7. Send it to Repeater.
8. Modify the mutation to use another email.
9. Send it and confirm that the email changes again.
10. Convert the request to POST with `Content-Type: application/x-www-form-urlencoded`.
11. The source notes that changing the method twice can be used in Repeater for this conversion.
12. Restore the deleted body using URL encoding.
13. The source's body contains `query`, `operationName`, and `variables`.
14. Use **Engagement tools > Generate CSRF PoC**.
15. Modify the generated HTML so that it changes the email to a third value.
16. Copy the HTML.
17. Open the exploit server.
18. Paste the HTML.
19. Deliver the exploit to the victim.

## Why it works

The lab endpoint accepts a browser-forgeable content type and does not require a CSRF token. The authenticated victim's session is therefore usable when the browser submits the malicious form.
