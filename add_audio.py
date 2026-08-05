# -*- coding: utf-8 -*-
import os
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update vocabulary items to include the audio button
# Target regex looks for the exact format we injected in the previous step
pattern = r'<li><strong>(.*?)</strong> <span style=\\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\\">(.*?)</span>:\s*(.*?)</li>'

def replace_with_audio(match):
    word = match.group(1)
    phonetic = match.group(2)
    meaning = match.group(3)
    
    # We add the speaker icon right after the word
    # Escaping double quotes inside the string for valid JSON injection
    return f'<li><strong>{word}</strong> <i class=\\"fa-solid fa-volume-high vocab-audio-btn\\" data-word=\\"{word}\\" style=\\"cursor: pointer; color: #3b82f6; margin-left: 6px; font-size: 0.95rem;\\" title=\\"Nghe phát âm\\"></i> <span style=\\"color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;\\">{phonetic}</span>: {meaning}</li>'

new_content = re.sub(pattern, replace_with_audio, content)

# 2. Inject TTS JavaScript logic before </body>
tts_script = """
<!-- TTS Vocabulary Audio Logic -->
<script>
document.addEventListener('click', function(e) {
    const btn = e.target.closest('.vocab-audio-btn');
    if (btn) {
        const word = btn.getAttribute('data-word');
        if (word && window.speechSynthesis) {
            // Cancel any ongoing speech
            window.speechSynthesis.cancel();
            
            const utterance = new SpeechSynthesisUtterance(word);
            utterance.lang = 'en-US';
            utterance.rate = 0.9; // Slightly slower for better clarity for learners
            
            // Add a temporary animation to the icon
            const origColor = btn.style.color;
            btn.style.color = '#10b981'; // Green while speaking
            btn.classList.add('fa-fade'); // FontAwesome fade animation
            
            utterance.onend = () => { 
                btn.style.color = origColor; 
                btn.classList.remove('fa-fade');
            };
            utterance.onerror = () => { 
                btn.style.color = origColor; 
                btn.classList.remove('fa-fade');
            };
            
            window.speechSynthesis.speak(utterance);
        }
    }
});
</script>
</body>"""

if '<!-- TTS Vocabulary Audio Logic -->' not in new_content:
    new_content = new_content.replace('</body>', tts_script)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Total words upgraded with audio button:", sum(1 for _ in re.finditer(r'vocab-audio-btn', new_content)))
print("Successfully injected audio buttons and TTS script!")
