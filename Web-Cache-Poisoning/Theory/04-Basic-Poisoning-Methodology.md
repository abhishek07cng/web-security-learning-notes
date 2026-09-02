# Basic Web Cache Poisoning Methodology

## Three core steps

```text
1. Identify and evaluate unkeyed inputs
2. Elicit a harmful response
3. Get the harmful response cached
```

## Step 1 — Identify unkeyed inputs

Test headers, cookies, and other request components that may influence the response without affecting the cache key.

Manual approach:

1. Capture a request.
2. Add a random input.
3. Compare the response.
4. Determine whether the input changes content or behavior.
5. Use Burp Comparer when differences are subtle.

## Param Miner

The source recommends Param Miner for automating header discovery:

```text
Right-click request
      ↓
Guess headers
      ↓
Param Miner tests candidate headers
      ↓
Review Issues / Output
```

## Safety during live testing

The source explicitly warns that unkeyed-input testing can accidentally poison a live cache for real users.

Use a unique cache key/cache buster during discovery so generated responses remain isolated to your testing activity.

## Step 2 — Elicit a harmful response

Determine exactly how the application processes the unkeyed input.

Potentially useful behavior includes:

- direct reflection
- dynamic URL generation
- resource imports
- unsafe processing of generated data

## Step 3 — Get it cached

Caching depends on factors such as:

- file extension
- content type
- route
- status code
- response headers
- cache configuration

Study the cache behavior before attempting the final poison.
