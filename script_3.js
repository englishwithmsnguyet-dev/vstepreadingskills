
let preferredVoice = null;
function loadVoices() {
    const voices = window.speechSynthesis.getVoices();
    // Prioritize high-quality, natural-sounding voices across OS (Google, Apple, Microsoft)
    const premiumNames = [
        'Google US English', 'Google UK English Female', 
        'Samantha', 'Daniel', 'Karen', 'Tessa', 
        'Microsoft Zira', 'Microsoft Aria', 'Microsoft Guy'
    ];
    
    for (const name of premiumNames) {
        preferredVoice = voices.find(v => v.name.includes(name));
        if (preferredVoice) break;
    }
    
    // Fallback to any en-US or en-GB if premium not found
    if (!preferredVoice) {
        preferredVoice = voices.find(v => v.lang.startsWith('en')) || null;
    }
}

// Voices load asynchronously in some browsers (like Chrome)
if (window.speechSynthesis) {
    loadVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = loadVoices;
    }
}

document.addEventListener('click', function(e) {
    const btn = e.target.closest('.vocab-audio-btn');
    if (btn) {
        const word = btn.getAttribute('data-word');
        if (word && window.speechSynthesis) {
            window.speechSynthesis.cancel(); // Reset
            
            const utterance = new SpeechSynthesisUtterance(word);
            utterance.lang = 'en-US';
            utterance.rate = 0.9;
            utterance.pitch = 1.05; // Slightly higher pitch often sounds more natural
            
            if (preferredVoice) {
                utterance.voice = preferredVoice;
            }
            
            const origColor = btn.style.color;
            btn.style.color = '#10b981'; // Active reading state
            btn.classList.add('fa-fade'); 
            
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
