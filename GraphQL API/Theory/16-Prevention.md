# Preventing GraphQL Attacks

## Schema and information exposure

The source recommends:

- disable introspection when the API is not public;
- if introspection must remain enabled for a public API, review the schema for unintended fields;
- disable suggestions;
- do not expose private user fields such as email addresses or user IDs.

## Brute-force and DoS defenses

Use:

- query-depth limits;
- operation limits;
- maximum query-byte limits;
- query cost analysis.

Operation limits can restrict the number of unique fields, aliases, and root fields accepted.

## CSRF defenses

The source recommends:

- accept queries only through JSON-encoded POST;
- validate that the supplied content matches the declared content type;
- use a secure CSRF-token mechanism.

The overall lesson is to enforce security at the API layer rather than relying on frontend behavior.
