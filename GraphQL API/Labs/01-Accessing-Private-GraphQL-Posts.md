# Lab 01 — Accessing Private GraphQL Posts

**Goal:** Find the hidden blog post and retrieve its secret password.

## Source-based steps

1. Open the blog page in Burp's browser.
2. Go to **Proxy > HTTP history**.
3. Observe that blog posts are retrieved through a GraphQL query.
4. Notice that blog post IDs are sequential.
5. Observe that ID `3` is missing, suggesting a hidden post.
6. Find the `POST /graphql/v1` request.
7. Send it to Repeater.
8. In Repeater, use **GraphQL > Set introspection query**.
9. Send the introspection query.
10. Inspect the schema and notice that `BlogPost` exposes `postPassword`.
11. Return to the original GraphQL request.
12. Open the GraphQL tab.
13. Change the `id` variable to `3`.
14. Add `postPassword` to the requested fields.
15. Send the request.
16. Copy the returned `postPassword` and submit it.

## What the lab teaches

The vulnerability combines schema discovery with an access-control/data-exposure issue: a field that is not requested by the normal UI is still exposed by the GraphQL schema.
