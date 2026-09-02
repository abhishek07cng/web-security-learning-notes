# Exploiting Unsanitized Arguments

The source recommends testing query arguments as an early GraphQL security check.

A common pattern is:

```graphql
product(id: 3) {
    id
    name
    listed
}
```

If the UI only displays listed products, but direct object lookup accepts an arbitrary ID, an attacker may retrieve hidden/unlisted objects.

## Testing workflow

1. Observe a normal query.
2. Identify object identifiers.
3. Look for sequential or predictable IDs.
4. Identify missing IDs.
5. Query those IDs directly.
6. Compare authorization behavior.
7. Determine whether hidden data becomes accessible.

This is fundamentally an authorization test. The GraphQL syntax is only the delivery mechanism.
