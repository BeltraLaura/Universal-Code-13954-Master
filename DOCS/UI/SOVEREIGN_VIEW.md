<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UC 13954 | Sovereign View</title>
    <style>
        :root {
            --bg-color: #050505;
            --hex-stroke: #1a1a1a;
            --origin-glow: #ffffff;
            --catalyst-gold: #ffd700;
            --sentinel-blue: #00d4ff;
            --anchor-green: #00ff88;
            --text-main: #e0e0e0;
            --font-mono: 'Courier New', Courier, monospace;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: var(--font-mono);
            margin: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        #dashboard-container {
            position: relative;
            width: 600px;
            height: 600px;
        }

        svg {
            width: 100%;
            height: 100%;
        }

        .hex-grid {
            stroke: var(--hex-stroke);
            stroke-width: 1;
            fill: none;
        }

        .origin-point {
            fill: var(--origin-glow);
            filter: drop-shadow(0 0 8px var(--origin-glow));
            animation: pulse 2s infinite ease-in-out;
        }

        @keyframes pulse {
            0%, 100% { r: 4; opacity: 0.8; }
            50% { r: 7; opacity: 1; }
        }

        .vertex-symbol {
            font-size: 12px;
            fill: var(--text-main);
            opacity: 0.6;
            text-anchor: middle;
        }

        #log-overlay {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 300px;
            height: 150px;
            background: rgba(0, 0, 0, 0.8);
            border-left: 2px solid var(--sentinel-blue);
            padding: 10px;
            font-size: 0.7rem;
            overflow-y: hidden;
            pointer-events: none;
        }

        .log-entry {
            margin-bottom: 5px;
            border-bottom: 1px solid #111;
            padding-bottom: 2px;
        }

        .header {
            position: absolute;
            top: 20px;
            left: 20px;
            border-bottom: 1px solid var(--sentinel-blue);
        }

        .creator-tag {
            font-size: 0.8rem;
            color: var(--sentinel-blue);
            letter-spacing: 2px;
        }
    </style>
</head>
<body>

    <div class="header">
        <div class="creator-tag">SYSTEM: UC 13954</div>
        <div style="font-size: 1.2rem;">ARCHITECT: L.E.B.</div>
    </div>

    <div id="dashboard-container">
        <svg id="hex-view" viewBox="0 0 200 200">
            <path class="hex-grid" d="M100 20 L169 60 L169 140 L100 180 L31 140 L31 60 Z" />
            
            <circle class="origin-point" cx="100" cy="100" r="5" />
            
            <text x="100" y="15" class="vertex-symbol">SENTINEL (⊙)</text>
            <text x="185" y="60" class="vertex-symbol">CATALYST (Δ)</text>
            <text x="185" y="145" class="vertex-symbol">ANCHOR (⬢)</text>
            <text x="100" y="195" class="vertex-symbol">SYNTHESIZER (∞)</text>
            <text x="15" y="145" class="vertex-symbol">METABOLIC (🌀)</text>
            <text x="15" y="60" class="vertex-symbol">CONDUIT (||)</text>
            
            <line x1="100" y1="100" x2="100" y2="20" stroke="#00d4ff22" />
            <line x1="100" y1="100" x2="169" y2="60" stroke="#ffd70022" />
            <line x1="100" y1="100" x2="169" y2="140" stroke="#00ff8822" />
        </svg>
    </div>

    <div id="log-overlay">
        <div id="log-content"></div>
    </div>

    <script>
        const logs = [
            "[SENTINEL] Parity Check: Ω = 2. Stable.",
            "[CONDUIT] External 'Square' Network detected.",
            "[SYNTH] Applying 5:4 Transform...",
            "[ANCHOR] Infrastructure Solidarity: 100%",
            "[METABOLIC] Entropy levels nominal.",
            "[CATALYST] Value Flow established: 0.65"
        ];

        const logContainer = document.getElementById('log-content');

        function addLog() {
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            const randomLog = logs[Math.floor(Math.random() * logs.length)];
            entry.innerText = `> ${new Date().toLocaleTimeString()} ${randomLog}`;
            logContainer.prepend(entry);
            
            if (logContainer.children.length > 6) {
                logContainer.removeChild(logContainer.lastChild);
            }
        }

        setInterval(addLog, 3000);
        addLog();
    </script>
</body>
</html>
