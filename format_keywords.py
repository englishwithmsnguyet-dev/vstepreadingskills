# -*- coding: utf-8 -*-
import os

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<p style=\\"margin-bottom: 12px; line-height: 1.8;\\"><strong>Bước 2:</strong> Gạch chân các từ khóa chính trong câu hỏi và các phương án trả lời, đặc biệt là:</p>\\n<p style=\\"margin-bottom: 12px; line-height: 1.8;\\">tên riêng (tên người, nơi chốn, tổ chức),</p>\\n<p style=\\"margin-bottom: 12px; line-height: 1.8;\\">số liệu (con số, tỉ lệ, năm),</p>\\n<p style=\\"margin-bottom: 12px; line-height: 1.8;\\">mốc thời gian, địa điểm,</p>\\n<p style=\\"margin-bottom: 12px; line-height: 1.8;\\">các từ/cụm từ nổi bật.</p>'

replacement = '<p style=\\"margin-bottom: 12px; line-height: 1.8;\\"><strong>Bước 2:</strong> Gạch chân các từ khóa chính trong câu hỏi và các phương án trả lời, đặc biệt tập trung ưu tiên nhóm <span style=\\"background: #fef08a; padding: 2px 6px; border-radius: 4px; font-weight: 700; color: #854d0e;\\">Từ khóa không biến đổi (Unchangeable Keywords)</span> - những từ gần như chắc chắn sẽ được giữ nguyên trong bài đọc, giúp bạn định vị thông tin cực kỳ nhanh và chính xác:</p>\\n<ul style=\\"list-style-type: none; padding-left: 0; margin-bottom: 16px; display: flex; flex-direction: column; gap: 8px;\\">\\n    <li><div style=\\"display: inline-block; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 6px; padding: 4px 10px; color: #991b1b; font-weight: 700; font-size: 0.95rem; margin-right: 8px;\\"><i class=\\"fa-solid fa-signature\\"></i> Tên riêng</div> <span style=\\"color: #475569; font-size: 1.02rem;\\">(Tên người, tên quốc gia, tên tổ chức được <strong>viết hoa chữ cái đầu</strong>)</span></li>\\n    <li><div style=\\"display: inline-block; background: #e0e7ff; border: 1px solid #a5b4fc; border-radius: 6px; padding: 4px 10px; color: #3730a3; font-weight: 700; font-size: 0.95rem; margin-right: 8px;\\"><i class=\\"fa-solid fa-hashtag\\"></i> Số liệu & Ký hiệu</div> <span style=\\"color: #475569; font-size: 1.02rem;\\">(Con số, phần trăm %, nhiệt độ °C, số lượng cụ thể)</span></li>\\n    <li><div style=\\"display: inline-block; background: #fef3c7; border: 1px solid #fde047; border-radius: 6px; padding: 4px 10px; color: #854d0e; font-weight: 700; font-size: 0.95rem; margin-right: 8px;\\"><i class=\\"fa-regular fa-calendar-days\\"></i> Mốc thời gian</div> <span style=\\"color: #475569; font-size: 1.02rem;\\">(Ngày, tháng, năm, thế kỷ, kỷ nguyên)</span></li>\\n    <li><div style=\\"display: inline-block; background: #dcfce7; border: 1px solid #86efac; border-radius: 6px; padding: 4px 10px; color: #166534; font-weight: 700; font-size: 0.95rem; margin-right: 8px;\\"><i class=\\"fa-solid fa-font\\"></i> Từ chuyên ngành</div> <span style=\\"color: #475569; font-size: 1.02rem;\\">(Các thuật ngữ đặc biệt cực kỳ khó hoặc không thể bị thay thế)</span></li>\\n</ul>'

if target in content:
    new_content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Target still not found. Let's check part of it:")
    print("Target part in content?", target[:100] in content)
