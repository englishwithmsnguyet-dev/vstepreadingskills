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

translations = [
    {
        "q": "Ý chính của đoạn văn là gì?",
        "opts": ["A. Cà phê giúp con người thư giãn", "B. Quán cà phê là nơi làm việc tốt nhất", "C. Tác động của cà phê lớn hơn hương vị của nó", "D. Cà phê cải thiện các tương tác xã hội"],
        "passage": "Cà phê không chỉ là một loại đồ uống; nó đóng một vai trò quan trọng trong nhiều nền văn hóa trên khắp thế giới. Ở một số quốc gia, uống cà phê là một thói quen hàng ngày mang mọi người lại với nhau để trò chuyện và thư giãn. Ở những nơi khác, nó gắn liền với năng suất và thường được tiêu thụ tại nơi làm việc. Các quán cà phê đã trở thành điểm gặp gỡ phổ biến, ảnh hưởng đến cả tương tác xã hội và kinh doanh. Cho dù được thưởng thức một mình hay cùng bạn bè, cà phê mang ý nghĩa văn hóa vượt xa hương vị của nó."
    },
    {
        "q": "Chủ đề chính của đoạn văn là gì?",
        "opts": ["A. Văn bản đánh máy tốt hơn viết tay", "B. Viết tay vẫn quan trọng cho việc học tập", "C. Công nghệ đang thay đổi hệ thống giáo dục", "D. Học sinh thích sử dụng máy tính xách tay hơn"],
        "passage": "Nhiều người nghĩ rằng viết tay không còn quan trọng trong thời đại kỹ thuật số. Học sinh thường ghi chú trên máy tính xách tay và hầu hết các tin nhắn đều được gõ. Ngay cả các tài liệu chính thức cũng được tạo và ký điện tử. Tuy nhiên, một số chuyên gia lập luận rằng viết tay giúp cải thiện trí nhớ, sự tập trung và việc học. Bất chấp công nghệ hiện đại, viết tay vẫn đóng một vai trò quan trọng trong giáo dục và phát triển nhận thức."
    },
    {
        "q": "Mục đích chính của đoạn văn là gì?",
        "opts": ["A. Thảo luận về lợi ích của canh tác đô thị", "B. Giải thích cách trồng rau trong thành phố", "C. So sánh canh tác đô thị và nông thôn", "D. Khuyến khích mọi người ăn thực phẩm tươi"],
        "passage": "Canh tác đô thị ngày càng trở nên phổ biến trong những năm gần đây. Với không gian hạn chế ở các thành phố, mọi người đang sử dụng sân thượng, ban công và vườn cộng đồng để trồng rau và trái cây. Phong trào này không chỉ cung cấp thực phẩm tươi sống mà còn thúc đẩy lối sống bền vững và củng cố mối quan hệ cộng đồng. Khi ngày càng có nhiều người nhận thức được các vấn đề môi trường, canh tác đô thị đưa ra một giải pháp thiết thực để cải thiện cả sức khỏe và hành tinh."
    },
    {
        "q": "Đoạn văn chủ yếu nói về điều gì?",
        "opts": ["A. Lợi ích của mạng xã hội", "B. Làm thế nào internet thay đổi giao tiếp", "C. Tác động tiêu cực của các cuộc gọi video", "D. Lịch sử giao tiếp của con người"],
        "passage": "Việc phát minh ra internet đã hoàn toàn thay đổi cách mọi người giao tiếp. Trước đây, việc gửi một tin nhắn có thể mất vài ngày hoặc thậm chí vài tuần, nhưng bây giờ chỉ mất vài giây. Phương tiện truyền thông xã hội, email và cuộc gọi video đã giúp mọi người dễ dàng giữ liên lạc trên toàn cầu. Tuy nhiên, một số chuyên gia lo lắng rằng giao tiếp trực tuyến làm giảm chất lượng của các tương tác ngoài đời thực."
    },
    {
        "q": "Ý chính của đoạn văn là gì?",
        "opts": ["A. Sách từng quá đắt trước thế kỷ 15", "B. Máy in đã biến đổi cách sản xuất và lan truyền thông tin", "C. Johannes Gutenberg là một nhà phát minh có ảnh hưởng ở châu Âu", "D. Sản xuất hàng loạt đã làm giảm chi phí của sách khoa học"],
        "passage": "Được phát minh vào thế kỷ 15 bởi Johannes Gutenberg, máy in đã cách mạng hóa cách chia sẻ thông tin. Trước khi nó ra đời, sách được chép tay, khiến chúng hiếm và đắt đỏ. Máy in cho phép sản xuất hàng loạt các văn bản, làm giảm mạnh chi phí của chúng. Sự đổi mới này đã làm tăng tỷ lệ biết chữ trên khắp châu Âu và tạo điều kiện cho sự lan truyền của những tư tưởng triết học và khoa học mới."
    },
    {
        "q": "Đoạn văn chủ yếu nói về điều gì?",
        "opts": ["A. Phương pháp ong sử dụng để lấy mật hoa", "B. Tầm quan trọng của loài ong trong thụ phấn và nguồn cung cấp thực phẩm toàn cầu", "C. Cách thực vật hoang dã sinh sản trong môi trường tự nhiên", "D. Sự suy giảm của quần thể ong trong nông nghiệp hiện đại"],
        "passage": "Loài ong đóng một vai trò quan trọng trong việc duy trì sự cân bằng của hệ sinh thái chúng ta thông qua sự thụ phấn. Khi bay từ hoa này sang hoa khác để lấy mật, chúng chuyển phấn hoa, giúp thực vật sinh sản. Quá trình này không chỉ cần thiết cho sự sống còn của thực vật hoang dã mà còn đối với nông nghiệp toàn cầu. Thực tế, người ta ước tính rằng một phần ba nguồn cung cấp thực phẩm của con người phụ thuộc vào quá trình thụ phấn của ong và các loài côn trùng khác."
    },
    {
        "q": "Câu nào tóm tắt tốt nhất ý chính của đoạn văn?",
        "opts": ["A. Endorphins là những hóa chất giúp giảm đau và cải thiện tâm trạng", "B. Tập thể dục thường xuyên rất có lợi cho sức khỏe tinh thần", "C. Hoạt động thể chất là phương pháp điều trị trầm cảm hiệu quả nhất", "D. Các chuyên gia y tế khuyên tập thể dục để xây dựng thể lực"],
        "passage": "Mặc dù những lợi ích về thể chất của việc tập thể dục thường xuyên đã được nhiều người biết đến, tác động tích cực của nó đối với sức khỏe tinh thần cũng sâu sắc không kém. Tham gia hoạt động thể chất giải phóng endorphin, những hóa chất tự nhiên trong não giúp giảm đau và cải thiện tâm trạng. Các bài tập thể dục thường xuyên đã được chứng minh là làm giảm các triệu chứng trầm cảm, giảm mức độ căng thẳng và nâng cao lòng tự trọng. Do đó, nhiều chuyên gia y tế khuyên tập thể dục như một phương pháp điều trị tự nhiên cho các vấn đề tâm lý khác nhau."
    },
    {
        "q": "Ý chính của đoạn văn là gì?",
        "opts": ["A. Những người tối giản tiết kiệm được nhiều tiền bằng cách không mua của cải vật chất", "B. Dọn dẹp nhà cửa là cách tốt nhất để giảm căng thẳng hàng ngày", "C. Chủ nghĩa tối giản là một lối sống tập trung vào việc tìm kiếm ý nghĩa bằng cách cắt giảm những thứ dư thừa", "D. Những trải nghiệm và mối quan hệ đắt giá hơn của cải vật chất"],
        "passage": "Chủ nghĩa tối giản là một lựa chọn lối sống tập trung vào việc chỉ sống với những thứ bạn thực sự cần. Bằng cách dọn dẹp nhà cửa và loại bỏ tài sản không cần thiết, những người theo chủ nghĩa tối giản nhằm mục đích giảm bớt căng thẳng và gánh nặng tài chính. Cách tiếp cận cuộc sống này khuyến khích mọi người coi trọng các trải nghiệm và mối quan hệ hơn là của cải vật chất. Cuối cùng, chủ nghĩa tối giản không chỉ là việc sở hữu ít đồ đạc hơn, mà là dành chỗ cho nhiều ý nghĩa và niềm vui hơn trong cuộc sống hằng ngày."
    },
    {
        "q": "Đoạn văn chủ yếu thảo luận điều gì?",
        "opts": ["A. Sự đa dạng của các loài sinh vật biển sống ở rạn san hô", "B. Các rạn san hô được xây dựng như thế nào theo thời gian bởi các polyp san hô", "C. Sự tương đồng giữa rừng nhiệt đới và rạn san hô", "D. Vòng đời và thói quen ăn uống của các polyp san hô"],
        "passage": "Các rạn san hô thường được gọi là rừng nhiệt đới của biển cả vì sự đa dạng sinh học đáng kinh ngạc của chúng. Những cấu trúc khổng lồ này thực chất được xây dựng bởi những sinh vật biển nhỏ bé gọi là polyp san hô. Khi những polyp này chết đi, bộ xương đá vôi cứng của chúng vẫn còn lại, và những thế hệ polyp mới phát triển trên bề mặt của chúng. Trải qua hàng nghìn năm, vòng tuần hoàn sinh tử liên tục này tạo ra những hệ sinh thái rạn san hô rộng lớn, đầy màu sắc, nuôi dưỡng hàng nghìn loài sinh vật biển ngày nay."
    },
    {
        "q": "Mục đích chính của đoạn văn là gì?",
        "opts": ["A. Giải thích cách lụa và gia vị được vận chuyển từ Trung Quốc đến châu Âu", "B. Mô tả sự xây dựng vật lý của mạng lưới Con đường Tơ lụa", "C. Nêu bật vai trò của Con đường Tơ lụa trong việc tạo điều kiện cho cả giao thương và giao lưu văn hóa", "D. Lập luận rằng các đổi mới công nghệ có giá trị hơn kim loại quý"],
        "passage": "Con đường Tơ lụa không phải là một con đường lát đá duy nhất, mà là một mạng lưới phức tạp các tuyến đường thương mại kết nối phương Đông và phương Tây. Bắt nguồn từ Trung Quốc, nó tạo điều kiện cho sự trao đổi hàng hóa như lụa, gia vị và kim loại quý. Tuy nhiên, tác động sâu sắc nhất của nó là sự giao lưu văn hóa mà nó thúc đẩy. Tôn giáo, triết lý và các đổi mới công nghệ đã du hành theo những tuyến đường này, định hình một cách cơ bản sự phát triển của các nền văn minh khắp châu Á, Trung Đông và châu Âu."
    }
]

for i, prac in enumerate(data['dang-01']['practices']):
    if i < len(translations):
        t = translations[i]
        prac['translationQuestion'] = t['q']
        prac['translationOptions'] = t['opts']
        prac['translationPassage'] = t['passage']

new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
lines = new_json_str.split('\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
indented_json_str = '\n'.join(indented_lines)

# Now, we also need to modify the JS in index.html to remove the Promise.all logic
js_to_replace = """                const translationPromises = [
                    translateWordENtoVI(prac.passage),
                    translateWordENtoVI(prac.question),
                    ...prac.options.map(opt => translateWordENtoVI(opt.replace(/^[A-D]\\.\\s*/, '')))
                ];
                
                Promise.all(translationPromises).then(([translatedPassage, translatedQuestion, ...translatedOptions]) => {
                    transBox.innerHTML = `
                        <h5 style="font-weight: 700; color: var(--primary-color); margin-bottom: 8px; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;"><i class="fa-solid fa-language"></i> BẢN DỊCH CHI TIẾT (TRANSLATIONS)</h5>
                        <div style="margin-bottom: 8px; font-size: 0.85rem; line-height: 1.4;">
                            <strong>Dịch câu hỏi:</strong> ${translatedQuestion || prac.question}
                        </div>
                        <div style="margin-bottom: 8px; font-size: 0.85rem; line-height: 1.4;">
                            <strong>Dịch các phương án lựa chọn:</strong>
                            <ul style="list-style: none; padding-left: 10px; margin-top: 4px; margin-bottom: 0;">
                                ${translatedOptions.map((optTrans, optIdx) => {
                                    const isCorrect = optIdx === prac.correctIdx;
                                    const letter = String.fromCharCode(65 + optIdx);
                                    const rawOpt = prac.options[optIdx].replace(/^[A-D]\\.\\s*/, '');
                                    let transText = optTrans || rawOpt;
                                    
                                    // Remove any potential double prefix returned by translator
                                    transText = transText.replace(/^[A-D]\\s*[\\.\\s-]\\s*/i, '');
                                    
                                    if (isCorrect) {
                                        return \\`<li style="color: var(--success-color); font-weight: bold; margin-bottom: 4px;"><i class="fa-solid fa-circle-check" style="font-size: 0.75rem;"></i> ${letter}. ${transText}</li>\\`;
                                    } else {
                                        return \\`<li style="color: var(--text-muted); margin-bottom: 4px;"><i class="fa-solid fa-circle" style="font-size: 0.35rem; vertical-align: middle; margin-right: 4px;"></i> ${letter}. ${transText}</li>\\`;
                                    }
                                }).join('')}
                            </ul>
                        </div>
                        <div style="font-size: 0.85rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; line-height: 1.4; text-align: justify;">
                            <strong>Dịch đoạn văn:</strong><br/>
                            <span style="color: var(--text-muted); font-style: italic;">${translatedPassage || prac.passage}</span>
                        </div>
                    `;
                }).catch(err => {
                    console.error("Translation fail:", err);
                    transBox.innerHTML = "<div style='font-size:0.85rem; color:var(--error-color);'>Không thể tải bản dịch tự động.</div>";
                });"""

js_replacement = """                
                const translatedPassage = prac.translationPassage || prac.passage;
                const translatedQuestion = prac.translationQuestion || prac.question;
                const translatedOptions = prac.translationOptions || prac.options.map(opt => opt.replace(/^[A-D]\\.\\s*/, ''));

                transBox.innerHTML = `
                    <h5 style="font-weight: 700; color: var(--primary-color); margin-bottom: 8px; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;"><i class="fa-solid fa-language"></i> BẢN DỊCH CHI TIẾT (TRANSLATIONS)</h5>
                    <div style="margin-bottom: 8px; font-size: 0.85rem; line-height: 1.4;">
                        <strong>Dịch câu hỏi:</strong> ${translatedQuestion}
                    </div>
                    <div style="margin-bottom: 8px; font-size: 0.85rem; line-height: 1.4;">
                        <strong>Dịch các phương án lựa chọn:</strong>
                        <ul style="list-style: none; padding-left: 10px; margin-top: 4px; margin-bottom: 0;">
                            ${translatedOptions.map((optTrans, optIdx) => {
                                const isCorrect = optIdx === prac.correctIdx;
                                const letter = String.fromCharCode(65 + optIdx);
                                let transText = optTrans;
                                
                                transText = transText.replace(/^[A-D]\\s*[\\.\\s-]\\s*/i, '');
                                
                                if (isCorrect) {
                                    return \\`<li style="color: var(--success-color); font-weight: bold; margin-bottom: 4px;"><i class="fa-solid fa-circle-check" style="font-size: 0.75rem;"></i> ${letter}. ${transText}</li>\\`;
                                } else {
                                    return \\`<li style="color: var(--text-muted); margin-bottom: 4px;"><i class="fa-solid fa-circle" style="font-size: 0.35rem; vertical-align: middle; margin-right: 4px;"></i> ${letter}. ${transText}</li>\\`;
                                }
                            }).join('')}
                        </ul>
                    </div>
                    <div style="font-size: 0.85rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; line-height: 1.4; text-align: justify;">
                        <strong>Dịch đoạn văn:</strong><br/>
                        <span style="color: var(--text-muted); font-style: italic;">${translatedPassage}</span>
                    </div>
                `;
"""

new_content = content[:match.start(1)] + indented_json_str + content[match.end(1):]

# Also remove the specific transBox.innerHTML loading spinner logic before this block
spinner_code = """                transBox.innerHTML = "<div style='font-size:0.85rem; color:var(--text-muted);'><i class='fa-solid fa-spinner fa-spin'></i> Đang tự động dịch chi tiết...</div>";
                transBox.classList.remove('hidden');"""
spinner_replacement = "                transBox.classList.remove('hidden');"
new_content = new_content.replace(spinner_code, spinner_replacement)

if js_to_replace in new_content:
    new_content = new_content.replace(js_to_replace, js_replacement)
else:
    print("Warning: Could not find exact JS replacement block.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected translations and disabled MyMemory API limits for Dạng 01!")
