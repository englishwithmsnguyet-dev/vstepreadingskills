# -*- coding: utf-8 -*-
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const dangsData = (.*?);\s*(const|let|var|function)', content, re.DOTALL)
if not match:
    print("Could not find dangsData")
    exit(1)
    
json_str = match.group(1).strip()
data = json.loads(json_str)

# Iterate over all dang-02 practices
for i, prac in enumerate(data['dang-02']['practices']):
    explanation = prac.get('explanation', '')
    
    # 1. Fix the audio button backslashes (e.g. data-word=\"empire\" -> data-word="empire")
    # We replace literal '\"' with '"' inside the explanation string
    explanation = explanation.replace('\\"', '"')
    
    # 2. Remove the yellow "BẢN DỊCH" block (if present)
    # The block looks like: <div style="background: #fffbeb; ... >... BẢN DỊCH ... </div>
    # and it is followed by <div style="background: #f0fdf4; (which is the TỪ VỰNG block)
    # So we can remove anything from <div style="background: #fffbeb; to the closing </div> right before <div style="background: #f0fdf4;
    
    # regex pattern
    pattern = r'<div style="background: #fffbeb;.*?</div>(?=<div style="background: #f0fdf4;)'
    explanation = re.sub(pattern, '', explanation, flags=re.DOTALL)
    
    prac['explanation'] = explanation

new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
# Fix indentation to match existing style
lines = new_json_str.split('\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
indented_json_str = '\n'.join(indented_lines)

new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully fixed audio quotes and removed duplicate translation blocks!")
