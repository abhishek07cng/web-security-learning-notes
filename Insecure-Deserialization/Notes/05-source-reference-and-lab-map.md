# Source Reference and Lab Map

This module preserves the PortSwigger Academy topics represented in the supplied source.

## Topic map

1. What is serialization?
2. What is insecure deserialization?
3. How insecure deserialization arises.
4. Impact.
5. Identification.
6. PHP serialization.
7. Java serialization.
8. Manipulating objects.
9. Modifying attributes.
10. Modifying data types.
11. Application functionality.
12. Magic methods.
13. Arbitrary object injection.
14. Gadget chains.
15. Pre-built gadget chains.
16. URLDNS and JRMPClient.
17. PHPGGC.
18. Documented gadget chains.
19. Custom gadget chains.
20. PHAR deserialization.
21. Memory corruption.
22. Prevention.

## Lab map

| Lab | Main concept |
|---|---|
| 01 | Modify serialized object / privilege escalation |
| 02 | Modify serialized data types / authentication bypass |
| 03 | Dangerous application functionality |
| 04 | Arbitrary object injection in PHP |
| 05 | Java Commons Collections gadget chain |
| 06 | PHP pre-built gadget chain and signed cookie |
| 07 | Ruby documented gadget chain |
| 08 | Custom Java gadget chain / SQL injection |
| 09 | Custom PHP gadget chain |
| 10 | PHAR deserialization |

## Source-derived principle

The central issue is deserialization of user-controllable data. A gadget chain is only one possible mechanism for turning that condition into impact.
