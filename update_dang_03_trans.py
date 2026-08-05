# -*- coding: utf-8 -*-
import json
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(\"dang-03\":\s*\{.*?\"practices\":\s*)(\[.*?\])(\s*\}\s*,\s*\"dang-04\")'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("Could not find dang-03 practices.")
    exit(1)

prefix = match.group(1)
practices_str = match.group(2)
suffix = match.group(3)

translations = [
    {
        "translationPassage": "Trong lớp học tiếng Anh, cô giáo Helen muốn làm cho bài học ngữ pháp bớt nhàm chán. Cô đã chia sẻ một vài <strong>giai thoại</strong>, hoặc những câu chuyện ngắn về thời gian cô du học ở London. Những trải nghiệm cá nhân hài hước này đã khiến học sinh bật cười và nhớ bài tốt hơn.",
        "translationQuestion": "Từ 'anecdotes' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. những bài học dài", "B. những câu chuyện ngắn", "C. những câu hỏi khó", "D. những quy tắc mới"]
    },
    {
        "translationPassage": "Khi chuẩn bị cho bài kiểm tra cuối kỳ, Linh cực kỳ <strong>thận trọng</strong>. Cô ấy kiểm tra từng câu trả lời trong bài kiểm tra của mình rất cẩn thận trước khi nộp cho giáo viên. Ngược lại, Tom khá cẩu thả, thường hoàn thành bài kiểm tra trong 10 phút và mắc nhiều lỗi chính tả.",
        "translationQuestion": "Từ 'cautious' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. cẩn thận", "B. vui vẻ", "C. nhanh nhẹn", "D. cẩu thả"]
    },
    {
        "translationPassage": "Trong những năm gần đây, các hiệu sách truyền thống trong thành phố đã chứng kiến sự <strong>sụt giảm</strong> dần về doanh số. Điều này chủ yếu là do nhiều độc giả trẻ thích mua sách kỹ thuật số trực tuyến hơn. Do sự sụt giảm doanh thu này, ba hiệu sách địa phương đã đóng cửa vĩnh viễn.",
        "translationQuestion": "Từ 'decline' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. sự gia tăng", "B. sự sụt giảm", "C. sự thành công", "D. sự mở rộng"]
    },
    {
        "translationPassage": "Sau khi làm việc chăm chỉ trong sáu tháng, đội ngũ phần mềm trẻ tuổi cuối cùng đã sẵn sàng <strong>ra mắt</strong> ứng dụng di động học ngôn ngữ mới của họ. Họ đã tổ chức một sự kiện lớn để giới thiệu ứng dụng với công chúng. Hàng ngàn học sinh đã tải nó về trong ngày đầu tiên.",
        "translationQuestion": "Từ 'launch' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. phá hủy", "B. che giấu", "C. bắt đầu/ra mắt", "D. lãng quên"]
    },
    {
        "translationPassage": "Mặc dù Nam đã trượt bài kiểm tra lái xe hai lần, anh ấy vẫn <strong>kiên quyết</strong> và từ chối bỏ cuộc. Anh ấy thực hành lái xe vào mỗi cuối tuần với anh trai mình và thử lại. Cuối cùng, nỗ lực kiên trì của anh ấy đã được đền đáp và anh ấy đã lấy được bằng lái xe.",
        "translationQuestion": "Từ 'determined' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. kiên trì", "B. lười biếng", "C. bối rối", "D. thất vọng"]
    },
    {
        "translationPassage": "Chiếc điện thoại thông minh mới có màn hình hoàn toàn <strong>trong suốt</strong>, không giống như các mẫu cũ có kính cứng, tối màu. Màn hình hiển thị rõ ràng này cho phép người dùng nhìn xuyên qua điện thoại để thấy bàn tay của họ đang cầm nó.",
        "translationQuestion": "Từ 'transparent' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. trong suốt/rõ ràng", "B. nặng nề", "C. đầy màu sắc", "D. vỡ"]
    },
    {
        "translationPassage": "Nhiều bác sĩ khuyên mọi người nên tiêu thụ nhiều nước và rau quả để duy trì sức khỏe. Hơn nữa, việc ngủ đủ giấc cũng rất <strong>quan trọng</strong>. Nếu không được nghỉ ngơi đầy đủ, cơ thể con người không thể hoạt động bình thường hoặc phục hồi sau một ngày làm việc dài.",
        "translationQuestion": "Từ 'vital' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. vô ích", "B. đắt đỏ", "C. quan trọng", "D. có hại"]
    },
    {
        "translationPassage": "Trong khi một số loài chim di cư đến các khu vực ấm áp hơn vào mùa đông, những loài khác lại là loài <strong>bản địa</strong> ở các vùng núi lạnh và ở lại đó quanh năm. Những loài chim bản địa này có bộ lông dày đặc biệt để bảo vệ chúng khỏi tuyết rơi lạnh giá.",
        "translationQuestion": "Từ 'indigenous' trong đoạn văn có nghĩa gần nhất với:",
        "translationOptions": ["A. ngoại lai", "B. bản địa", "C. nguy hiểm", "D. xinh đẹp"]
    }
]

parts = practices_str.split('"passage":')
if len(parts) - 1 != len(translations):
    print(f"Error: expected 8 practices, found {len(parts) - 1}")
    exit(1)

new_practices_str = parts[0]
for i in range(1, len(parts)):
    trans = translations[i-1]
    trans_json = f'"translationPassage": {json.dumps(trans["translationPassage"])}, "translationQuestion": {json.dumps(trans["translationQuestion"])}, "translationOptions": {json.dumps(trans["translationOptions"])}, \n                    '
    new_practices_str += trans_json + '"passage":' + parts[i]

new_content = content[:match.start()] + prefix + new_practices_str + suffix + content[match.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected translations for Dạng 03!")
