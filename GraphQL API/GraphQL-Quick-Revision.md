# GraphQL Quick Revision

### Core concepts

- **Query** → read data
- **Mutation** → change data
- **Subscription** → long-lived real-time updates
- **Schema** → API contract
- **Field** → requested data element
- **Argument** → value supplied to a field
- **Variable** → externalized dynamic input
- **Alias** → multiple instances/operations with unique names
- **Fragment** → reusable field selection
- **Introspection** → schema discovery
- **Suggestion** → possible schema disclosure through errors

### High-value tests

```text
1. Find endpoint
2. __typename
3. Introspection
4. Suggestions
5. IDOR/direct object references
6. Hidden/private fields
7. Sensitive mutations
8. Alias/rate-limit behavior
9. GET/form-urlencoded
10. CSRF
```

### Key defense principles

- Minimize schema exposure.
- Enforce authorization at resolver/field/object level.
- Disable unnecessary introspection.
- Disable schema suggestions.
- Limit query depth/size/aliases/operations.
- Use cost analysis.
- Accept JSON POST for GraphQL operations.
- Validate content type.
- Use secure CSRF tokens.
