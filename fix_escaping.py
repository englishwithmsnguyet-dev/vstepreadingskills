# -*- coding: utf-8 -*-
import os
import json

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('            {\n                "passage": "The Amazon Rainforest')
if idx != -1:
    end_idx = content.find('        ]\n    },\n    "dang-03": {', idx)
    if end_idx != -1:
        practice_09 = {
            "passage": "The Amazon Rainforest is the largest tropical rainforest in the world, covering over 5.5 million square kilometers. It is often referred to as the 'lungs of the Earth' because it produces around 20% of the world's oxygen. The forest is home to an incredible diversity of wildlife, including jaguars, sloths, and harpy eagles. However, it faces severe threats from deforestation, primarily driven by logging, agriculture, and cattle ranching.",
            "question": "According to the passage, what is the primary cause of deforestation in the Amazon Rainforest?",
            "options": [
                "A. Tourism and urban development.",
                "B. Logging, agriculture, and cattle ranching.",
                "C. Wildfires and climate change.",
                "D. The growing population of wildlife."
            ],
            "correctIdx": 1,
            "explanation": "Đoạn văn nêu rõ nguyên nhân gây ra nạn phá rừng là: 'primarily driven by logging, agriculture, and cattle ranching' (chủ yếu do khai thác gỗ, nông nghiệp và chăn nuôi gia súc). Trùng khớp với phương án B.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #fffbeb; border-left: 4px solid #fbbf24; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #92400e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-language\"></i> BẢN DỊCH</strong><p style=\"color: #92400e; margin: 0; font-size: 0.95rem; line-height: 1.7;\">Rừng mưa Amazon là khu rừng nhiệt đới lớn nhất thế giới, bao phủ diện tích hơn 5,5 triệu km2. Nó thường được mệnh danh là 'lá phổi của Trái đất' vì sản xuất khoảng 20% lượng oxy của thế giới. Khu rừng này là nhà của sự đa dạng động vật hoang dã đáng kinh ngạc, bao gồm báo đốm, lười, và đại bàng harpy. Tuy nhiên, nó đang đối mặt với những mối đe dọa nghiêm trọng từ nạn phá rừng, chủ yếu là do khai thác gỗ, nông nghiệp và chăn nuôi gia súc.</p></div><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>tropical rainforest</strong>: rừng mưa nhiệt đới</li><li><strong>lungs of the Earth</strong>: lá phổi của Trái Đất</li><li><strong>incredible diversity</strong>: sự đa dạng đáng kinh ngạc</li><li><strong>severe threats</strong>: những mối đe dọa nghiêm trọng</li><li><strong>deforestation</strong>: nạn phá rừng</li><li><strong>logging</strong>: khai thác gỗ</li><li><strong>cattle ranching</strong>: chăn nuôi gia súc</li></ul></div>"
        }
        
        practice_10 = {
            "passage": "Marie Curie was a pioneering physicist and chemist who conducted groundbreaking research on radioactivity. She was the first woman to win a Nobel Prize and remains the only person to win a Nobel Prize in two different scientific fields: Physics in 1903 and Chemistry in 1911. During World War I, she developed mobile radiography units to provide X-ray services to field hospitals, saving the lives of over a million wounded soldiers.",
            "question": "In which two scientific fields did Marie Curie win a Nobel Prize?",
            "options": [
                "A. Physics and Biology.",
                "B. Chemistry and Medicine.",
                "C. Physics and Chemistry.",
                "D. Mathematics and Physics."
            ],
            "correctIdx": 2,
            "explanation": "Đoạn văn cung cấp thông tin cụ thể: 'Physics in 1903 and Chemistry in 1911' (Vật lý năm 1903 và Hóa học năm 1911). Do đó, phương án C là chính xác.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #fffbeb; border-left: 4px solid #fbbf24; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #92400e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-language\"></i> BẢN DỊCH</strong><p style=\"color: #92400e; margin: 0; font-size: 0.95rem; line-height: 1.7;\">Marie Curie là một nhà vật lý và hóa học tiên phong, người đã tiến hành những nghiên cứu đột phá về hiện tượng phóng xạ. Bà là người phụ nữ đầu tiên giành giải Nobel và vẫn là người duy nhất giành giải Nobel trong hai lĩnh vực khoa học khác nhau: Vật lý năm 1903 và Hóa học năm 1911. Trong suốt Thế chiến I, bà đã phát triển các thiết bị chụp X-quang di động để cung cấp dịch vụ X-quang cho các bệnh viện dã chiến, cứu sống hơn một triệu binh sĩ bị thương.</p></div><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>pioneering</strong>: tiên phong</li><li><strong>groundbreaking research</strong>: nghiên cứu đột phá</li><li><strong>radioactivity</strong>: hiện tượng phóng xạ</li><li><strong>scientific fields</strong>: lĩnh vực khoa học</li><li><strong>radiography units</strong>: thiết bị chụp X-quang</li><li><strong>wounded soldiers</strong>: thương binh, binh sĩ bị thương</li></ul></div>"
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
        print('Fixed the bad escaping successfully!')
    else:
        print('Could not find end of bad insertion')
else:
    print('Could not find bad insertion')
