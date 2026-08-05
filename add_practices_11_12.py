# -*- coding: utf-8 -*-
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find dang-01 practices array and append to it.
# The pattern for dang-01:
pattern = r'(\"dang-01\":\s*\{.*?\"practices\":\s*\[)(.*?)(\]\s*\}\s*,\s*\"dang-02\")'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find dang-01 practices.")
    exit(1)

prefix = match.group(1)
practices_str = match.group(2)
suffix = match.group(3)

# We will append two new practices
new_practices = [
    {
        "passage": "The global popularity of electric vehicles (EVs) has surged over the past decade. Unlike traditional cars that run on gasoline, EVs use large battery packs to store electrical energy. This shift has significantly reduced greenhouse gas emissions in major cities. A recent environmental report shows that a typical EV produces about 60% less carbon emissions over its lifetime compared to a similar gasoline-powered car. However, the lack of charging stations in rural areas remains a significant challenge for long-distance travelers.",
        "question": "According to the passage, what is a major challenge for people driving electric vehicles over long distances?",
        "options": [
            "A. The high cost of electricity",
            "B. The lack of charging stations in rural areas",
            "C. The large size of the battery packs",
            "D. The slow speed of electric vehicles"
        ],
        "correctIdx": 1,
        "explanation": "Đoạn văn nêu rõ: 'the lack of charging stations in rural areas remains a significant challenge for long-distance travelers' (việc thiếu các trạm sạc ở các vùng nông thôn vẫn là một thách thức đáng kể đối với những người đi du lịch đường dài). Do đó, phương án B là chính xác.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>surge</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"surge\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(v) /sɜːdʒ/</span>: tăng vọt</li><li><strong>greenhouse gas emissions</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"greenhouse gas emissions\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(n) /ˈɡriːn.haʊs ɡæs ɪˈmɪʃ.ənz/</span>: lượng khí thải nhà kính</li><li><strong>rural areas</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"rural areas\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(n) /ˈrʊə.rəl ˈeə.ri.əz/</span>: các vùng nông thôn</li></ul></div>",
        "translationPassage": "Sự phổ biến toàn cầu của xe điện (EV) đã tăng vọt trong thập kỷ qua. Không giống như các loại xe truyền thống chạy bằng xăng, xe điện sử dụng các bộ pin lớn để lưu trữ năng lượng điện. Sự chuyển đổi này đã làm giảm đáng kể lượng khí thải nhà kính ở các thành phố lớn. Một báo cáo môi trường gần đây cho thấy một chiếc xe điện thông thường tạo ra lượng khí thải carbon ít hơn khoảng 60% trong suốt vòng đời của nó so với một chiếc xe chạy bằng xăng tương tự. Tuy nhiên, việc thiếu các trạm sạc ở các vùng nông thôn vẫn là một thách thức đáng kể đối với những người đi du lịch đường dài.",
        "translationQuestion": "Theo đoạn văn, đâu là một thách thức lớn đối với những người lái xe điện trên quãng đường dài?",
        "translationOptions": [
            "A. Chi phí điện cao",
            "B. Việc thiếu các trạm sạc ở các vùng nông thôn",
            "C. Kích thước lớn của các bộ pin",
            "D. Tốc độ chậm của xe điện"
        ]
    },
    {
        "passage": "Tomatoes are widely consumed around the world and are incredibly versatile in cooking. Although they are scientifically classified as a fruit because they contain seeds and develop from the ovary of a flower, they are treated as vegetables in the culinary world. This is primarily due to their savory flavor, which makes them a perfect ingredient for salads, sauces, and stews. In 1893, the U.S. Supreme Court even officially declared the tomato a vegetable for taxation purposes.",
        "question": "Why are tomatoes generally treated as vegetables in the culinary world?",
        "options": [
            "A. Because they contain seeds",
            "B. Because of their savory flavor",
            "C. Because they were taxed by the government",
            "D. Because they develop from a flower"
        ],
        "correctIdx": 1,
        "explanation": "Đoạn văn giải thích: 'they are treated as vegetables in the culinary world. This is primarily due to their savory flavor' (chúng được coi như rau củ trong thế giới ẩm thực. Điều này chủ yếu là do hương vị mặn mà của chúng). Vì vậy, phương án B là đáp án chính xác.<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\"><div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\"><li><strong>versatile</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"versatile\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(adj) /ˈvɜː.sə.taɪl/</span>: linh hoạt, đa dụng</li><li><strong>culinary</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"culinary\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(adj) /ˈkʌl.ɪ.nər.i/</span>: thuộc về ẩm thực, nấu nướng</li><li><strong>savory flavor</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"savory flavor\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">(n) /ˈseɪ.vər.i ˈfleɪ.vər/</span>: hương vị đậm đà, mặn mà</li></ul></div>",
        "translationPassage": "Cà chua được tiêu thụ rộng rãi trên toàn thế giới và cực kỳ linh hoạt trong nấu ăn. Mặc dù về mặt khoa học chúng được phân loại là một loại trái cây vì chứa hạt và phát triển từ bầu nhụy của một bông hoa, nhưng chúng lại được coi như rau củ trong thế giới ẩm thực. Điều này chủ yếu là do hương vị đậm đà (hơi mặn) của chúng, khiến chúng trở thành nguyên liệu hoàn hảo cho các món salad, nước sốt và món hầm. Năm 1893, Tòa án Tối cao Hoa Kỳ thậm chí đã chính thức tuyên bố cà chua là một loại rau củ vì mục đích tính thuế.",
        "translationQuestion": "Tại sao cà chua thường được coi như rau củ trong thế giới ẩm thực?",
        "translationOptions": [
            "A. Vì chúng chứa hạt",
            "B. Vì hương vị đậm đà/mặn mà của chúng",
            "C. Vì chúng bị chính phủ đánh thuế",
            "D. Vì chúng phát triển từ một bông hoa"
        ]
    }
]

# We want to insert the new practices at the end of the practices list.
# practices_str already ends with the last practice's closing brace `}`.
# Wait, if there are trailing commas, we need to handle it.
# Let's just append `, \n` + JSON serialized new_practices.
new_practices_json = json.dumps(new_practices, ensure_ascii=False, indent=4)
# Remove the square brackets [ ] from json.dumps output since we are appending elements
new_practices_inner = new_practices_json[1:-1]

# Ensure we separate them correctly. practices_str ends with `}` usually, but maybe spaces.
practices_str = practices_str.rstrip()
if practices_str.endswith(','):
    practices_str = practices_str[:-1]

new_practices_str = practices_str + ",\n" + new_practices_inner

new_content = content[:match.start()] + prefix + new_practices_str + suffix + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully added 2 new practices to Dạng 01!")
