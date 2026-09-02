# GraphQL Core Query Reference

## Universal query

```graphql
query{__typename}
```

## Introspection probe

```json
{
  "query": "{__schema{queryType{name}}}"
}
```

## Product query

```graphql
query {
    products {
        id
        name
        listed
    }
}
```

## Direct object lookup

```graphql
query {
    product(id: 3) {
        id
        name
        listed
    }
}
```

## Variable example

```graphql
query getEmployeeWithVariable($id: ID!) {
    getEmployees(id:$id) {
        name {
            firstname
            lastname
        }
    }
}
```

These examples are reproduced from the supplied source and should be used only in authorized labs/testing environments.
