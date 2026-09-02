# Bypassing Weak GraphQL Introspection Defenses

The source describes a common flawed defense: blocking a literal pattern such as `__schema{` with a regular expression.

GraphQL ignores certain whitespace/newline characters, so the query can remain valid while no longer matching the simplistic regex.

Example:

```graphql
query{__schema
{queryType{name}}}
```

Equivalent GET-style probing can also be tested when the endpoint accepts GET:

```text
/graphql?query=...
```

The source also recommends trying:

- spaces
- newlines
- commas
- alternative HTTP methods
- GET
- POST with `application/x-www-form-urlencoded`

### Core lesson

A regex that blocks one textual representation of an introspection query is not the same as actually disabling introspection at the GraphQL parser/security layer.
