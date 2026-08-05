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

theory = data['dang-01']['theory']

# Define the start of the block to replace
start_marker = "<div class='theory-example-box'"
start_idx = theory.find(start_marker)
if start_idx == -1:
    print("Could not find VÍ DỤ MINH HOẠ block in theory")
    exit(1)

# We will replace everything from start_marker to the end of the string
# Because the VÍ DỤ MINH HOẠ is the very last thing in the theory string of Dạng 01

new_block = """<div class="theory-mini-quiz" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #3b82f6; border-radius: 12px; padding: 20px; margin-top: 28px; margin-bottom: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
<div style="color: #2563eb; font-weight: 800; font-size: 1.15rem; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-book-open"></i> VÍ DỤ MINH HOẠ</div>
<div style="background: #f8fafc; border-left: 4px solid #cbd5e1; border-radius: 8px; padding: 14px; margin-bottom: 14px; font-size: 1.05rem; line-height: 1.7; color: #1e293b;">
Many people are turning to audiobooks as an alternative to traditional reading. With busy schedules, listeners find it convenient to enjoy books while commuting, exercising, or doing household chores. Audiobooks also support language learners by helping them improve pronunciation and listening comprehension. Publishers note that the format attracts readers who may not usually pick up a physical book, expanding access to literature. However, critics argue that listening may not offer the same depth of concentration as reading printed text.
</div>
<div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 12px; color: #0f172a;">What is the main idea of the passage?</div>
<div class="mini-quiz-options" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px;">
<button class="mini-quiz-option" data-opt="A" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">A. Audiobooks help people improve their pronunciation.</button>
<button class="mini-quiz-option" data-opt="B" data-correct="true" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">B. Audiobooks are becoming popular because they offer convenience and broaden access to reading.</button>
<button class="mini-quiz-option" data-opt="C" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">C. Critics believe audiobooks are less effective than printed books.</button>
<button class="mini-quiz-option" data-opt="D" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">D. People prefer audiobooks to reading physical books.</button>
</div>
<div style="text-align:center;">
<button class="mini-quiz-check-btn" style="background:#6366f1; color:#ffffff; border:none; border-radius:20px; padding:10px 24px; font-weight:700; font-size:1rem; cursor:pointer;"><i class="fa-solid fa-check-double"></i> Kiểm tra đáp án</button>
</div>
<div class="mini-quiz-explain" style="display:none; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:10px; padding:14px; margin-top:12px; color:#166534; font-size:1.02rem; line-height:1.65;">
<strong>✅ Đáp án đúng: B</strong><br>
🔍 <em>Giải thích chi tiết:</em><br>
<ul style="list-style-type: none; padding-left: 0; margin-bottom: 16px;">
<li style="margin-bottom: 8px; line-height: 1.8;"><strong>1. Tại sao chọn B?</strong></li>
</ul>
<p style="margin-bottom: 12px; line-height: 1.8;">Toàn đoạn mô tả sự phổ biến ngày càng tăng của audiobooks và tại sao chúng được nhiều người lựa chọn.</p>
<p style="margin-bottom: 12px; line-height: 1.8;">Tác giả liệt kê nhiều lợi ích: tiện lợi (commuting, exercising, chores), hỗ trợ người học ngôn ngữ, mở rộng khả năng tiếp cận sách cho người không thường đọc bản in.</p>
<p style="margin-bottom: 12px; line-height: 1.8;">Cuối đoạn có nhắc đến ý kiến phản biện, nhưng chỉ để bổ sung góc nhìn, không phải trọng tâm.</p>
<p style="margin-bottom: 12px; line-height: 1.8;">→ Ý chính phải khái quát toàn bộ: audiobooks đang được ưa chuộng vì sự tiện lợi và khả năng mở rộng việc tiếp cận sách → đúng với phương án B.</p>
<ul style="list-style-type: none; padding-left: 0; margin-bottom: 16px;">
<li style="margin-bottom: 8px; line-height: 1.8;"><strong>2. Vì sao các phương án khác sai?</strong></li>
</ul>
<p style="margin-bottom: 12px; line-height: 1.8;">A — Sai (quá hẹp). Đúng là audiobooks hỗ trợ người học ngôn ngữ, nhưng đây chỉ là một lợi ích cụ thể, không phải ý chính toàn bài.</p>
<p style="margin-bottom: 12px; line-height: 1.8;">C — Sai (một ý phụ). Đoạn văn có nhắc đến “critics argue…”, nhưng đây không phải trọng tâm. Khi tác giả chỉ dành 1 câu để nói, đó chỉ là ý bổ sung.</p>
<p style="margin-bottom: 12px; line-height: 1.8;">D — Sai (không đúng với đoạn văn). Đoạn không khẳng định “people prefer…” mà chỉ nói audiobooks giúp mở rộng đối tượng người đọc, không nói số đông “thích hơn”.</p>
</div>
</div>"""

theory = theory[:start_idx] + new_block
# Also, remove all line breaks from new_block to keep the JSON string clean, although json.dumps handles it.
theory = theory.replace('\n', '')

data['dang-01']['theory'] = theory

new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
# Fix indentation to match existing style
lines = new_json_str.split('\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
indented_json_str = '\n'.join(indented_lines)

new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully replaced static VÍ DỤ MINH HOẠ with interactive mini-quiz in dang-01!")
