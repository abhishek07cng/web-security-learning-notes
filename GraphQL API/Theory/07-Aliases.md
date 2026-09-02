# GraphQL Aliases

GraphQL normally does not allow multiple properties with the same name in one selection. Aliases provide unique names.

Example:

```graphql
query getProductDetails {
    product1: getProduct(id: "1") {
        id
        name
    }
    product2: getProduct(id: "2") {
        id
        name
    }
}
```

## Security significance

Aliases are intended to reduce the number of API calls, but they can also place multiple operations inside a single HTTP request.

The source highlights two important consequences:

- aliases can be used to query multiple objects in one request;
- aliases can be abused to bypass rate limiting when the limiter counts HTTP requests rather than GraphQL operations.

With mutations, aliases can effectively send multiple GraphQL messages in one HTTP request.
