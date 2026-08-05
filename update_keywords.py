# -*- coding: utf-8 -*-
import os
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update JS logic
js_target = """    // 2. Highlight quotes safely (using string literal for the span to avoid any escaping issues)
    res = res.replace(/'([^']+)'/g, '\\'<span style="color: #e11d48; font-weight: 800; background: #ffe4e6; padding: 2px 6px; border-radius: 6px; margin: 0 2px;">$1</span>\\'');
    res = hideTags(res); // Hide the span tags injected by the first replace to prevent the next replace from matching its style attributes
    res = res.replace(/"([^"]+)"/g, '\\"<span style="color: #e11d48; font-weight: 800; background: #ffe4e6; padding: 2px 6px; border-radius: 6px; margin: 0 2px;">$1</span>\\"');
    
    // 3. Hide the newly injected HTML tags
    res = hideTags(res);"""

js_replacement = """    // 2. Highlight quotes safely (using string literal for the span to avoid any escaping issues)
    res = res.replace(/'([^']+)'/g, '\\'<span style="color: #e11d48; font-weight: 800; background: #ffe4e6; padding: 2px 6px; border-radius: 6px; margin: 0 2px;">$1</span>\\'');
    res = hideTags(res); // Hide the span tags injected by the first replace to prevent the next replace from matching its style attributes
    res = res.replace(/"([^"]+)"/g, '\\"<span style="color: #e11d48; font-weight: 800; background: #ffe4e6; padding: 2px 6px; border-radius: 6px; margin: 0 2px;">$1</span>\\"');
    
    res = hideTags(res);
    
    // 2.5 Highlight specific non-changeable keywords using markdown **bold** syntax
    res = res.replace(/\\*\\*([^\\*]+)\\*\\*/g, '<span style="color: #059669; font-weight: 800; background: #d1fae5; padding: 2px 6px; border-radius: 6px; margin: 0 2px;">$1</span>');

    // 3. Hide the newly injected HTML tags
    res = hideTags(res);"""

if js_target in content:
    content = content.replace(js_target, js_replacement)
    print("Successfully updated JS highlightQuestionKeywords.")
else:
    print("Could not find JS target.")

# 2. Update JSON Data for dang-02
match = re.search(r'const dangsData = (.*?);\s*(const|let|var|function)', content, re.DOTALL)
if match:
    json_str = match.group(1).strip()
    try:
        data = json.loads(json_str)
        dang_02 = data.get('dang-02', {})
        practices = dang_02.get('practices', [])
        
        updates = {
            0: "What is the main reason for deforestation in the **Amazon rainforest**?",
            1: "What was likely the cause of **Marie Curie**’s death?",
            2: "According to the passage, why was the **Eiffel Tower** originally built?",
            3: "What ability do **dolphins** share with only a few other species?",
            4: "According to the passage, why was the **Great Wall of China** primarily built?",
            5: "What did **Alexander Fleming** discover by accident in **1928**?",
            6: "Why did the **Titanic** sink during its maiden voyage?",
            7: "Who were the first people to successfully reach the summit of **Mount Everest** in **1953**?",
            8: "According to the passage, where were the **first modern Olympic Games** held?",
            9: "According to the passage, how was **cacao** consumed by the **ancient Maya and Aztecs**?",
            10: "According to the passage, what is the main purpose of the **Perseverance rover**?",
            11: "According to the passage, where was **Vincent van Gogh** when he painted **'The Starry Night'**?"
        }
        
        for idx, new_q in updates.items():
            if idx < len(practices):
                practices[idx]['question'] = new_q
        
        new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
        # Indentation fix for insertion back into file
        lines = new_json_str.split('\\n')
        indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
        indented_json_str = '\\n'.join(indented_lines)
        
        new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated JSON data.")
    except Exception as e:
        print("Error processing JSON:", e)
else:
    print("Could not find JSON data.")
