# Lab 02 — Accidental Exposure of Private GraphQL Fields

**Goal:** Obtain the administrator's credentials and delete `carlos`.

## Source-based steps

1. Open the lab and select **My account**.
2. Attempt to log in.
3. In Burp HTTP history, observe that login is a GraphQL mutation.
4. Send the login request to Repeater.
5. Use **GraphQL > Set introspection query**.
6. Send it.
7. Save the GraphQL queries to the site map.
8. Inspect the discovered queries.
9. Identify `getUser`.
10. Notice that it returns a user's username and password.
11. Notice that the query accepts a direct ID.
12. Send `getUser` to Repeater.
13. Test ID values.
14. The source identifies administrator ID `1`.
15. Retrieve the administrator credentials.
16. Log in as administrator.
17. Open the Admin panel.
18. Delete `carlos`.

## Security lesson

A GraphQL schema can accidentally expose sensitive fields. Direct object references then make the exposure worse if authorization is not enforced per object and field.
