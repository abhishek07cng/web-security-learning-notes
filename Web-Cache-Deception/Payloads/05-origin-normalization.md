# Origin Server Normalization Payloads

## Basic Test

```text
/aaa/..%2fmy-account
```

---

## Generic Pattern

```text
/<arbitrary-directory>/..%2f<dynamic-path>
```

Example:

```text
/aaa/..%2fprofile
```

---

## Static Directory Variant

```text
/assets/..%2fprofile
```

Potential interpretation:

```text
Cache:
/assets/..%2fprofile
```

```text
Origin:
/profile
```

---

## Important Encoding

The encoded slash is:

```text
%2f
```

The dot-segment is:

```text
..
```

---

## Alternative Encodings

Where appropriate, test variations such as:

```text
/aaa/..%2fprofile
```

and other encoded forms of the traversal sequence.

---

## Objective

Determine whether the origin:

```text
Decodes the slash
+
Resolves the dot-segment
```

or instead treats the encoded sequence literally.