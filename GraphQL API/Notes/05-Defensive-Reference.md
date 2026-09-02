# Defensive Reference

## Information disclosure

- Disable introspection for non-public APIs.
- If public introspection is required, review every exposed field.
- Disable suggestions.
- Avoid exposing private user fields.

## Authorization

Do not assume that knowing an ID means the requester is authorized to access the object. Enforce authorization for each relevant object/field/mutation.

## Abuse resistance

Apply limits to:

- query depth
- unique fields
- aliases
- root fields
- query bytes
- computational cost

## CSRF

- JSON-encoded POST only
- strict content-type validation
- secure CSRF token mechanism

These controls are taken directly from the prevention guidance in the supplied source.
