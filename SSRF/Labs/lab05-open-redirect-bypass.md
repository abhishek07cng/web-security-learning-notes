# Lab 05: SSRF with Filter Bypass via Open Redirection

## Lab Description

The stock checker only allows requests to the local application.

However, the application also contains an Open Redirect vulnerability.

Your objective is to combine both vulnerabilities to access an internal administrator interface and delete the user **carlos**.

---

# Objective

- Find an Open Redirect.
- Use it to bypass SSRF protections.
- Delete the user `carlos`.

---

# Vulnerability

The application validates the initial URL but automatically follows HTTP redirects.

An Open Redirect allows the attacker to redirect the backend request to an internal resource.

---

# Finding the Redirect

Browse the application.

Click **Next Product**.

Observe the request:

```text
/product/nextProduct?currentProductId=6&path=...
```

The `path` parameter is copied into the `Location` response header.

This creates an Open Redirect.

---

# Exploit

Create the following URL:

```text
/product/nextProduct?path=http://192.168.0.12:8080/admin
```

Submit it through the `stockApi` parameter.

The backend follows the redirect.

---

## Delete Carlos

Modify the path:

```text
/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos
```

Send the request.

Carlos is deleted.

---

# Attack Flow

```
Attacker

↓

Allowed URL

↓

Open Redirect

↓

Internal Admin Panel

↓

Delete Carlos
```

---

# Why This Works

The application validates only the initial URL.

The backend HTTP client automatically follows the redirect without validating the final destination.

---

# Impact

Attackers can bypass SSRF protections even when direct requests to internal resources are blocked.

---

# Mitigation

- Validate redirected destinations.
- Disable automatic redirects when possible.
- Fix Open Redirect vulnerabilities.
- Restrict outbound requests.

---

# Bug Bounty Methodology

If SSRF appears blocked:

- Search for Open Redirects.
- Test whether redirects are followed.
- Verify whether redirected URLs are revalidated.

---

# Key Learnings

- Open Redirect and SSRF frequently combine into a powerful attack chain.
- Redirect validation is as important as initial URL validation.