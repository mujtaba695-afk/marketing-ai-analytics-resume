import os
import json

# Build complete ultra-clean Framer Cohesion portfolio HTML
framer_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mujtaba Sajawal — Executive Performance Marketing Lead</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800;900&family=Public+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #090A0F;
    --bg-surface: #12141D;
    --bg-card: #1A1D2B;
    --bg-card-hover: #222638;
    --border: #2A2F45;
    --border-bright: #3D4463;
    --accent: #3B82F6;
    --accent-glow: rgba(59, 130, 246, 0.25);
    --accent-cyan: #06B6D4;
    --accent-emerald: #10B981;
    --accent-purple: #8B5CF6;
    --text-primary: #FFFFFF;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
    --font-heading: 'Onest', sans-serif;
    --font-body: 'Inter', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    background: var(--bg);
    color: var(--text-primary);
    font-family: var(--font-body);
    font-size: 15px;
    line-height: 1.6;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }

  /* BACKGROUND GLOWS */
  .bg-glow {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }
  .glow-1 {
    position: absolute;
    top: -10%; left: 20%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.12) 0%, transparent 70%);
    border-radius: 50%;
  }
  .glow-2 {
    position: absolute;
    top: 40%; right: -10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%);
    border-radius: 50%;
  }

  /* CONTAINER */
  .container {
    max-width: 1160px;
    margin: 0 auto;
    padding: 0 24px;
    position: relative;
    z-index: 1;
  }

  /* NAVIGATION */
  .navbar {
    position: fixed;
    top: 20px; left: 50%;
    transform: translateX(-50%);
    z-index: 100;
    width: calc(100% - 48px);
    max-width: 1000px;
    background: rgba(18, 20, 29, 0.85);
    backdrop-filter: blur(16px);
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 10px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  }
  .nav-brand {
    font-family: var(--font-heading);
    font-size: 16px;
    font-weight: 800;
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .status-dot {
    width: 8px; height: 8px;
    background: var(--accent-emerald);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--accent-emerald);
  }
  .nav-links {
    display: flex;
    gap: 24px;
    list-style: none;
  }
  .nav-links a {
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 13px;
    font-weight: 500;
    transition: color 0.2s;
  }
  .nav-links a:hover { color: white; }
  .btn-download {
    background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%);
    color: white;
    padding: 8px 18px;
    border-radius: 100px;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .btn-download:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
  }

  /* HERO SECTION */
  .hero {
    padding-top: 140px;
    padding-bottom: 60px;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59, 130, 246, 0.1);
    border: 1px solid rgba(59, 130, 246, 0.25);
    color: var(--accent);
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 20px;
  }
  .hero-title {
    font-family: var(--font-heading);
    font-size: clamp(2.5rem, 5vw, 4.2rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.02em;
    margin-bottom: 18px;
    background: linear-gradient(180deg, #FFFFFF 0%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-subtitle {
    font-size: 1.15rem;
    color: var(--text-secondary);
    max-width: 780px;
    line-height: 1.6;
    margin-bottom: 32px;
  }
  .hero-meta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 40px;
  }
  .meta-tag {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* LOGO WALL */
  .logo-wall {
    padding: 30px 0 60px;
    border-bottom: 1px solid var(--border);
  }
  .logo-wall-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--text-muted);
    margin-bottom: 20px;
    font-weight: 700;
  }
  .logo-grid {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 28px;
  }
  .brand-logo-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    height: 52px;
    transition: border-color 0.2s, transform 0.2s;
  }
  .brand-logo-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
  }
  .brand-logo-img {
    height: 28px;
    width: auto;
    object-fit: contain;
    filter: brightness(1.2);
  }
  .brand-logo-name {
    font-family: var(--font-heading);
    font-weight: 700;
    font-size: 14px;
    color: white;
  }

  /* STATS COUNTER GRID */
  .stats-section {
    padding: 60px 0;
  }
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
    gap: 16px;
  }
  .stat-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px 20px;
    transition: transform 0.2s, border-color 0.2s;
  }
  .stat-card:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
  }
  .stat-num {
    font-family: var(--font-heading);
    font-size: 2.2rem;
    font-weight: 800;
    color: white;
    line-height: 1;
    margin-bottom: 6px;
  }
  .stat-num.accent { color: var(--accent); }
  .stat-num.emerald { color: var(--accent-emerald); }
  .stat-num.cyan { color: var(--accent-cyan); }
  .stat-desc {
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.4;
  }

  /* SECTION HEADER */
  .section-header {
    margin-bottom: 32px;
  }
  .section-tag {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--accent);
    font-weight: 700;
    margin-bottom: 6px;
  }
  .section-title {
    font-family: var(--font-heading);
    font-size: 2.2rem;
    font-weight: 800;
    color: white;
  }

  /* EXPERIENCE SECTION */
  .experience-section {
    padding: 60px 0;
  }
  .experience-grid {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  .exp-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 32px;
    transition: border-color 0.3s;
  }
  .exp-card:hover {
    border-color: var(--border-bright);
  }
  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 18px;
  }
  .exp-company-group {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .exp-logo-box {
    width: 48px; height: 48px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    flex-shrink: 0;
  }
  .exp-logo-box img {
    max-width: 32px;
    max-height: 32px;
    object-fit: contain;
  }
  .exp-role-title {
    font-family: var(--font-heading);
    font-size: 1.3rem;
    font-weight: 800;
    color: white;
  }
  .exp-company-name {
    font-size: 14px;
    color: var(--accent);
    font-weight: 600;
  }
  .exp-date-pill {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 500;
    font-family: var(--font-mono);
  }
  .exp-bullets {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .exp-bullets li {
    position: relative;
    padding-left: 20px;
    color: var(--text-secondary);
    font-size: 14px;
    line-height: 1.5;
  }
  .exp-bullets li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: bold;
  }

  /* SKILLS & STACK SECTION */
  .skills-section {
    padding: 60px 0;
  }
  .skills-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
  }
  .skill-group-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 24px;
  }
  .skill-group-title {
    font-family: var(--font-heading);
    font-size: 16px;
    font-weight: 700;
    color: white;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .skill-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .skill-pill {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: #CBD5E1;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    transition: background 0.2s, border-color 0.2s;
  }
  .skill-pill:hover {
    border-color: var(--accent);
    background: var(--bg-card-hover);
    color: white;
  }

  /* CERTIFICATIONS GRID */
  .cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-top: 24px;
  }
  .cert-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .cert-icon {
    width: 36px; height: 36px;
    background: rgba(59, 130, 246, 0.15);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent);
    font-weight: bold;
    flex-shrink: 0;
  }
  .cert-title {
    font-size: 13px;
    font-weight: 700;
    color: white;
  }

  /* FOOTER */
  .footer {
    padding: 60px 0 40px;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--text-muted);
    font-size: 13px;
  }

  @media (max-width: 768px) {
    .nav-links { display: none; }
    .hero-title { font-size: 2.5rem; }
    .exp-card { padding: 20px; }
  }
</style>
</head>
<body>

<div class="bg-glow">
  <div class="glow-1"></div>
  <div class="glow-2"></div>
</div>

<!-- NAVIGATION -->
<nav class="navbar">
  <a href="#" class="nav-brand">
    <div class="status-dot"></div>
    Mujtaba Sajawal
  </a>
  <ul class="nav-links">
    <li><a href="#experience">Experience</a></li>
    <li><a href="#stats">Impact</a></li>
    <li><a href="#skills">Core Stack</a></li>
    <li><a href="#certs">Certifications</a></li>
  </ul>
  <a href="outputs/Master_Executive_Resume/01_RESUME/Mujtaba_Sajawal_Executive_Master_Resume.docx" class="btn-download" download>Download DOCX</a>
</nav>

<!-- HERO SECTION -->
<div class="container">
  <section class="hero">
    <div class="hero-badge">
      <span>●</span> Available for Executive Opportunities in Dubai &amp; GCC
    </div>
    <h1 class="hero-title">Performance Marketing Lead &amp; Growth Specialist</h1>
    <p class="hero-subtitle">10+ years of experience scaling acquisition campaigns across luxury real estate, commercial property, e-commerce marketplaces, and high-ticket B2B/B2C sectors. Managing <strong>$5.3M USD</strong> in paid media spend and <strong>$100K+ USD</strong> in performance analytics &amp; AI tooling infrastructure.</p>
    
    <div class="hero-meta-row">
      <div class="meta-tag">📍 Dubai, United Arab Emirates</div>
      <div class="meta-tag">🚗 UAE Driving License</div>
      <div class="meta-tag">📧 mujtabasajawal@hotmail.com</div>
      <div class="meta-tag">📞 +971 5 432 27639</div>
    </div>
  </section>

  <!-- BRAND LOGO WALL -->
  <section class="logo-wall">
    <div class="logo-wall-label">Verified Experience &amp; Brand Track Record</div>
    <div class="logo-grid">
      <div class="brand-logo-card">
        <img src="logo_cw.png" alt="Cushman & Wakefield" class="brand-logo-img">
        <span class="brand-logo-name">Cushman &amp; Wakefield | Core</span>
      </div>
      <div class="brand-logo-card">
        <img src="logo_kf.png" alt="Knight Frank" class="brand-logo-img">
        <span class="brand-logo-name">Knight Frank MENA</span>
      </div>
      <div class="brand-logo-card">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#3B82F6" stroke-width="2"><path d="M3 21h18M3 7v14M21 7v14M6 11h12M6 15h12M9 7V3h6v4"/></svg>
        <span class="brand-logo-name">RNS Realty</span>
      </div>
      <div class="brand-logo-card">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        <span class="brand-logo-name">Footprint Real Estate</span>
      </div>
      <div class="brand-logo-card">
        <img src="logo_olx.png" alt="OLX Group" class="brand-logo-img">
        <span class="brand-logo-name">OLX Group</span>
      </div>
    </div>
  </section>

  <!-- KEY STATS SECTION -->
  <section class="stats-section" id="stats">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-num accent">$5.3M</div>
        <div class="stat-desc">Cumulative Paid Media Spend</div>
      </div>
      <div class="stat-card">
        <div class="stat-num emerald">$100K+</div>
        <div class="stat-desc">Analytics &amp; AI MarTech Tooling</div>
      </div>
      <div class="stat-card">
        <div class="stat-num cyan">+34%</div>
        <div class="stat-desc">B2B Commercial Lead Growth</div>
      </div>
      <div class="stat-card">
        <div class="stat-num accent">2x ROAS</div>
        <div class="stat-desc">Multi-Channel Performance</div>
      </div>
      <div class="stat-card">
        <div class="stat-num emerald">21%</div>
        <div class="stat-desc">Lead Leakage Recovered</div>
      </div>
      <div class="stat-card">
        <div class="stat-num cyan">+25%</div>
        <div class="stat-desc">Landing Page Conversion Uplift</div>
      </div>
    </div>
  </section>

  <!-- WORK EXPERIENCE SECTION -->
  <section class="experience-section" id="experience">
    <div class="section-header">
      <div class="section-tag">Career History</div>
      <h2 class="section-title">Professional Experience</h2>
    </div>

    <div class="experience-grid">
      
      <!-- Cushman & Wakefield -->
      <div class="exp-card">
        <div class="exp-header">
          <div class="exp-company-group">
            <div class="exp-logo-box"><img src="logo_cw.png" alt="Cushman & Wakefield"></div>
            <div>
              <div class="exp-role-title">Performance Marketing Lead</div>
              <div class="exp-company-name">Cushman &amp; Wakefield | Core (Dubai, UAE)</div>
            </div>
          </div>
          <div class="exp-date-pill">Aug 2025 – Present</div>
        </div>
        <ul class="exp-bullets">
          <li>Built the firm's first-ever performance marketing ecosystem from scratch, architecting paid media infrastructure across Google Ads, Meta, and LinkedIn on a $50K/month budget to acquire B2B commercial real estate clients across the UAE, driving a 34% increase in qualified lead volume while reducing CPL by 18%.</li>
          <li>Architected closed-loop conversion tracking by configuring Meta Conversion API (CAPI) and Google Offline Conversion API, feeding offline CRM deal closures from Salesforce and Dynamics 365 back into ad platforms to optimize value-based bidding algorithms.</li>
          <li>Eliminated lead leakage across website forms, commercial landing pages, and social channels, recovering 21% of previously lost inquiries and establishing automated CRM lead-routing rules to ensure zero qualified inbound opportunity went unworked.</li>
          <li>Connected Claude Enterprise APIs directly to Google Ads, Meta, LinkedIn, Brevo, and Keyword Planner, automating real-time campaign auditing, AI-driven email marketing workflows, and programmatic bid optimizations.</li>
          <li>Engineered a brand-compliant plug-and-play landing page template system, enabling rapid asset deployment and accelerating campaign launch velocity while boosting inquiry conversion rates by 25%.</li>
          <li>Architected automated weekly reporting pipelines and a live C-suite Sales Leaderboard dashboard, providing senior management with real-time visibility into B2B commercial sales team throughput and channel ROI.</li>
          <li>Oversaw database migration from Salesforce to Microsoft Dynamics 365 Sales, building lead-scoring models and multi-touch nurture workflows via Brevo email marketing and WhatsApp to maximize lead farming across all commercial service lines.</li>
          <li>Partnered cross-functionally with internal Design, Engineering, and Corporate Communications teams while directing external agency partners to execute integrated digital acquisition campaigns and brand initiatives.</li>
        </ul>
      </div>

      <!-- RNS Realty -->
      <div class="exp-card">
        <div class="exp-header">
          <div class="exp-company-group">
            <div class="exp-logo-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#3B82F6" stroke-width="2"><path d="M3 21h18M3 7v14M21 7v14M6 11h12M6 15h12M9 7V3h6v4"/></svg></div>
            <div>
              <div class="exp-role-title">Digital Marketing Manager (Contract)</div>
              <div class="exp-company-name">RNS Realty (Dubai, UAE)</div>
            </div>
          </div>
          <div class="exp-date-pill">Feb 2025 – Aug 2025</div>
        </div>
        <ul class="exp-bullets">
          <li>Spearheaded lower-funnel performance media campaigns across Meta Ads and Google Ads on a $40K/month budget, growing overall digital lead volume by 32% within 3 months and lifting campaign ROI by 26%.</li>
          <li>Integrated Bitrix24 CRM and revamped corporate website, capturing 100% of web inquiries and establishing automated email and WhatsApp nurture workflows triggered by dynamic CRM lead stage changes.</li>
          <li>Architected Meta Conversion API (CAPI) and Google Offline Conversion API, streaming offline deal stages from Bitrix24 back into ad platforms to optimize value-based bidding for luxury UAE real estate.</li>
          <li>Linked WhatsApp messaging directly with Bitrix24 CRM, enabling instant lead notifications, accelerating response times, and achieving a 35% open rate with a 17% conversion rate on retargeted audiences.</li>
          <li>Executed targeted international performance campaigns, attracting high-net-worth real estate buyers across the US, UK, and Canada.</li>
        </ul>
      </div>

      <!-- Knight Frank -->
      <div class="exp-card">
        <div class="exp-header">
          <div class="exp-company-group">
            <div class="exp-logo-box"><img src="logo_kf.png" alt="Knight Frank"></div>
            <div>
              <div class="exp-role-title">Performance Marketing Lead</div>
              <div class="exp-company-name">Knight Frank MENA (Dubai, UAE)</div>
            </div>
          </div>
          <div class="exp-date-pill">Sep 2023 – Apr 2025</div>
        </div>
        <ul class="exp-bullets">
          <li>Led performance marketing strategy for a premier global real estate brand, overseeing a $75K/month paid media budget plus $8K/month analytics and ad tech tooling across MENA, APAC, and Europe.</li>
          <li>Managed paid media campaigns across SEM, display, paid social (LinkedIn, Meta, Google, TikTok), affiliate, and email marketing, driving a 31% increase in lead volume with 2x ROAS.</li>
          <li>Established a multi-touch attribution (MTA) framework, value-based bidding, and UTM governance model, delivering a 12% uplift in overall ROI by reallocating budget to top-performing channels.</li>
          <li>Optimized acquisition funnels through continuous landing page and creative A/B testing, resulting in a 29% campaign ROI improvement.</li>
          <li>Designed automated CRM lead management and onboarding workflows using Zapier, achieving an 85% lead-qualification rate and reactivating 7% of dormant leads.</li>
          <li>Collaborated cross-functionally with internal Design, Engineering, and Corporate Communications teams to align digital campaign strategy with global brand standards and trading targets.</li>
        </ul>
      </div>

      <!-- Footprint -->
      <div class="exp-card">
        <div class="exp-header">
          <div class="exp-company-group">
            <div class="exp-logo-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div>
            <div>
              <div class="exp-role-title">Digital Marketing Specialist</div>
              <div class="exp-company-name">Footprint Real Estate (Dubai, UAE)</div>
            </div>
          </div>
          <div class="exp-date-pill">Feb 2023 – Sep 2023</div>
        </div>
        <ul class="exp-bullets">
          <li>Managed a $40K/month digital advertising budget across Meta, Google, LinkedIn, TikTok, Yandex, Snapchat, YouTube, and Bing, targeting ultra-high-net-worth luxury property buyers across MEA, APAC, and Europe.</li>
          <li>Ran targeted multi-platform luxury real estate acquisition campaigns that increased qualified lead volume by 37% and boosted website traffic by 40%.</li>
          <li>Analyzed digital campaign analytics and collaborated closely with sales teams to align digital acquisition spend with commercial trading targets.</li>
        </ul>
      </div>

      <!-- OLX Group -->
      <div class="exp-card">
        <div class="exp-header">
          <div class="exp-company-group">
            <div class="exp-logo-box"><img src="logo_olx.png" alt="OLX Group"></div>
            <div>
              <div class="exp-role-title">Category Manager – Performance &amp; Digital Growth</div>
              <div class="exp-company-name">OLX Group (Lahore, Pakistan)</div>
            </div>
          </div>
          <div class="exp-date-pill">Apr 2018 – Jan 2023</div>
        </div>
        <ul class="exp-bullets">
          <li>Delivered $120K USD annual revenue target with 23% YoY growth by managing category trade and digital performance campaigns in a high-volume marketplace environment.</li>
          <li>Managed a $50K/month digital acquisition budget across Meta, Google, and TikTok, growing user traffic by 11% and driving 17% overall revenue growth across Pakistan and UAE markets.</li>
          <li>Grew mobile app user acquisition through targeted app campaigns, achieving a 14% increase on iOS and a 29% increase on Android.</li>
          <li>Led a cross-functional marketing and operational team of 50+ members across 6 cities, earning 'Employee of the Year' honors in 2020.</li>
        </ul>
      </div>

    </div>
  </section>

  <!-- SKILLS & INFRASTRUCTURE SECTION -->
  <section class="skills-section" id="skills">
    <div class="section-header">
      <div class="section-tag">Technical Capabilities</div>
      <h2 class="section-title">Core Skills &amp; Infrastructure</h2>
    </div>

    <div class="skills-card-grid">
      <div class="skill-group-card">
        <div class="skill-group-title">🎯 Paid Media Platforms</div>
        <div class="skill-pills">
          <span class="skill-pill">Google Ads (PMax, Search, YouTube)</span>
          <span class="skill-pill">Meta Ads (Facebook/Instagram)</span>
          <span class="skill-pill">LinkedIn Ads</span>
          <span class="skill-pill">TikTok Ads</span>
          <span class="skill-pill">Display &amp; Video 360 (DV360)</span>
          <span class="skill-pill">Programmatic Buying</span>
          <span class="skill-pill">Value-Based Bidding</span>
        </div>
      </div>

      <div class="skill-group-card">
        <div class="skill-group-title">📊 Analytics &amp; Attribution</div>
        <div class="skill-pills">
          <span class="skill-pill">Google Analytics 4 (GA4)</span>
          <span class="skill-pill">Server-Side Tagging (sGTM)</span>
          <span class="skill-pill">Meta Conversion API (CAPI)</span>
          <span class="skill-pill">Google Offline Conversion API</span>
          <span class="skill-pill">Multi-Touch Attribution (MTA)</span>
          <span class="skill-pill">Power BI &amp; Looker Studio</span>
          <span class="skill-pill">Single Source of Truth (SSOT)</span>
        </div>
      </div>

      <div class="skill-group-card">
        <div class="skill-group-title">⚡ CRM &amp; Automation Stack</div>
        <div class="skill-pills">
          <span class="skill-pill">Bitrix24 CRM</span>
          <span class="skill-pill">Salesforce Sales Cloud</span>
          <span class="skill-pill">Microsoft Dynamics 365</span>
          <span class="skill-pill">Brevo Email Automation</span>
          <span class="skill-pill">Zapier &amp; n8n</span>
          <span class="skill-pill">WhatsApp CRM Workflows</span>
          <span class="skill-pill">Claude Enterprise APIs</span>
        </div>
      </div>
    </div>
  </section>

  <!-- CERTIFICATIONS SECTION -->
  <section style="padding: 40px 0 80px;" id="certs">
    <div class="section-header">
      <div class="section-tag">Verified Credentials</div>
      <h2 class="section-title">Certifications</h2>
    </div>

    <div class="cert-grid">
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">Meta Blueprint Certification</div></div>
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">Google Ads Apps Certification</div></div>
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">Display &amp; Video 360 (Google)</div></div>
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">TikTok Media Buying</div></div>
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">LinkedIn Marketing Solutions</div></div>
      <div class="cert-card"><div class="cert-icon">✓</div><div class="cert-title">Google Analytics Certification</div></div>
    </div>
  </section>

</div>

<footer class="footer">
  <div class="container">
    <p>© 2026 Mujtaba Sajawal · Performance Marketing &amp; AI Analytics Lead · Dubai, UAE</p>
  </div>
</footer>

</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(framer_html)

print("✅ Successfully built Framer Cohesion portfolio index.html with clean company logos!")
