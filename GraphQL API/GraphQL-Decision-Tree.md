# GraphQL Security Decision Tree

```text
START
 |
 |-- Find endpoint
 |     |-- Common paths?
 |     |-- "query not present"?
 |     |-- __typename works?
 |
 |-- Schema discovery
 |     |-- Introspection enabled?
 |     |       |-- YES -> enumerate schema
 |     |       |-- NO -> test suggestions / weak filtering / alternate methods
 |
 |-- Identify operations
 |     |-- Queries
 |     |-- Mutations
 |     |-- Subscriptions
 |
 |-- Authorization testing
 |     |-- Direct IDs?
 |     |-- Sequential/missing IDs?
 |     |-- Hidden fields?
 |     |-- Admin operations?
 |
 |-- Abuse controls
 |     |-- Aliases?
 |     |-- Rate limiting counts HTTP requests only?
 |     |-- Query depth/size/operation limits?
 |
 |-- CSRF
 |     |-- GET accepted?
 |     |-- form-urlencoded accepted?
 |     |-- content type validated?
 |     |-- CSRF token?
 |
 END -> document impact + remediation
```
