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

# 1. Update passages and translations for P3 and P4
prac_3 = data['dang-02']['practices'][2]
prac_3['passage'] = "The Eiffel Tower, completed in 1889, was originally built as the entrance arch to the World's Fair held in Paris. Designed by engineer Gustave Eiffel, it was initially criticized by many artists and intellectuals who considered it an eyesore. However, over time, it became one of the most iconic landmarks in the world and a symbol of France. Today, it attracts nearly seven million visitors each year."

# Update translation in explanation for P3
prac_3['explanation'] = prac_3['explanation'].replace(
    'với thời gian, nó đã trở thành một trong những địa danh mang tính biểu tượng nhất trên thế giới.',
    'với thời gian, nó đã trở thành một trong những địa danh mang tính biểu tượng nhất trên thế giới và là một biểu tượng của nước Pháp. Ngày nay, nó thu hút gần bảy triệu du khách mỗi năm.'
)

prac_4 = data['dang-02']['practices'][3]
prac_4['passage'] = "Dolphins are known for their intelligence and complex social behavior. They live in groups called pods and communicate with each other using a variety of clicks and whistles. Scientists have discovered that dolphins can recognize themselves in mirrors, a trait shared by only a few species. This suggests that they have a sense of self-awareness, which is a sign of high cognitive ability."

# Update translation in explanation for P4
prac_4['explanation'] = prac_4['explanation'].replace(
    'Điều này cho thấy chúng có ý thức về bản thân.',
    'Điều này cho thấy chúng có ý thức về bản thân, đó là một dấu hiệu của khả năng nhận thức cao.'
)

# 2. Append new vocabularies
new_vocab = {
    0: { # P1
        'biodiverse': '(adj) /ˌbaɪ.oʊ.daɪˈvɜːs/: đa dạng sinh học',
        'lung': '(n) /lʌŋ/: lá phổi',
        'destroy': '(v) /dɪˈstrɔɪ/: phá hủy',
        'forest': '(n) /ˈfɒr.ɪst/: khu rừng',
        'area': '(n) /ˈeə.ri.ə/: diện tích, khu vực'
    },
    1: { # P2
        'radioactive element': '(n) /ˌreɪ.di.oʊˈæk.tɪv ˈel.ɪ.mənt/: nguyên tố phóng xạ'
    },
    2: { # P3
        'originally': '(adv) /əˈrɪdʒ.ɪ.nəl.i/: ban đầu',
        'initially': '(adv) /ɪˈnɪʃ.əl.i/: ban đầu',
        'criticize': '(v) /ˈkrɪt.ɪ.saɪz/: chỉ trích',
        'artist': '(n) /ˈɑː.tɪst/: nghệ sĩ',
        'intellectual': '(n) /ˌɪn.təlˈek.tʃu.əl/: tri thức, người tri thức',
        'iconic': '(adj) /aɪˈkɒn.ɪk/: mang tính biểu tượng',
        'landmark': '(n) /ˈlænd.mɑːk/: địa danh nổi bật',
        'symbol': '(n) /ˈsɪm.bəl/: biểu tượng',
        'attract': '(v) /əˈtrækt/: thu hút',
        'visitor': '(n) /ˈvɪz.ɪ.tər/: du khách'
    },
    3: { # P4
        'a sense of self-awareness': '(n) /ə sens əv ˌself.əˈweə.nəs/: ý thức về bản thân',
        'whistle': '(n) /ˈwɪs.əl/: tiếng huýt sáo',
        'click': '(n) /klɪk/: tiếng lách cách',
        'cognitive ability': '(n) /ˈkɒɡ.nə.tɪv əˈbɪl.ə.ti/: khả năng nhận thức'
    },
    4: { # P5
        'empire': '(n) /ˈem.paɪər/: đế quốc',
        'protect': '(v) /prəˈtekt/: bảo vệ',
        'human history': '(n) /ˈhjuː.mən ˈhɪs.tər.i/: lịch sử nhân loại'
    },
    5: { # P6
        'discover': '(v) /dɪˈskʌv.ər/: khám phá',
        'zone': '(n) /zoʊn/: khu vực, vùng',
        'mark': '(v) /mɑːk/: đánh dấu'
    },
    6: { # P7
        'estimated': '(adj) /ˈes.tɪ.meɪ.tɪd/: ước tính',
        'crew': '(n) /kruː/: phi hành đoàn, thủy thủ đoàn',
        'commercial': '(adj) /kəˈmɜː.ʃəl/: thương mại',
        'peacetime': '(n) /ˈpiːs.taɪm/: thời bình'
    },
    7: { # P8
        'border': '(n) /ˈbɔː.dər/: biên giới',
        'authorities': '(n) /ɔːˈθɒr.ə.tiz/: nhà chức trách',
        'establish': '(v) /ɪˈstæb.lɪʃ/: thiết lập'
    },
    8: { # P9
        'competition': '(n) /ˌkɒm.pəˈtɪʃ.ən/: cuộc thi',
        'organize': '(v) /ˈɔː.ɡən.aɪz/: tổ chức',
        'event': '(n) /ɪˈvent/: sự kiện'
    },
    9: { # P10
        'spice': '(n) /spaɪs/: gia vị',
        'chili pepper': '(n) /ˈtʃɪl.i ˈpep.ər/: quả ớt',
        'gift': '(n) /ɡɪft/: món quà',
        'gods': '(n) /ɡɒdz/: các vị thần'
    },
    10: { # P11
        'decade': '(n) /ˈdek.eɪd/: thập kỷ',
        'pole': '(n) /poʊl/: cực (Trái đất/hành tinh)',
        'mission': '(n) /ˈmɪʃ.ən/: sứ mệnh, nhiệm vụ'
    },
    11: { # P12
        'painter': '(n) /ˈpeɪn.tər/: họa sĩ',
        'struggle': '(v) /ˈstrʌɡ.əl/: vật lộn, đấu tranh',
        'artwork': '(n) /ˈɑːt.wɜːk/: tác phẩm nghệ thuật',
        'oil painting': '(n) /ɔɪl ˈpeɪn.tɪŋ/: tranh sơn dầu'
    }
}

for prac_idx, words in new_vocab.items():
    prac = data['dang-02']['practices'][prac_idx]
    explanation = prac['explanation']
    
    # We will find the closing </ul> tag in explanation and insert new items before it
    ul_end_idx = explanation.rfind('</ul>')
    if ul_end_idx != -1:
        new_items_html = ""
        for word, meaning in words.items():
            # e.g. meaning: (adj) /ˌbaɪ.oʊ.daɪˈvɜːs/: đa dạng sinh học
            # Splitting phonetic and meaning
            parts = meaning.split(':', 1)
            phonetic = parts[0].strip()
            vn_meaning = parts[1].strip() if len(parts) > 1 else ""
            
            # Use the correct HTML format from earlier
            html_item = f'<li><strong>{word}</strong> <i class=\\"fa-solid fa-volume-high vocab-audio-btn\\" data-word=\\"{word}\\" style=\\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\\" title=\\"Nghe phát âm\\"></i> <span style=\\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\\">{phonetic}</span>: {vn_meaning}</li>'
            new_items_html += html_item
            
        prac['explanation'] = explanation[:ul_end_idx] + new_items_html + explanation[ul_end_idx:]

new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
# Indentation fix
lines = new_json_str.split('\\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
indented_json_str = '\\n'.join(indented_lines)

new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated passages, translations and vocabularies!")
