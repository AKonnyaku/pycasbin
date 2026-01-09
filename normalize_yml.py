import os

filepath = r'f:\Casbin_game\pycasbin\.github\workflows\performance-pr.yml'

with open(filepath, 'rb') as f:
    content = f.read()

# Normalize line endings to LF
content = content.replace(b'\r\n', b'\n')

# Remove trailing blank lines
content = content.strip() + b'\n'

with open(filepath, 'wb') as f:
    f.write(content)

print("Normalized line endings to LF and removed trailing spaces.")
