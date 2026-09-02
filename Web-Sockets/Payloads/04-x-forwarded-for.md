# X-Forwarded-For

The source demonstrates a design flaw caused by trusting an HTTP header for a security decision.

Lab header:

```http
X-Forwarded-For: 1.1.1.1
```

In the lab this was used to spoof the IP after the connection was banned.
