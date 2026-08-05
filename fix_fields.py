import re
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the start of the broken region
idx_dang03 = text.find('"dang-03":')
idx_start = text.find('",\n            "example": {', idx_dang03)
print('idx_start:', idx_start)

# Find the end of the broken region
end_marker = 'Hành động này không thể hoàn tác!");'
idx_end = text.find(end_marker, idx_start)
if idx_end != -1:
    idx_end += len(end_marker)
print('idx_end:', idx_end)

if idx_start == -1 or idx_end == -1:
    print("Could not find markers!")
    exit(1)

broken_region = text[idx_start:idx_end]

def escape_content(match):
    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)
    escaped = content.replace('"', '\\"').replace('\n', '\\n')
    return prefix + escaped + suffix

# Fix passage
broken_region = re.sub(r'("passage":\s*")(.*?)(".*?,\s*"question":)', escape_content, broken_region, flags=re.DOTALL)
# Fix question
broken_region = re.sub(r'("question":\s*")(.*?)(".*?,\s*"options":)', escape_content, broken_region, flags=re.DOTALL)
# Fix explanation
broken_region = re.sub(r'("explanation":\s*")(.*?)(".*?(?:\n\s*\}|,\s*"translationPassage":))', escape_content, broken_region, flags=re.DOTALL)
# Fix translationPassage
broken_region = re.sub(r'("translationPassage":\s*")(.*?)(".*?,\s*"translationQuestion":)', escape_content, broken_region, flags=re.DOTALL)
# Fix translationQuestion
broken_region = re.sub(r'("translationQuestion":\s*")(.*?)(".*?,\s*"translationOptions":)', escape_content, broken_region, flags=re.DOTALL)

# Fix theory
broken_region = re.sub(r'("theory":\s*")(.*?)(".*?,\s*(?:"example"|"practices"):)', escape_content, broken_region, flags=re.DOTALL)
# Fix title
broken_region = re.sub(r'("title":\s*")(.*?)(".*?,\s*"icon":)', escape_content, broken_region, flags=re.DOTALL)
# Fix description
broken_region = re.sub(r'("description":\s*")(.*?)(".*?,\s*"theory":)', escape_content, broken_region, flags=re.DOTALL)
# Fix icon
broken_region = re.sub(r'("icon":\s*")(.*?)(".*?,\s*"description":)', escape_content, broken_region, flags=re.DOTALL)

# Let's fix the options strings as well. They look like: "A. ...",
# Since options are inside arrays, we can just find the array and escape strings inside it.
# Actually, the options don't contain quotes or newlines, so they are probably fine.
# But there might be other properties like correctIdx which is an integer and doesn't need escaping.

fixed_text = text[:idx_start] + broken_region + text[idx_end:]

with open('index_fixed2.html', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Wrote index_fixed2.html")
