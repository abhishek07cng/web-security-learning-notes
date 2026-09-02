# Lab 04 — Bypassing GraphQL Brute-Force Protections

**Goal:** Brute-force the login mechanism and sign in as `carlos`.

## Source-based concept

The API rate-limits repeated requests from the same origin. GraphQL aliases allow many login mutations to be placed in one HTTP request.

## Source-provided JavaScript helper

The source provides a browser-console script that converts the authentication lab password list into aliased login operations. Preserve the exact script in `Payloads/05-Alias-Bruteforce-Generator.md` and in `00-Original-PortSwigger-Content.md`.

## Manual procedure

1. Open the lab in Burp's browser.
2. Go to **My account**.
3. Attempt an incorrect login.
4. Inspect the GraphQL login mutation in HTTP history.
5. Send it to Repeater.
6. Repeat incorrect requests until a rate-limit error appears.
7. In the GraphQL tab, construct a single `mutation {}` containing aliased login attempts.
8. Every alias should use username `carlos`.
9. Give each alias a different password from the supplied authentication list.
10. Request `success` for each alias.
11. If modifying the captured request, remove the variable dictionary and `operationName` field as described by the source.
12. Send the request.
13. Search the response for `true`.
14. Identify the password associated with the successful alias.
15. Log in as `carlos`.

Example structure:

```graphql
mutation {
    bruteforce0:login(input:{password: "123456", username: "carlos"}) {
        token
        success
    }
    bruteforce1:login(input:{password: "password", username: "carlos"}) {
        token
        success
    }
}
```

## Security lesson

Rate limiting must account for GraphQL operations, not merely HTTP requests.
