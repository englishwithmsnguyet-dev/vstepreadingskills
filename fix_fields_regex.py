import re
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index_fixed.html'
# Wait! I need index_fixed.html which is un-mangled.
# But I overwrote index_fixed.html into index.html!
# So index.html is the un-mangled one! Wait! In index.html, dang-04 theory is already escaped by update_dang_04_theory.py.
file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the start of the broken region
idx_dang03 = text.find('"dang-03":')
idx_start = text.find('",\n            "example": {', idx_dang03)

# Find the end of the broken region
end_marker = 'Hành động này không thể hoàn tác!");'
idx_end = text.find(end_marker, idx_start)
if idx_end != -1:
    idx_end += len(end_marker)

broken_region = text[idx_start:idx_end]

def escape_match(match):
    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)
    
    # First, unescape to make it idempotent
    unescaped = content.replace('\\"', '"').replace('\\n', '\n')
    # Then escape
    escaped = unescaped.replace('"', '\\"').replace('\n', '\\n')
    
    return prefix + escaped + suffix

# Match all string values!
# key: "[a-zA-Z0-9_]+"
# prefix: "key":\s*"
# content: [\s\S]*?
# suffix: "\s*(?:,\s*"[a-zA-Z0-9_]+":|\}|\])
pattern = r'("[a-zA-Z0-9_]+":\s*")([\s\S]*?)("(?:\s*,\s*"[a-zA-Z0-9_]+":|\s*\}|\s*\]))'

# We use re.sub
# But wait, since suffix includes the next key, if we replace it, we might consume the next key and prevent overlapping matches!
# To prevent consuming the next key, we can use positive lookahead for the next key!
pattern = r'("[a-zA-Z0-9_]+":\s*")([\s\S]*?)("(?=\s*,\s*"[a-zA-Z0-9_]+":|\s*\}|\s*\]))'

def escape_match_lookahead(match):
    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)
    
    unescaped = content.replace('\\"', '"').replace('\\n', '\n')
    escaped = unescaped.replace('"', '\\"').replace('\n', '\\n')
    
    return prefix + escaped + suffix

fixed_region = re.sub(pattern, escape_match_lookahead, broken_region)

# Wait! We ALSO need to fix string values inside arrays!
# Like "options": [\n "A. ...",\n "B. ..."\n]
# A string in an array:
# prefix: (\[\s*|,\s*)"
# content: [\s\S]*?
# suffix: "(?=\s*,|\s*\])
array_pattern = r'((?:\[|,)\s*")([\s\S]*?)("(?=\s*,|\s*\]))'

fixed_region = re.sub(array_pattern, escape_match_lookahead, fixed_region)

fixed_text = text[:idx_start] + fixed_region + text[idx_end:]

with open('index_fixed4.html', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Wrote index_fixed4.html")
