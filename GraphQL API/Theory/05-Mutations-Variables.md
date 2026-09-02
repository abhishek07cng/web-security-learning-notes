# Mutations and Variables

## Mutations

Mutations modify data: create, edit, or delete operations.

Example:

```graphql
mutation {
    createProduct(name: "Flamin' Cocktail Glasses", listed: "yes") {
        id
        name
        listed
    }
}
```

The source shows a JSON response containing the newly created product and its requested fields.

## Variables

Variables let values be supplied separately from the GraphQL query.

Example:

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

Variables:

```json
{
    "id": 1
}
```

### Why variables matter during testing

Variables make repeated testing easier. A tester can keep the query structure constant while changing IDs or other input values.

This is particularly relevant to access-control testing because direct object references can be manipulated through variables.
