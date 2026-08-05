import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find where the corruption starts (right after dangsData)
idx = text.find('const mockTestPassages =')

good_part = text[:idx]
corrupted_part = text[idx:]

# The corrupted part has literal '\n' and '\"' instead of newlines and quotes.
# We reverse the corruption:
fixed_part = corrupted_part.replace('\\n', '\n').replace('\\"', '"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(good_part + fixed_part)

print("Fixed Javascript corruption!")
