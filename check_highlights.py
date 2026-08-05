import re

html_file = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract everything inside dangsData object
match = re.search(r'const dangsData = (\{.*?\});\n\s*//', content, re.DOTALL)
if match:
    data_str = match.group(1)
    
    # 1. Look for highlights in inline styles
    styles = re.findall(r'style=\\"[^\"]*background[^\"]*\\"', data_str)
    print('Styles with background (count):', len(styles))
    for s in set(styles):
        if 'yellow' in s or 'green' in s or '#ff' in s or '#ffeb3b' in s or '#fef08a' in s:
            print('Suspicious style:', s)
            
    # 2. Look for classes with 'highlight'
    classes = re.findall(r'class=\\"[^\"]*highlight[^\"]*\\"', data_str)
    print('Classes with highlight:', set(classes))
    
    # 3. Look for 'mark' tag
    marks = re.findall(r'<mark.*?>', data_str)
    print('Mark tags:', marks)

else:
    print('dangsData not found')
