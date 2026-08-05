import json
import os

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

if idx_start == -1 or idx_end == -1:
    print("Could not find markers!")
    exit(1)

broken_region = text[idx_start:idx_end]

def escape_field(text_chunk, key, next_key_pattern):
    out = ""
    idx = 0
    while True:
        pos = text_chunk.find(key, idx)
        if pos == -1:
            out += text_chunk[idx:]
            break
        
        quote_pos = text_chunk.find('"', pos + len(key))
        if quote_pos == -1:
            break
        
        start_val = quote_pos + 1
        
        end_val = text_chunk.find(next_key_pattern, start_val)
        if end_val == -1:
            out += text_chunk[idx:start_val]
            idx = start_val
            continue
            
        prefix = text_chunk[idx:start_val]
        content = text_chunk[start_val:end_val]
        
        # Idempotent escaping: first unescape, then escape
        unescaped_content = content.replace('\\"', '"').replace('\\n', '\n')
        escaped_content = unescaped_content.replace('"', '\\"').replace('\n', '\\n')
        
        out += prefix + escaped_content
        idx = end_val
        
    return out

replacements = [
    ('"passage":', '",\n                "question":'),
    ('"question":', '",\n                "options":'),
    ('"explanation":', '",\n                "translationPassage":'),
    ('"explanation":', '"\n            }'),
    ('"translationPassage":', '",\n                "translationQuestion":'),
    ('"translationQuestion":', '",\n                "translationOptions":'),
    ('"theory":', '",\n            "example":'),
    ('"theory":', '",\n            "practices":'),
    ('"title":', '",\n            "icon":'),
    ('"description":', '",\n            "theory":'),
    ('"icon":', '",\n            "description":'),
]

for key, next_key in replacements:
    broken_region = escape_field(broken_region, key, next_key)

fixed_text = text[:idx_start] + broken_region + text[idx_end:]

with open('index_fixed3.html', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Wrote index_fixed3.html")
