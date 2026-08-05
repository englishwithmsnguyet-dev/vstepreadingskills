# -*- coding: utf-8 -*-
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(\"dang-04\":\s*\{.*?\"practices\":\s*\[)(.*?)(\]\s*\}\s*,\s*\"dang-05\")'
match = re.search(pattern, content, re.DOTALL)
if not match:
    print("Could not find dang-04 practices.")
    exit(1)

prefix = match.group(1)
suffix = match.group(3)

def generate_exp(explanation_text, vocab_items):
    vocab_html = ""
    for v in vocab_items:
        word, pos, ipa, meaning = v
        vocab_html += f'<li><strong>{word}</strong> <i class="fa-solid fa-volume-high vocab-audio-btn" data-word="{word}" style="cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;" title="Nghe phát âm"></i> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">({pos}) {ipa}</span>: {meaning}</li>'
    return f'{explanation_text}<hr style="margin: 16px 0; border: none; border-top: 1.5px dashed #cbd5e1;"><div style="background: #f0fdf4; border-left: 4px solid #22c55e; padding: 14px 18px; border-radius: 12px; margin-top: 16px;"><strong style="color: #166534; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px;"><i class="fa-solid fa-book-open"></i> TỪ VỰNG HỮU ÍCH</strong><ul style="margin: 0; padding-left: 20px; color: #166534; line-height: 1.7; font-size: 0.95rem;">{vocab_html}</ul></div>'

new_practices = [
    {
        "passage": "The blue whale is the largest animal known to have ever existed. These gentle giants can reach lengths of over 30 meters and weigh up to 180 tons. Despite their size, blue whales feed almost exclusively on tiny shrimp-like animals called krill. They are known for their deep, resonant calls that can travel hundreds of kilometers underwater.",
        "question": "Which of the following is NOT mentioned in the passage?",
        "options": [
            "A. Blue whales can grow longer than 30 meters.",
            "B. Blue whales communicate using sound.",
            "C. Blue whales mainly eat krill.",
            "D. Blue whales are fast swimmers."
        ],
        "correctIdx": 3,
        "explanation": generate_exp("Đoạn văn đề cập đến chiều dài (over 30m), thức ăn (krill), tiếng gọi giao tiếp (calls), nhưng không hề nhắc đến tốc độ bơi (fast swimmers).", [
            ("exist", "v", "/ɪɡˈzɪst/", "tồn tại"),
            ("gentle giant", "n", "/ˈdʒen.təl ˈdʒaɪ.ənt/", "người khổng lồ hiền lành"),
            ("exclusively", "adv", "/ɪkˈskluː.sɪv.li/", "chỉ dành riêng, duy nhất"),
            ("shrimp-like", "adj", "/ʃrɪmp laɪk/", "giống tôm"),
            ("krill", "n", "/krɪl/", "loài nhuyễn thể"),
            ("resonant", "adj", "/ˈrez.ən.ənt/", "vang dội"),
            ("underwater", "adv", "/ˌʌn.dəˈwɔː.tər/", "dưới nước")
        ]),
        "translationPassage": "Cá voi xanh là loài động vật lớn nhất từng tồn tại được biết đến. Những người khổng lồ hiền lành này có thể đạt chiều dài hơn 30 mét và nặng tới 180 tấn. Mặc dù có kích thước lớn, cá voi xanh hầu như chỉ ăn các loài động vật nhỏ giống tôm gọi là nhuyễn thể (krill). Chúng được biết đến với những tiếng gọi trầm, vang xa có thể truyền đi hàng trăm km dưới nước.",
        "translationQuestion": "Điều nào sau đây KHÔNG được đề cập trong đoạn văn?",
        "translationOptions": [
            "A. Cá voi xanh có thể dài hơn 30 mét.",
            "B. Cá voi xanh giao tiếp bằng âm thanh.",
            "C. Cá voi xanh chủ yếu ăn nhuyễn thể.",
            "D. Cá voi xanh bơi rất nhanh."
        ]
    },
    {
        "passage": "Many birds migrate thousands of kilometers each year to find food, escape harsh climates, or breed. The Arctic tern, for example, travels from the Arctic to the Antarctic and back again annually, making the longest known migration of any animal. Migration patterns are influenced by changes in temperature, food availability, and daylight hours. Some birds rely on the stars, the sun, and even Earth's magnetic field to navigate.",
        "question": "Which of the following is NOT mentioned in the passage?",
        "options": [
            "A. Birds migrate to avoid extreme weather.",
            "B. The Arctic tern has the longest migration distance of all animals.",
            "C. Migration is affected by environmental factors.",
            "D. Birds migrate in large groups for safety."
        ],
        "correctIdx": 3,
        "explanation": generate_exp("Đoạn văn nêu lý do di cư (find food, escape harsh climates -> avoid extreme weather), hành trình của chim nhạn Bắc Cực (longest known migration), và các yếu tố ảnh hưởng (temperature, daylight -> environmental), nhưng không nói chim di cư theo đàn lớn để an toàn.", [
            ("migrate", "v", "/maɪˈɡreɪt/", "di cư"),
            ("harsh climate", "n", "/hɑːʃ ˈklaɪ.mət/", "khí hậu khắc nghiệt"),
            ("breed", "v", "/briːd/", "sinh sản"),
            ("annually", "adv", "/ˈæn.ju.ə.li/", "hàng năm"),
            ("migration pattern", "n", "/maɪˈɡreɪ.ʃən ˈpæt.ən/", "mô hình di cư"),
            ("magnetic field", "n", "/mæɡˈnet.ɪk fiːld/", "từ trường"),
            ("navigate", "v", "/ˈnæv.ɪ.ɡeɪt/", "điều hướng, xác định phương hướng")
        ]),
        "translationPassage": "Nhiều loài chim di cư hàng ngàn km mỗi năm để tìm thức ăn, trốn tránh khí hậu khắc nghiệt, hoặc sinh sản. Ví dụ, chim nhạn Bắc Cực di chuyển từ Bắc Cực đến Nam Cực và ngược lại hàng năm, tạo nên chuyến di cư dài nhất được biết đến của bất kỳ loài động vật nào. Các mô hình di cư bị ảnh hưởng bởi những thay đổi về nhiệt độ, lượng thức ăn sẵn có, và số giờ ban ngày. Một số loài chim dựa vào các vì sao, mặt trời, và thậm chí cả từ trường Trái đất để xác định phương hướng.",
        "translationQuestion": "Điều nào sau đây KHÔNG được đề cập trong đoạn văn?",
        "translationOptions": [
            "A. Các loài chim di cư để tránh thời tiết khắc nghiệt.",
            "B. Chim nhạn Bắc Cực có quãng đường di cư dài nhất trong tất cả các loài động vật.",
            "C. Quá trình di cư bị ảnh hưởng bởi các yếu tố môi trường.",
            "D. Các loài chim di cư thành đàn lớn để đảm bảo an toàn."
        ]
    },
    {
        "passage": "Koalas are marsupials native to Australia. They spend most of their time in eucalyptus trees, eating the leaves and sleeping up to 20 hours a day. Koalas have strong claws to help them climb and rarely drink water, getting most of their moisture from eucalyptus leaves. However, habitat loss due to deforestation has threatened their population.",
        "question": "Which of the following is NOT mentioned in the passage?",
        "options": [
            "A. Koalas get most of their water from leaves.",
            "B. Koalas sleep for many hours each day.",
            "C. Koalas are found mainly in forests outside Australia.",
            "D. Koalas use their claws to climb trees."
        ],
        "correctIdx": 2,
        "explanation": generate_exp("Koalas are 'native to Australia' (bản địa Úc), do đó đáp án C nói koalas được tìm thấy chủ yếu ngoài nước Úc là sai hoàn toàn.", [
            ("marsupial", "n", "/mɑːˈsuː.pi.əl/", "thú có túi"),
            ("native", "adj", "/ˈneɪ.tɪv/", "bản địa"),
            ("eucalyptus", "n", "/ˌjuː.kəlˈɪp.təs/", "cây bạch đàn"),
            ("claw", "n", "/klɔː/", "móng vuốt"),
            ("moisture", "n", "/ˈmɔɪs.tʃər/", "hơi ẩm, nước"),
            ("habitat loss", "n", "/ˈhæb.ɪ.tæt lɒs/", "mất môi trường sống"),
            ("deforestation", "n", "/diːˌfɒr.ɪˈsteɪ.ʃən/", "sự tàn phá rừng")
        ]),
        "translationPassage": "Gấu túi (Koala) là loài thú có túi bản địa của Úc. Chúng dành hầu hết thời gian trên những cây bạch đàn, ăn lá cây và ngủ đến 20 giờ mỗi ngày. Gấu túi có móng vuốt chắc khỏe để giúp chúng leo trèo và hiếm khi uống nước, vì chúng lấy hầu hết lượng nước cần thiết từ lá bạch đàn. Tuy nhiên, tình trạng mất môi trường sống do nạn phá rừng đã đe dọa số lượng của chúng.",
        "translationQuestion": "Điều nào sau đây KHÔNG được đề cập trong đoạn văn?",
        "translationOptions": [
            "A. Gấu túi lấy hầu hết nước từ lá cây.",
            "B. Gấu túi ngủ nhiều giờ mỗi ngày.",
            "C. Gấu túi chủ yếu được tìm thấy ở các khu rừng ngoài nước Úc.",
            "D. Gấu túi sử dụng móng vuốt của chúng để leo cây."
        ]
    },
    {
        "passage": "Wind energy is one of the fastest-growing sources of renewable energy. It produces electricity without emitting greenhouse gases and reduces dependence on fossil fuels. Modern wind turbines are large and can generate power for thousands of homes. However, some people are concerned about noise and the impact on bird populations.",
        "question": "Which of the following is NOT true according to the passage?",
        "options": [
            "A. Wind turbines can supply power to many homes.",
            "B. Wind energy causes air pollution.",
            "C. Wind energy is considered renewable.",
            "D. Some people worry about its effects on birds."
        ],
        "correctIdx": 1,
        "explanation": generate_exp("Bài viết ghi rõ: 'produces electricity without emitting greenhouse gases' -> không phát thải khí nhà kính -> B nói gây ô nhiễm không khí là sai.", [
            ("renewable energy", "n", "/rɪˈnjuː.ə.bəl ˈen.ə.dʒi/", "năng lượng tái tạo"),
            ("emit", "v", "/iˈmɪt/", "phát ra, tỏa ra"),
            ("dependence", "n", "/dɪˈpen.dəns/", "sự phụ thuộc"),
            ("fossil fuel", "n", "/ˈfɒs.əl fjʊəl/", "nhiên liệu hóa thạch"),
            ("turbine", "n", "/ˈtɜː.baɪn/", "tuabin"),
            ("generate", "v", "/ˈdʒen.ə.reɪt/", "tạo ra, phát ra"),
            ("impact", "n", "/ˈɪm.pækt/", "tác động, ảnh hưởng")
        ]),
        "translationPassage": "Năng lượng gió là một trong những nguồn năng lượng tái tạo phát triển nhanh nhất. Nó sản xuất điện mà không phát thải khí nhà kính và giảm sự phụ thuộc vào nhiên liệu hóa thạch. Các tuabin gió hiện đại rất lớn và có thể tạo ra năng lượng cho hàng ngàn hộ gia đình. Tuy nhiên, một số người lo ngại về tiếng ồn và tác động lên quần thể các loài chim.",
        "translationQuestion": "Điều nào sau đây KHÔNG ĐÚNG theo đoạn văn?",
        "translationOptions": [
            "A. Tuabin gió có thể cung cấp năng lượng cho nhiều hộ gia đình.",
            "B. Năng lượng gió gây ra ô nhiễm không khí.",
            "C. Năng lượng gió được coi là có thể tái tạo.",
            "D. Một số người lo lắng về tác động của nó đối với các loài chim."
        ]
    },
    {
        "passage": "Honey is the only food that naturally never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly safe to eat. Its long shelf life is due to a unique chemical composition: it is low in moisture and highly acidic, creating an environment where bacteria and microorganisms cannot survive.",
        "question": "Which of the following is NOT mentioned as a reason why honey doesn't spoil?",
        "options": [
            "A. It has low moisture.",
            "B. It has high sugar content.",
            "C. It is highly acidic.",
            "D. Bacteria cannot survive in it."
        ],
        "correctIdx": 1,
        "explanation": generate_exp("Đoạn văn giải thích lý do mật ong không hỏng là do 'low in moisture' (độ ẩm thấp) và 'highly acidic' (có tính axit cao), giúp ngăn vi khuẩn ('bacteria cannot survive'). Nhưng không hề nhắc đến 'high sugar content' (hàm lượng đường cao) trong bài.", [
            ("naturally", "adv", "/ˈnætʃ.ər.əl.i/", "một cách tự nhiên"),
            ("spoil", "v", "/spɔɪl/", "bị hỏng, ôi thiu"),
            ("archaeologist", "n", "/ˌɑː.kiˈɒl.ə.dʒɪst/", "nhà khảo cổ học"),
            ("tomb", "n", "/tuːm/", "ngôi mộ"),
            ("shelf life", "n", "/ˈʃelf laɪf/", "thời hạn bảo quản"),
            ("chemical composition", "n", "/ˈkem.ɪ.kəl ˌkɒm.pəˈzɪʃ.ən/", "thành phần hóa học"),
            ("microorganism", "n", "/ˌmaɪ.krəʊˈɔː.ɡən.ɪ.zəm/", "vi sinh vật")
        ]),
        "translationPassage": "Mật ong là loại thực phẩm duy nhất tự nhiên không bao giờ bị hỏng. Các nhà khảo cổ học đã tìm thấy những hũ mật ong trong các ngôi mộ Ai Cập cổ đại đã hơn 3.000 năm tuổi và vẫn hoàn toàn an toàn để ăn. Thời hạn bảo quản lâu dài của nó là nhờ thành phần hóa học độc đáo: nó có độ ẩm thấp và có tính axit cao, tạo ra một môi trường mà vi khuẩn và vi sinh vật không thể sống sót.",
        "translationQuestion": "Điều nào sau đây KHÔNG được nhắc đến như một lý do tại sao mật ong không bị hỏng?",
        "translationOptions": [
            "A. Nó có độ ẩm thấp.",
            "B. Nó có hàm lượng đường cao.",
            "C. Nó có tính axit cao.",
            "D. Vi khuẩn không thể sống sót trong đó."
        ]
    },
    {
        "passage": "Despite a popular myth, the Great Wall of China is not visible from space with the naked eye. Astronauts in low Earth orbit have repeatedly confirmed that it is extremely difficult, if not impossible, to see the wall without visual aids. This is because the materials used to build it naturally blend in with the surrounding environment.",
        "question": "Which of the following is NOT true about the Great Wall of China according to the passage?",
        "options": [
            "A. It can be easily seen from space without a telescope.",
            "B. It was built using materials that blend with nature.",
            "C. Astronauts find it hard to see it from low Earth orbit.",
            "D. It is a myth that it is visible to the naked eye from space."
        ],
        "correctIdx": 0,
        "explanation": generate_exp("Bài viết ghi rõ 'is not visible from space with the naked eye' (không thể nhìn thấy từ vũ trụ bằng mắt thường). Do đó, đáp án A nói rằng nó có thể dễ dàng được nhìn thấy từ vũ trụ mà không cần kính viễn vọng là sai.", [
            ("myth", "n", "/mɪθ/", "lầm tưởng, huyền thoại"),
            ("visible", "adj", "/ˈvɪz.ə.bəl/", "có thể nhìn thấy"),
            ("naked eye", "n", "/ˌneɪ.kɪd ˈaɪ/", "mắt thường"),
            ("astronaut", "n", "/ˈæs.trə.nɔːt/", "phi hành gia"),
            ("orbit", "n", "/ˈɔː.bɪt/", "quỹ đạo"),
            ("visual aids", "n", "/ˈvɪʒ.u.əl eɪdz/", "dụng cụ hỗ trợ thị giác"),
            ("blend in", "v", "/blend ɪn/", "hòa nhập, lẫn vào")
        ]),
        "translationPassage": "Bất chấp một lầm tưởng phổ biến, Vạn Lý Trường Thành của Trung Quốc không thể được nhìn thấy từ vũ trụ bằng mắt thường. Các phi hành gia ở quỹ đạo thấp của Trái đất đã nhiều lần xác nhận rằng việc nhìn thấy bức tường mà không có thiết bị hỗ trợ thị giác là cực kỳ khó khăn, nếu không muốn nói là không thể. Điều này là do các vật liệu dùng để xây dựng nó tự nhiên lẫn vào với môi trường xung quanh.",
        "translationQuestion": "Điều nào sau đây KHÔNG ĐÚNG về Vạn Lý Trường Thành của Trung Quốc theo đoạn văn?",
        "translationOptions": [
            "A. Nó có thể dễ dàng được nhìn thấy từ vũ trụ mà không cần kính viễn vọng.",
            "B. Nó được xây bằng các vật liệu hòa lẫn với tự nhiên.",
            "C. Các phi hành gia thấy khó nhìn thấy nó từ quỹ đạo thấp của Trái đất.",
            "D. Việc nó có thể nhìn thấy bằng mắt thường từ vũ trụ chỉ là lầm tưởng."
        ]
    },
    {
        "passage": "Human sleep consists of multiple stages, typically cycling every 90 minutes. The stages include light sleep, deep sleep, and REM (Rapid Eye Movement) sleep. REM sleep is the period when most vivid dreaming occurs. While deep sleep helps restore the body physically, REM sleep is crucial for mental functions, learning, and memory consolidation.",
        "question": "Which of the following is NOT mentioned about the stages of sleep?",
        "options": [
            "A. A typical sleep cycle lasts about 90 minutes.",
            "B. Vivid dreaming usually happens during REM sleep.",
            "C. Deep sleep is mainly for mental restoration.",
            "D. Sleep includes light sleep, deep sleep, and REM sleep."
        ],
        "correctIdx": 2,
        "explanation": generate_exp("Bài đọc ghi rõ 'deep sleep helps restore the body physically' (giấc ngủ sâu giúp phục hồi cơ thể về mặt thể chất), chứ không phải 'mental restoration' (phục hồi tinh thần). Giấc ngủ REM mới chịu trách nhiệm cho 'mental functions' (tinh thần). Do đó, đáp án C là sai.", [
            ("consist of", "v", "/kənˈsɪst əv/", "bao gồm"),
            ("stage", "n", "/steɪdʒ/", "giai đoạn"),
            ("vivid", "adj", "/ˈvɪv.ɪd/", "sống động, rõ ràng"),
            ("restore", "v", "/rɪˈstɔːr/", "phục hồi, khôi phục"),
            ("physically", "adv", "/ˈfɪz.ɪ.kəl.i/", "về mặt thể chất"),
            ("crucial", "adj", "/ˈkruː.ʃəl/", "cực kỳ quan trọng"),
            ("memory consolidation", "n", "/ˈmem.ər.i kənˌsɒl.ɪˈdeɪ.ʃən/", "sự củng cố trí nhớ")
        ]),
        "translationPassage": "Giấc ngủ của con người bao gồm nhiều giai đoạn, thường lặp lại mỗi chu kỳ 90 phút. Các giai đoạn bao gồm giấc ngủ nông, giấc ngủ sâu, và giấc ngủ REM (Chuyển động mắt nhanh). Giấc ngủ REM là khoảng thời gian khi những giấc mơ sống động nhất xảy ra. Trong khi giấc ngủ sâu giúp phục hồi cơ thể về mặt thể chất, giấc ngủ REM lại cực kỳ quan trọng đối với các chức năng tinh thần, học tập và củng cố trí nhớ.",
        "translationQuestion": "Điều nào sau đây KHÔNG được đề cập về các giai đoạn của giấc ngủ?",
        "translationOptions": [
            "A. Một chu kỳ giấc ngủ điển hình kéo dài khoảng 90 phút.",
            "B. Mơ sống động thường xảy ra trong giấc ngủ REM.",
            "C. Giấc ngủ sâu chủ yếu dùng để phục hồi tinh thần.",
            "D. Giấc ngủ bao gồm giấc ngủ nông, giấc ngủ sâu và giấc ngủ REM."
        ]
    },
    {
        "passage": "Chocolate has a history spanning thousands of years, originating in Mesoamerica. The ancient Maya and Aztecs consumed it as a bitter beverage made from cacao beans, often mixed with spices or corn puree. They believed cacao was a gift from the gods and even used the beans as currency. It wasn't until chocolate was brought to Europe in the 16th century that sugar was added to make it sweet.",
        "question": "Which of the following is NOT true about chocolate in ancient Mesoamerica?",
        "options": [
            "A. It was consumed as a sweet drink.",
            "B. It was mixed with spices or corn puree.",
            "C. Cacao beans were used as money.",
            "D. It was considered a divine gift."
        ],
        "correctIdx": 0,
        "explanation": generate_exp("Đoạn văn nói rõ 'consumed it as a bitter beverage' (tiêu thụ như một thức uống đắng). Đường chỉ được thêm vào khi socola được mang đến châu Âu ('sugar was added to make it sweet'). Do đó, đáp án A nói nó được dùng như thức uống ngọt là sai.", [
            ("span", "v", "/spæn/", "kéo dài qua"),
            ("originate", "v", "/əˈrɪdʒ.ən.eɪt/", "bắt nguồn"),
            ("consume", "v", "/kənˈsjuːm/", "tiêu thụ, dùng"),
            ("bitter", "adj", "/ˈbɪt.ər/", "đắng"),
            ("beverage", "n", "/ˈbev.ər.ɪdʒ/", "thức uống"),
            ("currency", "n", "/ˈkʌr.ən.si/", "tiền tệ"),
            ("divine", "adj", "/dɪˈvaɪn/", "thần thánh")
        ]),
        "translationPassage": "Socola có lịch sử kéo dài hàng nghìn năm, bắt nguồn từ Mesoamerica. Người Maya và người Aztec cổ đại đã tiêu thụ nó như một loại đồ uống có vị đắng làm từ hạt ca cao, thường được trộn với gia vị hoặc ngô xay nhuyễn. Họ tin rằng ca cao là một món quà từ các vị thần và thậm chí đã sử dụng hạt của nó như một loại tiền tệ. Cho đến khi socola được mang đến châu Âu vào thế kỷ 16, đường mới được thêm vào để làm cho nó có vị ngọt.",
        "translationQuestion": "Điều nào sau đây KHÔNG ĐÚNG về socola ở Mesoamerica cổ đại?",
        "translationOptions": [
            "A. Nó được dùng như một loại đồ uống ngọt.",
            "B. Nó được trộn với gia vị hoặc ngô xay nhuyễn.",
            "C. Hạt ca cao được sử dụng làm tiền.",
            "D. Nó được coi là một món quà thần thánh."
        ]
    },
    {
        "passage": "The Earth's oceans cover more than 70% of the planet's surface, yet over 80% of our oceans remain unmapped and unexplored. The deep sea is a harsh environment with freezing temperatures, immense water pressure, and zero sunlight. Despite these extreme conditions, scientists have discovered bizarre creatures thriving near hydrothermal vents that release hot, mineral-rich water.",
        "question": "Which of the following is NOT mentioned as a characteristic of the deep sea?",
        "options": [
            "A. It has extremely cold temperatures.",
            "B. It receives no sunlight.",
            "C. It experiences strong ocean currents.",
            "D. It has very high water pressure."
        ],
        "correctIdx": 2,
        "explanation": generate_exp("Bài mô tả đại dương sâu thẳm có 'freezing temperatures' (lạnh giá), 'immense water pressure' (áp lực nước lớn), và 'zero sunlight' (không có ánh sáng mặt trời). Tuy nhiên, không có thông tin nào nhắc đến 'strong ocean currents' (dòng hải lưu mạnh).", [
            ("surface", "n", "/ˈsɜː.fɪs/", "bề mặt"),
            ("unmapped", "adj", "/ʌnˈmæpt/", "chưa được lập bản đồ"),
            ("unexplored", "adj", "/ˌʌn.ɪkˈsplɔːd/", "chưa được khám phá"),
            ("harsh", "adj", "/hɑːʃ/", "khắc nghiệt"),
            ("immense", "adj", "/ɪˈmens/", "vô cùng lớn"),
            ("bizarre", "adj", "/bɪˈzɑːr/", "kỳ lạ, kỳ quái"),
            ("hydrothermal vent", "n", "/ˌhaɪ.drəˈθɜː.məl vent/", "miệng phun thủy nhiệt")
        ]),
        "translationPassage": "Các đại dương trên Trái đất bao phủ hơn 70% bề mặt hành tinh, thế nhưng hơn 80% các đại dương của chúng ta vẫn chưa được lập bản đồ và chưa được khám phá. Biển sâu là một môi trường khắc nghiệt với nhiệt độ đóng băng, áp lực nước vô cùng lớn, và hoàn toàn không có ánh sáng mặt trời. Mặc cho những điều kiện khắc nghiệt này, các nhà khoa học đã khám phá ra những sinh vật kỳ lạ phát triển mạnh mẽ gần các miệng phun thủy nhiệt giải phóng nước nóng và giàu khoáng chất.",
        "translationQuestion": "Điều nào sau đây KHÔNG được nhắc đến như một đặc điểm của biển sâu?",
        "translationOptions": [
            "A. Nó có nhiệt độ cực kỳ lạnh.",
            "B. Nó không nhận được ánh sáng mặt trời.",
            "C. Nó có các dòng hải lưu mạnh.",
            "D. Nó có áp lực nước rất cao."
        ]
    },
    {
        "passage": "The discovery of coffee is widely attributed to an Ethiopian goat herder named Kaldi in the 9th century. According to the legend, Kaldi noticed that his goats became unusually energetic and could not sleep at night after eating berries from a certain tree. He reported his findings to a local monastery, where the monks made a drink with the berries and discovered that it kept them alert during long hours of evening prayer.",
        "question": "Which of the following is NOT true about the discovery of coffee according to the legend?",
        "options": [
            "A. It was discovered by an Ethiopian goat herder.",
            "B. The goats became sleepy after eating the berries.",
            "C. Monks used the berries to make a drink.",
            "D. The drink helped the monks stay awake during prayers."
        ],
        "correctIdx": 1,
        "explanation": generate_exp("Truyền thuyết kể rằng bầy dê trở nên 'unusually energetic and could not sleep' (cực kỳ năng động và không thể ngủ). Do đó, đáp án B nói bầy dê buồn ngủ sau khi ăn quả là hoàn toàn sai.", [
            ("discovery", "n", "/dɪˈskʌv.ər.i/", "sự khám phá"),
            ("attribute", "v", "/əˈtrɪb.juːt/", "cho là do, quy cho"),
            ("goat herder", "n", "/ɡəʊt ˈhɜː.dər/", "người chăn dê"),
            ("legend", "n", "/ˈledʒ.ənd/", "truyền thuyết"),
            ("energetic", "adj", "/ˌen.əˈdʒet.ɪk/", "tràn đầy năng lượng"),
            ("monastery", "n", "/ˈmɒn.ə.stri/", "tu viện"),
            ("alert", "adj", "/əˈlɜːt/", "tỉnh táo")
        ]),
        "translationPassage": "Việc khám phá ra cà phê được nhiều người cho là nhờ vào một người chăn dê ở Ethiopia tên là Kaldi vào thế kỷ thứ 9. Theo truyền thuyết, Kaldi nhận thấy bầy dê của mình trở nên cực kỳ năng động và không thể ngủ vào ban đêm sau khi ăn quả từ một loại cây nhất định. Anh ta báo cáo phát hiện của mình cho một tu viện địa phương, nơi các nhà sư đã làm một loại thức uống từ những quả này và phát hiện ra rằng nó giúp họ tỉnh táo trong những giờ cầu nguyện dài vào buổi tối.",
        "translationQuestion": "Điều nào sau đây KHÔNG ĐÚNG về việc khám phá ra cà phê theo truyền thuyết?",
        "translationOptions": [
            "A. Nó được phát hiện bởi một người chăn dê ở Ethiopia.",
            "B. Bầy dê trở nên buồn ngủ sau khi ăn những quả này.",
            "C. Các nhà sư đã sử dụng những quả này để làm đồ uống.",
            "D. Thức uống đã giúp các nhà sư tỉnh táo trong lúc cầu nguyện."
        ]
    },
    {
        "passage": "Mount Everest, the highest peak on Earth, is still growing. Because of the ongoing collision between the Indian and Eurasian tectonic plates, the Himalayas are continuously being pushed upwards. Scientists estimate that Everest grows by about 4 millimeters every year. Despite the freezing temperatures, high altitude, and lack of oxygen, hundreds of climbers attempt to reach its summit annually.",
        "question": "Which of the following is NOT mentioned in the passage?",
        "options": [
            "A. Mount Everest is the highest mountain on Earth.",
            "B. The mountain is getting taller every year.",
            "C. It costs a lot of money to climb Mount Everest.",
            "D. Climbers face a lack of oxygen near the summit."
        ],
        "correctIdx": 2,
        "explanation": generate_exp("Bài đọc nhắc đến việc Everest cao nhất (highest peak), ngày càng cao lên (growing / pushed upwards), và những khó khăn như thiếu oxy (lack of oxygen). Tuy nhiên, không có thông tin nào nhắc đến chi phí leo núi tốn kém.", [
            ("peak", "n", "/piːk/", "đỉnh núi"),
            ("ongoing", "adj", "/ˈɒnˌɡəʊ.ɪŋ/", "đang diễn ra"),
            ("collision", "n", "/kəˈlɪʒ.ən/", "sự va chạm"),
            ("tectonic plate", "n", "/tekˈtɒn.ɪk pleɪt/", "mảng kiến tạo"),
            ("estimate", "v", "/ˈes.tɪ.meɪt/", "ước tính"),
            ("altitude", "n", "/ˈæl.tɪ.tʃuːd/", "độ cao (so với mực nước biển)"),
            ("summit", "n", "/ˈsʌm.ɪt/", "đỉnh núi, chóp núi")
        ]),
        "translationPassage": "Đỉnh Everest, đỉnh núi cao nhất trên Trái đất, vẫn đang cao lên. Do sự va chạm không ngừng giữa các mảng kiến tạo Ấn Độ và Á-Âu, dãy Himalaya liên tục bị đẩy lên cao. Các nhà khoa học ước tính rằng Everest cao thêm khoảng 4 mm mỗi năm. Bất chấp nhiệt độ đóng băng, độ cao, và sự thiếu hụt oxy, hàng trăm người leo núi vẫn nỗ lực chinh phục đỉnh của nó hàng năm.",
        "translationQuestion": "Điều nào sau đây KHÔNG được đề cập trong đoạn văn?",
        "translationOptions": [
            "A. Đỉnh Everest là ngọn núi cao nhất trên Trái đất.",
            "B. Ngọn núi đang trở nên cao hơn mỗi năm.",
            "C. Tốn rất nhiều tiền để leo lên đỉnh Everest.",
            "D. Những người leo núi phải đối mặt với tình trạng thiếu oxy gần đỉnh."
        ]
    },
    {
        "passage": "Penguins are highly specialized marine birds adapted to life in the Southern Hemisphere. Unlike most birds, they cannot fly in the air; instead, their wings have evolved into flippers that make them excellent swimmers. Their dense feathers and thick layer of fat keep them warm in freezing waters. While they are famously associated with Antarctica, several species actually live in temperate zones, such as the Galapagos penguins.",
        "question": "Which of the following is NOT true about penguins according to the passage?",
        "options": [
            "A. All penguin species live in Antarctica.",
            "B. Their wings function as flippers for swimming.",
            "C. They have a thick layer of fat to stay warm.",
            "D. They are unable to fly."
        ],
        "correctIdx": 0,
        "explanation": generate_exp("Bài viết ghi: 'While they are famously associated with Antarctica, several species actually live in temperate zones' (Mặc dù chúng nổi tiếng gắn liền với Nam Cực, một vài loài thực sự sống ở vùng ôn đới). Do đó, đáp án A nói rằng TẤT CẢ các loài chim cánh cụt đều sống ở Nam Cực là sai.", [
            ("specialize", "v", "/ˈspeʃ.əl.aɪz/", "chuyên môn hóa, thích nghi đặc biệt"),
            ("marine", "adj", "/məˈriːn/", "thuộc về biển"),
            ("hemisphere", "n", "/ˈhem.ɪ.sfɪər/", "bán cầu"),
            ("evolve", "v", "/ɪˈvɒlv/", "tiến hóa"),
            ("flipper", "n", "/ˈflɪp.ər/", "chân vịt, màng bơi"),
            ("dense", "adj", "/dens/", "dày đặc"),
            ("temperate zone", "n", "/ˈtem.pər.ət zəʊn/", "vùng ôn đới")
        ]),
        "translationPassage": "Chim cánh cụt là những loài chim biển được đặc biệt hóa cao độ để thích nghi với cuộc sống ở Nam Bán Cầu. Không giống như hầu hết các loài chim khác, chúng không thể bay trên không; thay vào đó, đôi cánh của chúng đã tiến hóa thành các chân vịt khiến chúng trở thành những người bơi lội xuất sắc. Lớp lông dày đặc và lớp mỡ dày giúp chúng giữ ấm trong vùng nước đóng băng. Mặc dù chúng nổi tiếng gắn liền với Nam Cực, nhưng một vài loài thực chất lại sống ở các vùng ôn đới, ví dụ như chim cánh cụt Galapagos.",
        "translationQuestion": "Điều nào sau đây KHÔNG ĐÚNG về chim cánh cụt theo đoạn văn?",
        "translationOptions": [
            "A. Tất cả các loài chim cánh cụt đều sống ở Nam Cực.",
            "B. Cánh của chúng hoạt động như chân vịt để bơi lội.",
            "C. Chúng có một lớp mỡ dày để giữ ấm.",
            "D. Chúng không có khả năng bay."
        ]
    }
]

new_practices_json = json.dumps(new_practices, ensure_ascii=False, indent=4)
# Strip surrounding brackets so it fits inside the practices array brackets
new_practices_inner = new_practices_json[1:-1]

new_content = content[:match.start()] + prefix + new_practices_inner + suffix + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully replaced and expanded dang-04 practices to 12 items!")
