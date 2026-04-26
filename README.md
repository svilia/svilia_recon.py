<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Svilia Recon Scanner v1.0 — GitHub README</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&display=swap" rel="stylesheet"/>
<style>
:root {
  --bg: #0a0c10;
  --bg2: #0d1117;
  --bg3: #161b22;
  --bg4: #1c2333;
  --border: #21262d;
  --accent: #00ff88;
  --accent2: #00cfff;
  --accent3: #ff4c6a;
  --accent4: #ffd700;
  --text: #c9d1d9;
  --text2: #8b949e;
  --text3: #58a6ff;
  --glow: 0 0 20px rgba(0,255,136,0.4);
  --glow2: 0 0 20px rgba(0,207,255,0.4);
}

* { margin:0; padding:0; box-sizing:border-box; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Rajdhani', sans-serif;
  font-size: 15px;
  line-height: 1.6;
  min-height: 100vh;
}

/* SCANLINE EFFECT */
body::before {
  content:'';
  position:fixed;
  top:0; left:0; right:0; bottom:0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0,255,136,0.015) 2px,
    rgba(0,255,136,0.015) 4px
  );
  pointer-events:none;
  z-index:9999;
}

.github-header {
  background: var(--bg3);
  border-bottom: 1px solid var(--border);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 13px;
  color: var(--text2);
}

.gh-tab {
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all .2s;
}
.gh-tab.active {
  background: var(--bg);
  color: var(--text);
  border: 1px solid var(--border);
}
.gh-tab svg { width:16px; height:16px; fill:currentColor; }

.wrapper {
  max-width: 980px;
  margin: 0 auto;
  padding: 24px 16px;
}

/* ── HERO BANNER ── */
.hero {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 0;
  margin-bottom: 28px;
  overflow: hidden;
  position: relative;
}

.hero-top {
  background: #010409;
  padding: 28px 32px 22px;
  position: relative;
  overflow: hidden;
}

.hero-top::before {
  content:'';
  position:absolute;
  inset:0;
  background:
    radial-gradient(ellipse 60% 60% at 20% 50%, rgba(0,255,136,0.08) 0%, transparent 70%),
    radial-gradient(ellipse 40% 80% at 80% 30%, rgba(0,207,255,0.06) 0%, transparent 70%);
}

.hero-dots {
  display:flex; gap:7px; margin-bottom:18px; position:relative;
}
.hero-dots span {
  width:13px; height:13px; border-radius:50%;
}
.hero-dots span:nth-child(1){background:#ff5f57;}
.hero-dots span:nth-child(2){background:#febc2e;}
.hero-dots span:nth-child(3){background:#28c840;}

.hero-version {
  position:absolute;
  top:18px; right:24px;
  font-family:'Share Tech Mono',monospace;
  font-size:11px;
  color:var(--text2);
  background:var(--bg4);
  padding:3px 10px;
  border-radius:20px;
  border:1px solid var(--border);
}

.hero-logo {
  display:flex;
  align-items:center;
  gap:20px;
  position:relative;
}

.logo-icon {
  width:80px; height:80px;
  background: linear-gradient(135deg, #0d1117 40%, #1c2333);
  border: 2px solid var(--accent);
  border-radius:12px;
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow: var(--glow), inset 0 0 20px rgba(0,255,136,0.05);
  flex-shrink:0;
  position:relative;
  overflow:hidden;
}

.logo-icon::after {
  content:'';
  position:absolute;
  inset:-1px;
  background: linear-gradient(135deg, var(--accent), transparent, var(--accent2));
  border-radius:12px;
  opacity:.3;
  z-index:0;
}

.logo-icon svg {
  width:44px;height:44px;
  position:relative;z-index:1;
  filter: drop-shadow(0 0 8px var(--accent));
}

.hero-title-group h1 {
  font-family:'Orbitron',monospace;
  font-size:42px;
  font-weight:900;
  letter-spacing:3px;
  line-height:1;
}

.hero-title-group h1 .s { color:var(--accent); text-shadow: 0 0 20px var(--accent); }
.hero-title-group h1 .r { color:var(--accent2); text-shadow: 0 0 20px var(--accent2); }

.hero-subtitle {
  font-family:'Share Tech Mono',monospace;
  font-size:12px;
  color:var(--text2);
  margin-top:6px;
  letter-spacing:2px;
  text-transform:uppercase;
}

.hero-tagline {
  font-family:'Rajdhani',sans-serif;
  font-weight:600;
  font-size:16px;
  color:var(--text);
  margin-top:18px;
  padding-top:18px;
  border-top:1px solid rgba(255,255,255,0.06);
  position:relative;
}

/* BADGES */
.badges {
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  padding:18px 32px;
  border-bottom: 1px solid var(--border);
  background:var(--bg2);
}

.badge {
  display:inline-flex;
  align-items:center;
  gap:0;
  border-radius:4px;
  overflow:hidden;
  font-family:'Share Tech Mono',monospace;
  font-size:11.5px;
  height:22px;
  cursor:default;
}
.badge-left {
  background:#555;
  color:#fff;
  padding:0 8px;
  height:100%;
  display:flex;
  align-items:center;
}
.badge-right {
  color:#fff;
  padding:0 8px;
  height:100%;
  display:flex;
  align-items:center;
}
.badge-right.green  { background:#2ea44f; }
.badge-right.blue   { background:#1d6fa4; }
.badge-right.cyan   { background:#0891b2; }
.badge-right.yellow { background:#d29922; }
.badge-right.red    { background:#b91c1c; }
.badge-right.purple { background:#7c3aed; }
.badge-right.orange { background:#c05621; }
.badge-right.teal   { background:#0f766e; }

/* NAV BUTTONS */
.nav-buttons {
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  padding:18px 32px 22px;
  background:var(--bg3);
}

.nav-btn {
  display:inline-flex;
  align-items:center;
  gap:7px;
  padding:8px 18px;
  border-radius:6px;
  font-family:'Rajdhani',sans-serif;
  font-weight:700;
  font-size:14px;
  cursor:pointer;
  text-decoration:none;
  transition:all .2s;
  letter-spacing:.5px;
  text-transform:uppercase;
}

.nav-btn.primary {
  background: linear-gradient(135deg, var(--accent), #00cc6a);
  color:#000;
  box-shadow: 0 0 15px rgba(0,255,136,0.3);
}
.nav-btn.secondary {
  background: linear-gradient(135deg, var(--accent2), #0080ff);
  color:#000;
  box-shadow: 0 0 15px rgba(0,207,255,0.3);
}
.nav-btn.outline {
  background:transparent;
  color:var(--accent);
  border:1px solid var(--accent);
}
.nav-btn.outline:hover {
  background:rgba(0,255,136,0.08);
}
.nav-btn.outline2 {
  background:transparent;
  color:var(--text2);
  border:1px solid var(--border);
}
.nav-btn.outline2:hover {
  background:var(--bg4);
  color:var(--text);
}

/* STAT PILLS */
.stats-row {
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-bottom:24px;
}

.stat-pill {
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:8px;
  padding:10px 18px;
  display:flex;
  align-items:center;
  gap:10px;
  font-family:'Share Tech Mono',monospace;
  font-size:13px;
}
.stat-pill .stat-num {
  font-family:'Orbitron',monospace;
  font-size:18px;
  font-weight:700;
  color:var(--accent);
}
.stat-pill .stat-label {
  color:var(--text2);
  font-size:11px;
  text-transform:uppercase;
  letter-spacing:1px;
}

/* SECTION HEADERS */
.section {
  margin-bottom:32px;
}

.section-header {
  font-family:'Orbitron',monospace;
  font-size:16px;
  font-weight:700;
  color:var(--accent);
  letter-spacing:2px;
  margin-bottom:16px;
  padding-bottom:10px;
  border-bottom:1px solid rgba(0,255,136,0.2);
  display:flex;
  align-items:center;
  gap:10px;
}

.section-header::before {
  content:'▶';
  font-size:10px;
  opacity:.7;
}

/* FEATURE TABLE */
.feat-table {
  width:100%;
  border-collapse:collapse;
  font-family:'Rajdhani',sans-serif;
  font-size:14.5px;
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:10px;
  overflow:hidden;
}

.feat-table thead tr {
  background:var(--bg4);
}

.feat-table th {
  padding:12px 16px;
  text-align:left;
  font-family:'Orbitron',monospace;
  font-size:11px;
  letter-spacing:2px;
  color:var(--text2);
  text-transform:uppercase;
  border-bottom:1px solid var(--border);
}

.feat-table td {
  padding:11px 16px;
  border-bottom:1px solid rgba(33,38,45,0.6);
  vertical-align:middle;
}

.feat-table tr:last-child td { border-bottom:none; }

.feat-table tr:hover td {
  background:rgba(0,255,136,0.03);
}

.feat-icon {
  font-size:18px;
  margin-right:6px;
}

.feat-name {
  font-weight:700;
  color:var(--text);
}

.feat-cmd {
  font-family:'Share Tech Mono',monospace;
  font-size:12px;
  background:rgba(0,207,255,0.1);
  color:var(--accent2);
  padding:2px 8px;
  border-radius:4px;
  border:1px solid rgba(0,207,255,0.2);
  display:inline-block;
  margin-left:6px;
}

/* PORT TABLE */
.port-table {
  width:100%;
  border-collapse:collapse;
  font-family:'Share Tech Mono',monospace;
  font-size:12.5px;
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:10px;
  overflow:hidden;
}
.port-table th {
  background:var(--bg4);
  padding:10px 14px;
  text-align:left;
  color:var(--text2);
  border-bottom:1px solid var(--border);
  font-size:11px;
  letter-spacing:1px;
  text-transform:uppercase;
}
.port-table td {
  padding:9px 14px;
  border-bottom:1px solid rgba(33,38,45,0.5);
}
.port-table tr:last-child td { border-bottom:none; }
.port-table tr:hover td { background:rgba(0,255,136,0.025); }

.port-num {
  color:var(--accent);
  font-weight:700;
  font-size:13px;
}
.status-open {
  color:var(--accent);
  background:rgba(0,255,136,0.1);
  border:1px solid rgba(0,255,136,0.2);
  border-radius:4px;
  padding:1px 8px;
  font-size:11px;
}
.status-closed {
  color:var(--accent3);
  background:rgba(255,76,106,0.1);
  border:1px solid rgba(255,76,106,0.2);
  border-radius:4px;
  padding:1px 8px;
  font-size:11px;
}
.status-filtered {
  color:var(--accent4);
  background:rgba(255,215,0,0.1);
  border:1px solid rgba(255,215,0,0.2);
  border-radius:4px;
  padding:1px 8px;
  font-size:11px;
}

/* CODE BLOCK */
.code-block {
  background:#010409;
  border:1px solid var(--border);
  border-radius:8px;
  overflow:hidden;
  margin-bottom:16px;
  font-family:'Share Tech Mono',monospace;
}

.code-header {
  background:var(--bg4);
  padding:8px 16px;
  font-size:11px;
  color:var(--text2);
  display:flex;
  align-items:center;
  justify-content:space-between;
  border-bottom:1px solid var(--border);
}

.code-copy {
  background:transparent;
  border:1px solid var(--border);
  color:var(--text2);
  padding:3px 10px;
  border-radius:4px;
  font-size:11px;
  cursor:pointer;
  font-family:'Share Tech Mono',monospace;
  transition:.2s;
}
.code-copy:hover { border-color:var(--accent); color:var(--accent); }

.code-body {
  padding:16px 20px;
  font-size:13px;
  line-height:1.8;
  overflow-x:auto;
}

.c-comment { color:#6a737d; }
.c-cmd     { color:var(--accent); }
.c-flag    { color:var(--accent2); }
.c-arg     { color:var(--accent4); }
.c-str     { color:#f97316; }
.c-prompt  { color:var(--accent3); user-select:none; }

/* MODULE CARDS */
.module-grid {
  display:grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap:12px;
}

.module-card {
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:8px;
  padding:16px;
  transition:all .2s;
  position:relative;
  overflow:hidden;
}

.module-card::before {
  content:'';
  position:absolute;
  top:0; left:0; right:0;
  height:2px;
  background:linear-gradient(90deg, var(--accent), var(--accent2));
  opacity:0;
  transition:.2s;
}

.module-card:hover {
  border-color:rgba(0,255,136,0.3);
  transform:translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.module-card:hover::before { opacity:1; }

.module-icon { font-size:26px; margin-bottom:8px; }
.module-name {
  font-family:'Orbitron',monospace;
  font-size:11px;
  font-weight:700;
  color:var(--accent);
  letter-spacing:1px;
  margin-bottom:4px;
}
.module-desc {
  font-size:12px;
  color:var(--text2);
  line-height:1.4;
}

/* CONTRIBUTORS */
.contrib-section {
  margin-bottom:32px;
}

.contrib-grid {
  display:flex;
  flex-wrap:wrap;
  gap:16px;
}

.contrib-card {
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:10px;
  padding:16px 20px;
  display:flex;
  align-items:center;
  gap:14px;
  transition:all .2s;
  min-width:220px;
}
.contrib-card:hover {
  border-color:rgba(0,207,255,0.3);
  box-shadow: 0 4px 20px rgba(0,207,255,0.1);
}

.contrib-avatar {
  width:52px; height:52px;
  border-radius:50%;
  border:2px solid var(--border);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:22px;
  flex-shrink:0;
  position:relative;
  overflow:hidden;
  background:var(--bg4);
}

.contrib-avatar.dev1 { border-color:var(--accent); box-shadow:0 0 12px rgba(0,255,136,0.3); }
.contrib-avatar.dev2 { border-color:var(--accent2); box-shadow:0 0 12px rgba(0,207,255,0.3); }
.contrib-avatar.dev3 { border-color:var(--accent4); box-shadow:0 0 12px rgba(255,215,0,0.3); }
.contrib-avatar.dev4 { border-color:var(--accent3); box-shadow:0 0 12px rgba(255,76,106,0.3); }

.contrib-info .contrib-name {
  font-family:'Orbitron',monospace;
  font-size:13px;
  font-weight:700;
  color:var(--text);
}
.contrib-info .contrib-handle {
  font-family:'Share Tech Mono',monospace;
  font-size:11px;
  color:var(--accent2);
  margin-top:2px;
}
.contrib-info .contrib-role {
  font-size:11px;
  color:var(--text2);
  margin-top:3px;
}

.contrib-badge {
  display:inline-flex;
  align-items:center;
  gap:4px;
  font-family:'Share Tech Mono',monospace;
  font-size:10px;
  padding:2px 8px;
  border-radius:20px;
  margin-top:5px;
}
.contrib-badge.lead    { background:rgba(0,255,136,0.1); color:var(--accent); border:1px solid rgba(0,255,136,0.2); }
.contrib-badge.core    { background:rgba(0,207,255,0.1); color:var(--accent2); border:1px solid rgba(0,207,255,0.2); }
.contrib-badge.contrib { background:rgba(255,215,0,0.1); color:var(--accent4); border:1px solid rgba(255,215,0,0.2); }
.contrib-badge.sec     { background:rgba(255,76,106,0.1); color:var(--accent3); border:1px solid rgba(255,76,106,0.2); }

/* PLATFORM BADGES */
.platform-pills {
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-bottom:20px;
}
.plat-pill {
  background:var(--bg4);
  border:1px solid var(--border);
  border-radius:6px;
  padding:6px 14px;
  font-family:'Share Tech Mono',monospace;
  font-size:12px;
  color:var(--text2);
  display:flex;
  align-items:center;
  gap:6px;
}
.plat-pill.active { border-color:var(--accent); color:var(--accent); }
.plat-dot { width:7px;height:7px;border-radius:50%;background:currentColor; }

/* CALLOUT */
.callout {
  border-radius:8px;
  padding:14px 18px;
  margin-bottom:16px;
  display:flex;
  gap:12px;
  align-items:flex-start;
  font-size:14px;
}
.callout.warn {
  background:rgba(255,215,0,0.06);
  border:1px solid rgba(255,215,0,0.25);
  color:#c9a227;
}
.callout.info {
  background:rgba(0,207,255,0.05);
  border:1px solid rgba(0,207,255,0.2);
  color:#7dd3fc;
}
.callout.danger {
  background:rgba(255,76,106,0.06);
  border:1px solid rgba(255,76,106,0.25);
  color:#f87171;
}
.callout-icon { font-size:18px; flex-shrink:0; margin-top:1px; }

/* SCAN ANIMATION BOX */
.scan-demo {
  background:#010409;
  border:1px solid var(--border);
  border-radius:8px;
  padding:20px;
  font-family:'Share Tech Mono',monospace;
  font-size:12px;
  color:var(--accent);
  line-height:2;
  position:relative;
  overflow:hidden;
}

.scan-demo::before {
  content:'';
  position:absolute;
  left:0; right:0;
  height:1px;
  background:linear-gradient(90deg, transparent, var(--accent), transparent);
  opacity:.5;
  animation: scanline 3s linear infinite;
}

@keyframes scanline {
  0%   { top:-1px; }
  100% { top:101%; }
}

.scan-line { margin:2px 0; }
.sl-dim { color:#2a3a2a; }
.sl-bright { color:var(--accent); }
.sl-cyan { color:var(--accent2); }
.sl-yellow { color:var(--accent4); }
.sl-red { color:var(--accent3); }

/* FOOTER */
.readme-footer {
  margin-top:40px;
  padding:24px 0;
  border-top:1px solid var(--border);
  display:flex;
  align-items:center;
  justify-content:space-between;
  flex-wrap:wrap;
  gap:12px;
}
.footer-left {
  font-family:'Share Tech Mono',monospace;
  font-size:11px;
  color:var(--text2);
}
.footer-right {
  display:flex;
  gap:16px;
  font-family:'Share Tech Mono',monospace;
  font-size:11px;
}
.footer-link { color:var(--accent2); text-decoration:none; }

/* DIVIDER */
.divider {
  height:1px;
  background:linear-gradient(90deg,transparent,var(--border),transparent);
  margin:28px 0;
}

/* RESPONSIVE */
@media (max-width:640px) {
  .hero-logo { flex-direction:column; align-items:flex-start; }
  .hero-title-group h1 { font-size:28px; }
  .module-grid { grid-template-columns:1fr 1fr; }
  .nav-buttons { padding:14px 16px; }
  .badges { padding:14px 16px; }
  .hero-top { padding:20px 16px; }
}

/* BLINK CURSOR */
.cursor::after {
  content:'█';
  animation:blink 1s steps(1) infinite;
}
@keyframes blink {
  0%,100%{opacity:1;}
  50%{opacity:0;}
}

/* TOC */
.toc {
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:8px;
  padding:16px 20px;
  font-size:13.5px;
  margin-bottom:28px;
}
.toc-title {
  font-family:'Orbitron',monospace;
  font-size:11px;
  color:var(--text2);
  letter-spacing:2px;
  text-transform:uppercase;
  margin-bottom:10px;
}
.toc ul { list-style:none; padding-left:12px; }
.toc li { margin:4px 0; }
.toc a { color:var(--accent2); text-decoration:none; font-family:'Share Tech Mono',monospace; font-size:12px; }
.toc a:hover { color:var(--accent); }
.toc li::before { content:'→ '; color:var(--accent3); font-size:10px; }
</style>
</head>
<body>

<!-- GITHUB HEADER -->
<div class="github-header">
  <svg viewBox="0 0 16 16" width="20" height="20" fill="#c9d1d9"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
  <span style="color:#c9d1d9;font-weight:600;">svilia-dev</span>
  <span style="color:#8b949e;">/</span>
  <span style="color:var(--accent3);font-weight:600;">recon-scanner</span>
  <span style="flex:1"></span>
  <div class="gh-tab active">
    <svg viewBox="0 0 16 16"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v9.5A1.75 1.75 0 0114.25 13H8.06l-2.573 2.573A1.458 1.458 0 013 14.543V13H1.75A1.75 1.75 0 010 11.25v-9.5z"/></svg>
    README
  </div>
  <div class="gh-tab">
    <svg viewBox="0 0 16 16"><path d="M8.75.75a.75.75 0 00-1.5 0v5.19L5.03 3.72a.75.75 0 00-1.06 1.06l3.5 3.5a.75.75 0 001.06 0l3.5-3.5a.75.75 0 00-1.06-1.06L8.75 5.94V.75z"/></svg>
    MIT License
  </div>
</div>

<div class="wrapper">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-top">
      <div class="hero-dots">
        <span></span><span></span><span></span>
      </div>
      <div class="hero-version">svilia-recon-scanner — v1.0.0</div>

      <div class="hero-logo">
        <div class="logo-icon">
          <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Radar dish -->
            <circle cx="32" cy="32" r="28" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="4 3" opacity=".3"/>
            <circle cx="32" cy="32" r="18" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="3 3" opacity=".5"/>
            <circle cx="32" cy="32" r="9"  stroke="#00ff88" stroke-width="2" opacity=".8"/>
            <circle cx="32" cy="32" r="3"  fill="#00ff88"/>
            <!-- Sweep line -->
            <line x1="32" y1="32" x2="54" y2="20" stroke="#00cfff" stroke-width="2" stroke-linecap="round" opacity=".9"/>
            <!-- Blip -->
            <circle cx="50" cy="22" r="3" fill="#00cfff" opacity=".9"/>
            <circle cx="50" cy="22" r="6" stroke="#00cfff" stroke-width="1" opacity=".3"/>
          </svg>
        </div>
        <div class="hero-title-group">
          <h1><span class="s">SVILIA</span> <span class="r">RECON</span></h1>
          <h1 style="color:#e6edf3;text-shadow:none;font-size:36px;letter-spacing:6px;">SCANNER</h1>
          <div class="hero-subtitle">// Advanced Port &amp; Network Reconnaissance Framework</div>
        </div>
      </div>

      <div class="hero-tagline">
        ⚡ All-in-One Recon Tool for Security Researchers &amp; Pentesters — Fast, Modular &amp; Stealthy
      </div>
    </div>

    <!-- BADGES -->
    <div class="badges">
      <span class="badge"><span class="badge-left">version</span><span class="badge-right green">v1.0.0</span></span>
      <span class="badge"><span class="badge-left">python</span><span class="badge-right blue">3.10+</span></span>
      <span class="badge"><span class="badge-left">license</span><span class="badge-right cyan">MIT</span></span>
      <span class="badge"><span class="badge-left">stars</span><span class="badge-right yellow">⭐ 1.2k</span></span>
      <span class="badge"><span class="badge-left">forks</span><span class="badge-right orange">🍴 214</span></span>
      <span class="badge"><span class="badge-left">modules</span><span class="badge-right teal">18</span></span>
      <span class="badge"><span class="badge-left">platform</span><span class="badge-right purple">Linux / Kali / Parrot</span></span>
      <span class="badge"><span class="badge-left">status</span><span class="badge-right green">active</span></span>
      <span class="badge"><span class="badge-left">last commit</span><span class="badge-right blue">2 days ago</span></span>
    </div>

    <!-- NAV BUTTONS -->
    <div class="nav-buttons">
      <span class="nav-btn primary">⚙ Install Now</span>
      <span class="nav-btn secondary">⚡ Quick Start</span>
      <span class="nav-btn outline">📡 Port Scanner</span>
      <span class="nav-btn outline">🔍 OSINT Mode</span>
      <span class="nav-btn outline2">💡 Suggest Module</span>
      <span class="nav-btn outline2">📖 Wiki</span>
    </div>
  </div>

  <!-- STATS -->
  <div class="stats-row">
    <div class="stat-pill">
      <div>
        <div class="stat-num">65,535</div>
        <div class="stat-label">Ports Scanned</div>
      </div>
    </div>
    <div class="stat-pill">
      <div>
        <div class="stat-num">18</div>
        <div class="stat-label">Modules</div>
      </div>
    </div>
    <div class="stat-pill">
      <div>
        <div class="stat-num">400+</div>
        <div class="stat-label">Techniques</div>
      </div>
    </div>
    <div class="stat-pill">
      <div>
        <div class="stat-num">0.3s</div>
        <div class="stat-label">Avg Scan Speed</div>
      </div>
    </div>
    <div class="stat-pill">
      <div>
        <div class="stat-num">100%</div>
        <div class="stat-label">Open Source</div>
      </div>
    </div>
  </div>

  <!-- TOC -->
  <div class="toc">
    <div class="toc-title">📋 Table of Contents</div>
    <ul>
      <li><a href="#">About Svilia Recon Scanner</a></li>
      <li><a href="#">What's New in v1.0.0</a></li>
      <li><a href="#">Port Scanner Modules</a></li>
      <li><a href="#">Installation</a></li>
      <li><a href="#">Usage &amp; Commands</a></li>
      <li><a href="#">Common Port Reference Table</a></li>
      <li><a href="#">OSINT &amp; Recon Modules</a></li>
      <li><a href="#">Supported Platforms</a></li>
      <li><a href="#">Contributors</a></li>
      <li><a href="#">Legal Disclaimer</a></li>
    </ul>
  </div>

  <!-- ABOUT -->
  <div class="section">
    <div class="section-header">About Svilia Recon Scanner</div>
    <p style="color:var(--text2);font-size:15px;line-height:1.8;margin-bottom:14px;">
      <strong style="color:var(--text);">Svilia Recon Scanner</strong> is a high-speed, modular network reconnaissance framework designed for security professionals, ethical hackers, and CTF enthusiasts. Built with Python 3.10+, it combines multi-threaded port scanning, banner grabbing, OS fingerprinting, and OSINT intelligence gathering into a single unified terminal interface.
    </p>
    <p style="color:var(--text2);font-size:15px;line-height:1.8;margin-bottom:14px;">
      Unlike traditional scanners, Svilia features an <em style="color:var(--accent);">intelligent module engine</em> that automatically recommends the right scan profile based on your target, combined with a clean, hacker-aesthetic CLI that makes complex recon workflows simple.
    </p>
    <div class="callout info">
      <div class="callout-icon">ℹ️</div>
      <div>This tool is intended for <strong>authorized penetration testing and security research only</strong>. Always ensure you have explicit written permission before scanning any target system.</div>
    </div>
  </div>

  <!-- WHAT'S NEW -->
  <div class="section">
    <div class="section-header">What's New in v1.0.0</div>
    <table class="feat-table">
      <thead>
        <tr>
          <th width="30"></th>
          <th width="180">Feature</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="feat-icon">🚀</span></td>
          <td class="feat-name">Async Port Engine</td>
          <td style="color:var(--text2);">Rewritten from scratch using <code style="color:var(--accent2);background:rgba(0,207,255,0.08);padding:1px 6px;border-radius:3px;">asyncio</code> — scan 65,535 ports in under 2 seconds on LAN targets</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🧠</span></td>
          <td class="feat-name">Smart Profiling</td>
          <td style="color:var(--text2);">Type <code style="color:var(--accent);background:rgba(0,255,136,0.08);padding:1px 6px;border-radius:3px;">/</code> to search all modules by name, tag, or description keyword</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🏴</span></td>
          <td class="feat-name">Banner Grabbing</td>
          <td style="color:var(--text2);">Automatic service banner extraction with version detection on all open ports</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🌐</span></td>
          <td class="feat-name">OSINT Layer</td>
          <td style="color:var(--text2);">Passive reconnaissance: WHOIS, DNS enumeration, Shodan API, certificate transparency</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🎯</span></td>
          <td class="feat-name">Target Profiler</td>
          <td style="color:var(--text2);">Type <code style="color:var(--accent);background:rgba(0,255,136,0.08);padding:1px 6px;border-radius:3px;">r</code> — <em>"I want to scan a web server"</em> → shows relevant scan profile automatically</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🐳</span></td>
          <td class="feat-name">Docker Ready</td>
          <td style="color:var(--text2);">Zero-dependency Docker build — no external base images, fully self-contained</td>
        </tr>
        <tr>
          <td><span class="feat-icon">📦</span></td>
          <td class="feat-name">One-liner Install</td>
          <td style="color:var(--text2);">
            <code style="color:var(--accent3);background:rgba(255,76,106,0.08);padding:2px 8px;border-radius:4px;font-size:12px;">curl -sSL svilia.sh/install | sudo bash</code> — zero manual configuration
          </td>
        </tr>
        <tr>
          <td><span class="feat-icon">📊</span></td>
          <td class="feat-name">Export Reports</td>
          <td style="color:var(--text2);">Export scan results to JSON, XML, HTML, Markdown, or CSV formats instantly</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🔧</span></td>
          <td class="feat-name">Plugin System</td>
          <td style="color:var(--text2);">Drop any <code style="color:var(--accent4);background:rgba(255,215,0,0.08);padding:1px 6px;border-radius:3px;">.svp</code> plugin file into <code style="color:var(--accent4);background:rgba(255,215,0,0.08);padding:1px 6px;border-radius:3px;">~/.svilia/plugins/</code> — auto-loads on next run</td>
        </tr>
        <tr>
          <td><span class="feat-icon">🔒</span></td>
          <td class="feat-name">Stealth Mode</td>
          <td style="color:var(--text2);">SYN scan, decoy IPs, fragmented packets, and randomized timing to evade basic IDS</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PORT SCANNER DEMO -->
  <div class="section">
    <div class="section-header">Live Port Scanner Demo</div>
    <div class="scan-demo">
      <div class="scan-line sl-dim">████████████████████████████████████████████</div>
      <div class="scan-line" style="color:var(--accent4);">  SVILIA RECON SCANNER v1.0.0 — INITIALIZING</div>
      <div class="scan-line sl-dim">████████████████████████████████████████████</div>
      <div class="scan-line sl-dim">  </div>
      <div class="scan-line sl-cyan">  [*] Target     : 192.168.1.105</div>
      <div class="scan-line sl-cyan">  [*] Scan Type  : FULL TCP SYN + UDP</div>
      <div class="scan-line sl-cyan">  [*] Port Range : 1-65535</div>
      <div class="scan-line sl-cyan">  [*] Threads    : 1024</div>
      <div class="scan-line sl-cyan">  [*] Timeout    : 0.5s</div>
      <div class="scan-line sl-dim">  </div>
      <div class="scan-line sl-bright">  [SCAN] Starting async port sweep...</div>
      <div class="scan-line sl-dim">  ............................................</div>
      <div class="scan-line" style="color:var(--accent);">  [OPEN]  22/tcp   → SSH-2.0-OpenSSH_8.9p1</div>
      <div class="scan-line" style="color:var(--accent);">  [OPEN]  80/tcp   → Apache httpd 2.4.54</div>
      <div class="scan-line" style="color:var(--accent);">  [OPEN]  443/tcp  → nginx/1.22.0 (TLS 1.3)</div>
      <div class="scan-line sl-yellow">  [FILT]  8080/tcp → Filtered (no response)</div>
      <div class="scan-line" style="color:var(--accent);">  [OPEN]  3306/tcp → MySQL 8.0.31</div>
      <div class="scan-line sl-red">  [WARN]  3306/tcp → Port exposed! Consider firewall rule</div>
      <div class="scan-line" style="color:var(--accent);">  [OPEN]  6379/tcp → Redis 7.0.7 (NO AUTH)</div>
      <div class="scan-line sl-red">  [CRIT]  6379/tcp → Redis unauthenticated — HIGH RISK</div>
      <div class="scan-line sl-dim">  </div>
      <div class="scan-line sl-cyan">  [*] Scan complete in 1.34s</div>
      <div class="scan-line sl-cyan">  [*] 5 open ports | 1 filtered | 65529 closed</div>
      <div class="scan-line" style="color:var(--accent4);">  [*] Report saved: ./reports/192.168.1.105_scan.html</div>
      <div class="scan-line sl-dim">  </div>
      <div class="scan-line cursor" style="color:var(--accent);">  svilia@recon:~$ </div>
    </div>
  </div>

  <!-- MODULES -->
  <div class="section">
    <div class="section-header">Recon &amp; OSINT Modules</div>
    <div class="module-grid">
      <div class="module-card">
        <div class="module-icon">📡</div>
        <div class="module-name">PORT SCAN</div>
        <div class="module-desc">TCP SYN, UDP, Connect &amp; Stealth scanning with async engine</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🏴</div>
        <div class="module-name">BANNER GRAB</div>
        <div class="module-desc">Automatic service fingerprinting &amp; version detection</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🌐</div>
        <div class="module-name">DNS ENUM</div>
        <div class="module-desc">Subdomain brute-force, zone transfer, DNS record scraping</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🔍</div>
        <div class="module-name">WHOIS</div>
        <div class="module-desc">Full WHOIS lookup with registrar, ASN, and IP range data</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🛰️</div>
        <div class="module-name">SHODAN</div>
        <div class="module-desc">Shodan API integration for passive host intelligence</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🔐</div>
        <div class="module-name">SSL/TLS</div>
        <div class="module-desc">Certificate inspection, expiry check, weak cipher detection</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🕸️</div>
        <div class="module-name">WEB CRAWL</div>
        <div class="module-desc">Endpoint enumeration, hidden dirs, robots.txt &amp; sitemap</div>
      </div>
      <div class="module-card">
        <div class="module-icon">👤</div>
        <div class="module-name">USER ENUM</div>
        <div class="module-desc">Username harvesting from SSH, FTP, SMTP, HTTP services</div>
      </div>
      <div class="module-card">
        <div class="module-icon">💉</div>
        <div class="module-name">VULN SCAN</div>
        <div class="module-desc">CVE matching against detected service versions (offline DB)</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🗺️</div>
        <div class="module-name">TRACEROUTE</div>
        <div class="module-desc">Visual network path mapping with latency per hop</div>
      </div>
      <div class="module-card">
        <div class="module-icon">📧</div>
        <div class="module-name">EMAIL RECON</div>
        <div class="module-desc">MX records, SPF/DKIM/DMARC validation, email harvesting</div>
      </div>
      <div class="module-card">
        <div class="module-icon">🐳</div>
        <div class="module-name">DOCKER SCAN</div>
        <div class="module-desc">Detect exposed Docker APIs and container misconfigs</div>
      </div>
    </div>
  </div>

  <!-- INSTALLATION -->
  <div class="section">
    <div class="section-header">Installation</div>

    <div class="platform-pills">
      <div class="plat-pill active"><div class="plat-dot"></div> Kali Linux</div>
      <div class="plat-pill active"><div class="plat-dot"></div> ParrotOS</div>
      <div class="plat-pill active"><div class="plat-dot"></div> Ubuntu 20.04+</div>
      <div class="plat-pill active"><div class="plat-dot"></div> BlackArch</div>
      <div class="plat-pill" style="opacity:.4;"><div class="plat-dot"></div> macOS (partial)</div>
      <div class="plat-pill" style="opacity:.4;"><div class="plat-dot"></div> Windows WSL2</div>
    </div>

    <div class="code-block">
      <div class="code-header">
        <span>🐧 One-liner Install (Recommended)</span>
        <button class="code-copy" onclick="this.textContent='✓ Copied!'">Copy</button>
      </div>
      <div class="code-body">
        <div><span class="c-prompt">$ </span><span class="c-cmd">curl -sSL</span> <span class="c-str">https://svilia.sh/install</span> <span class="c-flag">|</span> <span class="c-cmd">sudo bash</span></div>
      </div>
    </div>

    <div class="code-block">
      <div class="code-header">
        <span>🐍 Manual Install (pip)</span>
        <button class="code-copy" onclick="this.textContent='✓ Copied!'">Copy</button>
      </div>
      <div class="code-body">
        <div><span class="c-comment"># Clone the repository</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">git clone</span> <span class="c-str">https://github.com/svilia-dev/recon-scanner.git</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">cd</span> recon-scanner</div>
        <div></div>
        <div><span class="c-comment"># Create virtual environment</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">python3 -m</span> venv .venv <span class="c-flag">&amp;&amp;</span> <span class="c-cmd">source</span> .venv/bin/activate</div>
        <div></div>
        <div><span class="c-comment"># Install dependencies</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">pip install</span> <span class="c-flag">-r</span> requirements.txt</div>
        <div></div>
        <div><span class="c-comment"># Run installer</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">sudo python3</span> setup.py install</div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-flag">--version</span></div>
      </div>
    </div>

    <div class="code-block">
      <div class="code-header">
        <span>🐳 Docker</span>
        <button class="code-copy" onclick="this.textContent='✓ Copied!'">Copy</button>
      </div>
      <div class="code-body">
        <div><span class="c-prompt">$ </span><span class="c-cmd">docker build</span> <span class="c-flag">-t</span> svilia-recon .</div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">docker run</span> <span class="c-flag">--rm -it</span> svilia-recon <span class="c-arg">192.168.1.1</span></div>
      </div>
    </div>
  </div>

  <!-- USAGE -->
  <div class="section">
    <div class="section-header">Usage &amp; Quick Commands</div>

    <div class="code-block">
      <div class="code-header">
        <span>⚡ Common Usage Examples</span>
        <button class="code-copy" onclick="this.textContent='✓ Copied!'">Copy</button>
      </div>
      <div class="code-body">
        <div><span class="c-comment"># Basic port scan (top 1000 ports)</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-arg">192.168.1.1</span></div>
        <div></div>
        <div><span class="c-comment"># Full scan all 65535 ports</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-arg">192.168.1.1</span> <span class="c-flag">-p 1-65535</span></div>
        <div></div>
        <div><span class="c-comment"># Stealth SYN scan with decoy IPs</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">sudo svilia</span> <span class="c-arg">192.168.1.1</span> <span class="c-flag">-sS --stealth --decoy</span> <span class="c-str">10.0.0.1,10.0.0.2</span></div>
        <div></div>
        <div><span class="c-comment"># OSINT mode (passive recon, no direct contact)</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-flag">--osint</span> <span class="c-arg">example.com</span></div>
        <div></div>
        <div><span class="c-comment"># Full recon profile (recommended)</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-arg">example.com</span> <span class="c-flag">--full --output</span> <span class="c-str">report.html</span></div>
        <div></div>
        <div><span class="c-comment"># Scan subnet range</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-arg">192.168.1.0/24</span> <span class="c-flag">--threads 512</span></div>
        <div></div>
        <div><span class="c-comment"># Vulnerability check on detected services</span></div>
        <div><span class="c-prompt">$ </span><span class="c-cmd">svilia</span> <span class="c-arg">192.168.1.1</span> <span class="c-flag">--vuln --cve-db local</span></div>
      </div>
    </div>
  </div>

  <!-- PORT REFERENCE TABLE -->
  <div class="section">
    <div class="section-header">Common Port Reference Table</div>
    <table class="port-table">
      <thead>
        <tr>
          <th>Port</th>
          <th>Protocol</th>
          <th>Service</th>
          <th>Status Example</th>
          <th>Risk Level</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="port-num">21</td>
          <td>TCP</td>
          <td style="color:var(--text);">FTP</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent3);">🔴 HIGH</td>
        </tr>
        <tr>
          <td class="port-num">22</td>
          <td>TCP</td>
          <td style="color:var(--text);">SSH</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent4);">🟡 MEDIUM</td>
        </tr>
        <tr>
          <td class="port-num">23</td>
          <td>TCP</td>
          <td style="color:var(--text);">Telnet</td>
          <td><span class="status-closed">CLOSED</span></td>
          <td style="color:var(--accent3);">🔴 CRITICAL</td>
        </tr>
        <tr>
          <td class="port-num">25</td>
          <td>TCP</td>
          <td style="color:var(--text);">SMTP</td>
          <td><span class="status-filtered">FILTERED</span></td>
          <td style="color:var(--accent4);">🟡 MEDIUM</td>
        </tr>
        <tr>
          <td class="port-num">53</td>
          <td>UDP/TCP</td>
          <td style="color:var(--text);">DNS</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent);">🟢 LOW</td>
        </tr>
        <tr>
          <td class="port-num">80</td>
          <td>TCP</td>
          <td style="color:var(--text);">HTTP</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent4);">🟡 MEDIUM</td>
        </tr>
        <tr>
          <td class="port-num">443</td>
          <td>TCP</td>
          <td style="color:var(--text);">HTTPS (TLS)</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent);">🟢 LOW</td>
        </tr>
        <tr>
          <td class="port-num">445</td>
          <td>TCP</td>
          <td style="color:var(--text);">SMB</td>
          <td><span class="status-closed">CLOSED</span></td>
          <td style="color:var(--accent3);">🔴 CRITICAL</td>
        </tr>
        <tr>
          <td class="port-num">3306</td>
          <td>TCP</td>
          <td style="color:var(--text);">MySQL</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent3);">🔴 HIGH</td>
        </tr>
        <tr>
          <td class="port-num">3389</td>
          <td>TCP</td>
          <td style="color:var(--text);">RDP</td>
          <td><span class="status-filtered">FILTERED</span></td>
          <td style="color:var(--accent3);">🔴 HIGH</td>
        </tr>
        <tr>
          <td class="port-num">5432</td>
          <td>TCP</td>
          <td style="color:var(--text);">PostgreSQL</td>
          <td><span class="status-closed">CLOSED</span></td>
          <td style="color:var(--accent3);">🔴 HIGH</td>
        </tr>
        <tr>
          <td class="port-num">6379</td>
          <td>TCP</td>
          <td style="color:var(--text);">Redis</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent3);">🔴 CRITICAL</td>
        </tr>
        <tr>
          <td class="port-num">8080</td>
          <td>TCP</td>
          <td style="color:var(--text);">HTTP Proxy</td>
          <td><span class="status-filtered">FILTERED</span></td>
          <td style="color:var(--accent4);">🟡 MEDIUM</td>
        </tr>
        <tr>
          <td class="port-num">9200</td>
          <td>TCP</td>
          <td style="color:var(--text);">Elasticsearch</td>
          <td><span class="status-open">OPEN</span></td>
          <td style="color:var(--accent3);">🔴 CRITICAL</td>
        </tr>
        <tr>
          <td class="port-num">27017</td>
          <td>TCP</td>
          <td style="color:var(--text);">MongoDB</td>
          <td><span class="status-closed">CLOSED</span></td>
          <td style="color:var(--accent3);">🔴 HIGH</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- LEGAL -->
  <div class="section">
    <div class="section-header">Legal Disclaimer</div>
    <div class="callout danger">
      <div class="callout-icon">⚠️</div>
      <div>
        <strong>FOR AUTHORIZED USE ONLY.</strong> Svilia Recon Scanner is provided for educational and authorized security testing purposes only. Unauthorized scanning or probing of systems you do not own or have explicit written permission to test is <strong>illegal</strong> and may violate the Computer Fraud and Abuse Act (CFAA), EU Computer Misuse laws, and equivalent regulations worldwide. The developers and contributors assume <strong>no liability</strong> for any misuse of this software. Use responsibly.
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- CONTRIBUTORS -->
  <div class="contrib-section">
    <div class="section-header">Contributors</div>
    <div class="contrib-grid">

      <div class="contrib-card">
        <div class="contrib-avatar dev1">🐉</div>
        <div class="contrib-info">
          <div class="contrib-name">Svilia</div>
          <div class="contrib-handle">@svilia-dev</div>
          <div class="contrib-role">Project Creator &amp; Lead Dev</div>
          <div class="contrib-badge lead">⚡ LEAD</div>
        </div>
      </div>

      <div class="contrib-card">
        <div class="contrib-avatar dev2">🦊</div>
        <div class="contrib-info">
          <div class="contrib-name">RedFoxSec</div>
          <div class="contrib-handle">@redfox_sec</div>
          <div class="contrib-role">Port Engine &amp; Async Core</div>
          <div class="contrib-badge core">🔧 CORE</div>
        </div>
      </div>

      <div class="contrib-card">
        <div class="contrib-avatar dev3">🦅</div>
        <div class="contrib-info">
          <div class="contrib-name">N3tHawk</div>
          <div class="contrib-handle">@n3thawk</div>
          <div class="contrib-role">OSINT Modules &amp; DNS</div>
          <div class="contrib-badge contrib">🌐 CONTRIB</div>
        </div>
      </div>

      <div class="contrib-card">
        <div class="contrib-avatar dev4">🕷️</div>
        <div class="contrib-info">
          <div class="contrib-name">ZeroTrace</div>
          <div class="contrib-handle">@zerotrace_0x</div>
          <div class="contrib-role">Stealth &amp; Evasion Research</div>
          <div class="contrib-badge sec">🔴 SEC</div>
        </div>
      </div>

    </div>
  </div>

  <!-- FOOTER -->
  <div class="readme-footer">
    <div class="footer-left">
      <div style="color:var(--accent);font-family:'Orbitron',monospace;font-size:12px;margin-bottom:4px;">SVILIA RECON SCANNER</div>
      <div>© 2024 svilia-dev • MIT License • Made with ❤️ for the security community</div>
    </div>
    <div class="footer-right">
      <a class="footer-link" href="#">📖 Docs</a>
      <a class="footer-link" href="#">🐛 Issues</a>
      <a class="footer-link" href="#">💬 Discord</a>
      <a class="footer-link" href="#">🐦 Twitter</a>
    </div>
  </div>

</div><!-- /wrapper -->

<script>
// Animate copy buttons
document.querySelectorAll('.code-copy').forEach(btn => {
  btn.addEventListener('click', () => {
    const orig = btn.textContent;
    btn.textContent = '✓ Copied!';
    btn.style.borderColor = 'var(--accent)';
    btn.style.color = 'var(--accent)';
    setTimeout(() => {
      btn.textContent = orig;
      btn.style.borderColor = '';
      btn.style.color = '';
    }, 2000);
  });
});
</script>
</body>
</html>
