# File Upload Bypass Cheat Sheet

## Extension Tricks

```text
Double Extension
Mixed Case
Null Byte
Trailing Dot
```

---

## Content-Type Bypass

```http
image/jpeg
image/png
```

---

## Polyglot Files

```text
Image
+
Server-side Script
```

---

## Path Traversal

```text
Escape Upload Folder
```

---

## Race Conditions

```text
Execute Before Deletion
```

---

## PUT Uploads

```http
PUT
```

---

# Testing Formula

```text
Extension
        ↓
Content-Type
        ↓
Content
        ↓
Storage
        ↓
Execution
```