import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Be My Valentine? 💖",
    page_icon="💌",
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
    <title>Valentine Proposal</title>
    <!-- Importing Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    
    <style>
        /* --- RESET & BODY STYLES --- */
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            margin: 0;
            padding: 0;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            font-family: 'Poppins', sans-serif;
            /* Romantic Gradient Background */
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            background: linear-gradient(to top, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        /* --- FLOATING HEARTS BACKGROUND --- */
        .heart-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }

        .floating-heart {
            position: absolute;
            bottom: -100px;
            color: rgba(255, 255, 255, 0.6);
            animation: floatUp linear infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
        }

        /* --- MAIN CARD --- */
        .container {
            text-align: center;
            z-index: 10;
            background: rgba(255, 255, 255, 0.35);
            backdrop-filter: blur(10px); /* Glassmorphism */
            padding: 3rem;
            border-radius: 25px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 90%;
            width: 500px;
            transition: all 0.5s ease;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #d63384; /* Deep Pink */
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        p {
            font-size: 1.2rem;
            color: #6a1b9a;
            margin-bottom: 30px;
        }

        /* --- BUTTONS --- */
        .btn-group {
            position: relative;
            height: 100px; /* Space for moving button */
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }

        button {
            padding: 12px 30px;
            font-size: 1.2rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
        }

        #yesBtn {
            background: linear-gradient(45deg, #ff00cc, #333399);
            background: linear-gradient(to right, #ff758c 0%, #ff7eb3 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
        }

        #yesBtn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(255, 117, 140, 0.6);
        }

        #noBtn {
            background: white;
            color: #ff758c;
            border: 2px solid #ff758c;
            position: relative; /* Default position */
        }

        /* --- SUCCESS MESSAGE HIDDEN INITIALLY --- */
        #success-container {
            display: none;
            z-index: 20;
            text-align: center;
        }
        
        #success-container h1 {
            font-size: 4rem;
        }
        
        #success-container h2 {
            font-size: 3rem;
            color: #fff;
            margin: 20px 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            font-family: 'Dancing Script', cursive;
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

        /* Mobile Adjustments */
        @media (max-width: 600px) {
            h1 { font-size: 2.5rem; }
            #success-container h2 { font-size: 2rem; }
            .container { padding: 2rem; width: 90%; }
        }

    </style>
</head>
<body>

    <!-- Floating Hearts Background -->
    <div class="heart-bg" id="heart-bg"></div>

    <!-- Question Screen -->
    <div class="container" id="question-card">
        <h1>Will you be my Valentine? 🌹</h1>
        <p>I promise chocolates, love, and bad jokes! 💕✨</p>
        
        <div class="btn-group">
            <button id="yesBtn">Yes! 💘</button>
            <button id="noBtn">No 😢</button>
        </div>
    </div>

    <!-- Success Screen -->
    <div id="success-container">
        <h1>YAYYY!! 🥰💖</h1>
        <h2>Indrajit's First Valentine....Damnnn</h2>
        <p style="font-size: 1.5rem; color: #fff; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            You just made my heart the happiest! <br>
            Can't wait to celebrate with you! 🥂✨🎆
        </p>
    </div>

    <!-- Canvas for Fireworks -->
    <canvas id="fireworks"></canvas>

    <script>
        // --- 1. GENERATE FLOATING HEARTS BACKGROUND ---
        function createHearts() {
            const container = document.getElementById('heart-bg');
            const heartCount = 20;
            for (let i = 0; i < heartCount; i++) {
                const heart = document.createElement('div');
                heart.classList.add('floating-heart');
                heart.innerHTML = '❤️';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
                heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
                heart.style.animationDelay = Math.random() * 5 + 's';
                container.appendChild(heart);
            }
        }
        createHearts();

        // --- 2. RUNAWAY 'NO' BUTTON LOGIC (CONSTRAINED TO CENTER) ---
        const noBtn = document.getElementById('noBtn');
        const questionCard = document.getElementById('question-card');
        
        // Function to move button within safe center bounds
        function moveButton() {
            // Define a restricted area in the center (e.g., 60% of viewport)
            // This prevents it from going off-screen
            const safeWidth = window.innerWidth * 0.6; 
            const safeHeight = window.innerHeight * 0.6;

            // Calculate offsets to center this safe zone
            const offsetX = (window.innerWidth - safeWidth) / 2;
            const offsetY = (window.innerHeight - safeHeight) / 2;

            // Random position within this safe zone
            const randomX = offsetX + Math.random() * (safeWidth - noBtn.offsetWidth);
            const randomY = offsetY + Math.random() * (safeHeight - noBtn.offsetHeight);

            noBtn.style.position = 'fixed'; 
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
        }

        // Trigger on mouse hover
        noBtn.addEventListener('mouseover', moveButton);
        // Trigger on touch (for mobile)
        noBtn.addEventListener('touchstart', (e) => {
            e.preventDefault(); // Prevent clicking
            moveButton();
        });
        
        // Just in case they try to click it fast
        noBtn.addEventListener('click', (e) => {
            e.preventDefault();
            moveButton();
        });


        // --- 3. 'YES' BUTTON LOGIC & FIREWORKS ---
        const yesBtn = document.getElementById('yesBtn');
        const successContainer = document.getElementById('success-container');
        const canvas = document.getElementById('fireworks');
        const ctx = canvas.getContext('2d');

        yesBtn.addEventListener('click', () => {
            // Hide question, show success
            questionCard.style.display = 'none';
            successContainer.style.display = 'block';
            
            // Start fireworks
            startFireworks();
        });

        // --- FIREWORKS ENGINE (Vanilla JS) ---
        let particles = [];
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function createParticle(x, y) {
            const particleCount = 30;
            for (let i = 0; i < particleCount; i++) {
                particles.push({
                    x: x,
                    y: y,
                    color: `hsl(${Math.random() * 360}, 100%, 50%)`,
                    radius: Math.random() * 4 + 1,
                    velocity: {
                        x: (Math.random() - 0.5) * 6,
                        y: (Math.random() - 0.5) * 6
                    },
                    alpha: 1,
                    decay: Math.random() * 0.015 + 0.005
                });
            }
        }

        function animateFireworks() {
            // Slight fade effect for trails
            ctx.fillStyle = 'rgba(255, 154, 158, 0.2)'; // Matches background slightly
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            particles.forEach((p, index) => {
                p.velocity.y += 0.05; // Gravity
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
            // Auto launch fireworks periodically
            setInterval(() => {
                const x = Math.random() * canvas.width;
                const y = Math.random() * (canvas.height / 2); // Top half
                createParticle(x, y);
            }, 800);
            
            // Also launch on click (confetti burst style)
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
# We use height=1000 to ensure it covers the screen on standard laptops
# Scrolling is set to false to keep the app feeling like a native single page
components.html(html_code, height=1000, scrolling=False)
