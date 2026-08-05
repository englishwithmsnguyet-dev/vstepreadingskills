import re
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Locate dang-04
idx_dang04 = text.find('"dang-04":')
idx_theory = text.find('"theory": "', idx_dang04)
idx_start = idx_theory + 11

# The escaped block ends before `, "example": {` inside dang-04
# Let's find exactly where the theory of dang-04 ends.
# Since the index.html is now correctly formatted, dang-04's theory ends with `",\n            "example": {`
idx_end = text.find('",\n            "example": {', idx_start)

if idx_end == -1:
    print("Could not find the end of dang-04 theory")
    exit(1)

# Extract and unescape the theory
theory_str_escaped = text[idx_start:idx_end]
theory_str = theory_str_escaped.replace('\\"', '"').replace('\\n', '\n')

# Now modify the theory string.
# We will remove the static "VÍ DỤ MINH HỌA" section at the end and replace it with the new interactive HTML.
# Let's find the VÍ DỤ MINH HỌA part.
remove_idx = theory_str.find('<p style="margin-bottom: 12px; line-height: 1.8;">VÍ DỤ MINH HỌA</p>')
if remove_idx == -1:
    print("Could not find VÍ DỤ MINH HỌA in theory")
    exit(1)

# Keep the theory before VÍ DỤ MINH HỌA
new_theory_str = theory_str[:remove_idx]

# Inject the new interactive quiz
quiz_html = '''<!-- VÍ DỤ MINH HOẠ -->
                    <div class="theory-mini-quiz" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; margin-bottom: 16px;">
                        <div style="color: #0891b2; font-weight: 700; font-size: 1.05rem; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-book-open"></i> VÍ DỤ MINH HOẠ</div>
                        <div style="background: #f8fafc; border-left: 4px solid #cbd5e1; border-radius: 8px; padding: 14px; margin-bottom: 14px; font-size: 1.05rem; line-height: 1.7; color: #1e293b;">
                            Many people are choosing to work from home due to recent technological developments. Remote work offers several advantages: employees save commuting time, enjoy more flexible schedules, and often experience higher productivity. However, working from home also presents challenges. Some workers feel isolated because they have fewer opportunities to interact with colleagues. Others struggle to balance household responsibilities with professional tasks. Despite these drawbacks, remote work continues to grow as companies adopt digital communication tools to support their teams.
                        </div>
                        <div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 12px; color: #0f172a;">Which of the following is NOT mentioned in the passage?</div>
                        <div class="mini-quiz-options" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px;">
                            <button class="mini-quiz-option" data-opt="A" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">A. Remote work can help employees reduce the amount of time spent traveling.</button>
                            <button class="mini-quiz-option" data-opt="B" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">B. Some employees find it difficult to manage both personal and work duties at home.</button>
                            <button class="mini-quiz-option" data-opt="C" data-correct="true" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">C. Remote work leads to lower productivity for most employees.</button>
                            <button class="mini-quiz-option" data-opt="D" style="text-align:left; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:10px; padding:12px 18px; font-size:1.05rem; color:#1e293b; cursor:pointer;">D. Some remote workers feel lonely due to limited social interaction.</button>
                        </div>
                        <div style="text-align:center;">
                            <button class="mini-quiz-check-btn" style="background:#6366f1; color:#ffffff; border:none; border-radius:20px; padding:10px 24px; font-weight:700; font-size:1rem; cursor:pointer;"><i class="fa-solid fa-check-double"></i> Kiểm tra đáp án</button>
                        </div>
                        <div class="mini-quiz-explain" style="display:none; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:10px; padding:14px; margin-top:12px; color:#166534; font-size:1.02rem; line-height:1.65;">
                            <strong>✅ Đáp án đúng: C. Remote work leads to lower productivity for most employees.</strong><br>
                            🔍 <em>Giải thích:</em> 
                            <br>A – Có nêu trong bài → Bài đọc nói rõ “employees save commuting time” → nghĩa là giảm thời gian đi lại → ĐÚNG với bài.
                            <br>B – Có nêu trong bài → Câu “Others struggle to balance household responsibilities with professional tasks” → chính là khó khăn khi cân bằng công việc và việc nhà → phù hợp với bài.
                            <br>C – KHÔNG được đề cập / trái với bài → Bài nói “often experience higher productivity” → năng suất tăng chứ không giảm. Do đó, đáp án C là không đúng theo bài → đáp án cần chọn.
                            <br>D – Có nêu trong bài → Câu “Some workers feel isolated because they have fewer opportunities to interact with colleagues” → nghĩa là cảm thấy cô lập, ít tương tác → phù hợp với đáp án D.
                        <hr style="margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;">
<div style="margin-bottom: 14px;"><strong>BẢN DỊCH CHI TIẾT:</strong></div>
<div style="background: #f8fafc; border-left: 4px solid #94a3b8; border-radius: 8px; padding: 12px; margin-bottom: 12px; font-size: 1rem; color: #475569;">
    Nhiều người đang chọn làm việc từ xa do sự phát triển công nghệ gần đây. Làm việc từ xa mang lại một số lợi ích: nhân viên tiết kiệm thời gian đi lại, tận hưởng lịch trình linh hoạt hơn, và thường đạt năng suất cao hơn. Tuy nhiên, làm việc từ xa cũng đưa ra những thách thức. Một số nhân viên cảm thấy bị cô lập vì họ có ít cơ hội tương tác với đồng nghiệp. Những người khác gặp khó khăn trong việc cân bằng trách nhiệm gia đình với các nhiệm vụ chuyên môn. Mặc dù có những hạn chế này, làm việc từ xa vẫn tiếp tục phát triển khi các công ty áp dụng các công cụ giao tiếp kỹ thuật số để hỗ trợ nhóm của họ.
</div>
<div style="font-weight: bold; margin-bottom: 8px; color: #334155;">Điều nào sau đây KHÔNG được đề cập trong đoạn văn?</div>
<div style="margin-bottom: 14px; color: #475569; padding-left: 10px; line-height: 1.7;">
    A. Làm việc từ xa có thể giúp nhân viên giảm lượng thời gian đi lại.<br>B. Một số nhân viên cảm thấy khó khăn trong việc quản lý cả nhiệm vụ cá nhân và công việc tại nhà.<br>C. Làm việc từ xa dẫn đến năng suất thấp hơn đối với hầu hết nhân viên.<br>D. Một số người làm việc từ xa cảm thấy cô đơn do sự tương tác xã hội bị hạn chế.
</div>
<div style="background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;">
    <strong style="color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
        <i class="fa-solid fa-book-open"></i> TỪ VỰNG HỮU ÍCH
    </strong>
    <ul style="margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;">
        <li><strong>remote work</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="remote work" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(n) /rɪˈməʊt wɜːk/</span>: làm việc từ xa</li>
        <li><strong>commute</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="commute" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(v) /kəˈmjuːt/</span>: đi lại thường xuyên</li>
        <li><strong>flexible</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="flexible" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(adj) /ˈflek.sə.bəl/</span>: linh hoạt</li>
        <li><strong>productivity</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="productivity" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(n) /ˌprɒd.ʌkˈtɪv.ə.ti/</span>: năng suất</li>
        <li><strong>isolated</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="isolated" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(adj) /ˈaɪ.sə.leɪ.tɪd/</span>: bị cô lập, cách ly</li>
        <li><strong>interact</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="interact" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(v) /ˌɪn.təˈrækt/</span>: tương tác</li>
        <li><strong>struggle</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="struggle" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(v) /ˈstrʌɡ.əl/</span>: gặp khó khăn, chật vật</li>
        <li><strong>drawback</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="drawback" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">(n) /ˈdrɔː.bæk/</span>: mặt hạn chế, điểm yếu</li>
    </ul>
</div>
</div>
</div>
'''

new_theory_str += quiz_html

# Escape the new theory string
new_theory_str_escaped = new_theory_str.replace('"', '\\"').replace('\n', '\\n')

# Inject back into text
new_text = text[:idx_start] + new_theory_str_escaped + text[idx_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully updated dang-04 theory!")
