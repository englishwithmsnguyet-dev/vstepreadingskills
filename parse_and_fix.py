import re
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index_fixed.html'
# Wait! I will use index.html which is un-mangled for dang-01 to dang-03, and dang-04 theory is escaped.
file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'const dangsData = (\{[\s\S]*?\});', text)
if not match:
    exit(1)
json_str = match.group(1)

# We will build a Python dictionary from json_str!
# Since json_str is broken, we will parse it manually.
# Let's extract each dang-XX
dangs_data = {}

dang_matches = list(re.finditer(r'"(dang-\d+)":\s*\{', json_str))
for i, dm in enumerate(dang_matches):
    dang_id = dm.group(1)
    start_idx = dm.end()
    if i + 1 < len(dang_matches):
        end_idx = dang_matches[i+1].start()
    else:
        end_idx = len(json_str)
        
    dang_str = json_str[start_idx:end_idx]
    
    # Extract root keys
    dang_obj = {}
    
    def extract_key(key, text_chunk):
        pattern = f'"{key}":\s*"'
        idx = text_chunk.find(pattern)
        if idx == -1: return None
        val_start = idx + len(pattern) - 1 # point to the quote
        
        # The value ends before the next key at this level.
        # Root keys: "title", "icon", "description", "theory", "example", "practices"
        next_keys = ['"title":', '"icon":', '"description":', '"theory":', '"example":', '"practices":']
        min_end = len(text_chunk)
        for nk in next_keys:
            nk_idx = text_chunk.find(nk, val_start)
            if nk_idx != -1 and nk_idx < min_end:
                min_end = nk_idx
                
        # min_end points to the start of the next key. The string ends before it, usually at `",\n`
        # Let's find the last quote before min_end
        val_end = text_chunk.rfind('"', val_start, min_end)
        
        val = text_chunk[val_start+1:val_end]
        # unescape it if it was escaped
        val = val.replace('\\"', '"').replace('\\n', '\n')
        return val

    dang_obj['title'] = extract_key('title', dang_str)
    dang_obj['icon'] = extract_key('icon', dang_str)
    dang_obj['description'] = extract_key('description', dang_str)
    dang_obj['theory'] = extract_key('theory', dang_str)
    
    # Extract example
    example_idx = dang_str.find('"example": {')
    if example_idx != -1:
        example_end = dang_str.find('"practices": [', example_idx)
        if example_end == -1: example_end = len(dang_str)
        example_str = dang_str[example_idx:example_end]
        
        def extract_practice_keys(text_chunk):
            obj = {}
            keys = ['passage', 'question', 'options', 'correctIdx', 'explanation', 'translationPassage', 'translationQuestion', 'translationOptions']
            
            for k in keys:
                if k == 'options' or k == 'translationOptions':
                    pattern = f'"{k}":\s*\['
                    idx = text_chunk.find(pattern)
                    if idx != -1:
                        arr_start = text_chunk.find('[', idx)
                        arr_end = text_chunk.find(']', arr_start)
                        arr_str = text_chunk[arr_start+1:arr_end]
                        # extract strings
                        opts = []
                        for m in re.finditer(r'"([^"]*)"', arr_str):
                            opts.append(m.group(1).replace('\\"', '"'))
                        obj[k] = opts
                elif k == 'correctIdx':
                    pattern = f'"{k}":\s*(\d+)'
                    m = re.search(pattern, text_chunk)
                    if m: obj[k] = int(m.group(1))
                else:
                    pattern = f'"{k}":\s*"'
                    idx = text_chunk.find(pattern)
                    if idx != -1:
                        val_start = idx + len(pattern) - 1
                        # find next key
                        next_keys = [f'"{nk}":' for nk in keys]
                        min_end = len(text_chunk)
                        for nk in next_keys:
                            nk_idx = text_chunk.find(nk, val_start)
                            if nk_idx != -1 and nk_idx < min_end:
                                min_end = nk_idx
                        # if no next key, find the end of the object `}`
                        if min_end == len(text_chunk):
                            min_end = text_chunk.rfind('}')
                        val_end = text_chunk.rfind('"', val_start, min_end)
                        val = text_chunk[val_start+1:val_end]
                        val = val.replace('\\"', '"').replace('\\n', '\n')
                        obj[k] = val
            return obj
            
        dang_obj['example'] = extract_practice_keys(example_str)
        
    # Extract practices
    practices_idx = dang_str.find('"practices": [')
    if practices_idx != -1:
        practices_str = dang_str[practices_idx:]
        # find all practice objects
        # they are between { and }
        practices = []
        depth = 0
        obj_start = -1
        for i, char in enumerate(practices_str):
            if char == '{':
                if depth == 0: obj_start = i
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0 and obj_start != -1:
                    obj_str = practices_str[obj_start:i+1]
                    practices.append(extract_practice_keys(obj_str))
        dang_obj['practices'] = practices
        
    dangs_data[dang_id] = dang_obj

# Let's dump it back!
new_json_str = json.dumps(dangs_data, ensure_ascii=False, indent=4)
new_json_str = "{\n    " + new_json_str[1:-1] + "\n}" # adjust braces

new_text = text[:match.start(1)] + new_json_str + text[match.end(1):]

with open('index_parsed.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Wrote index_parsed.html")
