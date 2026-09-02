# GraphQL Bug Bounty Checklist

## Endpoint discovery

- [ ] `/graphql`
- [ ] `/api`
- [ ] `/api/graphql`
- [ ] `/graphql/api`
- [ ] `/graphql/graphql`
- [ ] versioned paths
- [ ] `query{__typename}` tested
- [ ] `query not present` errors reviewed

## Schema

- [ ] introspection probe
- [ ] full introspection
- [ ] descriptions
- [ ] private fields
- [ ] deprecated fields
- [ ] suggestions
- [ ] weak `__schema{` regex tested

## Authorization

- [ ] sequential IDs
- [ ] missing IDs
- [ ] other user IDs
- [ ] hidden/unlisted objects
- [ ] sensitive fields
- [ ] admin mutations
- [ ] delete/update operations

## Input and abuse controls

- [ ] variables
- [ ] aliases
- [ ] rate limiting
- [ ] query depth
- [ ] operation limits
- [ ] query size
- [ ] expensive nested queries

## CSRF

- [ ] JSON POST only
- [ ] content-type validation
- [ ] GET accepted?
- [ ] form-urlencoded accepted?
- [ ] CSRF token present?

## Evidence

- [ ] exact request
- [ ] exact response
- [ ] authorization context
- [ ] impact
- [ ] reproducibility
