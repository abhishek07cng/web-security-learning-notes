# What Is GraphQL?

## Original content

GraphQL is an API query language designed for efficient client-server communication. It lets a client specify exactly which data should appear in the response, avoiding unnecessarily large REST responses and multiple calls.

A GraphQL service defines a contract between client and server. The client does not need to know where data resides; it sends a query to the GraphQL server, which retrieves the relevant data. GraphQL is platform-agnostic and can communicate with many kinds of data stores.

## Detailed explanation

Think of GraphQL as a structured interface over backend data.

Instead of requesting a fixed REST endpoint such as `/users/1/profile`, a client can ask for the exact fields it needs. This flexibility is useful for development, but it also means that **the schema and the authorization logic become critical security boundaries**.

A vulnerable resolver can expose data even when the frontend does not normally request it.
