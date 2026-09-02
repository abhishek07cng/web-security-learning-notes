# Fragments and Subscriptions

## Fragments

Fragments are reusable pieces of a query or mutation.

```graphql
fragment productInfo on Product {
    id
    name
    listed
}
```

They can then be included with:

```graphql
query {
    getProduct(id: 1) {
        ...productInfo
        stock
    }
}
```

Changing the fragment changes every operation that uses it.

## Subscriptions

Subscriptions are special operations that create a long-lived connection. They allow the server to push updates to the client.

They are useful for functionality such as chat or collaborative editing and are commonly implemented using WebSockets.

## Security relevance

When testing, do not limit investigation to queries and mutations. If subscriptions are exposed, they represent another operation surface and potentially another authorization boundary.
