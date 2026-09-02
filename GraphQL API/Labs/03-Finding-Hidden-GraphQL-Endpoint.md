# Lab 03 — Finding a Hidden GraphQL Endpoint

**Goal:** Find the hidden endpoint, bypass its weak introspection defense, and delete `carlos`.

## Source-based steps

### 1. Find the endpoint

1. In Repeater, probe common GraphQL paths.
2. Send a GET request to `/api`.
3. Observe a `Query not present` error.
4. Treat this as an endpoint clue.
5. Send:

```text
/api?query=query{__typename}
```

6. Confirm the GraphQL response:

```json
{
  "data": {
    "__typename": "query"
  }
}
```

### 2. Test introspection

1. Send an URL-encoded introspection query.
2. Observe that introspection is initially disallowed.
3. Modify the query so that a newline appears after `__schema`.
4. Resend it.
5. The source explains that a regex blocking `__schema{` can be bypassed by GraphQL-insignificant whitespace.

### 3. Find the deletion mutation

1. Save GraphQL queries to the site map.
2. Find `getUser`.
3. Send it to Repeater.
4. Change the ID until `carlos` is identified; the source gives ID `3`.
5. Find `deleteOrganizationUser` in the schema.
6. Send a mutation using ID `3`.

Example from the source:

```text
/api?query=mutation+%7B%0A%09deleteOrganizationUser%28input%3A%7Bid%3A+3%7D%29+%7B%0A%09%09user+%7B%0A%09%09%09id%0A%09%09%7D%0A%09%7D%0A%7D
```

## Security lesson

Endpoint discovery, schema discovery, weak introspection filtering, direct references, and dangerous mutations can combine into a complete attack path.
