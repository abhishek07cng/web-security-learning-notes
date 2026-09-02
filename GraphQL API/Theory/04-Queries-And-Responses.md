# GraphQL Queries

GraphQL queries retrieve data and are roughly comparable to GET operations in REST.

## Components

A query can contain:

1. An operation type.
2. An optional operation name.
3. A selection/data structure.
4. Optional arguments.

Example:

```graphql
query myGetProductQuery {
    getProduct(id: 123) {
        name
        description
    }
}
```

The response mirrors the requested structure.

## Important security point

A type may contain more fields than the client normally requests. Therefore, discovering additional fields can expose functionality or sensitive information that is not visible through the normal UI.

When testing, compare:

**what the frontend requests** vs. **what the schema allows**.
