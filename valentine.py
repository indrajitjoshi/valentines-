import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Strategic Proposal 📄",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS FOR STREAMLIT UI (To hide default elements)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        /* Hide Streamlit header, footer, and hamburger menu for immersion */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove padding to make iframe full screen */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. THE EMBEDDED WEB APP (HTML/CSS/JS)
# -----------------------------------------------------------------------------
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposal</title>
    <!-- Importing Classy Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
    
    <style>
        /* --- RESET & BODY STYLES --- */
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            margin: 0;
            padding: 0;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            font-family: 'Montserrat', sans-serif;
            /* Classy Blue Gradient Background */
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        /* --- BACKGROUND ELEMENTS (SUBTLE PARTICLES INSTEAD OF HEARTS) --- */
        .bg-element {
            position: absolute;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: floatUp linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-10vh) scale(1); opacity: 0; }
        }

        /* --- MAIN CARD (REEL LAYOUT 9:16 OPTIMIZED) --- */
        .container {
            text-align: center;
            z-index: 10;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(20px);
            /* Reduced padding for narrower width */
            padding: 2.5rem 1.5rem; 
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.4);
            
            /* Enforce Mobile/Reel Width */
            width: 90%;
            max-width: 400px; 
            
            transition: all 0.5s ease;
            
            /* Critical for trapping the No button inside */
            position: relative;
            overflow: hidden;
        }

        h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem; /* Slightly smaller for mobile width */
            color: #1e3c72; /* Royal Blue */
            margin-bottom: 15px;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        h3 {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #888;
            margin-bottom: 20px;
        }

        p {
            font-size: 1rem;
            color: #444;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .highlight {
            font-weight: 600;
            color: #1e3c72;
        }

        /* --- INPUT FIELDS --- */
        input[type="text"] {
            width: 100%;
            padding: 14px 15px;
            margin-bottom: 25px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-family: 'Montserrat', sans-serif;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.3s;
            text-align: center;
        }
        input[type="text"]:focus {
            border-color: #1e3c72;
        }

        /* --- BUTTONS --- */
        .btn-group {
            position: relative;
            height: 120px; /* More vertical space for mobile */
            display: flex;
            flex-direction: column; /* Stack buttons on mobile reel view */
            justify-content: center;
            align-items: center;
            gap: 15px;
        }

        button {
            width: 100%; /* Full width buttons */
            padding: 14px 20px;
            font-size: 1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        #yesBtn, #loginBtn {
            background: #1e3c72;
            color: white;
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3);
        }

        #yesBtn:hover, #loginBtn:hover {
            background: #2a5298;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
        }

        #noBtn {
            background: transparent;
            color: #888;
            border: 1px solid #ccc;
            position: relative;
        }

        #noBtn:hover {
            color: #d9534f;
            border-color: #d9534f;
        }

        /* --- SUCCESS MESSAGE --- */
        #success-container {
            display: none;
            z-index: 20;
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            padding: 3rem 1.5rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.4);
            
            /* Enforce Mobile/Reel Width */
            width: 90%;
            max-width: 400px;
        }
        
        #success-container h1 {
            font-size: 2.8rem;
            color: #1e3c72;
            margin-bottom: 10px;
        }
        
        #success-container h2 {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: #c5a059; /* Goldish color for accent */
            margin: 20px 0;
            font-style: italic;
            line-height: 1.4;
        }

        .kpi-box {
            margin-top: 30px;
            padding: 15px;
            background: #f8f9fa;
            border-left: 4px solid #1e3c72;
            text-align: left;
            border-radius: 4px;
        }

        /* --- FIREWORKS CANVAS --- */
        canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 15;
            pointer-events: none;
        }

    </style>
</head>
<body>

    <!-- Subtle Background Elements -->
    <div id="bg-container"></div>

    <!-- 1. LOGIN SCREEN -->
    <div class="container" id="login-card">
        <h3>Secure Access</h3>
        <h1>Identity Verification</h1>
        <p>Please enter your name to view the confidential proposal.</p>
        <input type="text" id="nameInput" placeholder="Enter your name..." autocomplete="off">
        <br>
        <button id="loginBtn">Proceed to Proposal</button>
    </div>

    <!-- 2. QUESTION SCREEN (Initially Hidden) -->
    <div class="container" id="question-card" style="display: none;">
        <h3>Executive Proposal</h3>
        <h1>Strategic Alliance Opportunity</h1>
        <p>
            I've analyzed the data, and the synergy is undeniable. 
            Proposed agenda includes <span class="highlight">dinner, drinks, and long-term value creation.</span><br><br>
            Does this align with your Q1 objectives?
        </p>
        
        <div class="btn-group">
            <button id="yesBtn">Accept Offer 🤝</button>
            <button id="noBtn">Decline</button>
        </div>
    </div>

    <!-- 3. SUCCESS SCREEN (Initially Hidden) -->
    <div id="success-container">
        <h1>Deal Closed! 🥂</h1>
        <h2 id="final-message"></h2>
        
        <div class="kpi-box">
            <p style="margin-bottom: 5px; font-weight: bold; color: #1e3c72;">MERGER UPDATE:</p>
            <p style="margin: 0; font-size: 0.95rem; color: #555;">
                Integration phase begins immediately. <br>
                Projected ROI: <strong>Infinite Happiness.</strong><br>
                Next Step: Celebration logistics are being finalized.
            </p>
        </div>
    </div>

    <!-- Canvas for Fireworks -->
    <canvas id="fireworks"></canvas>

    <script>
        // GLOBAL VARIABLE FOR NAME
        let partnerName = "Visitor";

        // --- 1. LOGIN LOGIC ---
        const loginCard = document.getElementById('login-card');
        const loginBtn = document.getElementById('loginBtn');
        const nameInput = document.getElementById('nameInput');
        const questionCard = document.getElementById('question-card');

        loginBtn.addEventListener('click', () => {
            const val = nameInput.value.trim();
            if (val) {
                partnerName = val;
                // Transition to next screen
                loginCard.style.display = 'none';
                questionCard.style.display = 'block';
            } else {
                nameInput.style.borderColor = '#d9534f';
                setTimeout(() => nameInput.style.borderColor = '#ddd', 1000);
            }
        });

        // Also allow Enter key
        nameInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') loginBtn.click();
        });


        // --- 2. GENERATE SUBTLE BACKGROUND ---
        function createBackground() {
            const container = document.getElementById('bg-container');
            const count = 15;
            for (let i = 0; i < count; i++) {
                const el = document.createElement('div');
                el.classList.add('bg-element');
                const size = Math.random() * 50 + 20;
                el.style.width = size + 'px';
                el.style.height = size + 'px';
                el.style.left = Math.random() * 100 + 'vw';
                el.style.animationDuration = (Math.random() * 10 + 10) + 's';
                el.style.animationDelay = Math.random() * 5 + 's';
                container.appendChild(el);
            }
        }
        createBackground();

        // --- 3. RUNAWAY 'NO' BUTTON LOGIC (CONSTRAINED TO CARD) ---
        const noBtn = document.getElementById('noBtn');
        
        function moveButton() {
            // We now calculate strictly based on the questionCard dimensions
            // clientWidth includes padding but not border
            const cardW = questionCard.clientWidth;
            const cardH = questionCard.clientHeight;
            
            const btnW = noBtn.offsetWidth;
            const btnH = noBtn.offsetHeight;

            // Maximum bounds within the card
            // We use a small buffer (15px) so it doesn't touch the absolute edge
            const buffer = 15;
            const maxLeft = cardW - btnW - buffer;
            const maxTop = cardH - btnH - buffer;

            // Generate random positions strictly within these bounds
            const randomX = Math.max(buffer, Math.random() * maxLeft);
            const randomY = Math.max(buffer, Math.random() * maxTop);

            // Change to Absolute positioning (relative to the card parent)
            noBtn.style.position = 'absolute'; 
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
            noBtn.style.zIndex = '100';
            
            // Funny changing text for MBA types
            const rejectionTexts = ["404 Error", "System Glitch", "Access Denied", "Try Again"];
            noBtn.innerText = rejectionTexts[Math.floor(Math.random() * rejectionTexts.length)];
        }

        noBtn.addEventListener('mouseover', moveButton);
        noBtn.addEventListener('touchstart', (e) => { e.preventDefault(); moveButton(); });
        noBtn.addEventListener('click', (e) => { e.preventDefault(); moveButton(); });


        // --- 4. 'YES' BUTTON LOGIC & FIREWORKS ---
        const yesBtn = document.getElementById('yesBtn');
        const successContainer = document.getElementById('success-container');
        const finalMessage = document.getElementById('final-message');
        const canvas = document.getElementById('fireworks');
        const ctx = canvas.getContext('2d');

        yesBtn.addEventListener('click', () => {
            // Set dynamic message
            finalMessage.innerText = `${partnerName}, Congratulations on becoming Indrajit's Valentine!`;
            
            questionCard.style.display = 'none';
            successContainer.style.display = 'block';
            startFireworks();
        });

        // --- FIREWORKS ENGINE (Refined for Classy Gold/Blue) ---
        let particles = [];
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function createParticle(x, y) {
            const particleCount = 40;
            for (let i = 0; i < particleCount; i++) {
                // Gold and Blue Fireworks
                const isGold = Math.random() > 0.5;
                const color = isGold 
                    ? `hsl(45, 80%, ${50 + Math.random() * 20}%)` // Gold range
                    : `hsl(215, 80%, ${60 + Math.random() * 20}%)`; // Blue range

                particles.push({
                    x: x,
                    y: y,
                    color: color,
                    radius: Math.random() * 3 + 1,
                    velocity: {
                        x: (Math.random() - 0.5) * 8,
                        y: (Math.random() - 0.5) * 8
                    },
                    alpha: 1,
                    decay: Math.random() * 0.015 + 0.005
                });
            }
        }

        function animateFireworks() {
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear completely for crisp look

            particles.forEach((p, index) => {
                p.velocity.y += 0.05;
                p.x += p.velocity.x;
                p.y += p.velocity.y;
                p.alpha -= p.decay;

                if (p.alpha <= 0) {
                    particles.splice(index, 1);
                } else {
                    ctx.save();
                    ctx.globalAlpha = p.alpha;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.fill();
                    ctx.restore();
                }
            });

            requestAnimationFrame(animateFireworks);
        }

        function startFireworks() {
            setInterval(() => {
                const x = Math.random() * canvas.width;
                const y = Math.random() * (canvas.height / 2);
                createParticle(x, y);
            }, 800);
            createParticle(window.innerWidth / 2, window.innerHeight / 2);
            animateFireworks();
        }

    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 4. RENDER THE COMPONENT
# -----------------------------------------------------------------------------
components.html(html_code, height=1000, scrolling=False)
