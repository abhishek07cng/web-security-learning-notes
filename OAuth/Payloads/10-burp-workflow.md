# Burp Workflow for OAuth Testing

## Step 1

Intercept the authorization request.

```
GET /authorize
```

---

## Step 2

Identify parameters.

```
client_id
redirect_uri
response_type
scope
state
```

---

## Step 3

Send to Repeater.

Modify one parameter at a time:

- redirect_uri
- state
- scope
- response_type

---

## Step 4

Observe callback.

```
code
access_token
id_token
```

---

## Step 5

Inspect token usage.

- /token
- /userinfo
- /me

---

## Step 6

Test callback pages.

Look for:

- Open Redirects
- XSS
- postMessage()
- Directory Traversal

---

## Step 7

Document

- Request
- Response
- Impact
- Root Cause
- Mitigation