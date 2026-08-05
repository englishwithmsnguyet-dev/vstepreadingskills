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

new_practices = [
    {
        "passage": "Invented in the 15th century by Johannes Gutenberg, the printing press revolutionized how information was shared. Before its creation, books were copied by hand, making them rare and expensive. The printing press allowed for mass production of texts, drastically lowering their cost. This innovation increased literacy rates across Europe and facilitated the spread of new scientific and philosophical ideas.",
        "question": "What is the main idea of the passage?",
        "options": [
            "A. Books were too expensive before the 15th century.",
            "B. The printing press transformed how information was produced and spread.",
            "C. Johannes Gutenberg was an influential inventor in Europe.",
            "D. Mass production reduced the cost of scientific books."
        ],
        "correctIdx": 1,
        "rationale": "Đoạn văn mô tả việc phát minh ra máy in (printing press) đã thay đổi cách chia sẻ thông tin, giúp sản xuất hàng loạt, giảm chi phí, tăng tỷ lệ biết chữ và lan truyền tư tưởng mới. Khái quát lại, máy in đã tạo ra cuộc cách mạng trong việc sản xuất và lan truyền thông tin (phương án B).",
        "vocab": [
            {"word": "invent", "meaning": "(v) /ɪnˈvent/: phát minh"},
            {"word": "revolutionize", "meaning": "(v) /ˌrev.əˈluː.ʃən.aɪz/: cách mạng hóa"},
            {"word": "mass production", "meaning": "(n) /ˌmæs prəˈdʌk.ʃən/: sản xuất hàng loạt"},
            {"word": "drastically", "meaning": "(adv) /ˈdræs.tɪ.kəl.i/: một cách mạnh mẽ, quyết liệt"},
            {"word": "literacy rate", "meaning": "(n) /ˈlɪt.ər.ə.si reɪt/: tỷ lệ biết chữ"},
            {"word": "facilitate", "meaning": "(v) /fəˈsɪl.ɪ.teɪt/: tạo điều kiện dễ dàng, thúc đẩy"}
        ]
    },
    {
        "passage": "Bees play a crucial role in maintaining the balance of our ecosystem through pollination. As they travel from flower to flower collecting nectar, they transfer pollen, which allows plants to reproduce. This process is essential not only for the survival of wild plants but also for global agriculture. In fact, it is estimated that one-third of the human food supply depends on pollination by bees and other insects.",
        "question": "What is the passage primarily about?",
        "options": [
            "A. The method bees use to collect nectar from flowers.",
            "B. The importance of bees in pollination and the global food supply.",
            "C. How wild plants reproduce in the natural environment.",
            "D. The decline of the bee population in modern agriculture."
        ],
        "correctIdx": 1,
        "rationale": "Xuyên suốt đoạn văn, tác giả nhấn mạnh vai trò thiết yếu của loài ong (crucial role) thông qua việc thụ phấn (pollination), đóng góp vào cả tự nhiên lẫn 1/3 nguồn cung ứng thực phẩm của con người. Ý chính là tầm quan trọng của loài ong trong việc thụ phấn và chuỗi thức ăn toàn cầu (phương án B).",
        "vocab": [
            {"word": "crucial", "meaning": "(adj) /ˈkruː.ʃəl/: vô cùng quan trọng, thiết yếu"},
            {"word": "ecosystem", "meaning": "(n) /ˈiː.koʊˌsɪs.təm/: hệ sinh thái"},
            {"word": "pollination", "meaning": "(n) /ˌpɒl.ɪˈneɪ.ʃən/: sự thụ phấn"},
            {"word": "nectar", "meaning": "(n) /ˈnek.tər/: mật hoa"},
            {"word": "reproduce", "meaning": "(v) /ˌriː.prəˈdjuːs/: sinh sản"},
            {"word": "agriculture", "meaning": "(n) /ˈæɡ.rɪ.kʌl.tʃər/: nông nghiệp"}
        ]
    },
    {
        "passage": "While the physical benefits of regular exercise are well known, its positive effects on mental health are equally profound. Engaging in physical activity releases endorphins, which are natural chemicals in the brain that reduce pain and improve mood. Regular workouts have been shown to alleviate symptoms of depression, reduce stress levels, and boost overall self-esteem. Consequently, many health professionals recommend exercise as a natural treatment for various psychological issues.",
        "question": "Which of the following best summarizes the main idea of the passage?",
        "options": [
            "A. Endorphins are chemicals that reduce pain and improve mood.",
            "B. Regular exercise is highly beneficial for mental health.",
            "C. Physical activity is the most effective treatment for depression.",
            "D. Health professionals recommend working out to build physical strength."
        ],
        "correctIdx": 1,
        "rationale": "Đoạn văn tập trung phân tích những tác động tích cực của việc tập thể dục đối với sức khỏe tinh thần (mental health), chẳng hạn như giải phóng endorphins, giảm trầm cảm, căng thẳng và nâng cao lòng tự trọng. Ý chính khái quát nhất là lợi ích to lớn của tập thể dục đối với tinh thần (phương án B).",
        "vocab": [
            {"word": "profound", "meaning": "(adj) /prəˈfaʊnd/: sâu sắc, to lớn"},
            {"word": "release", "meaning": "(v) /rɪˈliːs/: giải phóng, tiết ra"},
            {"word": "chemical", "meaning": "(n) /ˈkem.ɪ.kəl/: chất hóa học"},
            {"word": "alleviate", "meaning": "(v) /əˈliː.vi.eɪt/: làm nhẹ bớt, làm giảm"},
            {"word": "symptom", "meaning": "(n) /ˈsɪmp.təm/: triệu chứng"},
            {"word": "self-esteem", "meaning": "(n) /ˌself.ɪˈstiːm/: lòng tự trọng, sự tự tôn"},
            {"word": "psychological", "meaning": "(adj) /ˌsaɪ.kəˈlɒdʒ.ɪ.kəl/: thuộc về tâm lý"}
        ]
    },
    {
        "passage": "Minimalism is a lifestyle choice that focuses on living with only the things you truly need. By decluttering their homes and eliminating unnecessary possessions, minimalists aim to reduce stress and financial burden. This approach to life encourages people to value experiences and relationships over material goods. Ultimately, minimalism is not just about having less stuff, but about making room for more meaning and joy in everyday life.",
        "question": "What is the main point of the passage?",
        "options": [
            "A. Minimalists save a lot of money by not buying material goods.",
            "B. Decluttering the home is the best way to reduce daily stress.",
            "C. Minimalism is a lifestyle centered on finding meaning by reducing excess.",
            "D. Experiences and relationships are more expensive than physical possessions."
        ],
        "correctIdx": 2,
        "rationale": "Đoạn văn giải thích khái niệm về chủ nghĩa tối giản (minimalism) - một lối sống tập trung vào những thứ thực sự cần thiết, loại bỏ đồ đạc dư thừa để giảm căng thẳng và đề cao trải nghiệm, từ đó mang lại nhiều ý nghĩa hơn cho cuộc sống. Phương án C tóm tắt chính xác tinh thần này.",
        "vocab": [
            {"word": "minimalism", "meaning": "(n) /ˈmɪn.ɪ.mə.lɪ.zəm/: chủ nghĩa tối giản"},
            {"word": "declutter", "meaning": "(v) /ˌdiːˈklʌt.ər/: dọn dẹp, loại bỏ đồ đạc bừa bộn"},
            {"word": "eliminate", "meaning": "(v) /ɪˈlɪm.ɪ.neɪt/: loại bỏ"},
            {"word": "possession", "meaning": "(n) /pəˈzeʃ.ən/: tài sản, vật sở hữu"},
            {"word": "burden", "meaning": "(n) /ˈbɜː.dən/: gánh nặng"},
            {"word": "material goods", "meaning": "(n) /məˈtɪə.ri.əl ɡʊdz/: của cải vật chất"}
        ]
    },
    {
        "passage": "Coral reefs are often called the rainforests of the sea because of their incredible biodiversity. These massive structures are actually built by tiny marine animals called coral polyps. As these polyps die, their hard limestone skeletons remain, and new generations of polyps grow on top of them. Over thousands of years, this continuous cycle of life and death creates the vast, colorful reef ecosystems that support thousands of marine species today.",
        "question": "What does the passage mainly discuss?",
        "options": [
            "A. The variety of marine species living in coral reefs.",
            "B. How coral reefs are built over time by coral polyps.",
            "C. The similarities between rainforests and coral reefs.",
            "D. The life cycle and feeding habits of coral polyps."
        ],
        "correctIdx": 1,
        "rationale": "Dù đoạn văn có nhắc đến sự đa dạng sinh học ở câu đầu, nội dung cốt lõi của toàn đoạn là miêu tả quá trình hình thành của các rạn san hô (được xây dựng bởi các polyp san hô, lớp này đè lên lớp khác qua hàng ngàn năm). Do đó, phương án B khái quát chính xác nhất nội dung này.",
        "vocab": [
            {"word": "coral reef", "meaning": "(n) /ˈkɒr.əl riːf/: rạn san hô"},
            {"word": "biodiversity", "meaning": "(n) /ˌbaɪ.oʊ.daɪˈvɜː.sə.ti/: sự đa dạng sinh học"},
            {"word": "massive", "meaning": "(adj) /ˈmæs.ɪv/: to lớn, khổng lồ"},
            {"word": "polyp", "meaning": "(n) /ˈpɒl.ɪp/: sinh vật hình ống nhỏ, polyp"},
            {"word": "limestone", "meaning": "(n) /ˈlaɪm.stoʊn/: đá vôi"},
            {"word": "skeleton", "meaning": "(n) /ˈskel.ə.tən/: bộ xương"}
        ]
    },
    {
        "passage": "The Silk Road was not a single paved highway, but rather a complex network of trade routes connecting the East and the West. Originating in China, it facilitated the exchange of goods such as silk, spices, and precious metals. However, its most profound impact was the cultural exchange it fostered. Religions, philosophies, and technological innovations traveled along these routes, fundamentally shaping the development of civilizations across Asia, the Middle East, and Europe.",
        "question": "What is the primary purpose of the passage?",
        "options": [
            "A. To explain how silk and spices were transported from China to Europe.",
            "B. To describe the physical construction of the Silk Road network.",
            "C. To highlight the Silk Road's role in facilitating both trade and cultural exchange.",
            "D. To argue that technological innovations were more valuable than precious metals."
        ],
        "correctIdx": 2,
        "rationale": "Đoạn văn không chỉ nói về việc con đường tơ lụa (Silk Road) là một mạng lưới giao thương hàng hóa (silk, spices), mà còn nhấn mạnh tác động sâu sắc của nó trong việc giao lưu văn hóa, tôn giáo và công nghệ (cultural exchange). Phương án C bao hàm đủ cả hai yếu tố này (trade and cultural exchange).",
        "vocab": [
            {"word": "paved", "meaning": "(adj) /peɪvd/: được lát (đường)"},
            {"word": "route", "meaning": "(n) /ruːt/: tuyến đường"},
            {"word": "originate", "meaning": "(v) /əˈrɪdʒ.ən.eɪt/: bắt nguồn"},
            {"word": "facilitate", "meaning": "(v) /fəˈsɪl.ɪ.teɪt/: tạo điều kiện dễ dàng"},
            {"word": "profound", "meaning": "(adj) /prəˈfaʊnd/: sâu sắc, to lớn"},
            {"word": "foster", "meaning": "(v) /ˈfɒs.tər/: thúc đẩy, nuôi dưỡng"},
            {"word": "civilization", "meaning": "(n) /ˌsɪv.əl.əˈzeɪ.ʃən/: nền văn minh"}
        ]
    }
]

# Construct explanation string for each
for prac in new_practices:
    rationale = prac['rationale']
    vocab_list = prac['vocab']
    
    explanation_html = f"{rationale}<hr style=\"margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;\">"
    explanation_html += f"<div style=\"background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;\"><strong style=\"color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;\"><i class=\"fa-solid fa-book-open\"></i> TỪ VỰNG HỮU ÍCH</strong><ul style=\"margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;\">"
    
    for v in vocab_list:
        word = v['word']
        meaning_parts = v['meaning'].split(':', 1)
        phonetic = meaning_parts[0].strip()
        vn_meaning = meaning_parts[1].strip() if len(meaning_parts) > 1 else ""
        
        li = f"<li><strong>{word}</strong> <i class=\"fa-solid fa-volume-high vocab-audio-btn\" data-word=\"{word}\" style=\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\" title=\"Nghe phát âm\"></i> <span style=\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\">{phonetic}</span>: {vn_meaning}</li>"
        explanation_html += li
        
    explanation_html += "</ul></div>"
    
    prac_entry = {
        "passage": prac["passage"],
        "question": prac["question"],
        "options": prac["options"],
        "correctIdx": prac["correctIdx"],
        "explanation": explanation_html
    }
    data['dang-01']['practices'].append(prac_entry)

new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
lines = new_json_str.split('\\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
indented_json_str = '\\n'.join(indented_lines)

new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully added 6 new practices to Dạng 01!")
