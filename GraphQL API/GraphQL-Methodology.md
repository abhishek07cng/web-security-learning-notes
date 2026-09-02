# GraphQL Testing Methodology

## Phase 1 — Discovery

1. Check common paths:
   - `/graphql`
   - `/api`
   - `/api/graphql`
   - `/graphql/api`
   - `/graphql/graphql`
   - `/v1` variants
2. Send `query{__typename}`.
3. Test GET/POST behavior.
4. Watch for `query not present` errors.

## Phase 2 — Understand normal traffic

Use Burp's browser and HTTP history. Identify:

- query operations
- mutation operations
- variables
- object IDs
- returned fields
- request content type
- authentication/session behavior

## Phase 3 — Schema discovery

1. Probe introspection.
2. Run full introspection if available.
3. Save queries to the site map.
4. Inspect types and fields.
5. If disabled, test suggestions and weak filtering.

## Phase 4 — Authorization

Test:

- sequential IDs
- missing IDs
- other users' IDs
- hidden fields
- administrative queries/mutations
- direct object references

## Phase 5 — Abuse controls

Test:

- aliases
- operation count
- query depth
- query size
- rate limiting
- expensive nested queries

## Phase 6 — CSRF

Check:

- GET acceptance
- form-urlencoded POST acceptance
- content-type validation
- CSRF tokens
- authenticated state-changing mutations

## Phase 7 — Reporting

Record:

- endpoint
- operation
- affected field/mutation
- authorization boundary
- proof of impact
- required authentication
- recommended server-side remediation
