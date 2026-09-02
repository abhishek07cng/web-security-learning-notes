# Pre-Built Gadget Chains

Manually identifying gadget chains can be difficult and often requires source code.

Pre-built tools can provide known gadget chains for commonly used libraries.

## Java — ysoserial

`ysoserial` provides pre-discovered Java gadget chains.

The general workflow is:

1. Identify a likely library/framework.
2. Select a compatible gadget chain.
3. Provide the desired command/payload.
4. Generate the serialized object.
5. Pass it to the vulnerable deserialization point.

The Academy example uses Apache Commons Collections.

For Java 16+, the source gives:

```bash
java \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED \
 --add-opens=java.base/java.net=ALL-UNNAMED \
 --add-opens=java.base/java.util=ALL-UNNAMED \
 -jar ysoserial-all.jar [payload] '[command]'
```

For Java 15 and below:

```bash
java -jar ysoserial-all.jar [payload] '[command]'
```

## PHP — PHPGGC

PHP applications have equivalent gadget-chain tooling. The source names **PHP Generic Gadget Chains (PHPGGC)**.

## Important limitation

A pre-built chain works only when its assumptions match the target application's libraries/classes.
