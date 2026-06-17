# IDOR Testing Checklist

## Step 1 - Find Identifiers

Look For:

```text
id=
user=
userid=
account=
customer=
document=
invoice=
file=
```

---

## Step 2 - Modify Values

### Numeric IDs

```text
1001
1002
1003
```

---

### Usernames

```text
wiener
carlos
administrator
```

---

### GUIDs

```text
ea7f...
```

↓

```text
another-guid
```

---

## Step 3 - Test Resources

### Profiles

```text
/my-account
```

---

### Files

```text
.pdf
.txt
.csv
.docx
```

---

### API Keys

```text
/api-key
```

---

### Orders

```text
/order
```

---

## Step 4 - Analyze Response

Check:

```text
Status Code
Response Size
Response Data
Error Messages
```

---

## IDOR Mental Model

```text
Object Identifier
        ↓
Change Identifier
        ↓
Observe Response
```

---

## Related Labs

```text
Lab07
Lab08
Lab09
Lab10
Lab11
```