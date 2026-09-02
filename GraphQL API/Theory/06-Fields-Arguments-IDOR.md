# Fields, Arguments, and IDOR

## Fields

Fields are queryable data elements. The response follows the field structure requested by the client.

## Arguments

Arguments provide values for specific fields. The schema defines which arguments a field accepts.

Example:

```graphql
query myGetEmployeeQuery {
    getEmployees(id:1) {
        name {
            firstname
            lastname
        }
    }
}
```

## IDOR / access-control testing

The source explicitly warns that when user-supplied arguments are used to access objects directly, the API can be vulnerable to access-control flaws such as IDOR.

### Testing idea

If a normal request uses:

```text
id = 1
```

test whether another authorized-but-different identifier exposes another user's object.

The key question is not whether the ID exists. It is:

> **Does the current user have authorization to access the object represented by that ID?**

The source's hidden-product example demonstrates this: products 1, 2, and 4 are listed, while product 3 is missing. Querying product 3 directly reveals that it exists and is unlisted.
