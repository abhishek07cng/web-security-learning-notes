# Obfuscating File Extensions

## Overview

Applications often validate extensions incorrectly.

Attackers may exploit parsing differences.

---

# Common Techniques

## Mixed Case

```text
shell.pHp
```

---

## Double Extension

```text
shell.php.jpg
```

---

## Trailing Dot

```text
shell.php.
```

---

## URL Encoding

```text
shell%2Ephp
```

---

## Null Byte

```text
shell.php%00.jpg
```

---

## Multiple Extensions

```text
shell.p.phphp
```

---

# Why It Works

Different components:

```text
Application
Filesystem
Web Server
```

may interpret filenames differently.

---

# Attack Flow

```text
Filename Validation
        ↓
Parser Difference
        ↓
Malicious Extension Preserved
```

---

# Related Lab

```text
Lab05
```

---

# Bug Bounty Mental Model

Whenever uploads are filtered, ask:

```text
Can Filename Parsing Be Confused?
```

---

# Key Takeaways

- Filename parsing inconsistencies are common.
- Extension filters are frequently bypassed.