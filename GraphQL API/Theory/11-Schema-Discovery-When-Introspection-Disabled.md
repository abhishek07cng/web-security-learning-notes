# Schema Discovery When Introspection Is Disabled

## Suggestions

Apollo GraphQL can return suggestions when a query is slightly incorrect. Example behavior:

```text
There is no entry for 'productInfo'. Did you mean 'productInformation'?
```

Such errors can disclose valid schema names.

## Clairvoyance

The source describes Clairvoyance as a tool that can automatically recover all or part of a GraphQL schema from suggestions.

## Defense

For Apollo Server v4+, the source identifies:

```text
hideSchemaDetailsFromClientErrors
```

as the option for disabling suggestions.

## Testing principle

If introspection is disabled, do not assume that the schema is undiscoverable. Error messages and suggestions may still reveal useful structure.
