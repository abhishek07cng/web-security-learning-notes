# API Methodology

## Step 1 - Recon

Find:

```text
Endpoints
Methods
Parameters
Documentation
Authentication
```

Sources:

```text
JavaScript
Swagger
OpenAPI
Proxy History
Responses
```

---

## Step 2 - Identify Endpoints

Questions:

```text
What Resources Exist?
What Hidden APIs Exist?
```

---

## Step 3 - Enumerate Methods

Test:

```text
GET
POST
PUT
PATCH
DELETE
OPTIONS
HEAD
```

---

## Step 4 - Explore Parameters

Look For:

```text
Hidden Parameters
JSON Properties
Query Parameters
Path Parameters
```

---

## Step 5 - Test Content Types

Try:

```text
JSON
XML
Form Data
Multipart
```

---

## Step 6 - Search For Hidden Functionality

Questions:

```text
Can Additional Methods Be Used?
Can Extra Properties Be Added?
```

---

## Step 7 - Test Internal APIs

Questions:

```text
Can User Input Influence Backend Requests?
```

Targets:

```text
Search
Password Reset
Profile Update
```

---

## Step 8 - Assess Impact

```text
Privilege Escalation
Account Takeover
Information Disclosure
```

---

# Personal Formula

```text
Endpoint
        ↓
Methods
        ↓
Parameters
        ↓
Hidden Functionality
        ↓
Impact
```