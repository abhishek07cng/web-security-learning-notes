# Lab 08 — Developing a Custom Gadget Chain for Java Deserialization

## Objective

Use leaked source code to construct a gadget chain that extracts the administrator's password, then log in and delete `carlos`.

Credentials:

```text
wiener:peter
```

## Vulnerability discovery

1. Log in.
2. Identify the serialized Java object in the session cookie.
3. Request:

```text
/backup/AccessTokenUser.java
```

4. Navigate to:

```text
/backup
```

5. Identify:

```text
ProductTemplate.java
```

6. Observe that `ProductTemplate.readObject()` passes the `id` attribute into a SQL statement.
7. Write a Java program that creates a `ProductTemplate`, assigns an arbitrary ID, serializes it, and Base64-encodes it.
8. Test with a single apostrophe.
9. Submit the resulting serialized object as the session cookie.
10. Confirm PostgreSQL SQL injection from the error response.

## Extracting the password

The Academy's solution:

1. Enumerates **8 columns**.
2. Determines that columns **4, 5, and 6** do not accept strings.
3. Identifies the `users` table and `password` column.
4. Uses an error-based UNION query:

```sql
' UNION SELECT NULL, NULL, NULL, CAST(password AS numeric), NULL, NULL, NULL, NULL FROM users--
```

5. Extract the administrator password from the error.
6. Log in as administrator.
7. Open the admin panel.
8. Delete `carlos`.

## Hackvertor

Instead of recompiling the Java serializer for every payload, the Academy demonstrates using Hackvertor to automatically update offsets and Base64-encode the serialized object.

The workflow is:

```text
Serialized object template
        ↓
Insert SQL payload
        ↓
Hackvertor updates lengths/offsets
        ↓
Base64 encode
        ↓
Send as session cookie
```
