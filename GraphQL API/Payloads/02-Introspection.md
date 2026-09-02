# Introspection Reference

## Probe

```graphql
{__schema{queryType{name}}}
```

## Full introspection structure

The supplied source contains the full `IntrospectionQuery`, including the `FullType`, `InputValue`, and `TypeRef` fragments. The complete original source is preserved in `00-Original-PortSwigger-Content.md`.

### Practical testing

- First use the small probe.
- If enabled, use full introspection.
- If the full query fails, remove `onOperation`, `onFragment`, and `onField` as the source suggests.
- Save the resulting schema to Burp's site map.
- Inspect queries, mutations, types, fields, arguments, and descriptions.
