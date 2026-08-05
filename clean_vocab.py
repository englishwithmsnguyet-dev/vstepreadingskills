# -*- coding: utf-8 -*-
import json
import re
import os

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const dangsData = (.*?);\s*(const|let|var|function)', content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    data = json.loads(json_str)
    
    total_removed = 0
    for dang_key, dang_val in data.items():
        if 'practices' in dang_val:
            for i, prac in enumerate(dang_val['practices']):
                passage = prac.get('passage', '').lower()
                question = prac.get('question', '').lower()
                options = ' '.join(prac.get('options', [])).lower()
                all_text = passage + ' ' + question + ' ' + options
                
                explanation = prac.get('explanation', '')
                
                def remove_strange_word(m):
                    global total_removed
                    # m.group(0) is the entire <li>...</li>
                    # m.group(1) is the word
                    word = m.group(1).replace('**', '').lower()
                    if word not in all_text:
                        total_removed += 1
                        return '' # Remove it
                    return m.group(0) # Keep it
                
                # We apply re.sub to explanation
                # We need to make sure we don't accidentally match across multiple lis
                new_explanation = re.sub(r'<li><strong>(.*?)</strong>.*?</li>', remove_strange_word, explanation)
                
                prac['explanation'] = new_explanation

    print(f'Total strange words removed: {total_removed}')
    
    new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
    lines = new_json_str.split('\\n')
    indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
    indented_json_str = '\\n'.join(indented_lines)
    
    new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated file!")
else:
    print("Could not find dangsData")
