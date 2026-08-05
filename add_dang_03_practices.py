# -*- coding: utf-8 -*-
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate dang-03 practices array
pattern = r'(\"dang-03\":\s*\{.*?\"practices\":\s*\[)(.*?)(\]\s*\}\s*,\s*\"dang-04\")'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find dang-03 practices.")
    exit(1)

prefix = match.group(1)
practices_str = match.group(2)
suffix = match.group(3)

def generate_exp(explanation_text, vocab_items):
    vocab_html = ""
    for v in vocab_items:
        word, pos, ipa, meaning = v
        vocab_html += f'<li><strong>{word}</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="{word}" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">({pos}) {ipa}</span>: {meaning}</li>'
    
    return f'{explanation_text}<hr style="margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;"><div style="background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;"><strong style="color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;"><i class="fa-solid fa-book-open"></i> TỪ VỰNG HỮU ÍCH</strong><ul style="margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;">{vocab_html}</ul></div>'

new_practices = [
    {
        "passage": "After graduating from university, Mark decided not to become a teacher like his parents. Instead, he started a career in investment banking because it is highly <strong>lucrative</strong>. Within just three years, he was able to buy a large house and a luxury sports car with his bonuses.",
        "question": "The word 'lucrative' in the passage is closest in meaning to:",
        "options": ["A. stressful", "B. profitable", "C. dangerous", "D. boring"],
        "correctIdx": 1,
        "explanation": generate_exp("Đoạn văn nhắc đến việc Mark mua được một ngôi nhà lớn và một chiếc xe thể thao sang trọng nhờ tiền thưởng ('able to buy a large house and a luxury sports car'). Điều này cho thấy công việc của anh ấy tạo ra nhiều lợi nhuận hoặc sinh lời nhiều. Do đó, lucrative = profitable (sinh lời, hái ra tiền).", [
            ("lucrative", "adj", "/ˈluː.krə.tɪv/", "sinh lời, kiếm được nhiều tiền"),
            ("graduate", "v", "/ˈɡrædʒ.u.eɪt/", "tốt nghiệp"),
            ("investment banking", "n", "/ɪnˈvest.mənt ˈbæŋ.kɪŋ/", "ngân hàng đầu tư"),
            ("luxury", "adj", "/ˈlʌk.ʃər.i/", "sang trọng, xa xỉ"),
            ("bonus", "n", "/ˈbəʊ.nəs/", "tiền thưởng"),
            ("profitable", "adj", "/ˈprɒf.ɪ.tə.bəl/", "có lợi nhuận, sinh lời")
        ]),
        "translationPassage": "Sau khi tốt nghiệp đại học, Mark quyết định không trở thành giáo viên như cha mẹ mình. Thay vào đó, anh bắt đầu sự nghiệp trong lĩnh vực ngân hàng đầu tư vì nó cực kỳ <strong>sinh lời</strong>. Chỉ trong vòng ba năm, anh đã có thể mua một ngôi nhà lớn và một chiếc xe thể thao sang trọng bằng tiền thưởng của mình.",
        "translationQuestion": "Từ 'lucrative' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. căng thẳng", "B. sinh lời", "C. nguy hiểm", "D. nhàm chán"]
    },
    {
        "passage": "The company's new smartwatch is truly <strong>innovative</strong>. Unlike any other device on the market, it can project a holographic display into the air and translate 50 languages in real-time. This groundbreaking approach to technology has won several international awards for creativity.",
        "question": "The word 'innovative' in the passage is closest in meaning to:",
        "options": ["A. traditional", "B. creative", "C. expensive", "D. complicated"],
        "correctIdx": 1,
        "explanation": generate_exp("Từ 'unlike any other device' (không giống bất kỳ thiết bị nào khác) và cụm 'groundbreaking approach' (phương pháp mang tính đột phá) cũng như việc giành giải thưởng cho 'creativity' (sự sáng tạo) cho thấy innovative = creative (sáng tạo, đổi mới).", [
            ("innovative", "adj", "/ˈɪn.ə.və.tɪv/", "có tính đổi mới, sáng tạo"),
            ("project", "v", "/prəˈdʒekt/", "chiếu (hình ảnh)"),
            ("holographic", "adj", "/ˌhɒl.əˈɡræf.ɪk/", "toàn ảnh (3D)"),
            ("real-time", "adj", "/ˌrɪəl ˈtaɪm/", "thời gian thực"),
            ("groundbreaking", "adj", "/ˈɡraʊndˌbreɪ.kɪŋ/", "mang tính đột phá"),
            ("creativity", "n", "/ˌkriː.eɪˈtɪv.ə.ti/", "sự sáng tạo"),
            ("complicated", "adj", "/ˈkɒm.plɪ.keɪ.tɪd/", "phức tạp")
        ]),
        "translationPassage": "Chiếc đồng hồ thông minh mới của công ty thực sự <strong>đổi mới/sáng tạo</strong>. Không giống như bất kỳ thiết bị nào khác trên thị trường, nó có thể chiếu màn hình ba chiều vào không trung và dịch 50 ngôn ngữ trong thời gian thực. Phương pháp tiếp cận công nghệ mang tính đột phá này đã giành được một số giải thưởng quốc tế về tính sáng tạo.",
        "translationQuestion": "Từ 'innovative' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. truyền thống", "B. sáng tạo", "C. đắt đỏ", "D. phức tạp"]
    },
    {
        "passage": "During their hike through the dense forest, the explorers stumbled upon an old, ruined castle. It had been completely <strong>abandoned</strong> for centuries. The roof had collapsed, the walls were covered in thick vines, and no one had lived there since the medieval era.",
        "question": "The word 'abandoned' in the passage is closest in meaning to:",
        "options": ["A. newly built", "B. crowded", "C. left empty", "D. carefully protected"],
        "correctIdx": 2,
        "explanation": generate_exp("Ngữ cảnh mô tả 'no one had lived there since the medieval era' (không có ai sống ở đó kể từ thời trung cổ), và 'ruined castle' (lâu đài đổ nát). Điều này chỉ ra rằng abandoned = left empty (bị bỏ hoang, không ai ở).", [
            ("abandon", "v", "/əˈbæn.dən/", "bỏ rơi, bỏ hoang"),
            ("explorer", "n", "/ɪkˈsplɔː.rər/", "nhà thám hiểm"),
            ("stumble upon", "v", "/ˈstʌm.bəl əˈpɒn/", "tình cờ phát hiện"),
            ("ruined", "adj", "/ˈruː.ɪnd/", "đổ nát, bị hủy hoại"),
            ("collapse", "v", "/kəˈlæps/", "sụp đổ"),
            ("vine", "n", "/vaɪn/", "dây leo"),
            ("medieval era", "n", "/ˌmed.iˈiː.vəl ˈɪə.rə/", "thời trung cổ")
        ]),
        "translationPassage": "Trong suốt chuyến đi bộ đường dài xuyên qua khu rừng rậm rạp, những nhà thám hiểm tình cờ phát hiện ra một lâu đài cũ nát. Nó đã hoàn toàn bị <strong>bỏ hoang</strong> trong nhiều thế kỷ. Mái nhà đã sụp đổ, các bức tường bị bao phủ bởi những dây leo dày đặc, và không có ai sống ở đó kể từ thời trung cổ.",
        "translationQuestion": "Từ 'abandoned' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. mới được xây", "B. đông đúc", "C. bị bỏ hoang/để trống", "D. được bảo vệ cẩn thận"]
    },
    {
        "passage": "The coastal city faces a high risk of flooding every time there is a massive storm. To <strong>mitigate</strong> this ongoing problem, the local government has decided to build a massive sea wall and improve the drainage system to reduce the severity of the floods.",
        "question": "The word 'mitigate' in the passage is closest in meaning to:",
        "options": ["A. lessen", "B. increase", "C. ignore", "D. completely solve"],
        "correctIdx": 0,
        "explanation": generate_exp("Cụm từ 'to reduce the severity of the floods' (để giảm mức độ nghiêm trọng của lũ lụt) đóng vai trò giải thích trực tiếp mục đích của việc xây dựng đê biển. Do đó, mitigate = reduce/lessen (giảm nhẹ, làm dịu bớt).", [
            ("mitigate", "v", "/ˈmɪt.ɪ.ɡeɪt/", "giảm nhẹ, làm dịu đi"),
            ("coastal", "adj", "/ˈkəʊ.stəl/", "thuộc về bờ biển, ven biển"),
            ("risk of flooding", "n", "/rɪsk əv ˈflʌd.ɪŋ/", "nguy cơ ngập lụt"),
            ("massive storm", "n", "/ˈmæs.ɪv stɔːm/", "cơn bão lớn"),
            ("drainage system", "n", "/ˈdreɪ.nɪdʒ ˈsɪs.təm/", "hệ thống thoát nước"),
            ("severity", "n", "/sɪˈver.ə.ti/", "mức độ nghiêm trọng"),
            ("lessen", "v", "/ˈles.ən/", "làm giảm đi, làm nhỏ lại")
        ]),
        "translationPassage": "Thành phố ven biển phải đối mặt với nguy cơ ngập lụt cao mỗi khi có một cơn bão lớn. Để <strong>giảm nhẹ</strong> vấn đề dai dẳng này, chính quyền địa phương đã quyết định xây dựng một bức tường chắn biển khổng lồ và cải thiện hệ thống thoát nước để giảm mức độ nghiêm trọng của lũ lụt.",
        "translationQuestion": "Từ 'mitigate' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. giảm nhẹ", "B. gia tăng", "C. phớt lờ", "D. giải quyết triệt để"]
    }
]

# Ensure we separate them correctly.
practices_base = practices_str.rstrip()
if practices_base.endswith(','):
    practices_base = practices_base[:-1]

new_practices_json = json.dumps(new_practices, ensure_ascii=False, indent=4)
new_practices_inner = new_practices_json[1:-1]

new_practices_str = practices_base + ",\n" + new_practices_inner

new_content = content[:match.start()] + prefix + new_practices_str + suffix + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully added 4 practices to Dạng 03!")
