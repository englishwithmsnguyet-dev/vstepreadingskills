
// river-reading-academy script.js

// 1. Initial State
const state = {
    studentName: "",
    progress: {
        overview: true,
        skimmingTheory: false,
        scanningTheory: false,
        synonymLab: false,
        mockExam: false
    },
    miniPractices: {
        completedCount: 0,
        totalCount: 28 // 7 Types * 4 Practices
    },
    tooltipJustShown: false,
    eyeTracker: {
        active: false,
        timeoutIds: []
    },
    keywordGame: {
        selectedCard: null,
        score: 0,
        selectedSkimIdx: null,
        selectedScanIdx: null
    },
    vocabQuiz: {
        questions: [],
        currentIdx: 0,
        score: 0
    },
    synonymGame: {
        selectedQ: null,
        matches: 0
    },
    mockExam: {
        active: false,
        currentPassageIdx: 0,
        currentQuestionIndex: 0,
        answers: {}, // Question index -> selected letter
        submitted: false,
        score: 0,
        timerInterval: null,
        timeLeft: 900 // 15 minutes
    },
    vocabTest: {
        active: false,
        currentIndex: 0
    },
    savedWords: []
};

// 2. DOM Elements Mapping
const elements = {
    nameModal: document.getElementById('name-modal'),
    nameInput: document.getElementById('student-name-input'),
    startBtn: document.getElementById('start-lesson-btn'),
    studentDisplay: document.getElementById('student-name-display'),
    displayName: document.getElementById('display-name'),
    cockpitStudentName: document.getElementById('cockpit-student-name'),
    
    certModal: document.getElementById('certificate-modal'),
    certStudentName: document.getElementById('cert-student-name'),
    certScore: document.getElementById('cert-score'),
    closeCertBtn: document.getElementById('close-cert-btn'),
    shareCertBtn: document.getElementById('share-cert-btn'),
    
    themeToggle: document.getElementById('theme-toggle'),
    sidebarProgress: document.getElementById('sidebar-progress-bar'),
    progressText: document.getElementById('progress-text'),
    
    statsProgress: document.getElementById('stats-progress'),
    statsSpeed: document.getElementById('stats-speed'),
    statsAccuracy: document.getElementById('stats-accuracy'),
    statsVocab: document.getElementById('stats-vocab'),
    
    gazePoint: document.getElementById('gaze-point'),
    eyeLines: document.querySelectorAll('.eye-passage-line'),
    
    wordBankCount: document.getElementById('word-bank-count'),
    wordBankContainer: document.getElementById('word-bank-container'),
    emptyBankMessage: document.getElementById('empty-bank-message'),
    vocabActionsPanel: document.getElementById('vocab-actions-panel'),
    resetVocabBtn: document.getElementById('reset-vocab-btn'),
    
    vocabTooltip: document.getElementById('vocab-tooltip'),
    tooltipWord: document.getElementById('tooltip-word'),
    tooltipPos: document.getElementById('tooltip-pos'),
    tooltipPhonetic: document.getElementById('tooltip-phonetic'),
    tooltipMean: document.getElementById('tooltip-mean'),
    tooltipSaveBtn: document.getElementById('btn-tooltip-save'),
    tooltipSavedBadge: document.getElementById('tooltip-saved-badge'),
    tooltipSpeakBtn: document.getElementById('btn-tooltip-speak'),
    
    vocabTestBtn: document.getElementById('btn-vocab-test-mode'),
    vocabTestWidget: document.getElementById('flashcard-test-widget'),
    testFlashcard: document.getElementById('test-flashcard'),
    testCardInner: document.getElementById('test-card-inner'),
    testWordFront: document.getElementById('test-word-front'),
    testWordPhonetic: document.getElementById('test-word-phonetic'),
    testWordBack: document.getElementById('test-word-back'),
    testWordPos: document.getElementById('test-word-pos'),
    testWordMean: document.getElementById('test-word-mean'),
    testBtnFail: document.getElementById('test-btn-fail'),
    testBtnPass: document.getElementById('test-btn-pass'),
    testBtnClose: document.getElementById('btn-close-test-mode'),
    
    confettiCanvas: document.getElementById('confetti-canvas')
};

// 2.5 Predefined Vocabulary Database
const vocabData = {
    "remote work": {
        pos: "noun",
        phonetic: "/rɪˈməʊt wɜːk/",
        mean: "Hình thức làm việc từ xa thông qua công cụ công nghệ mà không cần đến văn phòng."
    },
    "commuting": {
        pos: "verb",
        phonetic: "/kəˈmjuːtɪŋ/",
        mean: "Sự di chuyển đi lại thường xuyên hàng ngày giữa nơi ở và nơi làm việc."
    },
    "modern technology": {
        pos: "noun",
        phonetic: "/ˈmɒdn tekˈnɒlədʒi/",
        mean: "Các công cụ, hệ thống phần cứng và phần mềm kỹ thuật số hiện đại phục vụ công việc."
    },
    "comfortable": {
        pos: "adjective",
        phonetic: "/ˈkʌmftəbl/",
        mean: "Thoải mái, dễ chịu về mặt thể chất hoặc tinh thần."
    },
    "productive": {
        pos: "adjective",
        phonetic: "/prəˈdʌktɪv/",
        mean: "Đạt năng suất cao, tạo ra nhiều giá trị, làm việc hiệu quả."
    },
    "drawback": {
        pos: "noun",
        phonetic: "/ˈdrɔːbæk/",
        mean: "Điểm hạn chế, nhược điểm, mặt tiêu cực của một vấn đề."
    },
    "popularity": {
        pos: "noun",
        phonetic: "/ˌpɒpjuˈlærəti/",
        mean: "Sự phổ biến, xu hướng được đông đảo mọi người ưa chuộng và hưởng ứng."
    },
    "private vehicles": {
        pos: "noun",
        phonetic: "/ˈpraɪvət ˈviːəklz/",
        mean: "Các loại phương tiện giao thông thuộc sở hữu cá nhân (như ô tô, xe máy)."
    },
    "air pollution": {
        pos: "noun",
        phonetic: "/eə pəˈluːʃn/",
        mean: "Sự nhiễm bẩn không khí bởi chất độc hại hoặc khí thải từ xe cộ, nhà máy."
    },
    "congestion": {
        pos: "noun",
        phonetic: "/kənˈdʒestʃən/",
        mean: "Tình trạng tắc nghẽn, kẹt xe khi lượng phương tiện vượt quá khả năng lưu thông."
    },
    "investing": {
        pos: "verb",
        phonetic: "/ɪnˈvestɪŋ/",
        mean: "Hành động đầu tư tiền bạc, công sức vào dự án để thu lại lợi ích lâu dài."
    },
    "affordable": {
        pos: "adjective",
        phonetic: "/əˈfɔːdəbl/",
        mean: "Giá cả phải chăng, vừa phải, phù hợp với khả năng chi trả của đa số mọi người."
    },
    "sustainable": {
        pos: "adjective",
        phonetic: "/səˈsteɪnəbl/",
        mean: "Bền vững, có khả năng duy trì lâu dài mà không gây hại cho môi trường."
    },
    "memorial": {
        pos: "noun",
        phonetic: "/məˈmɔːriəl/",
        mean: "Đài kỷ niệm, công trình tưởng niệm hoặc ghi nhớ một người hay sự kiện."
    },
    "sculpture": {
        pos: "noun",
        phonetic: "/ˈskʌlptʃə(r)/",
        mean: "Tác phẩm điêu khắc bằng đá, gỗ, kim loại hoặc đất sét."
    },
    "conceived": {
        pos: "verb",
        phonetic: "/kənˈsiːvd/",
        mean: "Được hình thành, phác thảo ý tưởng từ ban đầu trong tâm trí."
    },
    "excavation": {
        pos: "noun",
        phonetic: "/ˌekskəˈveɪʃn/",
        mean: "Sự khai quật, hoạt động đào đất hoặc đục đá trong xây dựng/khảo cổ."
    },
    "subsidized": {
        pos: "verb",
        phonetic: "/ˈsʌbsɪdaɪzd/",
        mean: "Được hỗ trợ tài chính, được trợ cấp tiền từ chính phủ hoặc cơ quan chức năng."
    },
    "prestigious": {
        pos: "adjective",
        phonetic: "/preˈstɪdʒəs/",
        mean: "Uy tín, danh giá, được mọi người ngưỡng mộ và coi trọng."
    },
    "inaugural": {
        pos: "adjective",
        phonetic: "/ɪˈnɔːɡjərəl/",
        mean: "Thuộc buổi khai mạc, mở màn, lần đầu tiên được tổ chức chính thức."
    },
    "laureates": {
        pos: "noun",
        phonetic: "/ˈlɔːriəts/",
        mean: "Những người vinh dự đoạt giải thưởng lớn (như giải Nobel, giải thưởng học thuật)."
    },
    "milestone": {
        pos: "noun",
        phonetic: "/ˈmaɪlstəʊn/",
        mean: "Cột mốc quan trọng, giai đoạn phát triển có tính chất bước ngoặt lịch sử."
    },
    "breakthroughs": {
        pos: "noun",
        phonetic: "/ˈbreɪkθruːz/",
        mean: "Những phát kiến vĩ đại, bước đột phá mang tính cách mạng trong nghiên cứu."
    }
};

// 3. Audio Synthesizer (Using Web Audio API)
let audioCtx = null;

function playSound(type) {
    try {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        
        const now = audioCtx.currentTime;
        
        if (type === 'click') {
            osc.frequency.setValueAtTime(600, now);
            gainNode.gain.setValueAtTime(0.05, now);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.1);
            osc.start(now);
            osc.stop(now + 0.1);
        } else if (type === 'success') {
            osc.frequency.setValueAtTime(523.25, now); // C5
            osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
            osc.frequency.setValueAtTime(783.99, now + 0.16); // G5
            osc.frequency.setValueAtTime(1046.50, now + 0.24); // C6
            gainNode.gain.setValueAtTime(0.08, now);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
            osc.start(now);
            osc.stop(now + 0.45);
        } else if (type === 'fail') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(220, now);
            osc.frequency.linearRampToValueAtTime(110, now + 0.25);
            gainNode.gain.setValueAtTime(0.08, now);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        } else if (type === 'chime') {
            osc.frequency.setValueAtTime(880, now);
            gainNode.gain.setValueAtTime(0.03, now);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
            osc.start(now);
            osc.stop(now + 0.15);
        } else if (type === 'complete') {
            // Fanfare
            osc.frequency.setValueAtTime(440, now);
            osc.frequency.setValueAtTime(554.37, now + 0.12);
            osc.frequency.setValueAtTime(659.25, now + 0.24);
            osc.frequency.setValueAtTime(880, now + 0.36);
            gainNode.gain.setValueAtTime(0.1, now);
            gainNode.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
            osc.start(now);
            osc.stop(now + 0.6);
        }
    } catch (e) {
        console.warn("Audio Context not allowed or initialized", e);
    }
}

// 4. Student Name Profile Modal Sequence
function initStudentProfile() {
    elements.startBtn.addEventListener('click', () => {
        const nameVal = elements.nameInput.value.trim();
        if (!nameVal) {
            elements.nameInput.style.borderColor = 'var(--error-color)';
            playSound('fail');
            return;
        }
        
        state.studentName = nameVal;
        playSound('success');
        
        // Hide Modal
        elements.nameModal.classList.add('hidden');
        
        // Bind UI Displays
        elements.displayName.textContent = state.studentName;
        elements.cockpitStudentName.textContent = `Học viên: ${state.studentName}`;
        elements.studentDisplay.classList.remove('hidden');
        
        // Save Name in LocalStorage
        localStorage.setItem('vstep_student_name', state.studentName);
        
        // Warm up sound context
        if (audioCtx) audioCtx.resume();
    });
    
    // Auto-login if previously saved
    const savedName = localStorage.getItem('vstep_student_name');
    if (savedName) {
        state.studentName = savedName;
        elements.nameModal.classList.add('hidden');
        elements.displayName.textContent = state.studentName;
        elements.cockpitStudentName.textContent = `Học viên: ${state.studentName}`;
        elements.studentDisplay.classList.remove('hidden');
        
        // Auto-load saved progress details
        const savedProgress = localStorage.getItem('vstep_progress');
        if (savedProgress) {
            try {
                state.progress = JSON.parse(savedProgress);
            } catch (e) { console.error(e); }
        }
        
        const savedMiniPractices = localStorage.getItem('vstep_mini_practices');
        if (savedMiniPractices) {
            try {
                state.miniPractices = JSON.parse(savedMiniPractices);
            } catch (e) { console.error(e); }
        }
        
        const savedWordsList = localStorage.getItem('vstep_saved_vocab');
        if (savedWordsList) {
            try {
                state.savedWords = JSON.parse(savedWordsList);
                renderWordBankList(); // Update Word Bank UI list instantly!
            } catch (e) { console.error(e); }
        }
        
        const savedMockExam = localStorage.getItem('vstep_mock_exam');
        if (savedMockExam) {
            try {
                const mockData = JSON.parse(savedMockExam);
                state.mockExam.submitted = mockData.submitted;
                state.mockExam.score = mockData.score;
                state.mockExam.answers = mockData.answers || {};
            } catch (e) { console.error(e); }
        }
    }
}

// 5. Theme Switcher (Dark/Light Mode)
function initThemeSwitcher() {
    elements.themeToggle.addEventListener('click', () => {
        playSound('click');
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        elements.themeToggle.innerHTML = isDark ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
        localStorage.setItem('vstep_theme_dark', isDark ? 'true' : 'false');
    });
    
    // Read cached preferences
    const cachedDark = localStorage.getItem('vstep_theme_dark');
    if (cachedDark === 'true') {
        document.body.classList.add('dark-mode');
        elements.themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
    }
}

// 6. Sidebar Navigation & Tab Controller
function initSidebarNav() {
    const subNavLinks = document.querySelectorAll('.sub-nav-links a');
    const contentSections = document.querySelectorAll('.content-section');
    
    subNavLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            playSound('click');
            
            const targetId = link.getAttribute('href');
            const targetSec = document.querySelector(targetId);
            
            if (targetSec) {
                // Hide all main content views
                contentSections.forEach(sec => sec.classList.add('hidden'));
                
                // Show target view
                targetSec.classList.remove('hidden');
                
                // Dynamic Eye-Tracking & Heatmap Lab Portal
                const eyeLab = document.getElementById('eye-tracker-lab-root');
                if (eyeLab) {
                    if (targetId === '#sec-skimming') {
                        const placeholder = document.getElementById('skimming-lab-placeholder');
                        if (placeholder) {
                            placeholder.appendChild(eyeLab);
                            resetLabGazeDisplay();
                            const radSkim = document.querySelector('input[name="lab-mode"][value="skim"]');
                            if (radSkim) radSkim.checked = true;
                        }
                    } else if (targetId === '#sec-scanning') {
                        const placeholder = document.getElementById('scanning-lab-placeholder');
                        if (placeholder) {
                            placeholder.appendChild(eyeLab);
                            resetLabGazeDisplay();
                            const radScan = document.querySelector('input[name="lab-mode"][value="scan"]');
                            if (radScan) radScan.checked = true;
                        }
                    }
                }
                
                // Toggle active menu styles
                subNavLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
                
                // Keep progress state updated
                const sectionName = link.dataset.section;
                if (sectionName === 'skimming-theory') state.progress.skimmingTheory = true;
                if (sectionName === 'scanning-theory') state.progress.scanningTheory = true;
                if (sectionName === 'synonym-lab') state.progress.synonymLab = true;
                if (sectionName === 'mock-test') state.progress.mockExam = true;
                
                // Dynamic Chapter 2 Loader
                const dangId = link.dataset.dangId;
                if (dangId) {
                    loadDangDetail(dangId);
                }
                
                updateProgress();
                window.scrollTo(0, 0);
            }
        });
    });
    
    // Chapter Collapse Toggles
    const groupHeaders = document.querySelectorAll('.lesson-group-header');
    groupHeaders.forEach(header => {
        header.addEventListener('click', () => {
            playSound('click');
            const parent = header.parentElement;
            if (parent.classList.contains('locked')) return;
            parent.classList.toggle('active');
        });
    });
}

// Debugging error reporter
function reportError(err) {
    console.error(err);
    const div = document.createElement('div');
    div.style.position = 'fixed';
    div.style.top = '0';
    div.style.left = '0';
    div.style.width = '100%';
    div.style.background = '#ffe4e6';
    div.style.color = '#9f1239';
    div.style.padding = '16px';
    div.style.zIndex = '999999';
    div.style.borderBottom = '3px solid #fda4af';
    div.style.fontFamily = 'monospace';
    div.style.fontSize = '13px';
    div.style.whiteSpace = 'pre-wrap';
    div.innerHTML = `<strong>Lỗi Nội Bộ (Try-Catch):</strong> ${err.message}<br/><strong>Stack Trace:</strong><br/>${err.stack}`;
    document.body.appendChild(div);
}

// 7. Dynamic Chapter 2 Question Type Loader & Mini Quizzes
function loadDangDetail(dangId) {
    try {
        const data = dangsData[dangId];
        if (!data) return;
    
    // Set headers
    document.getElementById('dang-title').textContent = data.title;
    document.getElementById('dang-desc').textContent = data.description;
    document.getElementById('dang-icon').className = `fa-solid ${data.icon} section-icon`;
    
    // Theory tab population with premium formatting post-processor
    const theoryContainer = document.getElementById('dang-theory-content');
    theoryContainer.innerHTML = data.theory;
    formatTheoryHTML(theoryContainer, false); // true = discard static example duplication
    
    // Extract rich explanation HTML from theory string to keep in memory for interactive card
    let richExplanationHTML = "";
    const theoryHtml = data.theory;
    let expIndex = theoryHtml.indexOf('🔍');
    if (expIndex === -1) expIndex = theoryHtml.indexOf('Giải thích');
    if (expIndex !== -1) {
        richExplanationHTML = theoryHtml.substring(expIndex);
    }
    
    // Example tab population
    document.getElementById('dang-example-passage').innerHTML = `<blockquote>"${data.example.passage}"</blockquote>`;
    document.getElementById('dang-example-question').innerHTML = highlightQuestionKeywords(data.example.question);
    
    const exampleOptions = document.getElementById('dang-example-options');
    exampleOptions.innerHTML = '';
    
    const exampleExpBox = document.getElementById('dang-example-explanation-box');
    exampleExpBox.classList.add('hidden');
    
    data.example.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        const cleanOpt = opt.replace(/^[A-D]\.\s*/, '');
        btn.innerHTML = `<span class="option-letter">${String.fromCharCode(65 + idx)}</span> <span class="option-val">${cleanOpt}</span>`;
        btn.addEventListener('click', () => {
            playSound('click');
            // Disable options
            exampleOptions.querySelectorAll('.option-btn').forEach(b => b.setAttribute('disabled', 'true'));
            
            if (idx === data.example.correctIdx) {
                playSound('success');
                btn.classList.add('correct');
            } else {
                playSound('fail');
                btn.classList.add('incorrect');
                exampleOptions.children[data.example.correctIdx].classList.add('correct');
            }
            
            // Build and load super detailed explanation
            let fullExplanation = data.example.explanation;
            if (richExplanationHTML) {
                fullExplanation = `<p style="margin-bottom: 12px; font-weight:bold; color:var(--success-color);">${data.example.explanation}</p>${richExplanationHTML}`;
            }
            
            const expEl = document.getElementById('dang-example-explanation');
            expEl.innerHTML = fullExplanation;
            formatTheoryHTML(expEl, false); // false = do NOT discard anything, just format!
            
            exampleExpBox.classList.remove('hidden');
        });
        exampleOptions.appendChild(btn);
    });
    
    // Practice tab population (4 interactive exercises)
    const practicesContainer = document.getElementById('dang-practices-list');
    practicesContainer.innerHTML = '';
}

// Helper function to dynamically wrap core VSTEP terminology inside highlight chips
function highlightQuestionKeywords(qText) {
    if (!qText) return "";
    let html = qText;
    
    // Core question terms across all 7 Dạngs to highlight in purple
    const keywords = [
        // Dạng 1: Main Idea
        "main idea", "mainly discuss", "primarily about", "main point", 
        "purpose", "best title", "best summarizes", "most suitable headline", 
        "summarizes", "headline", "best for", "best", "title",
        // Dạng 2: Details
        "according to", "states that", "is stated", "is mentioned", 
        "say about", "is true", "true", "mentioned", "stated",
        // Dạng 3: Vocabulary / Reference
        "closest in meaning", "closest meaning", "replaced by", "refers to", 
        "refer to", "replace", "meaning", "means", "in line",
        // Dạng 4: Negative
        "NOT true", "NOT mentioned", "NOT stated", "EXCEPT", "NOT",
        // Dạng 5: Inference
        "inferred", "infer", "implied", "implies", "imply", "most likely", "probably mean", "probably",
        // Dạng 6: Attitude / Tone
        "attitude", "tone", "author's opinion", "opinion",
        // Dạng 7: Insertion
        "best fits", "best fit", "inserted", "added", "square", "space"
    ];
    
    // Sort by length descending to match longer keywords first
    keywords.sort((a, b) => b.length - a.length);
    
    keywords.forEach(keyword => {
        // Match word boundaries case-insensitively
        const regex = new RegExp(`\\b(${keyword})\\b`, 'gi');
        html = html.replace(regex, `<span class="q-keyword-highlight">$1</span>`);
    });
    
    // Also highlight placeholders like [số đoạn] or [số] in orange
    html = html.replace(/(\[số đoạn\]|\[số\]|\[biểu tượng ô vuông\])/g, `<span class="q-placeholder-highlight">$1</span>`);
    
    return html;
}

// Helper function to highlight academic strategies in Vietnamese texts
function highlightStrategyText(text) {
    if (!text) return "";
    let html = text;
    
    // Core key terms in VSTEP Reading to highlight in bold primary blue/green
    const primaryHighlights = [
        "đọc lướt", "skimming", "Skimming",
        "đọc quét", "scanning", "Scanning",
        "câu chủ đề", "topic sentence", "Topic sentence",
        "từ khóa", "keywords", "Keywords",
        "ý khái quát", "general ideas", "General ideas",
        "từ đồng nghĩa", "synonyms", "paraphrase", "paraphrased",
        "ý chính", "chủ đề chính", "tiêu đề",
        "câu đầu và câu cuối", "câu đầu", "câu cuối",
        "trọng tâm", "khái quát"
    ];
    
    // Distractors and exclusions to highlight in italic warning red/amber
    const warningHighlights = [
        "loại bỏ", "loại trừ", "gây nhiễu", "bẫy",
        "quá hẹp", "too narrow", "quá rộng", "too broad",
        "bị bóp méo", "not mentioned", "không có trong bài", "chi tiết nhỏ", "supporting details"
    ];
    
    // Sort by length descending to match longer phrases first
    primaryHighlights.sort((a, b) => b.length - a.length);
    warningHighlights.sort((a, b) => b.length - a.length);
    
    primaryHighlights.forEach(term => {
        const regex = new RegExp(`(${term})`, 'gi');
        html = html.replace(regex, `<strong style="color: var(--primary-color);">$1</strong>`);
    });
    
    warningHighlights.forEach(term => {
        const regex = new RegExp(`(${term})`, 'gi');
        html = html.replace(regex, `<strong style="color: var(--error-color); font-style: italic;">$1</strong>`);
    });
    
    return html;
}

// Helper function to format plain theory HTML dynamically into high-fidelity UI components
function formatTheoryHTML(container, discardExample = true) {
    const html = container.innerHTML;
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = html;
    
    const children = Array.from(tempDiv.childNodes);
    const newElements = [];
    let discardRemaining = false;
    let currentSection = "";
    
    children.forEach(el => {
        if (discardExample && discardRemaining) return;
        
        if (el.nodeType !== Node.ELEMENT_NODE) {
            newElements.push(el);
            return;
        }
        
        const text = el.textContent || "";
        
        // Detect and discard static Example block duplicate (as it has its own dedicated interactive Tab 2)
        if (discardExample && (text.toUpperCase().includes('VÍ DỤ MINH HỌA') || text.toUpperCase().includes('VÍ DỤ MINH HOẠ'))) {
            discardRemaining = true;
            return;
        }
        
        // Match Steps: "Bước 1:", "Bước 2:"
        if (el.tagName === 'P' && text.trim().startsWith('Bước')) {
            const match = text.match(/^Bước\s*(\d+)[:.]\s*(.*)/i);
            if (match) {
                const stepCard = document.createElement('div');
                stepCard.className = 'theory-step-card';
                stepCard.innerHTML = `
                    <span class="theory-step-badge">BƯỚC ${match[1]}</span>
                    <div class="theory-step-desc">${highlightStrategyText(match[2])}</div>
                `;
                newElements.push(stepCard);
                return;
            }
        }
        
        // Match warning or Lưu ý blocks
        if (text.includes('LƯU Ý:') || text.includes('📌')) {
            const cleanText = text.replace(/^(📌\s*LƯU\s*Ý|LƯU\s*Ý|📌|📌\s*LƯU\s*Ý\s*[:.-]*|LƯU\s*Ý\s*[:.-]*|📌\s*[:.-]*)/i, '').replace(/^[:\s-]*/, '').trim();
            const callout = document.createElement('div');
            callout.className = 'theory-callout-box';
            callout.innerHTML = `
                <div class="theory-callout-icon"><i class="fa-solid fa-circle-exclamation"></i></div>
                <div class="theory-callout-body">
                    <strong>LƯU Ý QUAN TRỌNG:</strong> ${highlightStrategyText(cleanText)}
                </div>
            `;
            newElements.push(callout);
            return;
        }
        
        // Match sub-instructions in Strategy section
        if (el.tagName === 'P' && currentSection === 'strategy') {
            const subStepCard = document.createElement('div');
            subStepCard.className = 'theory-sub-step-card';
            subStepCard.innerHTML = `<i class="fa-solid fa-circle-notch" style="font-size: 0.65rem; margin-top:5px; flex-shrink:0; color: var(--success-color);"></i> <div class="sub-step-desc">${highlightStrategyText(text.trim())}</div>`;
            newElements.push(subStepCard);
            return;
        }
        
        // Match English VSTEP question templates
        if (el.tagName === 'P' && (
            text.trim().endsWith('?') || 
            /^(What|Which|Who|Where|When|Why|How|According|The\s+word|The\s+passage|The\s+author|The\s+paragraph|All\s+of\s+the\s+following)/i.test(text.trim())
        )) {
            const questionCard = document.createElement('div');
            questionCard.className = 'theory-question-chip';
            questionCard.innerHTML = `<i class="fa-solid fa-circle-question"></i> <code>${highlightQuestionKeywords(text.trim())}</code>`;
            newElements.push(questionCard);
            return;
        }
        
        // Match intro lines ending in colon (e.g. "thường có dạng:")
        if (el.tagName === 'P' && text.trim().endsWith(':')) {
            const introEl = document.createElement('p');
            introEl.className = 'theory-intro-text';
            introEl.innerHTML = `<i class="fa-solid fa-hand-point-right"></i> <span>${text.trim()}</span>`;
            newElements.push(introEl);
            return;
        }
        
        // Match short Vietnamese bullet/checklist points
        if (el.tagName === 'P' && text.trim().length < 60 && /[àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i.test(text)) {
            const bulletCard = document.createElement('div');
            bulletCard.className = 'theory-bullet-card';
            bulletCard.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${text.trim()}</span>`;
            newElements.push(bulletCard);
            return;
        }
        
        // Match headers and style icons contextually
        if (el.tagName === 'H4' || el.classList.contains('theory-sub-title')) {
            const header = document.createElement('h4');
            if (text.includes('I. THÔNG TIN')) {
                currentSection = "info";
                header.className = 'theory-section-header header-blue';
                header.innerHTML = `<i class="fa-solid fa-circle-info header-icon"></i> I. THÔNG TIN CƠ BẢN`;
            } else if (text.includes('II. NHẬN DẠNG')) {
                currentSection = "identify";
                header.className = 'theory-section-header header-purple';
                header.innerHTML = `<i class="fa-solid fa-magnifying-glass header-icon"></i> II. NHẬN DẠNG CÂU HỎI`;
            } else if (text.includes('III. CÁCH THỨC') || text.includes('III. CHIẾN THUẬT')) {
                currentSection = "strategy";
                header.className = 'theory-section-header header-green';
                header.innerHTML = `<i class="fa-solid fa-route header-icon"></i> III. CHIẾN THUẬT LÀM BÀI`;
            } else if (text.includes('VÍ DỤ MINH HỌA') || text.includes('VÍ DỤ MINH HOẠ')) {
                currentSection = "example";
                header.className = 'theory-section-header header-orange';
                header.innerHTML = `<i class="fa-solid fa-chalkboard-user header-icon"></i> VÍ DỤ MINH HỌA THỰC TẾ`;
            } else {
                header.className = 'theory-section-header header-blue';
                header.innerHTML = `<i class="fa-solid fa-lightbulb header-icon"></i> ${text}`;
            }
            newElements.push(header);
            return;
        }
        
        // Match answer keys like ✅ Đáp án đúng:
        if (text.includes('✅') || text.includes('Đáp án đúng:')) {
            const cleanAns = text.replace(/[✅:]/g, '').replace('Đáp án đúng', '').trim();
            const ansBox = document.createElement('div');
            ansBox.className = 'theory-answer-card';
            ansBox.innerHTML = `
                <div class="ans-badge"><i class="fa-solid fa-circle-check"></i> ĐÁP ÁN ĐÚNG</div>
                <div class="ans-value">${cleanAns}</div>
            `;
            newElements.push(ansBox);
            return;
        }
        
        // Match explanation headers or sections
        if (text.includes('🔍') || text.includes('Giải thích chi tiết') || text.includes('Giải thích:')) {
            const explainHeader = document.createElement('h5');
            explainHeader.className = 'theory-explain-title';
            explainHeader.innerHTML = `<i class="fa-solid fa-wand-magic-sparkles"></i> PHÂN TÍCH & GIẢI THÍCH CHI TIẾT`;
            newElements.push(explainHeader);
            return;
        }
        
        // Match A, B, C, D options lists
        if (el.tagName === 'P' && text.trim().match(/^[A-D]\s*\.\s*(.*)/i)) {
            const optMatch = text.trim().match(/^([A-D])\s*\.\s*(.*)/i);
            const optCard = document.createElement('div');
            optCard.className = 'theory-option-card';
            optCard.innerHTML = `
                <span class="theory-opt-letter">${optMatch[1]}</span>
                <span class="theory-opt-text">${optMatch[2]}</span>
            `;
            newElements.push(optCard);
            return;
        }
        
        // Standard elements
        newElements.push(el);
    });
    
    // Clear and rebuild container
    container.innerHTML = '';
    newElements.forEach(newEl => {
        if (newEl instanceof Node) {
            container.appendChild(newEl);
        }
    });
    
    data.practices.forEach((prac, pIdx) => {
        const card = document.createElement('div');
        card.className = 'mini-practice-card';
        card.innerHTML = `
            <div class="practice-passage">"${prac.passage}"</div>
            <p class="practice-question"><strong>Bài tập ${pIdx + 1}:</strong> ${highlightQuestionKeywords(prac.question)}</p>
            <div class="mini-options"></div>
            <button class="primary-btn btn-sm hidden check-practice-btn" style="margin-top: 12px; width: 100%; padding: 8px; border: none; font-weight: bold; background: var(--primary-color); color: white; border-radius: 12px; cursor: pointer;">KIỂM TRA (CHECK)</button>
            <div class="mini-feedback hidden" style="margin-top: 12px;"></div>
            <div class="translation-box hidden" style="margin-top: 12px; padding: 10px; border-radius: var(--radius-sm); border: 1.5px dashed var(--border-color); background: var(--primary-light);"></div>
        `;
        
        const optionsContainer = card.querySelector('.mini-options');
        const feedbackEl = card.querySelector('.mini-feedback');
        const transBox = card.querySelector('.translation-box');
        const checkBtn = card.querySelector('.check-practice-btn');
        
        prac.options.forEach((opt, idx) => {
            const btn = document.createElement('button');
            btn.className = 'mini-option';
            const cleanText = opt.replace(/^[A-D]\.\s*/, '');
            btn.textContent = `${String.fromCharCode(65 + idx)}. ${cleanText}`;
            btn.addEventListener('click', () => {
                if (card.dataset.completed === 'true') return;
                
                optionsContainer.querySelectorAll('.mini-option').forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                card.dataset.selectedIdx = idx;
                
                checkBtn.classList.remove('hidden');
            });
            optionsContainer.appendChild(btn);
        });
        
        checkBtn.addEventListener('click', () => {
            const idx = parseInt(card.dataset.selectedIdx);
            if (isNaN(idx)) return;
            
            checkBtn.classList.add('hidden');
            optionsContainer.querySelectorAll('.mini-option').forEach(b => b.setAttribute('disabled', 'true'));
            
            if (idx === prac.correctIdx) {
                playSound('success');
                optionsContainer.children[idx].classList.add('correct');
                card.dataset.completed = 'true';
                
                feedbackEl.innerHTML = `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong><br><span style="font-weight: normal; margin-top: 4px; display: block; font-size: 0.92rem;">${prac.explanation}</span>`;
                feedbackEl.className = 'mini-feedback';
                feedbackEl.classList.remove('hidden');
                
                // Increment completed mini practice counter
                state.miniPractices.completedCount++;
                updateProgress();
            } else {
                playSound('fail');
                optionsContainer.children[idx].classList.add('incorrect');
                optionsContainer.children[prac.correctIdx].classList.add('correct');
                
                feedbackEl.innerHTML = `<i class="fa-solid fa-circle-xmark text-red"></i> <strong>Chưa chính xác!</strong><br><span style="font-weight: normal; margin-top: 4px; display: block; font-size: 0.92rem;">${prac.explanation}</span>`;
                feedbackEl.className = 'mini-feedback';
                feedbackEl.classList.remove('hidden');
            }
            
            // Fetch translations dynamically using MyMemory translation helper
            transBox.innerHTML = "<div style='font-size:0.85rem; color:var(--text-muted);'><i class='fa-solid fa-spinner fa-spin'></i> Đang tự động dịch chi tiết...</div>";
            transBox.classList.remove('hidden');
            
            Promise.all([
                translateWordENtoVI(prac.passage),
                translateWordENtoVI(prac.question),
                translateWordENtoVI(prac.options[prac.correctIdx])
            ]).then(([translatedPassage, translatedQuestion, translatedCorrectOption]) => {
                transBox.innerHTML = `
                    <h5 style="font-weight: 700; color: var(--primary-color); margin-bottom: 8px; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;"><i class="fa-solid fa-language"></i> BẢN DỊCH CHI TIẾT (TRANSLATIONS)</h5>
                    <div style="margin-bottom: 6px; font-size: 0.85rem; line-height: 1.4;">
                        <strong>Dịch câu hỏi:</strong> ${translatedQuestion || prac.question}
                    </div>
                    <div style="margin-bottom: 8px; font-size: 0.85rem; line-height: 1.4;">
                        <strong>Đáp án đúng dịch nghĩa:</strong> <span style="color:var(--success-color); font-weight:bold;">${translatedCorrectOption || prac.options[prac.correctIdx]}</span>
                    </div>
                    <div style="font-size: 0.85rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; line-height: 1.4; text-align: justify;">
                        <strong>Dịch đoạn văn:</strong><br/>
                        <span style="color: var(--text-muted); font-style: italic;">"${translatedPassage || prac.passage}"</span>
                    </div>
                `;
            }).catch(err => {
                console.error("Translation fail:", err);
                transBox.innerHTML = "<div style='font-size:0.85rem; color:var(--error-color);'>Không thể tải bản dịch tự động.</div>";
            });
        });
        
        practicesContainer.appendChild(card);
    });
    
    // Reset to theory tab initially
    const tabBtns = document.querySelectorAll('[data-dang-tab]');
    const tabPanels = document.querySelectorAll('#sec-dang-chi-tiet .tab-panel');
    tabBtns.forEach(b => b.classList.remove('active'));
    const theoryBtn = document.querySelector('[data-dang-tab="tab-dang-theory"]');
    if (theoryBtn) theoryBtn.classList.add('active');
    tabPanels.forEach(p => p.classList.remove('active'));
    const theoryPanel = document.getElementById('tab-dang-theory');
    if (theoryPanel) theoryPanel.classList.add('active');
    } catch (err) {
        reportError(err);
    }
}

// 8. General Tabs Swapper (Overview compare/tactics/traps) - Removed

// 9. Eye-Tracking Simulator Gaze Sweeps (Chapter 1)
function initEyeTracker() {
    const btnHeatmap = document.getElementById('btn-toggle-heatmap');
    const btnGaze = document.getElementById('btn-toggle-gaze');
    const btnReset = document.getElementById('btn-reset-eye');
    
    if (btnHeatmap) btnHeatmap.addEventListener('click', toggleHeatmapOverlay);
    if (btnGaze) btnGaze.addEventListener('click', runLabGazeSimulation);
    if (btnReset) btnReset.addEventListener('click', resetLabGazeDisplay);
    
    // Add change listeners to radio buttons to update visualization
    const radios = document.getElementsByName('lab-mode');
    radios.forEach(radio => {
        radio.addEventListener('change', () => {
            resetLabGazeDisplay();
            if (state.eyeTracker.heatmapActive) {
                drawHeatmapDots();
            }
        });
    });
}

function toggleHeatmapOverlay() {
    playSound('click');
    const container = document.getElementById('heatmap-overlay-container');
    const toggleBtn = document.getElementById('btn-toggle-heatmap');
    if (!container || !toggleBtn) return;
    
    state.eyeTracker.heatmapActive = !state.eyeTracker.heatmapActive;
    
    if (state.eyeTracker.heatmapActive) {
        toggleBtn.innerHTML = '<i class="fa-solid fa-fire"></i> Tắt Bản Đồ Nhiệt';
        toggleBtn.style.background = 'var(--error-color)';
        container.style.opacity = '1';
        drawHeatmapDots();
    } else {
        toggleBtn.innerHTML = '<i class="fa-solid fa-fire"></i> Bật Bản Đồ Nhiệt (Heatmap)';
        toggleBtn.style.background = 'var(--accent-amber)';
        container.style.opacity = '0';
        container.innerHTML = '';
    }
}

function drawHeatmapDots() {
    const container = document.getElementById('heatmap-overlay-container');
    const display = document.getElementById('lab-display-container');
    if (!container || !display) return;
    
    const displayRect = display.getBoundingClientRect();
    container.innerHTML = '';
    
    const modeEl = document.querySelector('input[name="lab-mode"]:checked');
    const mode = modeEl ? modeEl.value : 'skim';
    
    let hotWords = [];
    if (mode === 'skim') {
        hotWords = [
            { id: 'lw-3', intensity: 'high' },
            { id: 'lw-4', intensity: 'high' },
            { id: 'lw-7', intensity: 'medium' },
            { id: 'lw-9', intensity: 'medium' },
            { id: 'lw-12', intensity: 'low' },
            { id: 'lw-15', intensity: 'low' },
            { id: 'lw-86', intensity: 'low' },
            { id: 'lw-89', intensity: 'high' },
            { id: 'lw-90', intensity: 'high' },
            { id: 'lw-93', intensity: 'medium' },
            { id: 'lw-94', intensity: 'medium' },
            { id: 'lw-100', intensity: 'medium' }
        ];
    } else {
        hotWords = [
            { id: 'lw-0', intensity: 'low' },
            { id: 'lw-17', intensity: 'low' },
            { id: 'lw-18', intensity: 'medium' },
            { id: 'lw-23', intensity: 'high' },
            { id: 'lw-24', intensity: 'high' }
        ];
    }
    
    hotWords.forEach(w => {
        const span = document.getElementById(w.id);
        if (!span) return;
        
        const rect = span.getBoundingClientRect();
        const x = rect.left - displayRect.left + rect.width / 2;
        const y = rect.top - displayRect.top + rect.height / 2;
        
        const bubble = document.createElement('div');
        bubble.className = 'heatmap-bubble';
        
        let size = 35;
        let color = 'rgba(239, 68, 68, 0.55)'; // Red
        if (w.intensity === 'medium') {
            size = 28;
            color = 'rgba(245, 158, 11, 0.5)'; // Orange
        } else if (w.intensity === 'low') {
            size = 22;
            color = 'rgba(16, 185, 129, 0.4)'; // Green
        }
        
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;
        bubble.style.background = `radial-gradient(circle, ${color} 0%, rgba(255,255,255,0) 70%)`;
        bubble.style.left = `${x}px`;
        bubble.style.top = `${y}px`;
        
        container.appendChild(bubble);
    });
}

function resetLabGazeDisplay() {
    state.eyeTracker.active = false;
    state.eyeTracker.timeoutIds.forEach(id => clearTimeout(id));
    state.eyeTracker.timeoutIds = [];
    
    const gazeDot = document.getElementById('gaze-point');
    if (gazeDot) {
        gazeDot.style.opacity = '0';
        gazeDot.style.left = '-100px';
        gazeDot.style.top = '-100px';
    }
    
    const svg = document.getElementById('gaze-path-svg');
    if (svg) svg.innerHTML = '';
    
    // Reset stats to baseline
    const wpmEl = document.getElementById('lab-stat-wpm');
    const skipEl = document.getElementById('lab-stat-skip');
    const fixationEl = document.getElementById('lab-stat-fixation');
    const attentionEl = document.getElementById('lab-stat-attention');
    
    if (wpmEl) wpmEl.textContent = '150 WPM';
    if (skipEl) skipEl.textContent = '0%';
    if (fixationEl) fixationEl.textContent = '220ms';
    if (attentionEl) attentionEl.textContent = 'Bình thường';
    
    // Clear highlights on spans
    document.querySelectorAll('.lab-word').forEach(w => {
        w.style.background = 'none';
        w.style.color = 'inherit';
    });
}

function runLabGazeSimulation() {
    resetLabGazeDisplay();
    state.eyeTracker.active = true;
    
    const gazeDot = document.getElementById('gaze-point');
    if (!gazeDot) return;
    gazeDot.style.opacity = '1';
    
    const display = document.getElementById('lab-display-container');
    if (!display) return;
    const displayRect = display.getBoundingClientRect();
    const svg = document.getElementById('gaze-path-svg');
    
    const modeEl = document.querySelector('input[name="lab-mode"]:checked');
    const mode = modeEl ? modeEl.value : 'skim';
    
    let sequence = [];
    if (mode === 'skim') {
        sequence = [
            { id: 'lw-0', wpm: 450, skip: '45%', fixation: '180ms', cognitive: 'Thấp' },
            { id: 'lw-3', wpm: 480, skip: '50%', fixation: '170ms', cognitive: 'Thấp' },
            { id: 'lw-4', wpm: 500, skip: '55%', fixation: '160ms', cognitive: 'Thấp' },
            { id: 'lw-7', wpm: 520, skip: '60%', fixation: '150ms', cognitive: 'Thấp' },
            { id: 'lw-9', wpm: 540, skip: '62%', fixation: '160ms', cognitive: 'Thấp' },
            { id: 'lw-13', wpm: 550, skip: '65%', fixation: '170ms', cognitive: 'Thấp' },
            { id: 'lw-14', wpm: 560, skip: '68%', fixation: '170ms', cognitive: 'Thấp' },
            { id: 'lw-49', wpm: 500, skip: '70%', fixation: '200ms', cognitive: 'Bình thường' },
            { id: 'lw-50', wpm: 520, skip: '72%', fixation: '190ms', cognitive: 'Thấp' },
            { id: 'lw-52', wpm: 540, skip: '73%', fixation: '180ms', cognitive: 'Thấp' },
            { id: 'lw-53', wpm: 550, skip: '74%', fixation: '180ms', cognitive: 'Thấp' },
            { id: 'lw-55', wpm: 550, skip: '74%', fixation: '180ms', cognitive: 'Thấp' },
            { id: 'lw-57', wpm: 560, skip: '75%', fixation: '170ms', cognitive: 'Thấp' },
            { id: 'lw-58', wpm: 550, skip: '75%', fixation: '190ms', cognitive: 'Thấp' }
        ];
    } else {
        sequence = [
            { id: 'lw-0', wpm: 600, skip: '85%', fixation: '120ms', cognitive: 'Tìm kiếm' },
            { id: 'lw-8', wpm: 650, skip: '90%', fixation: '110ms', cognitive: 'Tìm kiếm' },
            { id: 'lw-26', wpm: 620, skip: '92%', fixation: '110ms', cognitive: 'Tìm kiếm' },
            { id: 'lw-29', wpm: 630, skip: '93%', fixation: '115ms', cognitive: 'Tìm kiếm' },
            { id: 'lw-37', wpm: 350, skip: '90%', fixation: '320ms', cognitive: 'Phát hiện!' },
            { id: 'lw-38', wpm: 250, skip: '85%', fixation: '360ms', cognitive: 'Khóa mục tiêu' }
        ];
    }
    
    let points = [];
    let delay = 100;
    
    sequence.forEach((node, index) => {
        const tId = setTimeout(() => {
            if (!state.eyeTracker.active) return;
            
            const span = document.getElementById(node.id);
            if (!span) return;
            
            const rect = span.getBoundingClientRect();
            const x = rect.left - displayRect.left + rect.width / 2;
            const y = rect.top - displayRect.top + rect.height / 2;
            
            // Move Gaze Dot
            gazeDot.style.left = `${x}px`;
            gazeDot.style.top = `${y}px`;
            
            // Draw path lines
            points.push({ x, y });
            if (points.length > 1 && svg) {
                const prev = points[points.length - 2];
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', prev.x);
                line.setAttribute('y1', prev.y);
                line.setAttribute('x2', x);
                line.setAttribute('y2', y);
                line.setAttribute('stroke', mode === 'skim' ? 'rgba(253, 224, 71, 0.7)' : 'rgba(20, 184, 166, 0.7)');
                line.setAttribute('stroke-width', '3');
                line.setAttribute('class', 'gaze-line');
                svg.appendChild(line);
            }
            
            // Highlight text node currently focused
            span.style.background = mode === 'skim' ? 'rgba(253, 224, 71, 0.3)' : 'rgba(20, 184, 166, 0.3)';
            
            // Update stats
            const wpmEl = document.getElementById('lab-stat-wpm');
            const skipEl = document.getElementById('lab-stat-skip');
            const fixationEl = document.getElementById('lab-stat-fixation');
            const attentionEl = document.getElementById('lab-stat-attention');
            
            if (wpmEl) wpmEl.textContent = `${node.wpm} WPM`;
            if (skipEl) skipEl.textContent = node.skip;
            if (fixationEl) fixationEl.textContent = node.fixation;
            if (attentionEl) attentionEl.textContent = node.cognitive;
            
            playSound('chime');
            
            // Success chime at finish
            if (index === sequence.length - 1) {
                setTimeout(() => {
                    if (state.eyeTracker.active) {
                        playSound('success');
                    }
                }, 600);
            }
        }, delay);
        
        state.eyeTracker.timeoutIds.push(tId);
        delay += index === sequence.length - 1 ? 1200 : 700;
    });
}

// 10. Keyword Sorting Mini Game (Chapter 1)
function initKeywordsSortingGame() {
    const cards = document.querySelectorAll('.sort-card');
    const zones = document.querySelectorAll('.zone-box');
    
    cards.forEach(card => {
        card.addEventListener('click', () => {
            playSound('click');
            if (card.classList.contains('correct')) return;
            
            if (state.keywordGame.selectedCard === card) {
                card.classList.remove('selected');
                state.keywordGame.selectedCard = null;
            } else {
                cards.forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                state.keywordGame.selectedCard = card;
            }
        });
    });
    
    zones.forEach(zone => {
        zone.addEventListener('click', () => {
            if (!state.keywordGame.selectedCard) return;
            
            const card = state.keywordGame.selectedCard;
            const targetZoneGroup = zone.dataset.zone;
            const cardCorrectGroup = card.dataset.group;
            
            if (targetZoneGroup === cardCorrectGroup) {
                playSound('success');
                card.classList.remove('selected');
                card.classList.add('correct');
                
                // Move card element inside the drop list container
                zone.querySelector('.zone-cards-list').appendChild(card);
                state.keywordGame.score++;
                
                document.getElementById('game-score-display').textContent = `${state.keywordGame.score}/15`;
                state.keywordGame.selectedCard = null;
                
                if (state.keywordGame.score === 15) {
                    playSound('complete');
                    document.getElementById('game-feedback').classList.remove('hidden');
                    state.progress.scanningTheory = true;
                    updateProgress();
                }
            } else {
                playSound('fail');
                card.classList.add('shake');
                setTimeout(() => card.classList.remove('shake'), 500);
            }
        });
    });
}

// 11. Synonym Drag/Click Matching Board (Chapter 3)
function initSynonymMatchingGame() {
    const qDecks = document.querySelectorAll('#question-deck .synonym-item');
    const pDecks = document.querySelectorAll('#passage-deck .synonym-item');
    
    qDecks.forEach(item => {
        item.addEventListener('click', () => {
            playSound('click');
            if (item.classList.contains('matched')) return;
            
            if (state.synonymGame.selectedQ === item) {
                item.classList.remove('selected');
                state.synonymGame.selectedQ = null;
            } else {
                qDecks.forEach(q => q.classList.remove('selected'));
                item.classList.add('selected');
                state.synonymGame.selectedQ = item;
            }
        });
    });
    
    pDecks.forEach(item => {
        item.addEventListener('click', () => {
            if (!state.synonymGame.selectedQ) return;
            
            const qCard = state.synonymGame.selectedQ;
            const matchId = item.dataset.match;
            const qId = qCard.dataset.id;
            
            if (matchId === qId) {
                playSound('success');
                qCard.classList.remove('selected');
                qCard.classList.add('matched');
                item.classList.add('matched');
                
                // Bind matching connectors
                qCard.innerHTML = `${qCard.textContent} <i class="fa-solid fa-circle-check text-green"></i>`;
                item.innerHTML = `<i class="fa-solid fa-link"></i> ${item.textContent}`;
                
                state.synonymGame.matches++;
                state.synonymGame.selectedQ = null;
                
                if (state.synonymGame.matches === 4) {
                    playSound('complete');
                    document.getElementById('synonym-feedback').classList.remove('hidden');
                    state.progress.synonymLab = true;
                    updateProgress();
                }
            } else {
                playSound('fail');
                item.classList.add('shake');
                setTimeout(() => item.classList.remove('shake'), 500);
            }
        });
    });
}

// 12. CBT Mock Exam Simulator (Chapter 3)
function startSelectedMockPassage(idx) {
    playSound('click');
    const passage = mockTestPassages[idx];
    if (!passage) return;
    
    state.mockExam.active = true;
    state.mockExam.currentPassageIdx = idx;
    state.mockExam.currentQuestionIndex = 0;
    state.mockExam.answers = {};
    state.mockExam.submitted = false;
    state.mockExam.score = 0;
    state.mockExam.timeLeft = 900; // 15 mins
    
    // Hide Landing Page, Show Simulator Area
    document.getElementById('mock-landing-page').classList.add('hidden');
    document.getElementById('mock-exam-active-area').classList.remove('hidden');
    document.getElementById('exam-explanation-box').classList.add('hidden');
    
    // Load Title & Text
    document.getElementById('active-mock-title').textContent = passage.title;
    
    // Add wrap words with .vocab-term tags in active text dynamically
    let parsedText = passage.passage;
    state.savedWords.forEach(item => {
        const word = item.word;
        const regex = new RegExp(`\\b${word}\\b`, 'gi');
        // Pre-parse highlight references
    });
    
    document.getElementById('active-mock-text').innerHTML = parsedText;
    
    // Generate MCQ cards
    const qContainer = document.getElementById('active-mock-questions-container');
    qContainer.innerHTML = '';
    
    passage.questions.forEach((q, qIdx) => {
        const qCard = document.createElement('div');
        qCard.className = `mock-question-card ${qIdx === 0 ? 'active' : ''}`;
        qCard.dataset.q = qIdx;
        qCard.innerHTML = `
            <div class="question-header">
                <span class="q-badge">CÂU HỎI ${qIdx + 1}</span>
            </div>
            <p class="question-text">${q.question}</p>
            <div class="options-list"></div>
        `;
        
        const listDiv = qCard.querySelector('.options-list');
        q.options.forEach((opt, oIdx) => {
            const optLetter = String.fromCharCode(65 + oIdx);
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.dataset.option = optLetter;
            btn.dataset.correct = oIdx === q.correctIdx ? 'true' : 'false';
            
            const cleanText = opt.replace(/^[A-D]\.\s*/, '');
            btn.innerHTML = `<span class="option-letter">${optLetter}</span> <span class="option-val">${cleanText}</span>`;
            btn.addEventListener('click', () => {
                if (state.mockExam.submitted) return;
                
                playSound('click');
                // Set selected answer
                state.mockExam.answers[qIdx] = optLetter;
                
                // Highlight option selected
                listDiv.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                
                // Highlight corresponding navigation button
                const navBtn = document.querySelector(`.review-btn[data-q="${qIdx}"]`);
                if (navBtn) navBtn.classList.add('answered');
            });
            listDiv.appendChild(btn);
        });
        
        qContainer.appendChild(qCard);
    });
    
    // Generate Review navigation buttons
    const reviewNav = document.getElementById('exam-review-nav');
    reviewNav.innerHTML = '';
    passage.questions.forEach((_, qIdx) => {
        const btn = document.createElement('button');
        btn.className = `review-btn ${qIdx === 0 ? 'active' : ''}`;
        btn.dataset.q = qIdx;
        btn.textContent = qIdx + 1;
        btn.addEventListener('click', () => {
            changeQuestion(qIdx);
        });
        reviewNav.appendChild(btn);
    });
    
    // Setup explanation tabs
    const expTabs = document.getElementById('active-mock-explanation-tabs');
    expTabs.innerHTML = '';
    passage.questions.forEach((_, qIdx) => {
        const btn = document.createElement('button');
        btn.className = `tab-btn ${qIdx === 0 ? 'active' : ''}`;
        btn.dataset.exp = qIdx;
        btn.textContent = `Câu ${qIdx + 1}`;
        btn.addEventListener('click', () => {
            playSound('click');
            showExplanationDetailCard(qIdx);
        });
        expTabs.appendChild(btn);
    });
    
    const expCards = document.getElementById('active-mock-explanation-cards');
    expCards.innerHTML = '';
    passage.questions.forEach((q, qIdx) => {
        const card = document.createElement('div');
        card.className = `explanation-detail-card ${qIdx === 0 ? '' : 'hidden'}`;
        card.id = `exp-detail-${qIdx}`;
        card.innerHTML = `
            <div class="explanation-grid">
                <div class="explanation-col">
                    <div class="explanation-col-title"><i class="fa-solid fa-bullseye"></i> Giải thích đáp án</div>
                    <div class="explanation-col-content">${q.explanation}</div>
                </div>
            </div>
        `;
        expCards.appendChild(card);
    });
    
    // Start countdown timer
    if (state.mockExam.timerInterval) clearInterval(state.mockExam.timerInterval);
    state.mockExam.timerInterval = setInterval(() => {
        state.mockExam.timeLeft--;
        updateMockTimerDisplay();
        
        if (state.mockExam.timeLeft <= 0) {
            clearInterval(state.mockExam.timerInterval);
            submitMockExam();
        }
    }, 1000);
    
    updateMockTimerDisplay();
    bindVocabularyClickTooltips();
}

function updateMockTimerDisplay() {
    const mins = Math.floor(state.mockExam.timeLeft / 60);
    const secs = state.mockExam.timeLeft % 60;
    document.getElementById('exam-timer').textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function changeQuestion(qIdx) {
    if (qIdx < 0 || qIdx > 9) return;
    playSound('click');
    
    state.mockExam.currentQuestionIndex = qIdx;
    
    // Toggle active questions
    const questionCards = document.querySelectorAll('.mock-question-card');
    questionCards.forEach((card, i) => {
        if (i === qIdx) card.classList.add('active');
        else card.classList.remove('active');
    });
    
    // Toggle review indicators
    const reviewBtns = document.querySelectorAll('.review-btn');
    reviewBtns.forEach((btn, i) => {
        if (i === qIdx) btn.classList.add('active');
        else btn.classList.remove('active');
    });
    
    // Toggle prev/next disability
    document.getElementById('btn-prev-question').disabled = qIdx === 0;
    document.getElementById('btn-next-question').disabled = qIdx === 9;
}

function setupMockControls() {
    const prev = document.getElementById('btn-prev-question');
    const next = document.getElementById('btn-next-question');
    const submit = document.getElementById('btn-submit-exam');
    
    if (prev) {
        prev.addEventListener('click', () => {
            changeQuestion(state.mockExam.currentQuestionIndex - 1);
        });
    }
    if (next) {
        next.addEventListener('click', () => {
            changeQuestion(state.mockExam.currentQuestionIndex + 1);
        });
    }
    if (submit) {
        submit.addEventListener('click', submitMockExam);
    }
}

function submitMockExam() {
    if (state.mockExam.submitted) return;
    
    // Confirm confirmation
    if (state.mockExam.timeLeft > 0 && !confirm("Bạn có chắc chắn muốn nộp bài thi thử?")) {
        return;
    }
    
    playSound('complete');
    state.mockExam.submitted = true;
    clearInterval(state.mockExam.timerInterval);
    
    let correctCount = 0;
    const passage = mockTestPassages[state.mockExam.currentPassageIdx];
    
    // Grade MCQ cards
    const questionCards = document.querySelectorAll('.mock-question-card');
    questionCards.forEach((card, qIdx) => {
        const chosenLetter = state.mockExam.answers[qIdx];
        const correctLetter = String.fromCharCode(65 + passage.questions[qIdx].correctIdx);
        
        card.querySelectorAll('.option-btn').forEach(btn => {
            btn.setAttribute('disabled', 'true');
            const btnLetter = btn.dataset.option;
            
            if (btnLetter === correctLetter) {
                btn.classList.add('correct');
            }
            if (btnLetter === chosenLetter && chosenLetter !== correctLetter) {
                btn.classList.add('incorrect');
            }
        });
        
        if (chosenLetter === correctLetter) {
            correctCount++;
        }
    });
    
    state.mockExam.score = correctCount;
    state.progress.mockExam = true;
    updateProgress();
    
    // Show tutor explanations slides
    document.getElementById('exam-explanation-box').classList.remove('hidden');
    document.getElementById('exam-explanation-box').scrollIntoView({ behavior: 'smooth' });
    
    // Trigger certificate if 100% correct score achieved
    if (correctCount === 10) {
        setTimeout(() => {
            showCertificateModal(10, 10);
        }, 1500);
    } else {
        alert(`Bạn đã trả lời đúng ${correctCount}/10 câu hỏi! Xem phần giải thích chi tiết ở bên dưới để khắc phục lỗi sai nhé.`);
    }
}

function exitMockExamToLanding() {
    playSound('click');
    state.mockExam.active = false;
    if (state.mockExam.timerInterval) clearInterval(state.mockExam.timerInterval);
    
    document.getElementById('mock-landing-page').classList.remove('hidden');
    document.getElementById('mock-exam-active-area').classList.add('hidden');
}

function showExplanationDetailCard(qIdx) {
    const tabs = document.querySelectorAll('#active-mock-explanation-tabs .tab-btn');
    const cards = document.querySelectorAll('#active-mock-explanation-cards .explanation-detail-card');
    
    tabs.forEach((tab, i) => {
        if (i === qIdx) tab.classList.add('active');
        else tab.classList.remove('active');
    });
    
    cards.forEach((card, i) => {
        if (i === qIdx) card.classList.remove('hidden');
        else card.classList.add('hidden');
    });
}

// 13. Unified Global Selection Highlighter Tool
function applyGlobalHighlighterColor(color) {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed) return;
    
    playSound('click');
    const range = selection.getRangeAt(0);
    
    if (color === 'clear') {
        // Strip custom highlights classes
        const span = range.commonAncestorContainer.parentElement;
        if (span && span.classList.contains('custom-highlight')) {
            const textNode = document.createTextNode(span.textContent);
            span.parentNode.replaceChild(textNode, span);
        }
    } else {
        const span = document.createElement('span');
        span.className = `custom-highlight highlight-${color}`;
        span.style.background = color === 'yellow' ? 'rgba(253, 224, 71, 0.4)' : (color === 'green' ? 'rgba(134, 239, 172, 0.4)' : 'rgba(147, 197, 253, 0.4)');
        span.appendChild(range.extractContents());
        range.insertNode(span);
    }
    
    selection.removeAllRanges();
    const toolbar = document.getElementById('vocab-saver-toolbar');
    if (toolbar) toolbar.classList.add('hidden');
}

// Warm up the speechSynthesis voices list on page load
if ('speechSynthesis' in window) {
    window.speechSynthesis.getVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = () => {
            window.speechSynthesis.getVoices();
        };
    }
}

// Speech Synthesis speaker helper targeting natural Guy (US English) voice
function speakWord(text) {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        
        const voices = window.speechSynthesis.getVoices();
        const guyVoice = voices.find(v => v.name.includes('Guy') && v.name.includes('Natural')) ||
                         voices.find(v => v.name.includes('GuyNeural')) ||
                         voices.find(v => v.name.includes('Guy'));
                         
        const fallbackVoice = voices.find(v => v.name === 'Google US English Male') || 
                              voices.find(v => v.name === 'Alex') || 
                              voices.find(v => v.lang.startsWith('en') && v.name.toLowerCase().includes('male')) ||
                              voices.find(v => v.lang.startsWith('en') && (v.name.includes('David') || v.name.includes('Mark') || v.name.includes('Daniel'))) ||
                              voices.find(v => v.lang === 'en-US'); // Fallback
        
        if (guyVoice) {
            utterance.voice = guyVoice;
            utterance.rate = 1.0; // Guy Neural sounds perfect at 1.0 speed
            utterance.pitch = 1.0;
        } else if (fallbackVoice) {
            utterance.voice = fallbackVoice;
            utterance.rate = 1.0; 
            utterance.pitch = 1.05; // Slightly higher pitch makes the male voice sound younger and fresher
        } else {
            utterance.lang = 'en-US';
        }
        
        window.speechSynthesis.speak(utterance);
    } else {
        console.warn("Speech Synthesis not supported.");
    }
}

// Fetch phonetics dynamically from free Dictionary API for lookup words
async function fetchPhoneticForWord(word) {
    try {
        const res = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`);
        if (res.ok) {
            const data = await res.json();
            if (data && data[0]) {
                if (data[0].phonetic) return data[0].phonetic;
                if (data[0].phonetics) {
                    for (let p of data[0].phonetics) {
                        if (p.text) return p.text;
                    }
                }
            }
        }
    } catch (e) {
        console.warn("Phonetic lookup failed:", e);
    }
    return null;
}

// 14. Vocabulary Clicks Tooltips Database Sync
function bindVocabularyClickTooltips() {
    const vocabTerms = document.querySelectorAll('.vocab-term');
    vocabTerms.forEach(term => {
        term.addEventListener('click', (e) => {
            if (!term.classList.contains('active')) return;
            
            e.stopPropagation();
            playSound('chime');
            
            const word = term.dataset.word;
            const data = vocabData[word.toLowerCase()];
            
            if (data) {
                state.tooltipJustShown = true;
                
                // Populate tooltip contents
                elements.tooltipWord.textContent = word;
                elements.tooltipPos.textContent = `(${data.pos})`;
                elements.tooltipPhonetic.textContent = data.phonetic;
                elements.tooltipMean.textContent = data.mean;
                
                // Position Tooltip element
                const rect = term.getBoundingClientRect();
                const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                
                elements.vocabTooltip.style.left = `${rect.left + scrollLeft}px`;
                elements.vocabTooltip.style.top = `${rect.bottom + scrollTop + 8}px`;
                elements.vocabTooltip.classList.remove('hidden');
                
                // Set data properties on save button
                elements.tooltipSaveBtn.dataset.word = word;
                elements.tooltipSaveBtn.dataset.pos = data.pos;
                elements.tooltipSaveBtn.dataset.phonetic = data.phonetic;
                elements.tooltipSaveBtn.dataset.mean = data.mean;
                
                // Toggle Save button visibility based on existing saves
                const isAlreadySaved = state.savedWords.some(w => w.word.toLowerCase() === word.toLowerCase());
                if (isAlreadySaved) {
                    elements.tooltipSaveBtn.classList.add('hidden');
                    elements.tooltipSavedBadge.classList.remove('hidden');
                } else {
                    elements.tooltipSaveBtn.classList.remove('hidden');
                    elements.tooltipSavedBadge.classList.add('hidden');
                }
            }
        });
    });
    
    // Global single click on ANY word inside reading passages to auto-translate and show definition card!
    document.addEventListener('click', async (e) => {
        // Prevent trigger if clicking on menus, buttons, modals, input elements, or active tooltips
        if (e.target.closest('#vocab-saver-toolbar') || 
            e.target.closest('#vocab-tooltip') || 
            e.target.closest('button') || 
            e.target.closest('input') || 
            e.target.closest('a') || 
            e.target.closest('.color-dot') || 
            e.target.closest('.vocab-term') || 
            e.target.closest('.scan-clickable') || 
            e.target.closest('.sidebar-menu') || 
            e.target.closest('.sidebar-header') ||
            e.target.closest('.lesson-group-header') ||
            e.target.closest('#name-modal')) {
            return;
        }
        
        // Only trigger inside primary curriculum views and stats cockpit
        if (!e.target.closest('.content-section') && !e.target.closest('.dashboard-cockpit')) {
            return;
        }
        
        // Prevent single-word translation popups if there is an active text selection drag
        const selObj = window.getSelection();
        if (selObj && !selObj.isCollapsed && selObj.toString().trim().length > 0) {
            return;
        }
        
        // Extract caret coordinates
        let range;
        if (document.caretRangeFromPoint) {
            range = document.caretRangeFromPoint(e.clientX, e.clientY);
        } else if (e.rangeParent) {
            range = document.createRange();
            range.setStart(e.rangeParent, e.rangeOffset);
        }
        
        if (range && range.startContainer.nodeType === Node.TEXT_NODE) {
            const textNode = range.startContainer;
            const offset = range.startOffset;
            const text = textNode.textContent;
            
            // Detect word borders
            let start = offset;
            while (start > 0 && /\w/.test(text[start - 1])) {
                start--;
            }
            let end = offset;
            while (end < text.length && /\w/.test(text[end])) {
                end++;
            }
            
            const rawWord = text.substring(start, end).trim();
            const cleanWord = rawWord.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"']/g, "").trim();
            
            // Ensure clicked word is a valid English word string (between 2 and 25 letters)
            if (cleanWord.length >= 2 && cleanWord.length <= 25 && /^[A-Za-z'-]+$/.test(cleanWord)) {
                showFloatingWordDefinition(cleanWord, e.clientX, e.clientY);
            }
        }
    });
    
    // Bind click handler to the tooltip manual save button
    if (elements.tooltipSaveBtn) {
        elements.tooltipSaveBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            playSound('success');
            
            const w = elements.tooltipSaveBtn.dataset.word;
            const p = elements.tooltipSaveBtn.dataset.pos;
            const ph = elements.tooltipSaveBtn.dataset.phonetic;
            const m = elements.tooltipSaveBtn.dataset.mean;
            
            if (w) {
                addWordToSavedList(w, { pos: p, phonetic: ph, mean: m });
                elements.tooltipSaveBtn.classList.add('hidden');
                elements.tooltipSavedBadge.classList.remove('hidden');
            }
        });
    }
    
    // Bind click handler to the tooltip speak button
    if (elements.tooltipSpeakBtn) {
        elements.tooltipSpeakBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const w = elements.tooltipWord.textContent;
            if (w) {
                speakWord(w);
            }
        });
    }
    
    // Close tooltips click elsewhere
    document.addEventListener('click', (e) => {
        // Prevent closing instantly when clicking to open or inside tooltip
        if (state.tooltipJustShown) {
            state.tooltipJustShown = false;
            return;
        }
        if (!e.target.closest('#vocab-tooltip')) {
            elements.vocabTooltip.classList.add('hidden');
        }
    });
}

// Helper: Show floating definition card for any clicked/selected word
async function showFloatingWordDefinition(word, clientX, clientY) {
    const lowerWord = word.toLowerCase();
    const data = vocabData[lowerWord];
    
    state.tooltipJustShown = true;
    
    // Position floating card near caret coordinates
    const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    elements.vocabTooltip.style.left = `${clientX + scrollLeft - 50}px`;
    elements.vocabTooltip.style.top = `${clientY + scrollTop + 12}px`;
    
    // Show loading skeleton
    elements.tooltipWord.textContent = word;
    elements.tooltipPos.textContent = "";
    elements.tooltipPhonetic.textContent = "";
    elements.tooltipMean.textContent = "Đang tra cứu nghĩa...";
    
    // Default show save button, hide badge
    elements.tooltipSaveBtn.classList.remove('hidden');
    elements.tooltipSavedBadge.classList.add('hidden');
    elements.vocabTooltip.classList.remove('hidden');
    
    // Populate dataset properties
    elements.tooltipSaveBtn.dataset.word = word;
    elements.tooltipSaveBtn.dataset.pos = "tự động dịch";
    elements.tooltipSaveBtn.dataset.phonetic = "/lookup/";
    elements.tooltipSaveBtn.dataset.mean = "";
    
    // Check if word is already saved in user's list
    const isAlreadySaved = state.savedWords.some(w => w.word.toLowerCase() === lowerWord);
    if (isAlreadySaved) {
        elements.tooltipSaveBtn.classList.add('hidden');
        elements.tooltipSavedBadge.classList.remove('hidden');
    }
    
    if (data) {
        playSound('chime');
        elements.tooltipPos.textContent = `(${data.pos})`;
        elements.tooltipPhonetic.textContent = data.phonetic;
        elements.tooltipMean.textContent = data.mean;
        
        elements.tooltipSaveBtn.dataset.pos = data.pos;
        elements.tooltipSaveBtn.dataset.phonetic = data.phonetic;
        elements.tooltipSaveBtn.dataset.mean = data.mean;
    } else {
        // Fetch phonetics dynamically from free DictionaryAPI first
        const phonetic = await fetchPhoneticForWord(word);
        const displayPhonetic = phonetic ? phonetic : "";
        elements.tooltipPhonetic.textContent = displayPhonetic;
        elements.tooltipSaveBtn.dataset.phonetic = displayPhonetic ? displayPhonetic : "/lookup/";
        
        // Dynamic fetch translation from MyMemory API
        const translation = await translateWordENtoVI(word);
        if (translation) {
            playSound('chime');
            elements.tooltipPos.textContent = "(tự động dịch)";
            elements.tooltipPhonetic.textContent = "";
            elements.tooltipMean.textContent = translation;
            
            elements.tooltipSaveBtn.dataset.pos = "tự động dịch";
            elements.tooltipSaveBtn.dataset.phonetic = "/translated/";
            elements.tooltipSaveBtn.dataset.mean = translation;
        } else {
            elements.tooltipMean.textContent = "Không tìm thấy bản dịch tự động.";
            elements.tooltipSaveBtn.classList.add('hidden'); // Hide save button since no translation was found
        }
    }
}

// Helper: Asynchronous translation from English to Vietnamese
async function translateWordENtoVI(word) {
    try {
        const res = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(word)}&langpair=en|vi`);
        const data = await res.json();
        if (data && data.responseData && data.responseData.translatedText) {
            let translated = data.responseData.translatedText.trim();
            // Clean up same-word responses
            if (translated.toLowerCase() === word.toLowerCase() && data.matches) {
                for (let m of data.matches) {
                    if (m.translation && m.translation.trim().toLowerCase() !== word.toLowerCase()) {
                        translated = m.translation.trim();
                        break;
                    }
                }
            }
            return translated;
        }
    } catch (e) {
        console.warn("MyMemory translation call failed:", e);
    }
    return null;
}

// 14.5 Global Text Selection Word Saver
function initGlobalVocabSaver() {
    const toolbar = document.getElementById('vocab-saver-toolbar');
    if (!toolbar) return;
    
    // Listen for text selection releases on document
    document.addEventListener('mouseup', (e) => {
        // Delay slightly to prevent immediate closing/overwriting when clicking toolbar itself
        setTimeout(() => {
            const selection = window.getSelection();
            if (!selection || selection.isCollapsed) {
                toolbar.classList.add('hidden');
                return;
            }
            
            const selectedText = selection.toString().trim();
            // Validate selection range (between 2 and 100 chars, no carriage returns)
            if (selectedText.length < 2 || selectedText.length > 100 || selectedText.includes('\n')) {
                toolbar.classList.add('hidden');
                return;
            }
            
            // Show floating bubble toolbar
            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();
            const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Center the wider toolbar properly
            toolbar.style.left = `${rect.left + scrollLeft + (rect.width / 2) - 120}px`;
            toolbar.style.top = `${rect.top + scrollTop - 42}px`;
            
            // Reset text contextually based on word/phrase
            const spanText = document.getElementById('global-save-vocab-text');
            if (spanText) {
                spanText.textContent = selectedText.includes(' ') ? "Lưu cụm từ này" : "Lưu từ vựng này";
            }
            
            toolbar.classList.remove('hidden');
            toolbar.dataset.text = selectedText;
        }, 10);
    });
    
    // Hide toolbar when clicking outside
    document.addEventListener('mousedown', (e) => {
        if (e.target !== toolbar && !toolbar.contains(e.target)) {
            toolbar.classList.add('hidden');
        }
    });
    
    // Bind global save vocab button click
    const saveBtn = document.getElementById('btn-global-save-vocab');
    if (saveBtn) {
        saveBtn.addEventListener('click', async (e) => {
            e.stopPropagation();
            playSound('click');
            
            const rawWord = toolbar.dataset.text;
            if (!rawWord) {
                toolbar.classList.add('hidden');
                return;
            }
            const cleanWord = rawWord.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"']/g, "").trim();
            if (cleanWord.length < 2) {
                toolbar.classList.add('hidden');
                return;
            }
            
            const isPhrase = cleanWord.includes(' ');
            
            // Show loading state
            const spanText = document.getElementById('global-save-vocab-text');
            if (spanText) {
                spanText.textContent = isPhrase ? "Đang dịch & lưu cụm..." : "Đang dịch & lưu từ...";
            }
            
            const lowerWord = cleanWord.toLowerCase();
            
            // Check if word exists in our pre-defined database
            const preDefinedData = vocabData[lowerWord];
            if (preDefinedData) {
                addWordToSavedList(cleanWord, preDefinedData);
                playSound('success');
                toolbar.classList.add('hidden');
                return;
            }
            
            // Translate using MyMemory API
            const translation = await translateWordENtoVI(cleanWord);
            if (translation) {
                // Fetch actual phonetics dynamically for single words
                let displayPhonetic = "/phrase/";
                if (!isPhrase) {
                    const phonetic = await fetchPhoneticForWord(cleanWord);
                    displayPhonetic = phonetic ? phonetic : "/lookup/";
                }
                
                const customData = {
                    pos: isPhrase ? "cụm từ" : "tự động dịch",
                    phonetic: displayPhonetic,
                    mean: translation
                };
                addWordToSavedList(cleanWord, customData);
                playSound('success');
                toolbar.classList.add('hidden');
            } else {
                // Fallback to manual prompt
                toolbar.classList.add('hidden');
                setTimeout(() => {
                    const userMean = prompt(`Không thể dịch tự động từ '${cleanWord}'. Hãy nhập nghĩa tiếng Việt hoặc ghi chú của từ này:`);
                    if (userMean && userMean.trim().length > 0) {
                        const customData = {
                            pos: "tự định nghĩa",
                            phonetic: "/custom/",
                            mean: userMean.trim()
                        };
                        addWordToSavedList(cleanWord, customData);
                        playSound('success');
                    }
                }, 100);
            }
        });
    }
    
    // Bind highlighter dots inside this global toolbar
    const dots = toolbar.querySelectorAll('.color-dot');
    dots.forEach(dot => {
        dot.addEventListener('mousedown', (e) => {
            e.preventDefault(); // Stop selection loss
            e.stopPropagation();
            const color = dot.dataset.color;
            applyGlobalHighlighterColor(color);
        });
    });
}

function addWordToSavedList(word, data) {
    const exists = state.savedWords.some(w => w.word.toLowerCase() === word.toLowerCase());
    if (exists) return;
    
    // Enforce lowercase meaning for aesthetic consistency
    const lowercaseMean = data.mean ? data.mean.toLowerCase().trim() : "";
    const lowercaseData = { ...data, mean: lowercaseMean };
    
    state.savedWords.push({ word, ...lowercaseData });
    localStorage.setItem('vstep_saved_vocab', JSON.stringify(state.savedWords));
    
    renderWordBankList();
    updateProgress();
}

function renderWordBankList() {
    elements.wordBankCount.textContent = state.savedWords.length;
    elements.statsVocab.textContent = `${state.savedWords.length} từ`;
    
    if (state.savedWords.length === 0) {
        elements.wordBankContainer.innerHTML = '';
        elements.wordBankContainer.appendChild(elements.emptyBankMessage);
        elements.vocabActionsPanel.classList.add('hidden');
    } else {
        // Clear except message
        elements.wordBankContainer.innerHTML = '';
        elements.vocabActionsPanel.classList.remove('hidden');
        
        state.savedWords.forEach(w => {
            const card = document.createElement('div');
            card.className = 'vocab-item-card';
            card.style.background = 'var(--surface-solid)';
            card.style.border = '1px solid var(--border-color)';
            card.style.padding = '16px';
            card.style.position = 'relative';
            
            card.innerHTML = `
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
                    <div style="font-weight:700; color:var(--primary-color); font-size:1.1rem;">${w.word}</div>
                    <button class="speak-vocab-btn" style="background:none; border:none; color:var(--primary-color); cursor:pointer; font-size:0.95rem; padding:0; display:inline-flex; align-items:center; transition:transform 0.1s;" onmouseover="this.style.transform='scale(1.15)'" onmouseout="this.style.transform='scale(1)'" title="Phát âm"><i class="fa-solid fa-volume-high"></i></button>
                </div>
                <div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:8px;">${w.phonetic} • <span style="font-style:italic;">${w.pos}</span></div>
                <div style="font-size:0.92rem; line-height:1.5;">${w.mean}</div>
                <button class="remove-word-btn" style="position:absolute; top:8px; right:8px; background:none; border:none; color:var(--error-color); cursor:pointer; font-size:1.2rem; line-height:1;" title="Xóa từ này">&times;</button>
            `;
            
            card.querySelector('.speak-vocab-btn').addEventListener('click', (e) => {
                e.stopPropagation();
                speakWord(w.word);
            });
            
            card.querySelector('.remove-word-btn').addEventListener('click', (e) => {
                e.stopPropagation();
                playSound('click');
                state.savedWords = state.savedWords.filter(item => item.word.toLowerCase() !== w.word.toLowerCase());
                localStorage.setItem('vstep_saved_vocab', JSON.stringify(state.savedWords));
                renderWordBankList();
                updateProgress();
            });
            
            elements.wordBankContainer.appendChild(card);
        });
    }
}

function initVocabControls() {
    elements.resetVocabBtn.addEventListener('click', () => {
        if (confirm("Bạn có chắc chắn muốn xóa toàn bộ từ đã lưu?")) {
            playSound('click');
            state.savedWords = [];
            localStorage.removeItem('vstep_saved_vocab');
            renderWordBankList();
            updateProgress();
        }
    });
    
    // Load saved words from storage
    const cachedVocab = localStorage.getItem('vstep_saved_vocab');
    if (cachedVocab) {
        state.savedWords = JSON.parse(cachedVocab);
        renderWordBankList();
    }
    
    // Initialize Flashcard Widget click handlers
    elements.vocabTestBtn.addEventListener('click', () => {
        if (state.savedWords.length === 0) {
            alert("Hộp từ vựng của bạn chưa có từ nào! Hãy click các từ gạch chân ở bài đọc để lưu từ trước nhé.");
            return;
        }
        playSound('click');
        state.vocabTest.currentIndex = 0;
        loadFlashcard(0);
        elements.vocabTestWidget.classList.remove('hidden');
        elements.vocabTestWidget.scrollIntoView({ behavior: 'smooth' });
    });
    
    elements.testBtnClose.addEventListener('click', () => {
        playSound('click');
        elements.vocabTestWidget.classList.add('hidden');
    });
    
    elements.testFlashcard.addEventListener('click', () => {
        playSound('chime');
        elements.testCardInner.classList.toggle('flipped');
    });
    
    elements.testBtnFail.addEventListener('click', (e) => {
        e.stopPropagation();
        playSound('fail');
        elements.testCardInner.classList.remove('flipped');
        setTimeout(() => {
            state.vocabTest.currentIndex = (state.vocabTest.currentIndex + 1) % state.savedWords.length;
            loadFlashcard(state.vocabTest.currentIndex);
        }, 300);
    });
    
    elements.testBtnPass.addEventListener('click', (e) => {
        e.stopPropagation();
        playSound('success');
        elements.testCardInner.classList.remove('flipped');
        setTimeout(() => {
            state.vocabTest.currentIndex = (state.vocabTest.currentIndex + 1) % state.savedWords.length;
            loadFlashcard(state.vocabTest.currentIndex);
        }, 300);
    });
}

function loadFlashcard(idx) {
    const wordItem = state.savedWords[idx];
    if (!wordItem) return;
    
    elements.testWordFront.textContent = wordItem.word;
    elements.testWordPhonetic.textContent = wordItem.phonetic;
    elements.testWordBack.textContent = wordItem.word;
    elements.testWordPos.textContent = `(${wordItem.pos})`;
    elements.testWordMean.textContent = wordItem.mean;
}

// 15. Completion Certificate Fanfare Modals
function showCertificateModal(score, total) {
    playSound('complete');
    elements.certStudentName.textContent = state.studentName;
    elements.certScore.textContent = score;
    elements.certModal.classList.remove('hidden');
    
    initConfettiEffects();
}

function initCertificateClose() {
    elements.closeCertBtn.addEventListener('click', () => {
        playSound('click');
        elements.certModal.classList.add('hidden');
    });
    elements.shareCertBtn.addEventListener('click', () => {
        playSound('click');
        elements.certModal.classList.add('hidden');
    });
}

// 16. Confetti Particle Drawings (Completion Modal Canvas)
let confettiActive = false;
let confettiArr = [];

function initConfettiEffects() {
    const canvas = elements.confettiCanvas;
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    confettiArr = [];
    confettiActive = true;
    
    for (let i = 0; i < 120; i++) {
        confettiArr.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height - canvas.height,
            r: Math.random() * 6 + 4,
            d: Math.random() * canvas.height,
            color: `hsl(${Math.random() * 360}, 90%, 65%)`,
            tilt: Math.random() * 10 - 5,
            tiltAngleIncremental: Math.random() * 0.07 + 0.02,
            tiltAngle: 0
        });
    }
    
    function drawConfetti() {
        if (!confettiActive) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        confettiArr.forEach((p, idx) => {
            p.tiltAngle += p.tiltAngleIncremental;
            p.y += (Math.cos(p.d) + 3 + p.r / 2) / 2;
            p.x += Math.sin(p.tiltAngle);
            p.tilt = Math.sin(p.tiltAngle - idx/3) * 15;
            
            ctx.beginPath();
            ctx.lineWidth = p.r;
            ctx.strokeStyle = p.color;
            ctx.moveTo(p.x + p.tilt + p.r / 2, p.y);
            ctx.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
            ctx.stroke();
            
            // Loop particles from top
            if (p.y > canvas.height) {
                confettiArr[idx] = {
                    ...p,
                    x: Math.random() * canvas.width,
                    y: -20,
                    tilt: Math.random() * 10 - 5
                };
            }
        });
        
        requestAnimationFrame(drawConfetti);
    }
    
    drawConfetti();
    
    // Stop after 6 seconds automatically
    setTimeout(() => {
        confettiActive = false;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }, 6000);
}

// 17. Overall Completion Percentage Calculation
function updateProgress() {
    let completedSteps = 0;
    const totalSteps = 4; // Skimming, Scanning, Synonym, Mock Exam
    
    if (state.progress.skimmingTheory) completedSteps++;
    if (state.progress.scanningTheory) completedSteps++;
    if (state.progress.synonymLab) completedSteps++;
    if (state.progress.mockExam) completedSteps++;
    
    // Calculate global percentage based on basic steps and question types completed
    const baseProgress = (completedSteps / totalSteps) * 80; // 80% weight on chapters
    const miniPracticeProgress = (state.miniPractices.completedCount / state.miniPractices.totalCount) * 20; // 20% weight on quizzes
    
    const progress = Math.min(100, Math.round(baseProgress + miniPracticeProgress));
    
    elements.sidebarProgress.style.width = `${progress}%`;
    elements.progressText.textContent = `${progress}% Hoàn thành`;
    elements.statsProgress.textContent = `${progress}%`;
    
    // Toggle subnav checkmarks
    if (state.progress.skimmingTheory) markSidebarItemCompleted('skimming-theory');
    if (state.progress.scanningTheory) markSidebarItemCompleted('scanning-theory');
    if (state.progress.synonymLab) markSidebarItemCompleted('synonym-lab');
    if (state.progress.mockExam) markSidebarItemCompleted('vstep-mock-test');
    
    // Adjust WPM stats based on overall progress
    const baseWPM = 150;
    const gainedWPM = completedSteps * 35;
    elements.statsSpeed.textContent = `${baseWPM + gainedWPM} WPM`;
    
    // Bind accuracy
    if (state.mockExam.submitted) {
        const accuracy = Math.round((state.mockExam.score / 10) * 100);
        elements.statsAccuracy.textContent = `${accuracy}%`;
    } else {
        elements.statsAccuracy.textContent = '0%';
    }
}

function markSidebarItemCompleted(sectionName) {
    const indicator = document.getElementById(`status-${sectionName}`);
    if (indicator) {
        indicator.innerHTML = '<i class="fa-solid fa-circle-check" style="color:var(--success-color)"></i>';
    }
}

// Interactive Skimming Spans Toggles
function toggleSkimMode(checked) {
    playSound('chime');
    const s1 = document.getElementById('sk-s1');
    const s2 = document.getElementById('sk-s2');
    const s3 = document.getElementById('sk-s3');
    const s4 = document.getElementById('sk-s4');
    const s5 = document.getElementById('sk-s5');
    const s6 = document.getElementById('sk-s6');
    
    if (checked) {
        s1.classList.add('skim-highlight');
        s6.classList.add('skim-highlight');
        s2.classList.add('skim-blur');
        s3.classList.add('skim-blur');
        s4.classList.add('skim-blur');
        s5.classList.add('skim-blur');
    } else {
        s1.classList.remove('skim-highlight');
        s6.classList.remove('skim-highlight');
        s2.classList.remove('skim-blur');
        s3.classList.remove('skim-blur');
        s4.classList.remove('skim-blur');
        s5.classList.remove('skim-blur');
    }
}

// Skimming Interactive Examples Database
const skimmingExamples = {
    1: {
        passage: `
            <span class="skim-sentence" id="sk-s1">In recent years, more people have started working from home instead of <span class="vocab-term" data-word="commuting">commuting</span> to an office every day.</span>
            <span class="skim-sentence" id="sk-s2"> One major reason is that <span class="vocab-term" data-word="modern technology">modern technology</span> allows employees to communicate easily through video calls, emails, and online platforms.</span>
            <span class="skim-sentence" id="sk-s3"> Working remotely can also save time and money because people do not need to travel to work.</span>
            <span class="skim-sentence" id="sk-s4"> In addition, many workers feel more <span class="vocab-term" data-word="comfortable">comfortable</span> and <span class="vocab-term" data-word="productive">productive</span> when they can organize their own schedules.</span>
            <span class="skim-sentence" id="sk-s5"> However, some people believe that working from home may reduce opportunities for face-to-face interaction with colleagues.</span>
            <span class="skim-sentence" id="sk-s6"> Despite this <span class="vocab-term" data-word="drawback">drawback</span>, <span class="vocab-term" data-word="remote work">remote work</span> continues to gain <span class="vocab-term" data-word="popularity">popularity</span> in many countries around the world.</span>
        `,
        question: "What is the main idea of the paragraph?",
        translationQuestion: "Ý chính của đoạn văn này là gì?",
        options: [
            "A. The challenges of using technology at work",
            "B. The reasons why people prefer working in offices",
            "C. The growing popularity of working from home and its benefits",
            "D. The importance of commuting to work every day"
        ],
        translationOptions: [
            "A. Những thách thức của việc sử dụng công nghệ tại nơi làm việc",
            "B. Các lý do tại sao mọi người thích làm việc tại văn phòng hơn",
            "C. Sự phổ biến ngày càng tăng của làm việc tại nhà và các lợi ích của nó",
            "D. Tầm quan trọng của việc đi lại làm việc mỗi ngày"
        ],
        correctIdx: 2,
        feedback: `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong> Câu đầu tiên (Topic Sentence) và câu cuối cùng (Conclusion) đã được gạch chân/nổi bật ở trên để bạn thấy rõ: Ý chính của toàn đoạn chính là sự kết hợp giữa xu hướng làm việc từ xa và các lợi ích của nó.`,
        translationPassage: "Trong những năm gần đây, ngày càng nhiều người bắt đầu làm việc tại nhà thay vì đi lại đến văn phòng mỗi ngày. Một lý do lớn là công nghệ hiện đại cho phép nhân viên giao tiếp dễ dàng qua cuộc gọi video, email và các nền tảng trực tuyến. Làm việc từ xa cũng có thể tiết kiệm thời gian và tiền bạc vì mọi người không cần phải di chuyển đến nơi làm việc. Ngoài ra, nhiều người lao động cảm thấy thoải mái và hiệu quả hơn khi họ có thể tự sắp xếp thời gian biểu của mình. Tuy nhiên, một số người tin rằng làm việc tại nhà có thể làm giảm cơ hội tương tác trực tiếp với đồng nghiệp. Bất chấp hạn chế này, làm việc từ xa vẫn tiếp tục trở nên phổ biến ở nhiều quốc gia trên thế giới."
    },
    2: {
        passage: `
            <span class="skim-sentence" id="sk-s1">Many cities around the world are facing serious environmental problems due to the increasing number of <span class="vocab-term" data-word="private vehicles">private vehicles</span>.</span>
            <span class="skim-sentence" id="sk-s2"> Cars and motorcycles produce large amounts of <span class="vocab-term" data-word="air pollution">air pollution</span>, which can negatively affect people's health.</span>
            <span class="skim-sentence" id="sk-s3"> Traffic <span class="vocab-term" data-word="congestion">congestion</span> is another major issue, causing commuters to spend long hours on the road every day.</span>
            <span class="skim-sentence" id="sk-s4"> To address these problems, many governments are <span class="vocab-term" data-word="investing">investing</span> in public transportation systems such as buses, metro lines, and trains.</span>
            <span class="skim-sentence" id="sk-s5"> Public transport can reduce traffic jams, lower pollution levels, and provide a more <span class="vocab-term" data-word="affordable">affordable</span> way for people to travel.</span>
            <span class="skim-sentence" id="sk-s6"> For these reasons, many experts believe that improving public transportation is essential for <span class="vocab-term" data-word="sustainable">sustainable</span> urban development.</span>
        `,
        question: "What is the main idea of the paragraph?",
        translationQuestion: "Ý chính của đoạn văn này là gì?",
        options: [
            "A. The causes of traffic accidents in large cities",
            "B. The advantages of owning private vehicles",
            "C. The importance of improving public transportation in cities",
            "D. The history of public transportation systems"
        ],
        translationOptions: [
            "A. Các nguyên nhân gây tai nạn giao thông ở những thành phố lớn",
            "B. Các lợi thế của việc sở hữu phương tiện cá nhân",
            "C. Tầm quan trọng của việc cải thiện giao thông công cộng ở các thành phố",
            "D. Lịch sử của các hệ thống giao thông công cộng"
        ],
        correctIdx: 2,
        feedback: `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong> Câu đầu tiên đặt vấn đề về ô nhiễm/kẹt xe do xe cá nhân, và câu cuối kết luận giải pháp thiết yếu là cải thiện giao thông công cộng.`,
        translationPassage: "Nhiều thành phố trên thế giới đang đối mặt với các vấn đề môi trường nghiêm trọng do số lượng phương tiện cá nhân ngày càng tăng. Ô tô và xe máy tạo ra lượng lớn ô nhiễm không khí, có thể ảnh hưởng xấu đến sức khỏe của người dân. Ùn tắc giao thông là một vấn đề lớn khác, khiến người đi làm phải dành nhiều giờ trên đường mỗi ngày. Để giải quyết những vấn đề này, nhiều chính phủ đang đầu tư vào hệ thống giao thông công cộng như xe buýt, các tuyến tàu điện ngầm và xe lửa. Giao thông công cộng có thể giảm kẹt xe, giảm mức độ ô nhiễm và cung cấp một phương thức di chuyển hợp túi tiền hơn cho người dân. Vì những lý do này, nhiều chuyên gia tin rằng cải thiện giao thông công cộng là điều thiết yếu cho sự phát triển đô thị bền vững."
    }
};

let currentSkimExampleIdx = 1;

function switchSkimExample(exIdx) {
    currentSkimExampleIdx = exIdx;
    state.keywordGame.selectedSkimIdx = null;
    playSound('click');
    
    const btn1 = document.getElementById('btn-skim-ex1');
    const btn2 = document.getElementById('btn-skim-ex2');
    
    if (btn1 && btn2) {
        if (exIdx === 1) {
            btn1.style.background = 'var(--primary-color)';
            btn1.style.color = 'white';
            btn2.style.background = 'var(--surface-solid)';
            btn2.style.color = 'var(--text-color)';
        } else {
            btn2.style.background = 'var(--primary-color)';
            btn2.style.color = 'white';
            btn1.style.background = 'var(--surface-solid)';
            btn1.style.color = 'var(--text-color)';
        }
    }
    
    // Reset checkbox
    const toggleSkim = document.getElementById('toggle-skim-mode');
    if (toggleSkim) toggleSkim.checked = false;
    
    // Load passage html
    const data = skimmingExamples[exIdx];
    const passageContainer = document.getElementById('visual-skim-passage');
    if (passageContainer) {
        passageContainer.innerHTML = data.passage;
    }
    
    // Reset question content
    const questionBox = document.getElementById('skim-practice-question-box');
    if (questionBox) {
        let optionsHTML = '';
        data.options.forEach((opt, idx) => {
            optionsHTML += `<button class="mini-option" onclick="selectSkimAnswer(this, ${idx})">${opt}</button>`;
        });
        
        questionBox.innerHTML = `
            <p style="font-weight: 700; margin-bottom: 12px; color: var(--text-color);">${data.question}</p>
            <div style="display: grid; grid-template-columns: 1fr; gap: 10px;" id="skim-options-group">
                ${optionsHTML}
            </div>
            <button class="primary-btn btn-sm hidden" id="btn-check-skim" onclick="checkSkimAnswer()" style="margin-top: 15px; width: 100%; padding: 10px; border: none; font-weight: bold; background: var(--primary-color); color: white; border-radius: 12px; cursor: pointer;">KIỂM TRA (CHECK)</button>
            <div class="mini-feedback hidden" id="skim-feedback-box" style="margin-top: 15px;"></div>
            <div class="translation-box hidden" id="skim-translation-box" style="margin-top: 15px; padding: 12px; border-radius: var(--radius-sm); border: 1.5px dashed var(--border-color); background: var(--primary-light);"></div>
        `;
    }
    
    // Rebind tooltips
    bindVocabularyClickTooltips();
}

function selectSkimAnswer(btn, idx) {
    const opts = document.querySelectorAll('#skim-options-group .mini-option');
    opts.forEach(b => b.classList.remove('selected'));
    
    btn.classList.add('selected');
    state.keywordGame.selectedSkimIdx = idx;
    
    const checkBtn = document.getElementById('btn-check-skim');
    if (checkBtn) {
        checkBtn.classList.remove('hidden');
    }
}

function checkSkimAnswer() {
    const idx = state.keywordGame.selectedSkimIdx;
    if (idx === null) return;
    
    const currentData = skimmingExamples[currentSkimExampleIdx];
    const opts = document.querySelectorAll('#skim-options-group .mini-option');
    const fb = document.getElementById('skim-feedback-box');
    const transBox = document.getElementById('skim-translation-box');
    const checkBtn = document.getElementById('btn-check-skim');
    
    if (checkBtn) checkBtn.classList.add('hidden');
    opts.forEach(b => b.setAttribute('disabled', 'true'));
    
    if (idx === currentData.correctIdx) {
        playSound('success');
        opts[idx].classList.add('correct');
        
        // Auto-check and activate Skimming mode visual highlighting
        const toggleSkim = document.getElementById('toggle-skim-mode');
        if (toggleSkim) {
            toggleSkim.checked = true;
            toggleSkimMode(true);
        }
        
        // Auto-activate vocabulary terms dotted underlines and click handlers
        document.querySelectorAll('.vocab-term').forEach(t => t.classList.add('active'));
        
        state.progress.skimmingTheory = true;
        updateProgress();
    } else {
        playSound('fail');
        opts[idx].classList.add('incorrect');
        opts[currentData.correctIdx].classList.add('correct');
    }
    
    fb.innerHTML = currentData.feedback;
    fb.className = "mini-feedback";
    fb.classList.remove('hidden');
    
    // Show translations
    if (transBox) {
        transBox.innerHTML = `
            <h5 style="font-weight: 700; color: var(--primary-color); margin-bottom: 8px; font-size: 0.95rem; display: flex; align-items: center; gap: 6px;"><i class="fa-solid fa-language"></i> BẢN DỊCH CHI TIẾT (TRANSLATIONS)</h5>
            <div style="margin-bottom: 8px; font-size: 0.88rem; line-height: 1.4;">
                <strong>Dịch câu hỏi:</strong> ${currentData.translationQuestion}
            </div>
            <div style="margin-bottom: 10px; font-size: 0.88rem; line-height: 1.4;">
                <strong>Dịch phương án:</strong>
                <ul style="list-style-type: none; padding-left: 10px; margin: 4px 0;">
                    ${currentData.translationOptions.map((o, oIdx) => `<li style="margin-bottom: 4px; ${oIdx === currentData.correctIdx ? 'color:var(--success-color); font-weight:bold;' : ''}">${o}</li>`).join('')}
                </ul>
            </div>
            <div style="font-size: 0.88rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 8px; line-height: 1.5; text-align: justify;">
                <strong>Dịch đoạn văn:</strong><br/>
                <span style="color: var(--text-muted); font-style: italic;">"${currentData.translationPassage}"</span>
            </div>
        `;
        transBox.classList.remove('hidden');
    }
}

// Scanning Interactive Examples Database
const scanningExamples = {
    1: {
        passage: `
            <span class="scan-sentence">Mount Rushmore National <span class="vocab-term" data-word="memorial">memorial</span> is a massive monumental <span class="vocab-term" data-word="sculpture">sculpture</span> located in the Black Hills region of South Dakota.</span>
            <span class="scan-sentence"> The project was <span class="vocab-term" data-word="conceived">conceived</span> by historian Doane Robinson to promote tourism in the state.</span>
            <span class="scan-sentence"> Construction of the monument began in 1927 and officially ended in late October of <span id="scan-target-word">1941</span>.</span>
            <span class="scan-sentence"> Over the course of fourteen years, nearly four hundred workers carved the colossal granite faces of presidents.</span>
            <span class="scan-sentence"> Despite the hazardous conditions, not a single worker died during the <span class="vocab-term" data-word="excavation">excavation</span>.</span>
            <span class="scan-sentence"> The final construction cost was heavily <span class="vocab-term" data-word="subsidized">subsidized</span> by the federal government.</span>
        `,
        question: "In what year did the construction of the Mount Rushmore monument end?",
        translationQuestion: "Việc xây dựng tượng đài Mount Rushmore kết thúc vào năm nào?",
        options: [
            "A. 1927",
            "B. 1900",
            "C. 1941",
            "D. 1950"
        ],
        translationOptions: [
            "A. Năm 1927",
            "B. Năm 1900",
            "C. Năm 1941",
            "D. Năm 1950"
        ],
        correctIdx: 2,
        feedback: `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong> Từ khóa số liệu '1941' đã được định vị thành công bằng phương pháp Scanning (Đọc quét số liệu) trong đoạn văn dài.`,
        translationPassage: "Đài tưởng niệm Quốc gia Mount Rushmore là một tác phẩm điêu khắc hoành tráng khổng lồ nằm ở vùng Black Hills thuộc bang South Dakota. Dự án được khởi xướng bởi nhà sử học Doane Robinson nhằm thúc đẩy du lịch trong bang. Việc xây dựng tượng đài bắt đầu vào năm 1927 và chính thức kết thúc vào cuối tháng 10 năm 1941. Trong suốt mười bốn năm, gần bốn trăm công nhân đã chạm khắc các khuôn mặt tổng thống khổng lồ bằng đá granite. Bất chấp điều kiện nguy hiểm, không một công nhân nào thiệt mạng trong quá trình khai quật. Chi phí xây dựng cuối cùng được chính phủ liên bang tài trợ phần lớn."
    },
    2: {
        passage: `
            <span class="scan-sentence">The Nobel Prize is widely regarded as the most <span class="vocab-term" data-word="prestigious">prestigious</span> award available in the fields of science, literature, and peace.</span>
            <span class="scan-sentence"> It was established by Alfred Nobel, a Swedish chemist who acquired massive wealth from inventing dynamite.</span>
            <span class="scan-sentence"> The <span class="vocab-term" data-word="inaugural">inaugural</span> prizes were awarded in 1901 at the Royal Academy in Stockholm.</span>
            <span class="scan-sentence"> Among all the legendary <span class="vocab-term" data-word="laureates">laureates</span>, <span id="scan-target-word">Marie Curie</span> holds a unique place in scientific history.</span>
            <span class="scan-sentence"> She was the first female scientist to receive the award, winning it in Physics in 1903.</span>
            <span class="scan-sentence"> Later, she achieved another <span class="vocab-term" data-word="milestone">milestone</span> by winning a second Nobel Prize in Chemistry in 1911 for isolating pure radium.</span>
            <span class="scan-sentence"> Her scientific <span class="vocab-term" data-word="breakthroughs">breakthroughs</span> paved the way for modern research.</span>
        `,
        question: "Who was the first woman to win a Nobel Prize?",
        translationQuestion: "Ai là người phụ nữ đầu tiên giành giải Nobel?",
        options: [
            "A. Alfred Nobel",
            "B. Marie Curie",
            "C. Gustave Eiffel",
            "D. Gutzon Borglum"
        ],
        translationOptions: [
            "A. Alfred Nobel",
            "B. Marie Curie",
            "C. Gustave Eiffel",
            "D. Gutzon Borglum"
        ],
        correctIdx: 1,
        feedback: `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong> Từ khóa tên riêng 'Marie Curie' đã được định vị thành công (Đọc quét từ viết hoa/tên riêng) trong đoạn văn dài.`,
        translationPassage: "Giải Nobel được công nhận rộng rãi là giải thưởng danh giá nhất trong các lĩnh vực khoa học, văn học và hòa bình. Giải thưởng được thành lập bởi Alfred Nobel, một nhà hóa học người Thụy Điển, người đã có được khối tài sản khổng lồ từ việc phát minh ra thuốc nổ. Các giải thưởng đầu tiên được trao vào năm 1901 tại Học viện Hoàng gia ở Stockholm. Trong số tất cả các chủ nhân giải thưởng huyền thoại, Marie Curie giữ một vị trí độc nhất vô nhị trong lịch sử khoa học. Bà là nhà khoa học nữ đầu tiên nhận giải thưởng này, giành giải Nobel Vật lý năm 1903. Sau đó, bà đạt được một cột mốc khác khi giành giải Nobel Hóa học thứ hai vào năm 1911 nhờ phân tách radium tinh khiết. Những đột phá khoa học của bà đã mở đường cho nghiên cứu hiện đại."
    }
};

let currentScanExampleIdx = 1;

function switchScanExample(exIdx) {
    currentScanExampleIdx = exIdx;
    state.keywordGame.selectedScanIdx = null;
    playSound('click');
    
    const btn1 = document.getElementById('btn-scan-ex1');
    const btn2 = document.getElementById('btn-scan-ex2');
    
    if (btn1 && btn2) {
        if (exIdx === 1) {
            btn1.style.background = 'var(--primary-color)';
            btn1.style.color = 'white';
            btn2.style.background = 'var(--surface-solid)';
            btn2.style.color = 'var(--text-color)';
        } else {
            btn2.style.background = 'var(--primary-color)';
            btn2.style.color = 'white';
            btn1.style.background = 'var(--surface-solid)';
            btn1.style.color = 'var(--text-color)';
        }
    }
    
    // Load passage html
    const data = scanningExamples[exIdx];
    const passageContainer = document.getElementById('visual-scan-passage');
    if (passageContainer) {
        passageContainer.innerHTML = data.passage;
    }
    
    // Reset question content
    const questionBox = document.getElementById('scan-practice-question-box');
    if (questionBox) {
        let optionsHTML = '';
        data.options.forEach((opt, idx) => {
            optionsHTML += `<button class="mini-option" onclick="selectScanAnswer(this, ${idx})">${opt}</button>`;
        });
        
        questionBox.innerHTML = `
            <p style="font-weight: 700; margin-bottom: 12px; color: var(--text-color);">${data.question}</p>
            <div style="display: grid; grid-template-columns: 1fr; gap: 10px;" id="scan-options-group">
                ${optionsHTML}
            </div>
            <button class="primary-btn btn-sm hidden" id="btn-check-scan" onclick="checkScanAnswer()" style="margin-top: 15px; width: 100%; padding: 10px; border: none; font-weight: bold; background: var(--primary-color); color: white; border-radius: 12px; cursor: pointer;">KIỂM TRA (CHECK)</button>
            <div class="mini-feedback hidden" id="scan-feedback-box" style="margin-top: 15px;"></div>
            <div class="translation-box hidden" id="scan-translation-box" style="margin-top: 15px; padding: 12px; border-radius: var(--radius-sm); border: 1.5px dashed var(--border-color); background: var(--primary-light);"></div>
        `;
    }
    
    // Rebind tooltips
    bindVocabularyClickTooltips();
}

function selectScanAnswer(btn, idx) {
    const opts = document.querySelectorAll('#scan-options-group .mini-option');
    opts.forEach(b => b.classList.remove('selected'));
    
    btn.classList.add('selected');
    state.keywordGame.selectedScanIdx = idx;
    
    const checkBtn = document.getElementById('btn-check-scan');
    if (checkBtn) {
        checkBtn.classList.remove('hidden');
    }
}

function checkScanAnswer() {
    const idx = state.keywordGame.selectedScanIdx;
    if (idx === null) return;
    
    const currentData = scanningExamples[currentScanExampleIdx];
    const opts = document.querySelectorAll('#scan-options-group .mini-option');
    const fb = document.getElementById('scan-feedback-box');
    const transBox = document.getElementById('scan-translation-box');
    const checkBtn = document.getElementById('btn-check-scan');
    
    if (checkBtn) checkBtn.classList.add('hidden');
    opts.forEach(b => b.setAttribute('disabled', 'true'));
    
    if (idx === currentData.correctIdx) {
        playSound('success');
        opts[idx].classList.add('correct');
        
        // Activate target word highlight
        const targetWord = document.getElementById('scan-target-word');
        if (targetWord) {
            targetWord.classList.add('active');
        }
        
        // Auto-activate vocabulary terms dotted underlines and click handlers
        document.querySelectorAll('.vocab-term').forEach(t => t.classList.add('active'));
    } else {
        playSound('fail');
        opts[idx].classList.add('incorrect');
        opts[currentData.correctIdx].classList.add('correct');
    }
    
    fb.innerHTML = currentData.feedback;
    fb.className = "mini-feedback";
    fb.classList.remove('hidden');
    
    // Show translations
    if (transBox) {
        transBox.innerHTML = `
            <h5 style="font-weight: 700; color: var(--primary-color); margin-bottom: 8px; font-size: 0.95rem; display: flex; align-items: center; gap: 6px;"><i class="fa-solid fa-language"></i> BẢN DỊCH CHI TIẾT (TRANSLATIONS)</h5>
            <div style="margin-bottom: 8px; font-size: 0.88rem; line-height: 1.4;">
                <strong>Dịch câu hỏi:</strong> ${currentData.translationQuestion}
            </div>
            <div style="margin-bottom: 10px; font-size: 0.88rem; line-height: 1.4;">
                <strong>Dịch phương án:</strong>
                <ul style="list-style-type: none; padding-left: 10px; margin: 4px 0;">
                    ${currentData.translationOptions.map((o, oIdx) => `<li style="margin-bottom: 4px; ${oIdx === currentData.correctIdx ? 'color:var(--success-color); font-weight:bold;' : ''}">${o}</li>`).join('')}
                </ul>
            </div>
            <div style="font-size: 0.88rem; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 8px; line-height: 1.5; text-align: justify;">
                <strong>Dịch đoạn văn:</strong><br/>
                <span style="color: var(--text-muted); font-style: italic;">"${currentData.translationPassage}"</span>
            </div>
        `;
        transBox.classList.remove('hidden');
    }
}

// Interactive Scanning clicker game logic
const scanClickerStages = [
    {
        question: "Câu hỏi 1/5: Tìm năm John Bowlby đề xuất lý thuyết gắn kết tập tính học (1969)?",
        passage: 'Inspired by observations of imprinting, in <span class="scan-clickable" onclick="clickScanTerm(this, true)">1969</span> the British psychoanalyst <span class="scan-clickable" onclick="clickScanTerm(this, false)">John Bowlby</span> applied <span class="scan-clickable" onclick="clickScanTerm(this, false)">ethological theory</span> to the understanding of the relationship between an infant and its parents.',
        correctWord: "1969",
        explanation: "Chính xác! John Bowlby đề xuất lý thuyết gắn kết tập tính học vào năm 1969."
    },
    {
        question: "Câu hỏi 2/5: Tìm con số chỉ lượng xe đạp có ở Mỹ vào năm 1900 (10 million)?",
        passage: 'By happenstance, the number of people at the first New York show equaled the entire car population of the United States. In 1900, <span class="scan-clickable" onclick="clickScanTerm(this, true)">10 million</span> bicycles and an unknown number of <span class="scan-clickable" onclick="clickScanTerm(this, false)">horse-drawn carriages</span> provided the prime means of personal transportation.',
        correctWord: "10 million",
        explanation: "Chính xác! Có 10 triệu chiếc xe đạp ở Mỹ vào năm 1900."
    },
    {
        question: "Câu hỏi 3/5: Tìm năm bắt đầu dự án điêu khắc tượng đài Mount Rushmore (1927)?",
        passage: 'The creation of Mount Rushmore monument took 14 years – from <span class="scan-clickable" onclick="clickScanTerm(this, true)">1927</span> to <span class="scan-clickable" onclick="clickScanTerm(this, false)">1941</span> – and nearly a million dollars. These were times when money was difficult to come by and many people were jobless.',
        correctWord: "1927",
        explanation: "Xuất sắc! Bức tượng bắt đầu khắc vào năm 1927 và hoàn thành năm 1941."
    },
    {
        question: "Câu hỏi 4/5: Tìm nhiệt độ sôi của nước tinh khiết đo bằng độ Fahrenheit (212 degrees)?",
        passage: 'Under standard atmospheric conditions at sea level, pure water reaches its boiling point at exactly <span class="scan-clickable" onclick="clickScanTerm(this, true)">212 degrees</span> Fahrenheit, which corresponds to <span class="scan-clickable" onclick="clickScanTerm(this, false)">100 degrees</span> Celsius.',
        correctWord: "212 degrees",
        explanation: "Chính xác! Nước tinh khiết sôi ở 212 độ Fahrenheit."
    },
    {
        question: "Câu hỏi 5/5: Tìm năm giải Nobel Vật lý đầu tiên được trao tặng cho Wilhelm Röntgen (1901)?",
        passage: 'The inaugural Nobel Prize in Physics was awarded in <span class="scan-clickable" onclick="clickScanTerm(this, true)">1901</span> to the German physicist <span class="scan-clickable" onclick="clickScanTerm(this, false)">Wilhelm Röntgen</span> for his discovery of X-rays, marking a historical milestone in modern medicine.',
        correctWord: "1901",
        explanation: "Tuyệt vời! Giải Nobel Vật lý đầu tiên được trao vào năm 1901."
    }
];

// Add stage state variables to local state directly
state.scanningClicker = {
    stage: 0,
    completed: false
};

function initScanClicker() {
    const stageData = scanClickerStages[state.scanningClicker.stage];
    if (!stageData) return;
    
    const questionEl = document.getElementById('scan-clicker-question');
    const passageEl = document.getElementById('scan-clicker-passage');
    const progressEl = document.getElementById('scan-clicker-progress');
    const feedbackEl = document.getElementById('scan-clicker-feedback');
    
    if (questionEl) questionEl.textContent = stageData.question;
    if (passageEl) passageEl.innerHTML = stageData.passage;
    if (progressEl) progressEl.textContent = `${state.scanningClicker.stage}/${scanClickerStages.length}`;
    if (feedbackEl) feedbackEl.classList.add('hidden');
}

function clickScanTerm(btn, isCorrect) {
    if (state.scanningClicker.completed) return;
    const fb = document.getElementById('scan-clicker-feedback');
    
    if (isCorrect) {
        playSound('success');
        btn.classList.add('correct');
        
        fb.innerHTML = `<i class="fa-solid fa-circle-check text-green"></i> <strong>${scanClickerStages[state.scanningClicker.stage].correctWord}</strong>: ${scanClickerStages[state.scanningClicker.stage].explanation}`;
        fb.className = "mini-feedback";
        fb.classList.remove('hidden');
        
        state.scanningClicker.completed = true;
        
        setTimeout(() => {
            state.scanningClicker.stage++;
            state.scanningClicker.completed = false;
            
            if (state.scanningClicker.stage < scanClickerStages.length) {
                initScanClicker();
            } else {
                playSound('complete');
                document.getElementById('scan-clicker-question').innerHTML = `<i class="fa-solid fa-trophy text-yellow"></i> CHÚC MỪNG! Bạn đã hoàn thành toàn bộ Thử thách Đọc Quét Tốc Độ!`;
                document.getElementById('scan-clicker-passage').innerHTML = `<p style="text-align:center; padding: 20px; font-weight:700; color:var(--success-color);"><i class="fa-solid fa-circle-check"></i> Bản đồ định vị từ khóa đã được kích hoạt thành công trên hệ thống!</p>`;
                document.getElementById('scan-clicker-progress').textContent = `${scanClickerStages.length}/${scanClickerStages.length}`;
                
                state.progress.scanningTheory = true;
                updateProgress();
            }
        }, 2200);
    } else {
        playSound('fail');
        btn.classList.add('incorrect');
        setTimeout(() => btn.classList.remove('incorrect'), 800);
    }
}

// 17.5 Interactive Vocab Writing Quiz Game (Trả bài từ vựng)
function initVocabQuiz() {
    const setupBox = document.getElementById('vocab-quiz-setup');
    const quizBox = document.getElementById('vocab-quiz-interface');
    const resultBox = document.getElementById('vocab-quiz-result');
    
    const startBtn = document.getElementById('btn-start-vocab-quiz');
    const checkBtn = document.getElementById('btn-vocab-quiz-check');
    const nextBtn = document.getElementById('btn-vocab-quiz-next');
    const retryBtn = document.getElementById('btn-vocab-quiz-retry');
    
    const quizInput = document.getElementById('vocab-quiz-input');
    const viMeaning = document.getElementById('vocab-quiz-vi-meaning');
    const progressSpan = document.getElementById('vocab-quiz-progress');
    const feedbackBox = document.getElementById('vocab-quiz-feedback');
    const hintPara = document.getElementById('vocab-quiz-hint');
    const resultText = document.getElementById('vocab-quiz-result-text');
    
    if (!startBtn) return;
    
    startBtn.addEventListener('click', () => {
        if (state.savedWords.length < 3) {
            alert("⚠️ Bạn cần lưu ít nhất 3 từ/cụm từ vào Hộp từ vựng để bắt đầu Trả bài!");
            return;
        }
        
        playSound('click');
        // Shuffle savedWords and select up to 5 questions
        const shuffled = [...state.savedWords].sort(() => 0.5 - Math.random());
        state.vocabQuiz.questions = shuffled.slice(0, Math.min(5, shuffled.length));
        state.vocabQuiz.currentIdx = 0;
        state.vocabQuiz.score = 0;
        
        setupBox.classList.add('hidden');
        quizBox.classList.remove('hidden');
        resultBox.classList.add('hidden');
        
        loadQuizQuestion();
    });
    
    function loadQuizQuestion() {
        const q = state.vocabQuiz.questions[state.vocabQuiz.currentIdx];
        
        quizInput.value = "";
        quizInput.removeAttribute('disabled');
        quizInput.style.borderColor = "var(--border-color)";
        
        viMeaning.textContent = q.mean;
        
        // Show smart hint containing first letter and length
        const firstLetter = q.word.trim().charAt(0).toUpperCase();
        hintPara.textContent = `Gợi ý: Bắt đầu bằng chữ '${firstLetter}' (${q.word.length} ký tự)`;
        
        progressSpan.textContent = `Từ thứ ${state.vocabQuiz.currentIdx + 1}/${state.vocabQuiz.questions.length}`;
        feedbackBox.classList.add('hidden');
        
        checkBtn.classList.remove('hidden');
        nextBtn.classList.add('hidden');
        
        setTimeout(() => quizInput.focus(), 50);
    }
    
    checkBtn.addEventListener('click', () => {
        const q = state.vocabQuiz.questions[state.vocabQuiz.currentIdx];
        const typed = quizInput.value.trim().toLowerCase();
        const correct = q.word.trim().toLowerCase();
        
        checkBtn.classList.add('hidden');
        nextBtn.classList.remove('hidden');
        quizInput.setAttribute('disabled', 'true');
        feedbackBox.classList.remove('hidden');
        
        if (typed === correct) {
            playSound('success');
            quizInput.style.borderColor = "var(--success-color)";
            feedbackBox.innerHTML = `<i class="fa-solid fa-circle-check text-green"></i> <strong>Chính xác!</strong> Bạn viết rất chuẩn.`;
            feedbackBox.className = "mini-feedback correct";
            feedbackBox.style.color = "var(--success-color)";
            state.vocabQuiz.score++;
        } else {
            playSound('fail');
            quizInput.style.borderColor = "var(--error-color)";
            feedbackBox.innerHTML = `<i class="fa-solid fa-circle-xmark text-red"></i> <strong>Chưa chính xác!</strong> Đáp án đúng là: <span style="color:var(--success-color); font-weight:bold;">${q.word}</span>`;
            feedbackBox.className = "mini-feedback incorrect";
            feedbackBox.style.color = "var(--error-color)";
        }
    });
    
    nextBtn.addEventListener('click', () => {
        state.vocabQuiz.currentIdx++;
        if (state.vocabQuiz.currentIdx < state.vocabQuiz.questions.length) {
            loadQuizQuestion();
        } else {
            playSound('complete');
            quizBox.classList.add('hidden');
            resultBox.classList.remove('hidden');
            resultText.innerHTML = `Bạn đã trả lời đúng <strong>${state.vocabQuiz.score}/${state.vocabQuiz.questions.length}</strong> từ vựng!`;
        }
    });
    
    retryBtn.addEventListener('click', () => {
        playSound('click');
        const shuffled = [...state.savedWords].sort(() => 0.5 - Math.random());
        state.vocabQuiz.questions = shuffled.slice(0, Math.min(5, shuffled.length));
        state.vocabQuiz.currentIdx = 0;
        state.vocabQuiz.score = 0;
        
        setupBox.classList.add('hidden');
        quizBox.classList.remove('hidden');
        resultBox.classList.add('hidden');
        
        loadQuizQuestion();
    });
    
    // Bind Enter key trigger inside text input box
    quizInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            if (!checkBtn.classList.contains('hidden')) {
                checkBtn.click();
            } else if (!nextBtn.classList.contains('hidden')) {
                nextBtn.click();
            }
        }
    });
}

// 18. Initialize Application Core
document.addEventListener('DOMContentLoaded', () => {
    const initSafely = (name, fn) => {
        try {
            fn();
        } catch (e) {
            console.warn(`[Fault Isolation] Error initializing ${name}:`, e);
        }
    };

    initSafely('StudentProfile', initStudentProfile);
    initSafely('ThemeSwitcher', initThemeSwitcher);
    initSafely('SidebarNav', initSidebarNav);
    initSafely('EyeTracker', initEyeTracker);
    initSafely('KeywordsSortingGame', initKeywordsSortingGame);
    initSafely('SynonymMatchingGame', initSynonymMatchingGame);
    initSafely('MockControls', setupMockControls);
    initSafely('VocabControls', initVocabControls);
    initSafely('CertificateClose', initCertificateClose);
    initSafely('DangDetailTabs', initDangDetailTabs);
    
    // Bind visual map toggle
    try {
        const toggleSkim = document.getElementById('toggle-skim-mode');
        if (toggleSkim) {
            toggleSkim.addEventListener('change', (e) => {
                toggleSkimMode(e.target.checked);
            });
        }
    } catch (e) {
        console.error('Error binding Skim Toggle:', e);
    }
    
    initSafely('ScanClicker', initScanClicker);
    initSafely('VocabularyClickTooltips', bindVocabularyClickTooltips);
    initSafely('GlobalVocabSaver', initGlobalVocabSaver);
    initSafely('VocabQuiz', initVocabQuiz);
    initSafely('Progress', updateProgress);
    initSafely('SkimExampleInit', () => switchSkimExample(1));
    initSafely('ScanExampleInit', () => switchScanExample(1));

    // Initial mount of eye tracker lab to skimming placeholder
    try {
        const eyeLab = document.getElementById('eye-tracker-lab-root');
        const skimPlaceholder = document.getElementById('skimming-lab-placeholder');
        if (eyeLab && skimPlaceholder) {
            skimPlaceholder.appendChild(eyeLab);
        }
    } catch(e) {
        console.error('Error mounting initial eye lab:', e);
    }
});

// Global initialization for Chapter 2 Dạng tabs
function initDangDetailTabs() {
    const tabBtns = document.querySelectorAll('[data-dang-tab]');
    const tabPanels = document.querySelectorAll('#sec-dang-chi-tiet .tab-panel');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            playSound('click');
            const targetPanelId = btn.dataset.dangTab;
            
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            tabPanels.forEach(p => {
                if (p.id === targetPanelId) p.classList.add('active');
                else p.classList.remove('active');
            });
        });
    });
}

// 19. Save Learning Progress manually via LocalStorage
function saveLearningProgress() {
    playSound('success');
    
    // Save progress sub-states
    localStorage.setItem('vstep_progress', JSON.stringify(state.progress));
    localStorage.setItem('vstep_mini_practices', JSON.stringify(state.miniPractices));
    localStorage.setItem('vstep_saved_vocab', JSON.stringify(state.savedWords));
    localStorage.setItem('vstep_mock_exam', JSON.stringify({
        submitted: state.mockExam.submitted,
        score: state.mockExam.score,
        answers: state.mockExam.answers
    }));
    
    alert("🎉 Tuyệt vời! Toàn bộ tiến độ học tập và Hộp từ vựng của bạn đã được lưu thành công!");
}

// 20. Clear/Reset Learning Progress manually
function resetLearningProgress() {
    const confirmReset = confirm("⚠️ CẢNH BÁO: Bạn có chắc chắn muốn xóa toàn bộ lịch sử học tập, điểm thi thử và Hộp từ vựng để bắt đầu học lại từ đầu không?\n\nHành động này không thể hoàn tác!");
    if (!confirmReset) return;
    
    // Clear all localStorage keys
    localStorage.removeItem('vstep_student_name');
    localStorage.removeItem('vstep_progress');
    localStorage.removeItem('vstep_mini_practices');
    localStorage.removeItem('vstep_saved_vocab');
    localStorage.removeItem('vstep_mock_exam');
    localStorage.removeItem('vstep_theme_dark');
    
    // Refresh page to reset state completely
    window.location.reload();
}


