# CORS Recon Checklist

## Goal

Quickly identify CORS misconfigurations during reconnaissance.

---

# Step 1 — Identify API Endpoints

Look for endpoints that return sensitive data.

Examples:

```
/api/
/graphql
/account
/profile
/me
/settings
/user
```

---

# Step 2 — Check Response Headers

Look for:

```
Access-Control-Allow-Origin

Access-Control-Allow-Credentials

Access-Control-Allow-Methods

Access-Control-Allow-Headers

Access-Control-Expose-Headers
```

---

# Step 3 — Modify the Origin Header

Test:

```http
Origin: https://evil.com
```

Observe whether the response reflects the supplied origin.

---

# Step 4 — Test Credentials

Check whether:

```http
Access-Control-Allow-Credentials: true
```

is present.

Credentialed responses are usually higher impact.

---

# Step 5 — Test Special Origins

```
Origin: null

Origin: https://trusted.com.evil.com

Origin: https://trusted.com@evil.com

Origin: http://trusted.com
```

---

# Step 6 — Inspect Trusted Origins

Questions:

- Are HTTP origins trusted?
- Are staging domains trusted?
- Are development servers trusted?
- Are subdomains trusted?

---

# Step 7 — Review Sensitive Responses

Look for:

- API Keys
- JWTs
- Personal Information
- Account Details
- Email Addresses
- Internal IDs

---

# Quick Checklist

- Arbitrary Origin Reflection
- Wildcard ACAO
- Credentials Enabled
- Trusted null Origin
- Weak Origin Parsing
- Trusted HTTP Origin
- Sensitive API Responses