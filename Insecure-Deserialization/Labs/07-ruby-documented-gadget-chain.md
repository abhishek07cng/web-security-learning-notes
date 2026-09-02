# Lab 07 — Ruby Deserialization with a Documented Gadget Chain

## Objective

Adapt a documented Ruby deserialization gadget chain to delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

## Steps

1. Log in.
2. Observe that the session cookie contains a serialized/marshaled Ruby object.
3. Send the request to Burp Repeater.
4. Locate the documented **Universal Deserialisation Gadget for Ruby 2.x-3.x** referenced by the Academy.
5. Copy the payload-generation script.
6. Change the command from:

```text
id
```

to:

```text
rm /home/carlos/morale.txt
```

7. Replace the final output lines with:

```ruby
puts Base64.encode64(payload)
```

8. Run the script.
9. Copy the Base64-encoded serialized object.
10. Replace the session cookie.
11. URL-encode it.
12. Send the request.

## Payload-generation concepts

The Academy example uses RubyGems classes and `Net::WriteAdapter` objects to create a method-invocation chain.

The key idea is to understand how data flows through the existing classes rather than inventing new application code.
