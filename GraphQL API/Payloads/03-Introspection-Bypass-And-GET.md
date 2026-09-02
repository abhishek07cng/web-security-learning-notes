# Introspection Defense Testing

## Newline variation

```graphql
query{__schema
{queryType{name}}}
```

This tests a defense that blocks a literal `__schema{` pattern.

## GET variation

The source demonstrates URL-encoded introspection through a GET request:

```text
GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D
```

## Testing variations from the source

- whitespace after `__schema`
- newline after `__schema`
- commas where syntactically permitted
- GET instead of POST
- POST with `application/x-www-form-urlencoded`

The purpose is to identify whether the defense is parser-aware or merely filtering one textual pattern.
