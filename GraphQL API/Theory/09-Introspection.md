# GraphQL Introspection

Introspection is a built-in GraphQL capability for querying information about the API's schema.

It is useful for IDEs and documentation tools, but it can disclose information useful to an attacker.

## Basic probe

```graphql
{__schema{queryType{name}}}
```

The source recommends disabling introspection in production where the API is not intended for public use.

## Full introspection

A full introspection query can enumerate:

- query type
- mutation type
- subscription type
- types
- fields
- arguments
- interfaces
- enum values
- possible types
- directives
- descriptions
- deprecation information

## Testing interpretation

Introspection is not automatically a vulnerability in every deployment. The security concern is **unnecessary exposure of schema information**, especially private fields or sensitive functionality.

Burp can generate introspection queries and Burp Scanner can report enabled introspection.
