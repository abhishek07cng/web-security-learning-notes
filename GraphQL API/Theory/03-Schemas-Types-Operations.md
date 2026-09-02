# GraphQL Schemas, Types, and Operations

## Schema

A GraphQL schema describes the structure of available data. It defines types, fields, arguments, and relationships.

Example from the source:

```graphql
type Product {
    id: ID!
    name: String!
    description: String!
    price: Int
}
```

The `!` means the field is non-nullable/required.

## Three operation types

### Query
Fetches data.

### Mutation
Adds, changes, or removes data.

### Subscription
Creates a long-lived connection so the server can proactively push updates.

The source notes that GraphQL operations generally use one endpoint, commonly with POST, and the operation type/name determines how the request is handled.

## Security significance

The schema is extremely valuable during testing because it can reveal:

- available queries
- mutations
- subscriptions
- fields
- arguments
- types
- relationships
- descriptions
- deprecated fields

An exposed schema can substantially reduce the amount of guesswork required by an attacker.
