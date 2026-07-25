with open("index.html", "r") as f:
    content = f.read()

# Replace Cushman section in index.html
old_cw = """  <!-- CUSHMAN & WAKEFIELD -->
  <div class="experience-item current">
    <div class="experience-header">
      <div class="company-logo"><img src="logo_cw.png" alt="Cushman & Wakefield"></div>
      <div class="experience-meta">
        <div class="role">Performance Marketing Lead</div>
        <div class="company">Cushman & Wakefield · Core</div>
      </div>
      <div class="experience-dates">Aug 2025 — Present<div class="location">Dubai, UAE</div></div>
    </div>
    <p class="experience-description">Dual mandate leading the marketing analytics ecosystem (end-to-end attribution, GTM tagging, custom database pipelines) and driving organization-wide AI transformation. Built and deployed custom AI agents, automated web scrapers, and API integrations to streamline campaign execution and establish a centralized single source of truth (SSOT).</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+34%</div><div class="achievement-text">Increase in qualified lead volume while reducing Cost Per Lead (CPL) by 18%</div></div>
      <div class="achievement"><div class="achievement-metric">Power BI</div><div class="achievement-text">Developed Power BI dashboards & automated ETL pipelines with custom Python scripts to deliver performance insights to senior leadership weekly</div></div>
      <div class="achievement"><div class="achievement-metric">Salesforce</div><div class="achievement-text">Architected and deployed an AI-engineered local webpage synced with Salesforce API to automate and real-time update sales metrics</div></div>
      <div class="achievement"><div class="achievement-metric">IDEs</div><div class="achievement-text">Engineered high-converting marketing landing pages via dual-IDE AI workflows in VS Code (Claude) & Google Antigravity (Gemini), boosting inquiries by 25%</div></div>
      <div class="achievement"><div class="achievement-metric">MCPs</div><div class="achievement-text">Pioneered programmatic paid media optimization by configuring Google & Meta Ads MCPs for autonomous bidding and budget changes</div></div>
      <div class="achievement"><div class="achievement-metric">Dynamics</div><div class="achievement-text">Led Salesforce to Microsoft Dynamics 365 database migration with zero data loss, establishing a standardized schema for lead scoring</div></div>
    </div>
  </div>"""

new_cw = """  <!-- CUSHMAN & WAKEFIELD -->
  <div class="experience-item current">
    <div class="experience-header">
      <div class="company-logo"><img src="logo_cw.png" alt="Cushman & Wakefield"></div>
      <div class="experience-meta">
        <div class="role">Performance Marketing Lead</div>
        <div class="company">Cushman & Wakefield · Core</div>
      </div>
      <div class="experience-dates">Aug 2025 – Present<div class="location">Dubai, UAE</div></div>
    </div>
    <p class="experience-description">Architected the firm's first-ever performance marketing ecosystem from scratch, managing $50K/month paid media spend to acquire B2B commercial real estate clients across the UAE. Directing closed-loop attribution, offline API tracking, AI workflow automation, and cross-functional leadership across Design, Engineering, Communications, and external agencies.</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+34%</div><div class="achievement-text">Increase in B2B commercial lead volume with -18% CPL reduction on $50K/mo spend</div></div>
      <div class="achievement"><div class="achievement-metric">Offline API</div><div class="achievement-text">Architected Meta CAPI & Google Offline Conversion API syncing Salesforce/Dynamics deal closures</div></div>
      <div class="achievement"><div class="achievement-metric">+21% Leak</div><div class="achievement-text">Eliminated lead leakage across forms, landing pages, and social channels, recovering 21% inquiries</div></div>
      <div class="achievement"><div class="achievement-metric">Claude AI</div><div class="achievement-text">Connected Claude Enterprise APIs to Google Ads, Meta, LinkedIn, Brevo, and Keyword Planner</div></div>
      <div class="achievement"><div class="achievement-metric">+25% Conv</div><div class="achievement-text">Engineered plug-and-play landing page template system, boosting inquiry conversion by 25%</div></div>
      <div class="achievement"><div class="achievement-metric">Dynamics</div><div class="achievement-text">Oversaw Salesforce to MS Dynamics 365 migration with lead scoring & Brevo/WhatsApp nurture</div></div>
    </div>
  </div>"""

old_rns = """  <!-- RNS -->
  <div class="experience-item">
    <div class="experience-header">
      <div class="company-logo"><svg><use href="#company-rns"/></svg></div>
      <div class="experience-meta">
        <div class="role">Digital Marketing Manager</div>
        <div class="company">RNS Realty</div>
      </div>
      <div class="experience-dates">Feb 2025 — Aug 2025<div class="location">Dubai, UAE · Contract</div></div>
    </div>
    <p class="experience-description">Directed performance marketing and CRM analytics. Configured data tracking frameworks and audience segmentations to scale email, WhatsApp, and CRM automation campaigns while improving conversion analytics.</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+32%</div><div class="achievement-text">Lead volume growth in 3 months via paid campaigns</div></div>
      <div class="achievement"><div class="achievement-metric">+26%</div><div class="achievement-text">ROI improvement via integrated campaign spend optimization</div></div>
      <div class="achievement"><div class="achievement-metric">CRM</div><div class="achievement-text">Designed email, WhatsApp, and CRM campaigns with data-led segmentation</div></div>
      <div class="achievement"><div class="achievement-metric">41%</div><div class="achievement-text">Social media follower growth via calendar management</div></div>
    </div>
  </div>"""

new_rns = """  <!-- RNS -->
  <div class="experience-item">
    <div class="experience-header">
      <div class="company-logo"><svg><use href="#company-rns"/></svg></div>
      <div class="experience-meta">
        <div class="role">Digital Marketing Manager (Contract)</div>
        <div class="company">RNS Realty</div>
      </div>
      <div class="experience-dates">Feb 2025 – Aug 2025<div class="location">Dubai, UAE</div></div>
    </div>
    <p class="experience-description">Spearheaded lower-funnel performance campaigns on a $40K/month budget. Integrated Bitrix24 CRM, revamped corporate website, and configured Meta CAPI & Google Offline Conversion API with automated WhatsApp lead stage triggers for luxury UAE and international property buyers (US, UK, Canada).</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+32%</div><div class="achievement-text">Digital lead volume growth within 3 months and +26% campaign ROI</div></div>
      <div class="achievement"><div class="achievement-metric">Bitrix24</div><div class="achievement-text">Integrated Bitrix24 CRM & revamped website to capture 100% web inquiries and automate workflows</div></div>
      <div class="achievement"><div class="achievement-metric">CAPI / API</div><div class="achievement-text">Architected Meta CAPI & Google Offline Conversion API to optimize value-based bidding</div></div>
      <div class="achievement"><div class="achievement-metric">WhatsApp</div><div class="achievement-text">Linked WhatsApp to Bitrix24, achieving 35% open rate & 17% conversion rate on retargeted leads</div></div>
    </div>
  </div>"""

old_kf = """  <!-- KNIGHT FRANK -->
  <div class="experience-item">
    <div class="experience-header">
      <div class="company-logo"><img src="logo_kf.png" alt="Knight Frank"></div>
      <div class="experience-meta">
        <div class="role">Performance Marketing Lead</div>
        <div class="company">Knight Frank MENA</div>
      </div>
      <div class="experience-dates">Sep 2023 — Apr 2025<div class="location">Dubai, UAE</div></div>
    </div>
    <p class="experience-description">Managed multi-channel paid acquisition and performance analytics. Architected a multi-touch attribution modeling framework to track customer journeys and optimized digital campaign ROI across Google, Meta, TikTok, and LinkedIn.</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+12%</div><div class="achievement-text">ROI uplift via multi-touch attribution and budget reallocation</div></div>
      <div class="achievement"><div class="achievement-metric">+29%</div><div class="achievement-text">Campaign ROI improvement via continuous A/B testing</div></div>
      <div class="achievement"><div class="achievement-metric">85%</div><div class="achievement-text">Qualified lead rate sustained through targeted retargeting</div></div>
      <div class="achievement"><div class="achievement-metric">2× ROI</div><div class="achievement-text">Increased lead generation on Meta, Google, and TikTok Ads</div></div>
    </div>
  </div>"""

new_kf = """  <!-- KNIGHT FRANK -->
  <div class="experience-item">
    <div class="experience-header">
      <div class="company-logo"><img src="logo_kf.png" alt="Knight Frank"></div>
      <div class="experience-meta">
        <div class="role">Performance Marketing Lead</div>
        <div class="company">Knight Frank MENA</div>
      </div>
      <div class="experience-dates">Sep 2023 – Apr 2025<div class="location">Dubai, UAE</div></div>
    </div>
    <p class="experience-description">Directed performance marketing strategy across MENA, APAC, and Europe, managing a $75K/month paid media budget plus $8K/month analytics and ad tech tooling. Built multi-touch attribution (MTA) frameworks, Zapier CRM lead management workflows, and collaborated cross-functionally with Design, Engineering, and Communications.</p>
    <div class="achievements">
      <div class="achievement"><div class="achievement-metric">+31%</div><div class="achievement-text">Lead volume growth with 2x ROAS across SEM, Display, Meta, LinkedIn & TikTok</div></div>
      <div class="achievement"><div class="achievement-metric">+12% ROI</div><div class="achievement-text">Uplift in campaign ROI via Multi-Touch Attribution (MTA) & budget reallocation</div></div>
      <div class="achievement"><div class="achievement-metric">Zapier</div><div class="achievement-text">Designed automated CRM lead management using Zapier (85% qualification, 7% dormant reactivated)</div></div>
      <div class="achievement"><div class="achievement-metric">+29%</div><div class="achievement-text">Campaign ROI improvement through continuous landing page & creative A/B testing</div></div>
    </div>
  </div>"""

content = content.replace(old_cw, new_cw)
content = content.replace(old_rns, new_rns)
content = content.replace(old_kf, new_kf)

with open("index.html", "w") as f:
    f.write(content)

print("✅ Updated index.html successfully.")
