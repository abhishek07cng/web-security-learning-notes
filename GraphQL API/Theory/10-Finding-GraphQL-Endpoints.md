# Finding GraphQL Endpoints

## Universal query

The source identifies:

```graphql
query{__typename}
```

as a universal query.

A GraphQL endpoint should return a response containing:

```json
{"data": {"__typename": "query"}}
```

`__typename` is a reserved field available on GraphQL objects.

## Common paths

Try universal queries against common locations such as:

```text
/graphql
/api
/api/graphql
/graphql/api
/graphql/graphql
```

The source also suggests trying `/v1` variants.

## Error-based discovery

A non-GraphQL request may produce a `query not present` or similar error. This can itself be a useful endpoint clue.

## Request methods

Production GraphQL endpoints should ideally accept POST requests using `application/json`. Some implementations also accept:

- GET
- POST with `application/x-www-form-urlencoded`

Testing alternative methods is therefore useful when locating endpoints and when assessing CSRF exposure.
