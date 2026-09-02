# Rate Limiting and GraphQL Aliases

Traditional rate limiting may count HTTP requests.

GraphQL can place many operations inside one HTTP request through aliases:

```graphql
query {
    isValidDiscount(code: $code) { valid }
    isValidDiscount2: isValidDiscount(code: $code) { valid }
    isValidDiscount3: isValidDiscount(code: $code) { valid }
}
```

If the application limits requests rather than operations, one HTTP request may contain many attempts.

## Defensive controls from the source

- limit query depth
- limit unique fields
- limit aliases
- limit root fields
- limit query size in bytes
- perform cost analysis

These controls also help reduce denial-of-service opportunities caused by expensive GraphQL operations.
