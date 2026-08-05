import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<script>')
if idx == -1:
    print('No script tag')
    sys.exit(0)

js_code = text[idx+8 : text.rfind('</script>')]

in_string = False
string_char = ''
is_escaped = False

line_num = 1
for i, char in enumerate(js_code):
    if char == '\n':
        if in_string and string_char != '`' and not is_escaped:
            print(f'Syntax Error: Unterminated string constant at line {line_num}!')
            # Print the context
            start = max(0, i - 50)
            end = min(len(js_code), i + 50)
            print(repr(js_code[start:end]))
            sys.exit(1)
        line_num += 1
        is_escaped = False
        continue

    if not in_string:
        if char in ["'", '"', '`']:
            in_string = True
            string_char = char
            is_escaped = False
    else:
        if is_escaped:
            is_escaped = False
        elif char == '\\':
            is_escaped = True
        elif char == string_char:
            in_string = False

print('No unterminated strings found!')
