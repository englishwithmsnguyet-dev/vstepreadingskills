# -*- coding: utf-8 -*-
import sys

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The specific block to remove
target = """                const translationPromises = [
                    translateWordENtoVI(prac.passage),
                    translateWordENtoVI(prac.question),
                    ...prac.options.map(opt => translateWordENtoVI(opt.replace(/^[A-D]\.\s*/, '')))
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
                                    const rawOpt = prac.options[optIdx].replace(/^[A-D]\.\s*/, '');
                                    let transText = optTrans || rawOpt;
                                    
                                    // Remove any potential double prefix returned by translator
                                    transText = transText.replace(/^[A-D]\s*[\.\s-]\s*/i, '');
                                    
                                    if (isCorrect) {
                                        return `<li style="color: var(--success-color); font-weight: bold; margin-bottom: 4px;"><i class="fa-solid fa-circle-check" style="font-size: 0.75rem;"></i> ${letter}. ${transText}</li>`;
                                    } else {
                                        return `<li style="color: var(--text-muted); margin-bottom: 4px;"><i class="fa-solid fa-circle" style="font-size: 0.35rem; vertical-align: middle; margin-right: 4px;"></i> ${letter}. ${transText}</li>`;
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

replacement = """                const translatedPassage = prac.translationPassage || prac.passage;
                const translatedQuestion = prac.translationQuestion || prac.question;
                const translatedOptions = prac.translationOptions || prac.options.map(opt => opt.replace(/^[A-D]\.\s*/, ''));

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
                                transText = transText.replace(/^[A-D]\s*[\.\s-]\s*/i, '');
                                if (isCorrect) {
                                    return \`<li style="color: var(--success-color); font-weight: bold; margin-bottom: 4px;"><i class="fa-solid fa-circle-check" style="font-size: 0.75rem;"></i> ${letter}. ${transText}</li>\`;
                                } else {
                                    return \`<li style="color: var(--text-muted); margin-bottom: 4px;"><i class="fa-solid fa-circle" style="font-size: 0.35rem; vertical-align: middle; margin-right: 4px;"></i> ${letter}. ${transText}</li>\`;
                                }
                            }).join('')}
                        </ul>
                    </div>
                    <div style="font-size: 0.85rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; line-height: 1.4; text-align: justify;">
                        <strong>Dịch đoạn văn:</strong><br/>
                        <span style="color: var(--text-muted); font-style: italic;">${translatedPassage}</span>
                    </div>
                `;"""

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacement successful!")
else:
    print("Target not found. Doing fuzzy match...")
    import re
    # Match from const translationPromises to catch(err => { ... });
    pattern = r"const translationPromises = \[.*?\];\s*Promise\.all\(translationPromises\)\.then\(\(\[.*?\]\) => \{.*?\n\s*\}\)\.catch\(err => \{.*?\n\s*\}\);"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + replacement + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fuzzy replacement successful!")
    else:
        print("Fuzzy match failed too.")
