# -*- coding: utf-8 -*-
import os
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We look for the start of Practice 09
start_str = '            {\n                "passage": "The Amazon Rainforest is the largest tropical rainforest'
idx = content.find(start_str)

if idx != -1:
    # Find the end of Practice 10, which is the end of dang-02's practices array
    end_str = '        ]\n    },\n    "dang-03": {'
    end_idx = content.find(end_str, idx)
    
    if end_idx != -1:
        # Generate the new Practice 09 and 10
        practice_09 = {
            "passage": "The modern Olympic Games, inspired by ancient Greek competitions, were first held in Athens, Greece, in 1896. The event was organized by Pierre de Coubertin, who founded the International Olympic Committee (IOC) two years earlier. The 1896 Games featured 280 athletes from 13 nations, competing in 43 events across nine sports, including athletics, cycling, and swimming. Today, the Olympics have grown into a massive international sporting festival with thousands of athletes from over 200 countries.",
            "question": "According to the passage, where were the first modern Olympic Games held?",
            "options": [
                "A. Paris, France.",
                "B. Athens, Greece.",
                "C. Rome, Italy.",
                "D. London, England."
            ],
            "correctIdx": 1,
            "explanation": "Đoạn văn có thông tin trực tiếp: 'were first held in Athens, Greece, in 1896' (được tổ chức lần đầu tại Athens, Hy Lạp, vào năm 1896). Trùng khớp với phương án B.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #fffbeb; border-left: 4px solid #fbbf24; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #92400e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-language\"></i> BẢN DỊCH</strong><p style=\"color: #92400e; margin: 0; font-size: 0.95rem; line-height: 1.7;\">Thế vận hội Olympic hiện đại, lấy cảm hứng từ các cuộc thi ở Hy Lạp cổ đại, được tổ chức lần đầu tại Athens, Hy Lạp, vào năm 1896. Sự kiện này được tổ chức bởi Pierre de Coubertin, người đã thành lập Ủy ban Olympic Quốc tế (IOC) hai năm trước đó. Thế vận hội năm 1896 có sự tham gia của 280 vận động viên từ 13 quốc gia, tranh tài ở 43 nội dung thi đấu thuộc 9 môn thể thao, bao gồm điền kinh, xe đạp và bơi lội. Ngày nay, Thế vận hội đã phát triển thành một lễ hội thể thao quốc tế khổng lồ với hàng nghìn vận động viên từ hơn 200 quốc gia.</p></div><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>inspired by</strong>: lấy cảm hứng từ</li><li><strong>ancient</strong>: cổ đại</li><li><strong>founded</strong>: thành lập</li><li><strong>International Olympic Committee</strong>: Ủy ban Olympic Quốc tế</li><li><strong>featured</strong>: có sự tham gia của, bao gồm</li><li><strong>athletes</strong>: vận động viên</li><li><strong>competing</strong>: tranh tài, thi đấu</li><li><strong>massive</strong>: to lớn, khổng lồ</li></ul></div>"
        }
        
        practice_10 = {
            "passage": "Chocolate has a rich history that dates back thousands of years to ancient Mesoamerica. The Mayans and Aztecs consumed cacao not as a sweet treat, but as a bitter, frothy drink mixed with spices and chili peppers. They believed cacao beans were a gift from the gods and even used them as a form of currency. It wasn't until the Spanish brought cacao to Europe in the 16th century that sugar was added, eventually transforming it into the sweet chocolate we enjoy today.",
            "question": "According to the passage, how did the Mayans and Aztecs consume cacao?",
            "options": [
                "A. As a sweet, solid chocolate bar.",
                "B. As a medicine for common illnesses.",
                "C. As a bitter, frothy drink mixed with spices.",
                "D. As a dessert served after meals."
            ],
            "correctIdx": 2,
            "explanation": "Đoạn văn nêu rõ: 'consumed cacao not as a sweet treat, but as a bitter, frothy drink mixed with spices and chili peppers' (tiêu thụ cacao không phải như một món ngọt, mà như một thức uống đắng, sủi bọt pha với các loại gia vị và ớt). Trùng khớp với phương án C.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #fffbeb; border-left: 4px solid #fbbf24; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #92400e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-language\"></i> BẢN DỊCH</strong><p style=\"color: #92400e; margin: 0; font-size: 0.95rem; line-height: 1.7;\">Sô-cô-la có một lịch sử phong phú kéo dài hàng nghìn năm từ thời Trung Mỹ cổ đại. Người Maya và người Aztec tiêu thụ cacao không phải như một món ngọt, mà như một thức uống đắng, sủi bọt được pha trộn với các loại gia vị và ớt. Họ tin rằng hạt cacao là một món quà từ các vị thần và thậm chí còn sử dụng chúng như một hình thức tiền tệ. Phải cho đến khi người Tây Ban Nha mang cacao đến châu Âu vào thế kỷ 16, đường mới được thêm vào, cuối cùng biến nó thành loại sô-cô-la ngọt ngào mà chúng ta thưởng thức ngày nay.</p></div><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>rich history</strong>: lịch sử phong phú</li><li><strong>ancient Mesoamerica</strong>: Trung Mỹ cổ đại</li><li><strong>consumed</strong>: tiêu thụ, sử dụng</li><li><strong>bitter</strong>: đắng</li><li><strong>frothy drink</strong>: thức uống sủi bọt</li><li><strong>currency</strong>: tiền tệ</li><li><strong>transforming</strong>: biến đổi</li></ul></div>"
        }

        def format_practice(p):
            s = '            {\n'
            s += '                "passage": ' + json.dumps(p["passage"], ensure_ascii=False) + ',\n'
            s += '                "question": ' + json.dumps(p["question"], ensure_ascii=False) + ',\n'
            s += '                "options": [\n'
            for i, opt in enumerate(p["options"]):
                s += '                    ' + json.dumps(opt, ensure_ascii=False)
                if i < len(p["options"])-1: s += ','
                s += '\n'
            s += '                ],\n'
            s += f'                "correctIdx": {p["correctIdx"]},\n'
            s += '                "explanation": ' + json.dumps(p["explanation"], ensure_ascii=False) + '\n'
            s += '            }'
            return s
            
        new_content = content[:idx] + format_practice(practice_09) + ',\n' + format_practice(practice_10) + '\n' + content[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Successfully replaced Practice 09 and 10 with new topics!')
    else:
        print('Could not find end of Practice 10')
else:
    print('Could not find start of Practice 09')
