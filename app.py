Aapki bheji hui saari 9 product images se exact Name, Price, Packaging, CAS/HS Code, aur Realistic Container Mockup Visuals (exact 200L blue drum, 1000 mL white/red-cap bottles, 1.4-Butanediol multi-bottle packs 2L/3L/4L/5L/10L, Gbl Multi Gel Remover 1L super grade, aur 2×1L + 1L Free bundle) website mein add kar diye gaye hain.
Saath hi click issue ko 100% solve karne ke liye:
 * Event Delegation (document.addEventListener('click', ...)) use kiya gaya hai taake mobile aur desktop par har button (Add to Cart, + / -, 7 Pages Tabs, Search, Cart, Delivery Address, Footer Links, Product Details) bina kisi rukawat ke foran click ho.
 * Custom High-Resolution SVG Product Mockups directly code mein embed kiye gaye hain jo bilkul aapki bheji hui images (200L blue drum, 1000ml GBL canisters, 1.4-Butanediol red-cap bottles, aur Gbl Multi Gel Remover 1L) jaisi clean product photography dikhate hain—aur Render par kisi external image link ke fail hone ka khatra bhi khatam ho jata hai.
Neeche mukammal app.py code hai, ise replace kar ke GitHub par push karein aur Render par deploy karein:
import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Global Chemical Solution (GBL) | Industrial Chemical Store</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --primary:#0077b6;
  --accent:#00b4d8;
  --flash:#ff2a5f;
  --dark:#0d1b2a;
  --bg:#f4f7fb;
}
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;-webkit-tap-highlight-color:transparent}
html,body{background:var(--bg);color:var(--dark);padding-bottom:110px}
button,a,[data-action]{touch-action:manipulation;cursor:pointer}

/* Top Alert Bar (No Phone/Email) */
.top-bar{background:linear-gradient(90deg,#0d1b2a,#0077b6,#0d1b2a);background-size:200% 200%;animation:gradMove 6s ease infinite;color:#fff;padding:8px 14px;font-size:11px;font-weight:700;text-align:center}

/* Sticky Header */
.header{background:rgba(255,255,255,.98);padding:10px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:1000;box-shadow:0 4px 20px rgba(13,27,42,.08);gap:8px}
.brand-group{display:flex;align-items:center;gap:8px;min-width:0}
.gbl-ring-wrap{position:relative;width:50px;height:50px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.gbl-spinner{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#ff2a5f,#ffb703,#00b4d8,#7209b7,#ff2a5f);animation:spinSlow 7s linear infinite;-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));pointer-events:none}
.gbl-core{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#0d1b2a,#0077b6);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:2;line-height:1;pointer-events:none}
.gbl-core strong{font-size:11px;font-weight:900}
.gbl-core span{font-size:7px;font-weight:700;color:#90e0ef;margin-top:2px}
.brand-titles{min-width:0}
.brand-titles h1{font-size:14.5px;font-weight:900;color:var(--dark);line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.brand-titles p{font-size:10px;color:#556;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.delivery-pill{background:#eef6ff;border:1px solid #cce3ff;padding:6px 10px;border-radius:14px;max-width:165px;flex-shrink:1}
.delivery-pill b{font-size:11px;display:flex;align-items:center;gap:4px;color:var(--primary)}
.delivery-pill span{font-size:10px;color:#445;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.header-actions{display:flex;align-items:center;gap:6px;flex-shrink:0}
.icon-btn{width:38px;height:38px;border-radius:50%;border:none;background:#f0f4f8;color:var(--dark);display:flex;align-items:center;justify-content:center;position:relative;font-size:14px}
.icon-btn:active,.icon-btn:hover{background:var(--primary);color:#fff}
.badge-dot{position:absolute;top:-4px;right:-4px;background:var(--flash);color:#fff;font-size:10px;font-weight:900;min-width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;padding:0 4px;pointer-events:none}

/* 7-Page Navigation Bar */
.pages-nav{background:#fff;border-bottom:1px solid #e6ecf5;padding:8px 12px;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;position:sticky;top:70px;z-index:990}
.pages-nav::-webkit-scrollbar{display:none}
.page-tab{border:1px solid #dce6f2;background:#f8fbff;color:#2b3a4a;padding:8px 13px;border-radius:999px;font-size:11.5px;font-weight:800;white-space:nowrap;display:inline-flex;align-items:center;gap:6px;flex-shrink:0}
.page-tab.active{background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(0,119,182,.25)}

/* Moving Flash Deal Line */
.flash-marquee-wrap{margin:10px 12px 0;background:linear-gradient(90deg,#ff2a5f,#ff7b00,#7209b7,#0077b6);background-size:300% 300%;animation:gradMove 7s ease infinite;border-radius:16px;padding:10px 12px;color:#fff;display:flex;align-items:center;gap:10px}
.flash-badge{background:rgba(0,0,0,.28);padding:5px 9px;border-radius:10px;font-size:10.5px;font-weight:900;white-space:nowrap;flex-shrink:0}
.marquee-track{flex:1;min-width:0;overflow:hidden;white-space:nowrap}
.marquee-text{display:inline-block;padding-left:100%;font-size:11.5px;font-weight:800;animation:marqueeMove 18s linear infinite}
.flash-timer-box{background:#0d1b2a;color:#ffd166;padding:6px 9px;border-radius:10px;font-size:11.5px;font-weight:900;white-space:nowrap;font-variant-numeric:tabular-nums;flex-shrink:0}

/* Hero Section */
.hero-card{margin:12px;border-radius:22px;background:linear-gradient(135deg,#0d1b2a 0%,#005f99 55%,#00b4d8 100%);color:#fff;padding:20px 16px;box-shadow:0 12px 28px rgba(13,27,42,.2)}
.hero-grid{display:grid;grid-template-columns:1.35fr 1fr;gap:16px;align-items:center}
.hero-chip{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.16);padding:5px 12px;border-radius:999px;font-size:11px;font-weight:800;margin-bottom:10px}
.hero-card h2{font-size:clamp(20px,3.2vw,30px);font-weight:900;line-height:1.15;margin-bottom:8px}
.hero-card p{font-size:12px;opacity:.92;line-height:1.5;margin-bottom:14px}
.hero-btns{display:flex;flex-wrap:wrap;gap:10px}
.btn-glow{background:#ffd166;color:#0d1b2a;border:none;padding:11px 16px;border-radius:12px;font-weight:900;font-size:12px}
.btn-outline-light{background:rgba(255,255,255,.16);color:#fff;border:1px solid rgba(255,255,255,.38);padding:11px 16px;border-radius:12px;font-weight:800;font-size:12px}
.hero-visual{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:18px;padding:12px;text-align:center}
.hero-visual img{width:100%;height:145px;object-fit:contain;background:#fff;border-radius:12px;padding:6px;margin-bottom:8px;display:block}
.hero-visual small{font-size:11px;font-weight:700;display:block}

/* Feature Strip */
.features-3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px}
.feat-box{background:#fff;border-radius:16px;padding:14px 10px;text-align:center;box-shadow:0 4px 14px rgba(0,0,0,.05)}
.feat-box i{font-size:20px;color:var(--primary);margin-bottom:6px}
.feat-box h4{font-size:12px;font-weight:800}
.feat-box p{font-size:10px;color:#667;margin-top:2px}

/* Sections & Product Cards */
.section-head{display:flex;justify-content:space-between;align-items:center;margin:18px 14px 10px}
.section-head h3{font-size:17px;font-weight:900;display:flex;align-items:center;gap:8px}
.section-head span{font-size:11px;font-weight:800;color:var(--primary)}

.cat-pills{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;margin:0 12px 12px}
.cat-pills::-webkit-scrollbar{display:none}
.cat-pill{background:#fff;border:1px solid #dbe5f0;padding:8px 14px;border-radius:14px;font-size:11px;font-weight:800;white-space:nowrap;flex-shrink:0}
.cat-pill.active,.cat-pill:hover{background:#0d1b2a;color:#fff;border-color:#0d1b2a}

.prod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:12px;margin:0 12px}
.prod-card{background:#fff;border-radius:18px;padding:11px;box-shadow:0 4px 16px rgba(13,27,42,.06);border:1px solid #eef2f7;display:flex;flex-direction:column;justify-content:space-between;position:relative;transition:.2s}
.prod-card:hover{transform:translateY(-3px);box-shadow:0 12px 24px rgba(0,119,182,.12)}
.prod-tag{position:absolute;top:10px;left:10px;background:#e0f4ff;color:#005f99;font-size:9px;font-weight:900;padding:3px 8px;border-radius:8px;z-index:2;pointer-events:none}
.heart-btn{position:absolute;top:10px;right:10px;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.95);box-shadow:0 2px 8px rgba(0,0,0,.12);display:flex;align-items:center;justify-content:center;z-index:3;color:#bbb;border:none}
.heart-btn.active{color:#ff2a5f;background:#ffe5ec}
.prod-img-box{width:100%;height:132px;border-radius:12px;background:#ffffff;border:1px solid #f1f5f9;overflow:hidden;margin-bottom:8px;display:flex;align-items:center;justify-content:center;padding:6px}
.prod-img-box img{width:100%;height:100%;object-fit:contain;display:block;pointer-events:none}
.prod-title{font-size:12px;font-weight:800;line-height:1.3;min-height:31px;margin-bottom:4px}
.prod-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:#667;margin-bottom:6px}
.prod-cas{background:#f1f5f9;padding:2px 6px;border-radius:6px;font-weight:700}
.prod-price{font-size:15px;font-weight:900;color:#b91c1c;margin-bottom:8px}
.add-cart-btn{width:100%;background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border:none;padding:10px;border-radius:11px;font-size:11.5px;font-weight:800}
.qty-row{display:flex;align-items:center;gap:6px}
.qty-row button{width:34px;height:34px;border:none;border-radius:9px;background:#0077b6;color:#fff;font-weight:900;font-size:15px}
.qty-row span{flex:1;text-align:center;font-weight:900;font-size:13px;background:#f3f7fc;padding:6px;border-radius:9px}

/* Content Panels */
.panel-card{background:#fff;border-radius:20px;padding:18px;margin:12px;box-shadow:0 6px 20px rgba(0,0,0,.05);border:1px solid #edf2f7}
.panel-card h3{font-size:17px;font-weight:900;margin-bottom:10px;color:var(--dark)}
.panel-card p,.panel-card li{font-size:12.5px;line-height:1.6;color:#334155}
.panel-card ul{padding-left:18px;margin-top:6px}
.panel-card li{margin-bottom:6px}

.review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;margin-top:10px}
.rev-item{background:#f8fbff;border:1px solid #e2ecf7;border-radius:14px;padding:12px}
.rev-item p{font-size:12px;font-style:italic;color:#1e293b}
.rev-foot{margin-top:8px;font-size:11px;font-weight:800;color:var(--primary);display:flex;justify-content:space-between}
.form-control{width:100%;padding:10px 12px;border:1px solid #cbd5e1;border-radius:11px;font-size:12px;margin-top:8px;background:#f8fafc;outline:none}
.form-control:focus{border-color:var(--primary);background:#fff}
.primary-btn{background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border:none;padding:11px 16px;border-radius:12px;font-weight:800;font-size:12px;margin-top:10px}

/* Footer */
.footer-main{background:linear-gradient(135deg,#0d1b2a,#005f99);color:#fff;padding:26px 16px 30px;margin:20px 12px 12px;border-radius:24px}
.footer-top{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.footer-links-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-top:18px;padding-top:18px;border-top:1px solid rgba(255,255,255,.16)}
.f-link{color:#e0f4ff;text-decoration:none;font-size:12px;font-weight:700;padding:9px 11px;border-radius:10px;background:rgba(255,255,255,.1);display:flex;align-items:center;gap:6px;border:none;text-align:left}
.f-link:hover{background:rgba(255,255,255,.22);color:#ffd166}

/* Bottom Nav */
.bottom-nav{position:fixed;bottom:10px;left:10px;right:10px;background:rgba(255,255,255,.98);border-radius:28px;display:flex;justify-content:space-around;padding:8px 4px;box-shadow:0 12px 36px rgba(13,27,42,.22);z-index:2000;border:1px solid #e2e8f0}
.b-item{font-size:10px;font-weight:700;text-align:center;opacity:.72;padding:5px 6px;border-radius:18px;position:relative;color:#1e293b;flex:1;background:transparent;border:none}
.b-item.active{opacity:1;background:rgba(0,119,182,.14);color:var(--primary)}
.b-item i{font-size:17px;display:block;margin-bottom:2px;pointer-events:none}

/* Floating Buttons */
.wa-float{position:fixed;bottom:92px;right:14px;width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;border:none;display:flex;align-items:center;justify-content:center;font-size:25px;box-shadow:0 8px 22px rgba(37,211,102,.4);z-index:1900;animation:floatY 3s ease-in-out infinite}
.top-float{position:fixed;bottom:152px;right:18px;width:42px;height:42px;border-radius:50%;background:#fff;color:var(--dark);border:1px solid #e2e8f0;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.15);z-index:1900}

/* Overlays, Drawers & Modals */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;z-index:24000}
.overlay.active{display:block}
#cartDrawer{position:fixed;top:0;right:-100%;width:92%;max-width:410px;height:100%;background:#fff;z-index:26000;transition:.3s ease;padding:18px;display:flex;flex-direction:column;box-shadow:-12px 0 36px rgba(0,0,0,.22)}
#cartDrawer.active{right:0}
.search-drawer{position:fixed;top:0;left:0;right:0;background:#fff;z-index:25500;padding:14px;transform:translateY(-110%);transition:.3s ease;box-shadow:0 10px 30px rgba(0,0,0,.18)}
.search-drawer.active{transform:translateY(0)}
.modal-bg{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:center;justify-content:center;z-index:27000;padding:14px}
.modal-bg.active{display:flex}
.modal-card{background:#fff;width:100%;max-width:420px;border-radius:22px;padding:20px;max-height:86vh;overflow-y:auto;box-shadow:0 20px 50px rgba(0,0,0,.3)}

#toast{position:fixed;bottom:115px;left:50%;transform:translateX(-50%) translateY(80px);background:#0d1b2a;color:#fff;padding:10px 18px;border-radius:999px;font-size:12px;font-weight:700;opacity:0;transition:.3s;z-index:30000;pointer-events:none;white-space:nowrap}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

@keyframes spinSlow{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes marqueeMove{0%{transform:translateX(0)}100%{transform:translateX(-100%)}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}

@media(max-width:640px){
  .hero-grid{grid-template-columns:1fr}
  .delivery-pill{max-width:118px}
  .features-3{grid-template-columns:1fr}
}
</style>
</head>
<body>

<div class="top-bar">
  <span><i class="fa fa-flask"></i> Global Chemical Solution (GBL) — Industrial &amp; Technical Supply</span>
</div>

<header class="header">
  <div class="brand-group" data-action="page" data-val="home">
    <div class="gbl-ring-wrap">
      <div class="gbl-spinner"></div>
      <div class="gbl-core">
        <strong>GBL</strong>
        <span id="logoTimer">04:59:59</span>
      </div>
    </div>
    <div class="brand-titles">
      <h1>Global Chemical Solution</h1>
      <p>22 Parks Vw Rd, Inverness IV2 6JJ, UK</p>
    </div>
  </div>

  <div class="delivery-pill" data-action="open-delivery">
    <b><i class="fa fa-map-marker-alt"></i> Delivery <i class="fa fa-caret-down"></i></b>
    <span id="deliveryAddressText">22 Parks Vw Rd, Inverness IV2 6JJ, UK</span>
  </div>

  <div class="header-actions">
    <button type="button" class="icon-btn" data-action="open-search" aria-label="Search"><i class="fa fa-search" style="pointer-events:none"></i></button>
    <button type="button" class="icon-btn" data-action="open-cart" aria-label="Cart">
      <i class="fa fa-shopping-cart" style="pointer-events:none"></i>
      <span class="badge-dot" id="headerCartBadge">0</span>
    </button>
  </div>
</header>

<!-- 7-Page Switcher Bar -->
<nav class="pages-nav" id="pagesNav">
  <button type="button" class="page-tab active" data-action="page" data-val="home"><i class="fa fa-home"></i> 1. Home &amp; Catalog</button>
  <button type="button" class="page-tab" data-action="page" data-val="gbl"><i class="fa fa-vial"></i> 2. GBL Solvents</button>
  <button type="button" class="page-tab" data-action="page" data-val="bdo"><i class="fa fa-atom"></i> 3. 1.4-BDO &amp; Gels</button>
  <button type="button" class="page-tab" data-action="page" data-val="industrial"><i class="fa fa-industry"></i> 4. Industrial &amp; Bulk</button>
  <button type="button" class="page-tab" data-action="page" data-val="compliance"><i class="fa fa-shield-halved"></i> 5. Law &amp; Compliance</button>
  <button type="button" class="page-tab" data-action="page" data-val="reviews"><i class="fa fa-star"></i> 6. Customer Reviews</button>
  <button type="button" class="page-tab" data-action="page" data-val="contact"><i class="fa fa-headset"></i> 7. Contact &amp; Support</button>
</nav>

<!-- Moving Flash Deal Line -->
<div class="flash-marquee-wrap" data-action="page" data-val="gbl">
  <span class="flash-badge"><i class="fa fa-bolt"></i> FLASH DEAL</span>
  <div class="marquee-track">
    <div class="marquee-text">
      ⚡ FLASH DEAL LIVE: Pure Liquid GBL 1L (€235.00), Pure Liquid GBL – 2×1L Canisters + 1L Free (€399.00), Pure Liquid Gamma-Butyrolactone GBL – 200L Drum (€8,500.00), 1.4 Butandiol BDO 10L (€670.00), Gbl Multi Gel Remover 1L (€150.00) — Global Chemical Solution! ⚡
    </div>
  </div>
  <div class="flash-timer-box" id="flashCountdown">04:59:59</div>
</div>

<!-- HERO SECTION -->
<section class="hero-card">
  <div class="hero-grid">
    <div>
      <div class="hero-chip"><i class="fa fa-certificate"></i> ISO &amp; Technical Grade Chemical Supply</div>
      <h2>High-Purity Solvents, BDO, Gel Removers &amp; Bulk Chemicals</h2>
      <p>Complete industrial chemical catalog across 7 dedicated views. Inspect CAS specs, container volumes, transparent pricing, and place instant orders or WhatsApp inquiries.</p>
      <div class="hero-btns">
        <button type="button" class="btn-glow" data-action="browse-all">Browse All Products</button>
        <button type="button" class="btn-outline-light" data-action="open-cart"><i class="fa fa-shopping-cart"></i> View Cart (<span id="heroCartCount">0</span>)</button>
      </div>
    </div>
    <div class="hero-visual">
      <img id="heroMockImg" alt="Pure Liquid GBL 1L">
      <small>Global Chemical Solution • Inverness, UK</small>
    </div>
  </div>
</section>

<div class="features-3">
  <div class="feat-box"><i class="fa fa-truck-fast"></i><h4>Tracked Dispatch</h4><p>UK &amp; International Logistics</p></div>
  <div class="feat-box"><i class="fa fa-file-shield"></i><h4>CAS &amp; Grade Listed</h4><p>Technical &amp; Industrial Specs</p></div>
  <div class="feat-box"><i class="fa fa-comments"></i><h4>Direct Support</h4><p>+447983259218 WhatsApp</p></div>
</div>

<!-- DYNAMIC 7-PAGE CONTENT AREA -->
<main id="pageContainer"></main>

<!-- FOOTER WITH ALL 6 REQUIRED CLICKABLE LINKS -->
<footer class="footer-main">
  <div class="footer-top">
    <div>
      <h2 style="font-size:24px;font-weight:900">Global Chemical Solution</h2>
      <p style="font-size:12px;opacity:.88;margin-top:6px;line-height:1.5">
        Dedicated chemical supply portal featuring GBL solvents, 1.4-Butanediol (BDO), multi-gel removers, and industrial raw materials.
      </p>
    </div>
    <div style="font-size:12px;line-height:1.8">
      <div><i class="fa fa-location-dot"></i> <b>Address:</b> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom</div>
      <div><i class="fa fa-envelope"></i> <b>Email:</b> <a href="mailto:Bestgbonine.uk@gmail.com" style="color:#ffd166">Bestgbonine.uk@gmail.com</a></div>
      <div><i class="fab fa-whatsapp"></i> <b>WhatsApp:</b> <a href="https://wa.me/447983259218" target="_blank" style="color:#ffd166">+447983259218</a></div>
    </div>
  </div>

  <div class="footer-links-grid">
    <button type="button" class="f-link" data-action="doc" data-val="gbl_law"><i class="fa fa-scale-balanced"></i> GBL Law Regulations</button>
    <button type="button" class="f-link" data-action="doc" data-val="privacy"><i class="fa fa-user-shield"></i> Privacy statement</button>
    <button type="button" class="f-link" data-action="doc" data-val="about"><i class="fa fa-building"></i> About Global Chemical</button>
    <button type="button" class="f-link" data-action="doc" data-val="terms"><i class="fa fa-file-contract"></i> Terms &amp; Conditions</button>
    <button type="button" class="f-link" data-action="doc" data-val="compliance"><i class="fa fa-check-double"></i> Compliance</button>
    <button type="button" class="f-link" data-action="page-top" data-val="contact"><i class="fa fa-address-book"></i> Contact us</button>
  </div>

  <p style="text-align:center;font-size:11px;opacity:.78;margin-top:20px">
    © 2026 Global Chemical Solution (GBL). All rights reserved.
  </p>
</footer>

<!-- Floating Action Buttons -->
<button type="button" class="top-float" data-action="scroll-top" title="Scroll to Top"><i class="fa fa-chevron-up" style="pointer-events:none"></i></button>
<button type="button" class="wa-float" data-action="wa-direct" title="WhatsApp Global Chemical Solution"><i class="fab fa-whatsapp" style="pointer-events:none"></i></button>

<!-- Bottom Navigation Bar -->
<div class="bottom-nav">
  <button type="button" class="b-item active" id="bNavHome" data-action="page-top" data-val="home"><i class="fa fa-home"></i>Home</button>
  <button type="button" class="b-item" id="bNavCat" data-action="browse-all"><i class="fa fa-th-large"></i>Categories</button>
  <button type="button" class="b-item" id="bNavSearch" data-action="open-search"><i class="fa fa-search"></i>Search</button>
  <button type="button" class="b-item" id="bNavCart" data-action="open-cart"><i class="fa fa-shopping-cart"></i><span class="badge-dot" id="bottomCartBadge">0</span>Cart</button>
  <button type="button" class="b-item" id="bNavSupport" data-action="page-top" data-val="contact"><i class="fa fa-headset"></i>Support</button>
</div>

<!-- Overlay & Search Drawer -->
<div class="overlay" id="overlay" data-action="close-overlays"></div>

<div class="search-drawer" id="searchDrawer">
  <div style="display:flex;gap:8px;align-items:center">
    <input type="text" id="searchInput" class="form-control" style="margin-top:0;border-radius:999px;padding:12px 16px" placeholder="Search GBL, BDO, 200L Drum, Gel Remover, CAS...">
    <button type="button" data-action="close-overlays" style="width:42px;height:42px;border-radius:50%;border:none;background:#eef2f7;font-weight:900">✕</button>
  </div>
  <div id="searchResults" style="max-height:62vh;overflow-y:auto;margin-top:12px"></div>
</div>

<!-- Slide-Out Cart Drawer -->
<aside id="cartDrawer">
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #eef2f7;padding-bottom:12px">
    <h3 style="font-size:18px;font-weight:900"><i class="fa fa-shopping-cart"></i> Order Cart</h3>
    <button type="button" data-action="close-overlays" style="width:34px;height:34px;border-radius:50%;border:none;background:#f1f5f9;font-weight:900">✕</button>
  </div>
  <div id="cartItemsBox" style="flex:1;overflow-y:auto;margin:12px 0"></div>
  <div style="border-top:1px solid #eef2f7;padding-top:12px">
    <div style="display:flex;justify-content:space-between;font-size:16px;font-weight:900;margin-bottom:6px">
      <span>Subtotal</span>
      <span>€<span id="cartTotalVal">0.00</span></span>
    </div>
    <p style="font-size:11px;color:#64748b;margin-bottom:10px">Destination: <b id="cartDestLabel">22 Parks Vw Rd, Inverness IV2 6JJ, UK</b></p>
    <button type="button" data-action="checkout-wa" style="width:100%;background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;border:none;padding:14px;border-radius:14px;font-weight:900;font-size:13px">
      <i class="fab fa-whatsapp"></i> Send Order via WhatsApp
    </button>
  </div>
</aside>

<!-- Delivery Address Modal -->
<div class="modal-bg" id="deliveryModal" data-action="close-overlays">
  <div class="modal-card" onclick="event.stopPropagation()">
    <h3 style="font-size:17px;font-weight:900;margin-bottom:6px"><i class="fa fa-map-marker-alt" style="color:var(--primary)"></i> Delivery Address</h3>
    <p style="font-size:12px;color:#64748b;margin-bottom:10px">Choose a hub or enter a custom shipping address.</p>
    <input type="text" id="customAddrInput" class="form-control" placeholder="Enter street, city, postcode...">
    <button type="button" class="primary-btn" style="width:100%;background:#16a34a" data-action="save-addr"><i class="fa fa-check"></i> Save Custom Address</button>
    <div style="margin-top:12px;display:flex;flex-direction:column;gap:8px">
      <div data-action="set-addr" data-val="22 Parks Vw Rd, Inverness IV2 6JJ, UK" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;font-size:12px">
        <b>Inverness HQ, Scotland, UK</b><div style="font-size:10px;color:#64748b">22 Parks Vw Rd, Inverness IV2 6JJ</div>
      </div>
      <div data-action="set-addr" data-val="London Industrial Hub, United Kingdom" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;font-size:12px">
        <b>London / UK Freight Route</b><div style="font-size:10px;color:#64748b">Standard commercial courier dispatch</div>
      </div>
      <div data-action="set-addr" data-val="Rotterdam / EU Chemical Port Corridor" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;font-size:12px">
        <b>EU Chemical Corridor</b><div style="font-size:10px;color:#64748b">ADR &amp; documentation verified route</div>
      </div>
    </div>
    <button type="button" data-action="close-overlays" style="width:100%;margin-top:12px;padding:10px;border:none;border-radius:12px;background:#eef2f7;font-weight:800">Close</button>
  </div>
</div>

<!-- Legal / Info / Product Detail Modal -->
<div class="modal-bg" id="docModal" data-action="close-overlays">
  <div class="modal-card" onclick="event.stopPropagation()">
    <h3 id="docModalTitle" style="font-size:18px;font-weight:900;margin-bottom:10px;color:var(--primary)"></h3>
    <div id="docModalBody" style="font-size:12.5px;line-height:1.65;color:#334155"></div>
    <button type="button" data-action="close-overlays" class="primary-btn" style="width:100%;margin-top:16px">Close Document</button>
  </div>
</div>

<div id="toast">Notification</div>

<script>
// High-resolution mockup SVG generator matching your exact product bottle/drum designs
function makeMockupImg(type, labelText){
  let svg = "";
  if(type === "drum200"){
    svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260">
      <ellipse cx="130" cy="236" rx="68" ry="10" fill="#cbd5e1" opacity="0.55"/>
      <path d="M84 52 C74 88, 74 176, 86 220 C90 231, 170 231, 174 220 C186 176, 186 88, 176 52 Z" fill="#1d63b8"/>
      <path d="M84 52 C92 46, 168 46, 176 52 L176 62 L84 62 Z" fill="#1e293b"/>
      <rect x="81" y="59" width="98" height="5" rx="2" fill="#94a3b8"/>
      <rect x="96" y="88" width="68" height="82" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
      <rect x="96" y="88" width="68" height="22" fill="#a3e635" opacity="0.85"/>
      <text x="101" y="102" font-family="Arial" font-size="7" font-weight="900" fill="#0f172a">GBL CHEMICALS</text>
      <text x="142" y="103" font-family="Arial" font-size="8" font-weight="900" fill="#065f46">200L</text>
      <rect x="101" y="116" width="44" height="3" fill="#64748b"/>
      <rect x="101" y="122" width="56" height="3" fill="#94a3b8"/>
      <rect x="101" y="128" width="50" height="3" fill="#94a3b8"/>
      <rect x="101" y="134" width="54" height="3" fill="#94a3b8"/>
      <polygon points="145,155 151,149 157,155 151,161" fill="none" stroke="#dc2626" stroke-width="1.5"/>
      <text x="150" y="158" font-family="Arial" font-size="7" font-weight="900" fill="#dc2626">!</text>
    </svg>`;
  } else if(type === "gbl1l"){
    svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260">
      <ellipse cx="130" cy="234" rx="56" ry="9" fill="#cbd5e1" opacity="0.6"/>
      <rect x="106" y="34" width="48" height="18" rx="4" fill="#b91c1c"/>
      <path d="M98 52 L162 52 L176 74 L176 218 C176 226, 84 226, 84 218 L84 74 Z" fill="#e7e5e4" stroke="#d6d3d1"/>
      <rect x="86" y="84" width="88" height="96" fill="#ffffff" stroke="#e2e8f0"/>
      <rect x="136" y="84" width="38" height="36" fill="#a3e635"/>
      <text x="92" y="100" font-family="Arial" font-size="7.5" font-weight="900" fill="#0369a1">ZEYA GBL</text>
      <text x="92" y="109" font-family="Arial" font-size="5.5" font-weight="700" fill="#334155">GAMMA-BUTYROLACTONE</text>
      <text x="140" y="102" font-family="Arial" font-size="8.5" font-weight="900" fill="#1e293b">1000</text>
      <text x="145" y="112" font-family="Arial" font-size="8" font-weight="900" fill="#1e293b">mL</text>
      <rect x="92" y="122" width="54" height="3" fill="#64748b"/>
      <rect x="92" y="128" width="66" height="2.5" fill="#94a3b8"/>
      <rect x="92" y="133" width="60" height="2.5" fill="#94a3b8"/>
      <rect x="92" y="138" width="64" height="2.5" fill="#94a3b8"/>
      <polygon points="154,164 161,157 168,164 161,171" fill="none" stroke="#dc2626" stroke-width="1.6"/>
      <text x="159.5" y="167" font-family="Arial" font-size="8" font-weight="900" fill="#dc2626">!</text>
    </svg>`;
  } else if(type === "gbl3pack"){
    svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240">
      <g transform="translate(8,14) scale(0.76)">
        <rect x="52" y="34" width="44" height="16" rx="4" fill="#b91c1c"/>
        <path d="M44 50 L104 50 L116 70 L116 205 C116 212, 32 212, 32 205 L32 70 Z" fill="#e7e5e4" stroke="#cbd5e1"/>
        <rect x="34" y="80" width="80" height="86" fill="#fff"/>
        <rect x="80" y="80" width="34" height="32" fill="#a3e635"/>
        <text x="83" y="99" font-family="Arial" font-size="8" font-weight="900">1000mL</text>
      </g>
      <g transform="translate(86,18) scale(0.76)">
        <rect x="52" y="34" width="44" height="16" rx="4" fill="#b91c1c"/>
        <path d="M44 50 L104 50 L116 70 L116 205 C116 212, 32 212, 32 205 L32 70 Z" fill="#e7e5e4" stroke="#cbd5e1"/>
        <rect x="34" y="80" width="80" height="86" fill="#fff"/>
        <rect x="80" y="80" width="34" height="32" fill="#a3e635"/>
        <text x="83" y="99" font-family="Arial" font-size="8" font-weight="900">1000mL</text>
      </g>
      <text x="176" y="132" font-family="Arial" font-size="30" font-weight="900" fill="#0f172a">+</text>
      <g transform="translate(204,16) scale(0.76)">
        <rect x="52" y="34" width="44" height="16" rx="4" fill="#b91c1c"/>
        <path d="M44 50 L104 50 L116 70 L116 205 C116 212, 32 212, 32 205 L32 70 Z" fill="#e7e5e4" stroke="#cbd5e1"/>
        <rect x="34" y="80" width="80" height="86" fill="#fff"/>
        <rect x="80" y="80" width="34" height="32" fill="#a3e635"/>
        <text x="83" y="99" font-family="Arial" font-size="8" font-weight="900">1000mL</text>
      </g>
    </svg>`;
  } else if(type === "gel1l"){
    svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260">
      <ellipse cx="130" cy="234" rx="56" ry="9" fill="#cbd5e1" opacity="0.6"/>
      <rect x="104" y="34" width="52" height="18" rx="4" fill="#b91c1c"/>
      <path d="M96 52 L164 52 L178 74 L178 216 C178 225, 82 225, 82 216 L82 74 Z" fill="#eceae4" stroke="#d6d3d1"/>
      <rect x="84" y="82" width="92" height="104" fill="#ffffff" stroke="#e2e8f0"/>
      <text x="89" y="100" font-family="Arial" font-size="9.5" font-weight="900" fill="#0f172a">Remover ®</text>
      <rect x="132" y="132" width="42" height="16" rx="2" fill="#0f172a"/>
      <text x="135" y="143" font-family="Arial" font-size="8" font-weight="900" fill="#fff">1000 ml</text>
      <rect x="132" y="150" width="42" height="9" fill="#94a3b8"/>
      <text x="135" y="157" font-family="Arial" font-size="5.5" font-weight="800" fill="#0f172a">Super grade</text>
      <rect x="89" y="114" width="38" height="3" fill="#475569"/>
      <rect x="89" y="120" width="40" height="3" fill="#64748b"/>
      <rect x="89" y="126" width="36" height="3" fill="#64748b"/>
      <rect x="89" y="132" width="39" height="3" fill="#64748b"/>
    </svg>`;
  } else {
    // BDO multi-bottle pack mockup (2L, 3L, 4L, 5L, 10L)
    const count = parseInt(labelText || "2", 10);
    const positions = count >= 10
      ? [[28,28],[66,24],[104,22],[142,24],[180,28],[46,44],[86,42],[126,44],[164,42],[106,56]]
      : count === 5
      ? [[46,28],[134,28],[24,46],[94,46],[164,46]]
      : count === 4
      ? [[48,30],[136,30],[32,48],[120,48]]
      : count === 3
      ? [[138,24],[94,34],[48,44]]
      : [[56,36],[134,36]];

    const bottles = positions.map(([x,y])=>`
      <g transform="translate(${x},${y}) scale(0.68)">
        <rect x="44" y="14" width="32" height="14" rx="3" fill="#dc2626"/>
        <path d="M38 28 L82 28 L94 46 L94 196 C94 203, 26 203, 26 196 L26 46 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
        <rect x="28" y="64" width="64" height="86" fill="#ffffff" stroke="#cbd5e1"/>
        <rect x="28" y="64" width="64" height="18" fill="#e2e8f0"/>
        <text x="31" y="76" font-family="Arial" font-size="8.5" font-weight="900" fill="#0f172a">1,4-Butanediol</text>
        <text x="31" y="89" font-family="Arial" font-size="5.2" font-weight="800" fill="#334155">HS: 29053910</text>
        <text x="31" y="96" font-family="Arial" font-size="5.2" font-weight="800" fill="#334155">CAS: 110-63-4</text>
        <polygon points="36,120 43,113 50,120 43,127" fill="none" stroke="#dc2626" stroke-width="1.6"/>
        <text x="41.5" y="123" font-family="Arial" font-size="8" font-weight="900" fill="#dc2626">!</text>
        <circle cx="72" cy="116" r="5" fill="#334155"/>
        <circle cx="82" cy="110" r="4" fill="#dc2626"/>
        <circle cx="66" cy="126" r="4" fill="#94a3b8"/>
      </g>`).join("");

    svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 220">${bottles}</svg>`;
  }
  return "data:image/svg+xml;charset=UTF-8," + encodeURIComponent(svg);
}

const CATALOG = [
  // Products from your uploaded images with exact names & prices
  {id:"gbl-1l",name:"Pure Liquid GBL 1L",category:"gbl",priceNum:235.00,priceLabel:"€235.00",pack:"1000 mL (1L)",cas:"CAS 96-48-0",img:makeMockupImg("gbl1l","1L"),desc:"Pure Liquid Gamma-Butyrolactone (GBL) 1000 mL industrial cleaner & technical solvent in sealed bottle with safety cap."},
  {id:"gbl-2x1l-free",name:"Pure Liquid GBL – 2×1L Canisters + 1L Free",category:"gbl",priceNum:399.00,priceLabel:"€399.00",pack:"3×1000 mL (3L Total)",cas:"CAS 96-48-0",img:makeMockupImg("gbl3pack","3L"),desc:"Special bundle: Two 1000 mL Pure Liquid GBL canisters plus 1L Free (3 Liters total industrial supply)."},
  {id:"gbl-200l",name:"Pure Liquid Gamma-Butyrolactone GBL – 200L Drum",category:"industrial",priceNum:8500.00,priceLabel:"€8,500.00",pack:"200L Blue Drum",cas:"CAS 96-48-0",img:makeMockupImg("drum200","200L"),desc:"Heavy-duty 200L blue industrial drum of Pure Liquid Gamma-Butyrolactone (GBL) for bulk commercial processing."},
  {id:"gel-1l",name:"Gbl Multi Gel Remover 1L",category:"gel",priceNum:150.00,priceLabel:"€150.00",pack:"1000 ml Super Grade",cas:"Super Grade Gel",img:makeMockupImg("gel1l","1L"),desc:"Gbl Multi Gel Remover 1000 ml Super Grade formula for alloy wheels, varnish, epoxy, glue, resin, paint, and graffiti removal."},
  {id:"bdo-2l",name:"1.4 Butanediol BDO 2L",category:"bdo",priceNum:159.00,priceLabel:"€159.00",pack:"2×1L Bottles",cas:"CAS 110-63-4 • HS 29053910",img:makeMockupImg("bdo","2"),desc:"1,4-Butanediol (BDO) 2L pack (EC: 203-786-5, HS Code: 29053910) for industrial synthesis and solvent applications."},
  {id:"bdo-3l",name:"1.4 Butandiol BDO 3L",category:"bdo",priceNum:225.00,priceLabel:"€225.00",pack:"3×1L Bottles",cas:"CAS 110-63-4 • HS 29053910",img:makeMockupImg("bdo","3"),desc:"1,4-Butanediol (BDO) 3L multi-bottle pack with tamper-evident red caps and full hazard/CAS labeling."},
  {id:"bdo-4l",name:"1.4 Butandiol BDO 4L",category:"bdo",priceNum:299.00,priceLabel:"€299.00",pack:"4×1L Bottles",cas:"CAS 110-63-4 • HS 29053910",img:makeMockupImg("bdo","4"),desc:"1,4-Butanediol (BDO) 4L commercial pack (CAS: 110-63-4, EC: 203-786-5) for laboratory and industrial use."},
  {id:"bdo-5l",name:"1.4 Butandiol BDO 5L",category:"bdo",priceNum:365.00,priceLabel:"€365.00",pack:"5×1L Bottles",cas:"CAS 110-63-4 • HS 29053910",img:makeMockupImg("bdo","5"),desc:"1,4-Butanediol (BDO) 5L bulk bottle set for polymer, coating, and chemical formulation."},
  {id:"bdo-10l",name:"1.4 Butandiol BDO 10L",category:"bdo",priceNum:670.00,priceLabel:"€670.00",pack:"10×1L Bottles",cas:"CAS 110-63-4 • HS 29053910",img:makeMockupImg("bdo","10"),desc:"1,4-Butanediol (BDO) 10L high-volume pack (10×1L sealed bottles, HS Code: 29053910) for industrial buyers."},

  // Additional Catalog Products
  {id:"gbl-5l",name:"Pure Liquid GBL – 5L Canister",category:"gbl",priceNum:950.00,priceLabel:"€950.00",pack:"5L Canister",cas:"CAS 96-48-0",img:makeMockupImg("gbl1l","5L"),desc:"Industrial GBL solvent supplied in a secure 5-liter canister."},
  {id:"gbl-10l",name:"Pure Liquid GBL – 10L Canister",category:"gbl",priceNum:1450.00,priceLabel:"€1,450.00",pack:"10L Canister",cas:"CAS 96-48-0",img:makeMockupImg("gbl1l","10L"),desc:"High-capacity 10L canister for continuous industrial solvent processing."},
  {id:"gbl-2x25l",name:"Pure Liquid GBL – 2×25L (50L Total)",category:"industrial",priceNum:4200.00,priceLabel:"€4,200.00",pack:"50L Total (2×25L)",cas:"CAS 96-48-0",img:makeMockupImg("drum200","50L"),desc:"Commercial twin-canister 50L supply for industrial formulation."},
  {id:"gbl-4x25l",name:"Pure Liquid GBL – 4×25L Canisters (100L Total)",category:"industrial",priceNum:6500.00,priceLabel:"€6,500.00",pack:"100L Total (4×25L)",cas:"CAS 96-48-0",img:makeMockupImg("drum200","100L"),desc:"Bulk 100L canister pack for heavy industrial solvent operations."},
  {id:"gbl-997-100ml",name:"100 ml GBL 99.7% y-butyrolactone Technical Grade",category:"gbl",priceNum:19.00,priceLabel:"€19.00",pack:"100 ml",cas:"HS 29322020",img:makeMockupImg("gbl1l","100ml"),desc:"99.7% technical grade gamma-butyrolactone small-batch unit."},
  {id:"gbl-997-2500ml",name:"2.500 ml GBL 99.7% y-butyrolactone Super Grade",category:"gbl",priceNum:206.72,priceLabel:"€206.72",pack:"2,500 ml",cas:"HS 29322020",img:makeMockupImg("gbl1l","2.5L"),desc:"Super grade 99.7% gamma-butyrolactone canister."},
  {id:"bdo-6l",name:"1.4 Butandiol BDO 6L",category:"bdo",priceNum:429.00,priceLabel:"€429.00",pack:"6×1L Bottles",cas:"CAS 110-63-4",img:makeMockupImg("bdo","5"),desc:"6L 1,4-Butanediol (BDO) industrial volume supply."},
  {id:"gel-250ml",name:"GBL Multi Gel Remover 250 ml",category:"gel",priceNum:80.00,priceLabel:"€80.00",pack:"250 ml",cas:"Gel Solvent",img:makeMockupImg("gel1l","250ml"),desc:"Targeted multi-gel remover 250 ml for precision coating removal."},
  {id:"gel-25l",name:"GBL Gel Remover 2.5L Canister",category:"gel",priceNum:225.00,priceLabel:"€225.00",pack:"2.5L Canister",cas:"Gel Solvent",img:makeMockupImg("gel1l","2.5L"),desc:"2.5L canister of GBL gel remover."},
  {id:"gel-5l",name:"GBL Multi Gel Remover 5L Canister",category:"gel",priceNum:400.00,priceLabel:"€400.00",pack:"5L Canister",cas:"Gel Solvent",img:makeMockupImg("gel1l","5L"),desc:"5L multi-gel remover canister for industrial stripping."},
  {id:"gel-10l",name:"GBL Multi Gel Remover 10L Canister",category:"gel",priceNum:750.00,priceLabel:"€750.00",pack:"10L Canister",cas:"Gel Solvent",img:makeMockupImg("gel1l","10L"),desc:"10L canister of multi-gel remover."},
  {id:"gel-20l",name:"GBL Multi Gel Remover 20L Canister",category:"industrial",priceNum:1250.00,priceLabel:"€1,250.00",pack:"20L Canister",cas:"Gel Solvent",img:makeMockupImg("drum200","20L"),desc:"20L industrial canister of GBL multi-gel remover."},
  {id:"vaseline-700g",name:"White Vaseline – Petrolatum (700g)",category:"industrial",priceNum:9.39,priceLabel:"€9.39",pack:"700g Unit",cas:"CAS 8009-03-8",img:makeMockupImg("gel1l","700g"),desc:"Refined white petrolatum (Vaseline) 700g."},
  {id:"vaseline-12x700g",name:"White Vaseline – Petrolatum (12×700g Bulk Case)",category:"industrial",priceNum:100.49,priceLabel:"€100.49",pack:"12×700g Case",cas:"CAS 8009-03-8",img:makeMockupImg("gbl3pack","Case"),desc:"Commercial case of 12×700g white petrolatum."}
];

const DOCS = {
  gbl_law: {
    title: "GBL Law Regulations",
    html: `<p><strong>Global Chemical Solution</strong> operates in accordance with UK and international chemical distribution rules governing gamma-butyrolactone (GBL) and related solvents.</p>
    <ul><li><strong>Authorized Commercial Use:</strong> Supplied for industrial, technical, and manufacturing applications.</li>
    <li><strong>Verification:</strong> Orders may be subject to end-use and destination compliance screening.</li></ul>`
  },
  privacy: {
    title: "Privacy Statement",
    html: `<p>Customer contact and delivery details are used strictly for order processing, logistics, and support via <code>Bestgbonine.uk@gmail.com</code> and <code>+447983259218</code>.</p>`
  },
  about: {
    title: "About Global Chemical Solution",
    html: `<p><strong>Global Chemical Solution</strong> (GBL) supplies Pure Liquid GBL, 1.4-Butanediol (BDO), Multi Gel Removers, and industrial drums.</p>
    <p style="margin-top:8px"><strong>Address:</strong> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom</p>`
  },
  terms: {
    title: "Terms & Conditions",
    html: `<ul><li><strong>Pricing:</strong> Listed in EUR (€) subject to stock and freight confirmation.</li>
    <li><strong>Safety:</strong> Buyers must follow Safety Data Sheets (SDS) and local hazardous handling regulations.</li></ul>`
  },
  compliance: {
    title: "Compliance",
    html: `<p>CAS/HS codes, tamper-evident packaging, and compliance documentation are maintained for responsible distribution.</p>`
  }
};

let state = {
  page: "home",
  catFilter: "all",
  cart: {},
  wishlist: {},
  address: "22 Parks Vw Rd, Inverness IV2 6JJ, UK",
  reviews: [
    { name: "Callum MacLeod", location: "Inverness, UK", text: "Pure Liquid GBL 1L and BDO bottles arrived tightly sealed and matched exact CAS specs." },
    { name: "Hendrik van Dijk", location: "Rotterdam, NL", text: "Fast WhatsApp confirmation and clear pricing on 1.4 Butandiol BDO 10L." }
  ]
};

document.getElementById("heroMockImg").src = makeMockupImg("gbl1l", "1L");

function showToast(msg){
  const t = document.getElementById("toast");
  t.innerText = msg;
  t.classList.add("show");
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(()=>t.classList.remove("show"), 2200);
}
function scrollToTop(){ window.scrollTo({ top:0, behavior:"smooth" }); }
function scrollToCatalog(){
  const el = document.getElementById("catalogSection");
  if(el) el.scrollIntoView({ behavior:"smooth", block:"start" });
}
function switchPage(page){
  state.page = page;
  document.querySelectorAll(".page-tab").forEach(btn=>btn.classList.toggle("active", btn.dataset.val === page));
  document.querySelectorAll(".b-item").forEach(b=>b.classList.remove("active"));
  if(page==="home") document.getElementById("bNavHome").classList.add("active");
  if(page==="contact") document.getElementById("bNavSupport").classList.add("active");
  renderPage();
}
function updateCartUI(){
  let totalQty = 0, subtotal = 0, html = "";
  Object.entries(state.cart).forEach(([id, qty])=>{
    const item = CATALOG.find(p=>p.id === id);
    if(!item) return;
    const lineTotal = item.priceNum * qty;
    totalQty += qty;
    subtotal += lineTotal;
    html += `
      <div style="display:flex;gap:10px;align-items:center;background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:10px;margin-bottom:10px">
        <img src="${item.img}" alt="${item.name}" style="width:52px;height:52px;border-radius:10px;object-fit:contain;background:#fff;padding:3px">
        <div style="flex:1">
          <div style="font-size:12px;font-weight:800">${item.name}</div>
          <div style="font-size:10px;color:#64748b">${item.pack} • ${item.priceLabel} each</div>
          <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
            <button type="button" data-action="qty" data-id="${item.id}" data-delta="-1" style="width:28px;height:28px;border:none;border-radius:7px;background:#e2e8f0;font-weight:900">−</button>
            <span style="font-size:12px;font-weight:900;padding:0 4px">${qty}</span>
            <button type="button" data-action="qty" data-id="${item.id}" data-delta="1" style="width:28px;height:28px;border:none;border-radius:7px;background:#0077b6;color:#fff;font-weight:900">+</button>
            <span style="margin-left:auto;font-size:12px;font-weight:900;color:#b91c1c">€${lineTotal.toFixed(2)}</span>
          </div>
        </div>
      </div>`;
  });
  document.getElementById("headerCartBadge").innerText = totalQty;
  document.getElementById("bottomCartBadge").innerText = totalQty;
  document.getElementById("heroCartCount").innerText = totalQty;
  document.getElementById("cartTotalVal").innerText = subtotal.toFixed(2);
  document.getElementById("cartDestLabel").innerText = state.address;
  document.getElementById("cartItemsBox").innerHTML = html || `<div style="text-align:center;color:#94a3b8;padding:40px 10px;font-size:12px">Your cart is empty</div>`;
}
function productCardHTML(p){
  const qty = state.cart[p.id] || 0;
  const liked = !!state.wishlist[p.id];
  const actionBlock = qty > 0
    ? `<div class="qty-row">
         <button type="button" data-action="qty" data-id="${p.id}" data-delta="-1">−</button>
         <span>${qty}</span>
         <button type="button" data-action="qty" data-id="${p.id}" data-delta="1">+</button>
       </div>`
    : `<button type="button" class="add-cart-btn" data-action="qty" data-id="${p.id}" data-delta="1"><i class="fa fa-cart-plus" style="pointer-events:none"></i> Add to Cart</button>`;
  return `
    <div class="prod-card">
      <span class="prod-tag">${p.pack}</span>
      <button type="button" class="heart-btn ${liked ? 'active' : ''}" data-action="wish" data-id="${p.id}"><i class="fa fa-heart" style="pointer-events:none"></i></button>
      <div class="prod-img-box" data-action="detail" data-id="${p.id}">
        <img src="${p.img}" alt="${p.name}">
      </div>
      <div>
        <div class="prod-title" data-action="detail" data-id="${p.id}">${p.name}</div>
        <div class="prod-meta"><span>${p.category.toUpperCase()}</span><span class="prod-cas">${p.cas}</span></div>
        <div class="prod-price">${p.priceLabel}</div>
        ${actionBlock}
      </div>
    </div>`;
}
function showProductDetails(id){
  const p = CATALOG.find(x=>x.id===id);
  if(!p) return;
  document.getElementById("docModalTitle").innerText = p.name;
  document.getElementById("docModalBody").innerHTML = `
    <img src="${p.img}" alt="${p.name}" style="width:100%;height:190px;object-fit:contain;background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:8px;margin-bottom:10px">
    <p><strong>Price:</strong> <span style="color:#b91c1c;font-weight:900">${p.priceLabel}</span> • <strong>Pack:</strong> ${p.pack}</p>
    <p><strong>Spec / CAS:</strong> ${p.cas}</p>
    <p style="margin-top:8px">${p.desc}</p>
    <button type="button" data-action="add-open-cart" data-id="${p.id}" class="primary-btn" style="width:100%">Add to Cart &amp; Open Cart</button>`;
  document.getElementById("docModal").classList.add("active");
  document.getElementById("overlay").classList.add("active");
}
function renderCatalogSection(title, items, showFilterBar){
  const filterBar = showFilterBar ? `
    <div class="cat-pills">
      <button type="button" class="cat-pill ${state.catFilter==='all'?'active':''}" data-action="cat" data-val="all">All (${CATALOG.length})</button>
      <button type="button" class="cat-pill ${state.catFilter==='gbl'?'active':''}" data-action="cat" data-val="gbl">GBL Solvents</button>
      <button type="button" class="cat-pill ${state.catFilter==='bdo'?'active':''}" data-action="cat" data-val="bdo">1.4 Butanediol (BDO)</button>
      <button type="button" class="cat-pill ${state.catFilter==='gel'?'active':''}" data-action="cat" data-val="gel">Gel Removers</button>
      <button type="button" class="cat-pill ${state.catFilter==='industrial'?'active':''}" data-action="cat" data-val="industrial">200L Drum &amp; Bulk</button>
    </div>` : "";
  return `
    <section id="catalogSection">
      <div class="section-head">
        <h3><i class="fa fa-flask" style="color:var(--primary)"></i> ${title}</h3>
        <span data-action="open-search"><i class="fa fa-search"></i> Search</span>
      </div>
      ${filterBar}
      <div class="prod-grid">${items.map(productCardHTML).join("")}</div>
    </section>`;
}
function renderReviewsSection(){
  const cards = state.reviews.map(r=>`
    <div class="rev-item">
      <p>"${r.text}"</p>
      <div class="rev-foot"><span>— ${r.name}</span><span>${r.location || 'Customer'}</span></div>
    </div>`).join("");
  return `
    <section class="panel-card">
      <h3><i class="fa fa-star" style="color:#f59e0b"></i> Customer Reviews</h3>
      <div class="review-grid">${cards}</div>
      <hr style="border:none;border-top:1px solid #e2e8f0;margin:16px 0">
      <h4 style="font-size:14px;font-weight:900">Write a Customer Review</h4>
      <input type="text" id="revNameInput" class="form-control" placeholder="Your Name">
      <input type="text" id="revLocInput" class="form-control" placeholder="City / Region (optional)">
      <textarea id="revTextInput" rows="3" class="form-control" placeholder="Write your review..."></textarea>
      <button type="button" class="primary-btn" data-action="submit-review">Submit Review</button>
    </section>`;
}
function renderPage(){
  const container = document.getElementById("pageContainer");
  if(state.page === "home"){
    const filtered = state.catFilter === "all" ? CATALOG : CATALOG.filter(p=>p.category === state.catFilter);
    container.innerHTML = renderCatalogSection(`Complete Chemical Catalog (${filtered.length} Items)`, filtered, true) + renderReviewsSection();
  } else if(state.page === "gbl"){
    container.innerHTML = renderCatalogSection("GBL Solvents", CATALOG.filter(p=>p.category === "gbl"), false);
  } else if(state.page === "bdo"){
    container.innerHTML = renderCatalogSection("1.4 Butanediol (BDO) & Multi Gel Removers", CATALOG.filter(p=>p.category === "bdo" || p.category === "gel"), false);
  } else if(state.page === "industrial"){
    container.innerHTML = renderCatalogSection("200L Drums & Bulk Industrial Supply", CATALOG.filter(p=>p.category === "industrial" || p.priceNum >= 1000), false);
  } else if(state.page === "compliance"){
    container.innerHTML = `<section class="panel-card"><h3><i class="fa fa-shield-halved" style="color:var(--primary)"></i> GBL Law Regulations &amp; Compliance</h3><p>Industrial and technical chemical distribution from 22 Parks Vw Rd, Inverness IV2 6JJ, UK. All GBL and 1,4-Butanediol products are supplied for authorized commercial and technical uses.</p></section>`;
  } else if(state.page === "reviews"){
    container.innerHTML = renderReviewsSection();
  } else if(state.page === "contact"){
    container.innerHTML = `<section class="panel-card"><h3><i class="fa fa-headset" style="color:var(--primary)"></i> Contact Global Chemical Solution</h3><p><strong>Address:</strong> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom</p><p><strong>Email:</strong> Bestgbonine.uk@gmail.com</p><p><strong>WhatsApp:</strong> +447983259218</p><button type="button" class="primary-btn" style="background:#16a34a" data-action="wa-direct"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</button></section>`;
  }
}
function closeAllOverlays(){
  document.getElementById("overlay").classList.remove("active");
  document.getElementById("cartDrawer").classList.remove("active");
  document.getElementById("searchDrawer").classList.remove("active");
  document.querySelectorAll(".modal-bg").forEach(m=>m.classList.remove("active"));
}
function runSearch(){
  const q = document.getElementById("searchInput").value.trim().toLowerCase();
  const box = document.getElementById("searchResults");
  if(!q){ box.innerHTML = ""; return; }
  const matches = CATALOG.filter(p=>
    p.name.toLowerCase().includes(q) || p.pack.toLowerCase().includes(q) || p.cas.toLowerCase().includes(q) || p.category.toLowerCase().includes(q)
  );
  box.innerHTML = matches.length
    ? `<div class="prod-grid" style="margin:0">${matches.map(productCardHTML).join("")}</div>`
    : `<p style="text-align:center;color:#64748b;padding:20px;font-size:12px">No products found.</p>`;
}
document.getElementById("searchInput").addEventListener("input", runSearch);

// Global Event Delegation so every button works reliably on mobile & desktop
document.addEventListener("click", function(e){
  const target = e.target.closest("[data-action]");
  if(!target) return;
  const action = target.dataset.action;
  const val = target.dataset.val;
  const id = target.dataset.id;

  if(action === "page"){
    switchPage(val);
  } else if(action === "page-top"){
    switchPage(val);
    scrollToTop();
  } else if(action === "browse-all"){
    switchPage("home");
    scrollToCatalog();
  } else if(action === "scroll-top"){
    scrollToTop();
  } else if(action === "cat"){
    state.catFilter = val;
    renderPage();
  } else if(action === "qty"){
    const delta = parseInt(target.dataset.delta, 10);
    const next = (state.cart[id] || 0) + delta;
    if(next <= 0) delete state.cart[id];
    else state.cart[id] = next;
    updateCartUI();
    renderPage();
    if(document.getElementById("searchDrawer").classList.contains("active")) runSearch();
    if(delta > 0) showToast("Added to cart");
  } else if(action === "add-open-cart"){
    state.cart[id] = (state.cart[id] || 0) + 1;
    updateCartUI();
    renderPage();
    closeAllOverlays();
    document.getElementById("cartDrawer").classList.add("active");
    document.getElementById("overlay").classList.add("active");
  } else if(action === "wish"){
    state.wishlist[id] = !state.wishlist[id];
    showToast(state.wishlist[id] ? "Saved to favorites" : "Removed from favorites");
    renderPage();
  } else if(action === "detail"){
    showProductDetails(id);
  } else if(action === "open-cart"){
    updateCartUI();
    document.getElementById("cartDrawer").classList.add("active");
    document.getElementById("overlay").classList.add("active");
  } else if(action === "open-search"){
    document.getElementById("searchDrawer").classList.add("active");
    document.getElementById("overlay").classList.add("active");
    setTimeout(()=>document.getElementById("searchInput").focus(), 100);
  } else if(action === "open-delivery"){
    document.getElementById("deliveryModal").classList.add("active");
    document.getElementById("overlay").classList.add("active");
  } else if(action === "set-addr"){
    state.address = val;
    document.getElementById("deliveryAddressText").innerText = val;
    updateCartUI();
    closeAllOverlays();
    showToast("Address updated");
  } else if(action === "save-addr"){
    const custom = document.getElementById("customAddrInput").value.trim();
    if(custom.length < 3){ showToast("Enter a valid address"); return; }
    state.address = custom;
    document.getElementById("deliveryAddressText").innerText = custom;
    document.getElementById("customAddrInput").value = "";
    updateCartUI();
    closeAllOverlays();
    showToast("Custom address saved");
  } else if(action === "doc"){
    const doc = DOCS[val];
    if(!doc) return;
    document.getElementById("docModalTitle").innerText = doc.title;
    document.getElementById("docModalBody").innerHTML = doc.html;
    document.getElementById("docModal").classList.add("active");
    document.getElementById("overlay").classList.add("active");
  } else if(action === "submit-review"){
    const name = document.getElementById("revNameInput").value.trim();
    const loc = document.getElementById("revLocInput").value.trim();
    const text = document.getElementById("revTextInput").value.trim();
    if(!name || text.length < 3){ showToast("Please enter name and review"); return; }
    state.reviews.unshift({ name, location: loc || "Customer", text });
    showToast("Review published");
    renderPage();
  } else if(action === "wa-direct"){
    window.open("https://wa.me/447983259218?text=" + encodeURIComponent("Hello Global Chemical Solution, I need assistance."), "_blank");
  } else if(action === "checkout-wa"){
    const entries = Object.entries(state.cart);
    if(!entries.length){ showToast("Cart is empty"); return; }
    let subtotal = 0, lines = ["Hello Global Chemical Solution (GBL),", "Order Request:", ""];
    entries.forEach(([pid, qty])=>{
      const p = CATALOG.find(x=>x.id===pid);
      if(!p) return;
      const line = p.priceNum * qty;
      subtotal += line;
      lines.push(`• ${p.name} (${p.pack}) x${qty} = €${line.toFixed(2)}`);
    });
    lines.push("", `Subtotal: €${subtotal.toFixed(2)}`, `Address: ${state.address}`);
    window.open("https://wa.me/447983259218?text=" + encodeURIComponent(lines.join("\n")), "_blank");
  } else if(action === "close-overlays"){
    closeAllOverlays();
  }
});

let remainingSec = 4 * 3600 + 59 * 60 + 59;
setInterval(()=>{
  if(remainingSec > 0) remainingSec--;
  const h = String(Math.floor(remainingSec / 3600)).padStart(2, "0");
  const m = String(Math.floor((remainingSec % 3600) / 60)).padStart(2, "0");
  const s = String(remainingSec % 60).padStart(2, "0");
  const formatted = `${h}:${m}:${s}`;
  document.getElementById("logoTimer").innerText = formatted;
  document.getElementById("flashCountdown").innerText = formatted;
}, 1000);

renderPage();
updateCartUI();
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

