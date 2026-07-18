# redirect_uri Testing Checklist

## Exact Match

```
https://evil.com
```

---

## Prefix Tests

```
https://trusted.com.evil.com
```

---

## Username Injection

```
https://trusted.com@evil.com
```

---

## Fragment Tests

```
https://trusted.com#evil.com
```

---

## Query Tests

```
https://trusted.com?next=https://evil.com
```

---

## Path Traversal

```
/oauth-callback/../post
```

---

## Duplicate Parameters

```
redirect_uri=A

redirect_uri=B
```

---

## Encoded Variants

```
%2e%2e/

%252e%252e/

%2f

%252f
```

---

## Checklist

- Prefix validation
- Wildcards
- Regex bypass
- Open redirects
- Directory traversal