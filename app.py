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
  --card:#ffffff;
}
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;-webkit-tap-highlight-color:transparent}
body{background:var(--bg);color:var(--dark);padding-bottom:105px;overflow-x:hidden}

/* Top Alert Bar */
.top-bar{background:linear-gradient(90deg,#0d1b2a,#0077b6,#0d1b2a);background-size:200% 200%;animation:gradMove 6s ease infinite;color:#fff;padding:8px 14px;font-size:11px;font-weight:700;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px}

/* Sticky Header */
.header{background:rgba(255,255,255,.95);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);padding:10px 14px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:999;box-shadow:0 6px 24px rgba(13,27,42,.08);gap:10px}
.brand-group{display:flex;align-items:center;gap:10px;cursor:pointer}
.gbl-ring-wrap{position:relative;width:54px;height:54px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.gbl-spinner{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#ff2a5f,#ffb703,#00b4d8,#7209b7,#ff2a5f);animation:spinSlow 7s linear infinite;-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px))}
.gbl-core{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#0d1b2a,#0077b6);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(0,119,182,.35);z-index:2;line-height:1}
.gbl-core strong{font-size:12px;font-weight:900;letter-spacing:.5px}
.gbl-core span{font-size:8px;font-weight:700;color:#90e0ef;margin-top:2px}
.brand-titles h1{font-size:16px;font-weight:900;color:var(--dark);line-height:1.1}
.brand-titles p{font-size:10px;color:#556;font-weight:600}

.delivery-pill{background:#eef6ff;border:1px solid #cce3ff;padding:6px 10px;border-radius:14px;cursor:pointer;transition:.25s;max-width:210px}
.delivery-pill:hover{background:#dff0ff;transform:translateY(-1px)}
.delivery-pill b{font-size:11px;display:flex;align-items:center;gap:4px;color:var(--primary)}
.delivery-pill span{font-size:10px;color:#445;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.header-actions{display:flex;align-items:center;gap:8px}
.icon-btn{width:38px;height:38px;border-radius:50%;border:none;background:#f0f4f8;color:var(--dark);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;transition:.25s;font-size:14px}
.icon-btn:hover{background:var(--primary);color:#fff;transform:translateY(-2px)}
.badge-dot{position:absolute;top:-4px;right:-4px;background:var(--flash);color:#fff;font-size:10px;font-weight:900;min-width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;padding:0 4px}

/* 7-Page Navigation Bar (Desktop & Tablet) */
.pages-nav{background:#fff;border-bottom:1px solid #e6ecf5;padding:8px 12px;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;position:sticky;top:74px;z-index:990}
.pages-nav::-webkit-scrollbar{display:none}
.page-tab{border:1px solid #dce6f2;background:#f8fbff;color:#2b3a4a;padding:7px 14px;border-radius:999px;font-size:12px;font-weight:800;cursor:pointer;white-space:nowrap;transition:.25s;display:flex;align-items:center;gap:6px}
.page-tab:hover{border-color:var(--primary);color:var(--primary)}
.page-tab.active{background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border-color:transparent;box-shadow:0 6px 16px rgba(0,119,182,.28)}

/* Moving Flash Deal Line */
.flash-marquee-wrap{margin:10px 12px 0;background:linear-gradient(90deg,#ff2a5f,#ff7b00,#7209b7,#0077b6);background-size:300% 300%;animation:gradMove 7s ease infinite;border-radius:16px;padding:10px 14px;color:#fff;display:flex;align-items:center;gap:12px;box-shadow:0 8px 22px rgba(255,42,95,.25)}
.flash-badge{background:rgba(0,0,0,.28);padding:5px 10px;border-radius:10px;font-size:11px;font-weight:900;white-space:nowrap;letter-spacing:.4px}
.marquee-track{flex:1;overflow:hidden;white-space:nowrap;position:relative}
.marquee-text{display:inline-block;padding-left:100%;font-size:12px;font-weight:800;animation:marqueeMove 18s linear infinite}
.flash-timer-box{background:#0d1b2a;color:#ffd166;padding:6px 10px;border-radius:10px;font-size:12px;font-weight:900;white-space:nowrap;font-variant-numeric:tabular-nums}

/* Hero Banner */
.hero-card{margin:12px;border-radius:22px;background:linear-gradient(135deg,#0d1b2a 0%,#005f99 55%,#00b4d8 100%);color:#fff;padding:22px 18px;position:relative;overflow:hidden;box-shadow:0 14px 32px rgba(13,27,42,.2);animation:fadeUp .5s ease}
.hero-card::after{content:'';position:absolute;right:-40px;bottom:-40px;width:190px;height:190px;border-radius:50%;background:rgba(255,255,255,.08);animation:pulseFloat 4s ease-in-out infinite}
.hero-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:16px;align-items:center;position:relative;z-index:2}
.hero-chip{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.16);padding:5px 12px;border-radius:999px;font-size:11px;font-weight:800;margin-bottom:10px}
.hero-card h2{font-size:clamp(20px,3.2vw,30px);font-weight:900;line-height:1.15;margin-bottom:8px}
.hero-card p{font-size:12px;opacity:.92;line-height:1.5;margin-bottom:14px}
.hero-btns{display:flex;flex-wrap:wrap;gap:10px}
.btn-glow{background:#ffd166;color:#0d1b2a;border:none;padding:10px 16px;border-radius:12px;font-weight:900;font-size:12px;cursor:pointer;transition:.25s;box-shadow:0 6px 18px rgba(255,209,102,.35)}
.btn-glow:hover{transform:translateY(-2px) scale(1.02)}
.btn-outline-light{background:rgba(255,255,255,.14);color:#fff;border:1px solid rgba(255,255,255,.35);padding:10px 16px;border-radius:12px;font-weight:800;font-size:12px;cursor:pointer;transition:.25s}
.btn-outline-light:hover{background:rgba(255,255,255,.25)}
.hero-visual{background:rgba(255,255,255,.12);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.22);border-radius:18px;padding:12px;text-align:center}
.hero-visual img{width:100%;height:145px;object-fit:cover;border-radius:12px;margin-bottom:8px}
.hero-visual small{font-size:11px;font-weight:700;display:block}

/* Feature Strip */
.features-3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px}
.feat-box{background:#fff;border-radius:16px;padding:14px 10px;text-align:center;box-shadow:0 4px 14px rgba(0,0,0,.05);transition:.25s}
.feat-box:hover{transform:translateY(-3px)}
.feat-box i{font-size:20px;color:var(--primary);margin-bottom:6px}
.feat-box h4{font-size:12px;font-weight:800}
.feat-box p{font-size:10px;color:#667;margin-top:2px}

/* Sections & Product Cards */
.section-head{display:flex;justify-content:space-between;align-items:center;margin:18px 14px 10px}
.section-head h3{font-size:18px;font-weight:900;display:flex;align-items:center;gap:8px}
.section-head span{font-size:11px;font-weight:800;color:var(--primary);cursor:pointer}

.cat-pills{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;margin:0 12px 12px}
.cat-pills::-webkit-scrollbar{display:none}
.cat-pill{background:#fff;border:1px solid #dbe5f0;padding:8px 14px;border-radius:14px;font-size:11px;font-weight:800;cursor:pointer;white-space:nowrap;transition:.25s}
.cat-pill.active,.cat-pill:hover{background:#0d1b2a;color:#fff;border-color:#0d1b2a}

.prod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(175px,1fr));gap:12px;margin:0 12px}
.prod-card{background:#fff;border-radius:18px;padding:11px;box-shadow:0 4px 16px rgba(13,27,42,.06);border:1px solid #eef2f7;display:flex;flex-direction:column;justify-content:space-between;position:relative;transition:.3s;animation:fadeUp .4s ease}
.prod-card:hover{transform:translateY(-5px);box-shadow:0 14px 28px rgba(0,119,182,.14)}
.prod-tag{position:absolute;top:10px;left:10px;background:#e0f4ff;color:#005f99;font-size:9px;font-weight:900;padding:3px 8px;border-radius:8px;z-index:2}
.heart-btn{position:absolute;top:10px;right:10px;width:28px;height:28px;border-radius:50%;background:rgba(255,255,255,.92);box-shadow:0 2px 8px rgba(0,0,0,.1);display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;color:#bbb;transition:.25s}
.heart-btn.active{color:#ff2a5f;background:#ffe5ec}
.prod-img-box{width:100%;height:112px;border-radius:12px;background:#f7f9fc;display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:8px;cursor:pointer}
.prod-img-box img{width:100%;height:100%;object-fit:cover;transition:.35s}
.prod-card:hover .prod-img-box img{transform:scale(1.07)}
.prod-title{font-size:12px;font-weight:800;line-height:1.3;min-height:31px;margin-bottom:4px;cursor:pointer}
.prod-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:#667;margin-bottom:6px}
.prod-cas{background:#f1f5f9;padding:2px 6px;border-radius:6px;font-weight:700}
.prod-price{font-size:15px;font-weight:900;color:var(--primary);margin-bottom:8px}
.add-cart-btn{width:100%;background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border:none;padding:9px;border-radius:11px;font-size:11px;font-weight:800;cursor:pointer;transition:.25s}
.add-cart-btn:hover{filter:brightness(1.06)}
.qty-row{display:flex;align-items:center;gap:6px}
.qty-row button{width:32px;height:32px;border:none;border-radius:9px;background:#0077b6;color:#fff;font-weight:900;font-size:15px;cursor:pointer}
.qty-row span{flex:1;text-align:center;font-weight:900;font-size:13px;background:#f3f7fc;padding:6px;border-radius:9px}

/* Content Panels (Reviews, Compliance, Info Pages) */
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
.primary-btn{background:linear-gradient(135deg,#0077b6,#00b4d8);color:#fff;border:none;padding:11px 16px;border-radius:12px;font-weight:800;font-size:12px;cursor:pointer;margin-top:10px}

/* Footer with Required Links */
.footer-main{background:linear-gradient(135deg,#0d1b2a,#005f99);color:#fff;padding:28px 16px 32px;margin:20px 12px 12px;border-radius:24px}
.footer-top{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.footer-links-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-top:18px;padding-top:18px;border-top:1px solid rgba(255,255,255,.16)}
.f-link{color:#e0f4ff;text-decoration:none;font-size:12px;font-weight:700;padding:8px 10px;border-radius:10px;background:rgba(255,255,255,.08);cursor:pointer;transition:.2s;display:flex;align-items:center;gap:6px}
.f-link:hover{background:rgba(255,255,255,.2);color:#ffd166;transform:translateX(3px)}

/* Bottom Nav */
.bottom-nav{position:fixed;bottom:10px;left:10px;right:10px;background:rgba(255,255,255,.94);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-radius:28px;display:flex;justify-content:space-around;padding:8px 4px;box-shadow:0 12px 36px rgba(13,27,42,.2);z-index:1000;border:1px solid rgba(255,255,255,.7)}
.b-item{font-size:10px;font-weight:700;text-align:center;opacity:.65;cursor:pointer;padding:4px 8px;border-radius:18px;position:relative;transition:.25s;color:#1e293b}
.b-item.active{opacity:1;background:rgba(0,119,182,.14);color:var(--primary)}
.b-item i{font-size:17px;display:block;margin-bottom:2px}

/* Floating Buttons */
.wa-float{position:fixed;bottom:92px;right:14px;width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:0 8px 22px rgba(37,211,102,.4);cursor:pointer;z-index:998;animation:floatY 3s ease-in-out infinite}
.top-float{position:fixed;bottom:154px;right:18px;width:42px;height:42px;border-radius:50%;background:#fff;color:var(--dark);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.15);cursor:pointer;z-index:998}

/* Drawers, Search & Modals */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;z-index:15000}
.overlay.active{display:block}
#cartDrawer{position:fixed;top:0;right:-100%;width:92%;max-width:410px;height:100%;background:#fff;z-index:25000;transition:.35s ease;padding:18px;display:flex;flex-direction:column;box-shadow:-12px 0 36px rgba(0,0,0,.22)}
#cartDrawer.active{right:0}
.search-drawer{position:fixed;top:0;left:0;right:0;background:#fff;z-index:22000;padding:14px;transform:translateY(-100%);transition:.35s ease;box-shadow:0 10px 30px rgba(0,0,0,.18)}
.search-drawer.active{transform:translateY(0)}
.modal-bg{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:center;justify-content:center;z-index:26000;padding:14px}
.modal-bg.active{display:flex}
.modal-card{background:#fff;width:100%;max-width:420px;border-radius:22px;padding:20px;max-height:86vh;overflow-y:auto;box-shadow:0 20px 50px rgba(0,0,0,.3)}

#toast{position:fixed;bottom:115px;left:50%;transform:translateX(-50%) translateY(80px);background:#0d1b2a;color:#fff;padding:10px 18px;border-radius:999px;font-size:12px;font-weight:700;opacity:0;transition:.35s;z-index:30000;pointer-events:none;white-space:nowrap}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

@keyframes spinSlow{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes marqueeMove{0%{transform:translateX(0)}100%{transform:translateX(-100%)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes pulseFloat{0%,100%{transform:scale(1)}50%{transform:scale(1.12)}}

@media(max-width:640px){
  .hero-grid{grid-template-columns:1fr}
  .delivery-pill{max-width:130px}
  .features-3{grid-template-columns:1fr}
}
</style>
</head>
<body>

<div class="top-bar">
  <span><i class="fa fa-flask"></i> Global Chemical Solution (GBL) — Industrial & Technical Supply</span>
  <span><i class="fa fa-phone"></i> +447983259218 | Bestgbonine.uk@gmail.com</span>
</div>

<header class="header">
  <div class="brand-group" onclick="switchPage('home')">
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

  <div class="delivery-pill" onclick="openDeliveryModal()">
    <b><i class="fa fa-map-marker-alt"></i> Delivery <i class="fa fa-caret-down"></i></b>
    <span id="deliveryAddressText">22 Parks Vw Rd, Inverness IV2 6JJ, UK</span>
  </div>

  <div class="header-actions">
    <button class="icon-btn" onclick="openSearch()" title="Search Chemicals"><i class="fa fa-search"></i></button>
    <button class="icon-btn" onclick="openCart()" title="Shopping Cart">
      <i class="fa fa-shopping-cart"></i>
      <span class="badge-dot" id="headerCartBadge">0</span>
    </button>
  </div>
</header>

<!-- 7-Page Switcher Bar -->
<nav class="pages-nav" id="pagesNav">
  <button class="page-tab active" data-page="home" onclick="switchPage('home')"><i class="fa fa-home"></i> 1. Home & Catalog</button>
  <button class="page-tab" data-page="gbl" onclick="switchPage('gbl')"><i class="fa fa-vial"></i> 2. GBL Solvents</button>
  <button class="page-tab" data-page="bdo" onclick="switchPage('bdo')"><i class="fa fa-atom"></i> 3. 1.4-BDO & Gels</button>
  <button class="page-tab" data-page="industrial" onclick="switchPage('industrial')"><i class="fa fa-industry"></i> 4. Industrial & Bulk</button>
  <button class="page-tab" data-page="compliance" onclick="switchPage('compliance')"><i class="fa fa-shield-halved"></i> 5. Law & Compliance</button>
  <button class="page-tab" data-page="reviews" onclick="switchPage('reviews')"><i class="fa fa-star"></i> 6. Customer Reviews</button>
  <button class="page-tab" data-page="contact" onclick="switchPage('contact')"><i class="fa fa-headset"></i> 7. Contact & Support</button>
</nav>

<!-- Animated Flash Deal Line -->
<div class="flash-marquee-wrap" onclick="switchPage('gbl')">
  <span class="flash-badge"><i class="fa fa-bolt"></i> FLASH DEAL</span>
  <div class="marquee-track">
    <div class="marquee-text">
      ⚡ FLASH DEAL LIVE: Pure Liquid GBL 1L (€235.00), 2×1L + 1L Free (€399.00), GBL Gel Remover 2.5L (€225.00), 1.4 Butanediol BDO 10L (€670.00), White Vaseline 700g (€9.39) — Fast UK & EU Dispatch from Global Chemical Solution! ⚡
    </div>
  </div>
  <div class="flash-timer-box" id="flashCountdown">04:59:59</div>
</div>

<!-- HERO SECTION -->
<section class="hero-card">
  <div class="hero-grid">
    <div>
      <div class="hero-chip"><i class="fa fa-certificate"></i> ISO & Technical Grade Chemical Supply</div>
      <h2>High-Purity Solvents, BDO, Gel Removers & Bulk Chemicals</h2>
      <p>Complete industrial chemical catalog across 7 dedicated views. Inspect CAS specs, container volumes, transparent pricing, and place instant orders or WhatsApp inquiries.</p>
      <div class="hero-btns">
        <button class="btn-glow" onclick="switchPage('home');scrollToCatalog()">Browse All Products</button>
        <button class="btn-outline-light" onclick="openCart()"><i class="fa fa-shopping-cart"></i> View Cart (<span id="heroCartCount">0</span>)</button>
      </div>
    </div>
    <div class="hero-visual">
      <img src="https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=600" alt="Laboratory and industrial chemical containers">
      <small>Global Chemical Solution • Inverness, UK</small>
    </div>
  </div>
</section>

<div class="features-3">
  <div class="feat-box"><i class="fa fa-truck-fast"></i><h4>Tracked Dispatch</h4><p>UK & International Logistics</p></div>
  <div class="feat-box"><i class="fa fa-file-shield"></i><h4>CAS & Grade Listed</h4><p>Technical & Industrial Specs</p></div>
  <div class="feat-box"><i class="fa fa-comments"></i><h4>Direct Support</h4><p>+447983259218 WhatsApp</p></div>
</div>

<!-- DYNAMIC 7-PAGE CONTENT AREA -->
<main id="pageContainer"></main>

<!-- FOOTER WITH ALL 6 REQUIRED CLICKABLE LINKS -->
<footer class="footer-main">
  <div class="footer-top">
    <div>
      <h2 style="font-size:24px;font-weight:900;letter-spacing:.5px">Global Chemical Solution</h2>
      <p style="font-size:12px;opacity:.88;margin-top:6px;line-height:1.5">
        Dedicated chemical supply portal featuring GBL solvents, 1.4 Butanediol (BDO), multi-gel removers, and industrial raw materials.
      </p>
    </div>
    <div style="font-size:12px;line-height:1.8">
      <div><i class="fa fa-location-dot"></i> <b>Address:</b> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom</div>
      <div><i class="fa fa-envelope"></i> <b>Email:</b> <a href="mailto:Bestgbonine.uk@gmail.com" style="color:#ffd166">Bestgbonine.uk@gmail.com</a></div>
      <div><i class="fab fa-whatsapp"></i> <b>WhatsApp:</b> <a href="https://wa.me/447983259218" target="_blank" style="color:#ffd166">+447983259218</a></div>
    </div>
  </div>

  <div class="footer-links-grid">
    <a class="f-link" onclick="openDocModal('gbl_law')"><i class="fa fa-scale-balanced"></i> GBL Law Regulations</a>
    <a class="f-link" onclick="openDocModal('privacy')"><i class="fa fa-user-shield"></i> Privacy statement</a>
    <a class="f-link" onclick="openDocModal('about')"><i class="fa fa-building"></i> About Global Chemical</a>
    <a class="f-link" onclick="openDocModal('terms')"><i class="fa fa-file-contract"></i> Terms &amp; Conditions</a>
    <a class="f-link" onclick="openDocModal('compliance')"><i class="fa fa-check-double"></i> Compliance</a>
    <a class="f-link" onclick="switchPage('contact');scrollToTop()"><i class="fa fa-address-book"></i> Contact us</a>
  </div>

  <p style="text-align:center;font-size:11px;opacity:.78;margin-top:20px">
    © 2026 Global Chemical Solution (GBL). All rights reserved.
  </p>
</footer>

<!-- Floating Action Buttons -->
<div class="top-float" onclick="scrollToTop()" title="Scroll to Top"><i class="fa fa-chevron-up"></i></div>
<div class="wa-float" onclick="openWhatsAppDirect()" title="WhatsApp Global Chemical Solution"><i class="fab fa-whatsapp"></i></div>

<!-- Bottom Navigation Bar (Rainbow Mart Style) -->
<div class="bottom-nav">
  <div class="b-item active" id="bNavHome" onclick="switchPage('home');scrollToTop()"><i class="fa fa-home"></i>Home</div>
  <div class="b-item" id="bNavCat" onclick="switchPage('home');scrollToCatalog()"><i class="fa fa-th-large"></i>Categories</div>
  <div class="b-item" id="bNavSearch" onclick="openSearch()"><i class="fa fa-search"></i>Search</div>
  <div class="b-item" id="bNavCart" onclick="openCart()"><i class="fa fa-shopping-cart"></i><span class="badge-dot" id="bottomCartBadge">0</span>Cart</div>
  <div class="b-item" id="bNavSupport" onclick="switchPage('contact');scrollToTop()"><i class="fa fa-headset"></i>Support</div>
</div>

<!-- Overlay & Search Drawer -->
<div class="overlay" id="overlay" onclick="closeAllOverlays()"></div>

<div class="search-drawer" id="searchDrawer">
  <div style="display:flex;gap:8px;align-items:center">
    <input type="text" id="searchInput" class="form-control" style="margin-top:0;border-radius:999px;padding:12px 16px" placeholder="Search GBL, BDO, Gel Remover, Vaseline, CAS..." oninput="runSearch()">
    <button onclick="closeSearch()" style="width:42px;height:42px;border-radius:50%;border:none;background:#eef2f7;font-weight:900;cursor:pointer">✕</button>
  </div>
  <div id="searchResults" style="max-height:62vh;overflow-y:auto;margin-top:12px"></div>
</div>

<!-- Slide-Out Cart Drawer -->
<aside id="cartDrawer">
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #eef2f7;padding-bottom:12px">
    <h3 style="font-size:18px;font-weight:900"><i class="fa fa-shopping-cart"></i> Order Cart</h3>
    <button onclick="closeCart()" style="width:34px;height:34px;border-radius:50%;border:none;background:#f1f5f9;font-weight:900;cursor:pointer">✕</button>
  </div>
  <div id="cartItemsBox" style="flex:1;overflow-y:auto;margin:12px 0"></div>
  <div style="border-top:1px solid #eef2f7;padding-top:12px">
    <div style="display:flex;justify-content:space-between;font-size:16px;font-weight:900;margin-bottom:6px">
      <span>Subtotal</span>
      <span>€<span id="cartTotalVal">0.00</span></span>
    </div>
    <p style="font-size:11px;color:#64748b;margin-bottom:10px">Destination: <b id="cartDestLabel">22 Parks Vw Rd, Inverness IV2 6JJ, UK</b></p>
    <button onclick="checkoutWhatsApp()" style="width:100%;background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;border:none;padding:14px;border-radius:14px;font-weight:900;font-size:13px;cursor:pointer">
      <i class="fab fa-whatsapp"></i> Send Order via WhatsApp
    </button>
  </div>
</aside>

<!-- Delivery Address Modal -->
<div class="modal-bg" id="deliveryModal" onclick="closeAllOverlays()">
  <div class="modal-card" onclick="event.stopPropagation()">
    <h3 style="font-size:17px;font-weight:900;margin-bottom:6px"><i class="fa fa-map-marker-alt" style="color:var(--primary)"></i> Delivery Address</h3>
    <p style="font-size:12px;color:#64748b;margin-bottom:10px">Choose a hub or enter a custom shipping address.</p>
    <input type="text" id="customAddrInput" class="form-control" placeholder="Enter street, city, postcode...">
    <button class="primary-btn" style="width:100%;background:#16a34a" onclick="saveCustomAddress()"><i class="fa fa-check"></i> Save Custom Address</button>
    <div style="margin-top:12px;display:flex;flex-direction:column;gap:8px">
      <div onclick="setDeliveryAddr('22 Parks Vw Rd, Inverness IV2 6JJ, UK')" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;cursor:pointer;font-size:12px">
        <b>Inverness HQ, Scotland, UK</b><div style="font-size:10px;color:#64748b">22 Parks Vw Rd, Inverness IV2 6JJ</div>
      </div>
      <div onclick="setDeliveryAddr('London Industrial Hub, United Kingdom')" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;cursor:pointer;font-size:12px">
        <b>London / UK Freight Route</b><div style="font-size:10px;color:#64748b">Standard commercial courier dispatch</div>
      </div>
      <div onclick="setDeliveryAddr('Rotterdam / EU Chemical Port Corridor')" style="padding:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;cursor:pointer;font-size:12px">
        <b>EU Chemical Corridor</b><div style="font-size:10px;color:#64748b">ADR &amp; documentation verified route</div>
      </div>
    </div>
    <button onclick="closeAllOverlays()" style="width:100%;margin-top:12px;padding:10px;border:none;border-radius:12px;background:#eef2f7;font-weight:800;cursor:pointer">Close</button>
  </div>
</div>

<!-- Legal / Info Document Modal -->
<div class="modal-bg" id="docModal" onclick="closeAllOverlays()">
  <div class="modal-card" onclick="event.stopPropagation()">
    <h3 id="docModalTitle" style="font-size:18px;font-weight:900;margin-bottom:10px;color:var(--primary)"></h3>
    <div id="docModalBody" style="font-size:12.5px;line-height:1.65;color:#334155"></div>
    <button onclick="closeAllOverlays()" class="primary-btn" style="width:100%;margin-top:16px">Close Document</button>
  </div>
</div>

<div id="toast">Notification</div>

<script>
const CATALOG = [
  {
    id:"gbl-1l", name:"Pure Liquid GBL 1L", category:"gbl", page:"gbl",
    priceNum:235.00, priceLabel:"€235.00", pack:"1 Liter Container", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6?w=500",
    desc:"Industrial gamma-butyrolactone (GBL) solvent in sealed chemical-resistant container for technical cleaning, coating removal, and manufacturing."
  },
  {
    id:"gbl-2x1l-free", name:"Pure Liquid GBL – 2×1L Canisters + 1L Free", category:"gbl", page:"gbl",
    priceNum:399.00, priceLabel:"€399.00", pack:"3 Liters Total (2×1L + 1L Free)", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1581093458791-9f3c3250e4b0?w=500",
    desc:"Promotional multi-canister bundle of Pure Liquid GBL for high-frequency industrial solvent applications."
  },
  {
    id:"gbl-5l", name:"Pure Liquid GBL – 5L Canister", category:"gbl", page:"gbl",
    priceNum:950.00, priceLabel:"€950.00", pack:"5L Canister", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1576086213369-97a306d36557?w=500",
    desc:"Industrial GBL solvent supplied in a secure 5-liter container for paint, coating, adhesive removal, and surface preparation."
  },
  {
    id:"gbl-10l", name:"Pure Liquid GBL – 10L Canister", category:"gbl", page:"gbl",
    priceNum:1450.00, priceLabel:"€1,450.00", pack:"10L Canister", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=500",
    desc:"High-capacity 10L canister for continuous solvent processing and commercial facility maintenance."
  },
  {
    id:"gbl-2x25l", name:"Pure Liquid GBL – 2×25L (50L Total)", category:"gbl", page:"gbl",
    priceNum:4200.00, priceLabel:"€4,200.00", pack:"50L Total (2×25L)", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=500",
    desc:"Commercial twin-canister 50L supply for industrial formulation and residue breakdown."
  },
  {
    id:"gbl-4x25l", name:"Pure Liquid GBL – 4×25L Canisters (100L Total)", category:"gbl", page:"gbl",
    priceNum:6500.00, priceLabel:"€6,500.00", pack:"100L Total (4×25L)", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1518152006812-edab29b069ac?w=500",
    desc:"Bulk 100L canister pack engineered for heavy industrial solvent operations."
  },
  {
    id:"gbl-200l", name:"Pure Liquid Gamma-Butyrolactone GBL – 200L Drum", category:"gbl", page:"industrial",
    priceNum:8500.00, priceLabel:"€8,500.00", pack:"200L Drum", cas:"CAS 96-48-0",
    img:"https://images.unsplash.com/photo-1563213126-a427aed14b89?w=500",
    desc:"High-volume 200L steel/HDPE drum for large-scale chemical processing, manufacturing, and contract supply."
  },
  {
    id:"gbl-997-100ml", name:"100 ml GBL 99.7% y-butyrolactone Technical Grade", category:"gbl", page:"gbl",
    priceNum:19.00, priceLabel:"€19.00", pack:"100 ml", cas:"HS 29322020",
    img:"https://images.unsplash.com/photo-1616671276441-2f2c277b8bf6?w=500",
    desc:"99.7% technical grade gamma-butyrolactone sample/small-batch unit for testing and specialized applications."
  },
  {
    id:"gbl-997-2500ml", name:"2.500 ml GBL 99.7% y-butyrolactone Super Grade", category:"gbl", page:"gbl",
    priceNum:206.72, priceLabel:"€206.72", pack:"2,500 ml Canister", cas:"HS 29322020",
    img:"https://images.unsplash.com/photo-1579154204601-01588f351e67?w=500",
    desc:"Super grade 99.7% gamma-butyrolactone canister for high-precision industrial solvent requirements."
  },
  {
    id:"bdo-2l", name:"1.4 Butanediol BDO 2L", category:"bdo", page:"bdo",
    priceNum:159.00, priceLabel:"€159.00", pack:"2 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1587854692152-cbe660dbde88?w=500",
    desc:"1.4-Butanediol (BDO) 2L industrial intermediate and solvent grade."
  },
  {
    id:"bdo-3l", name:"1.4 Butandiol BDO 3L", category:"bdo", page:"bdo",
    priceNum:225.00, priceLabel:"€225.00", pack:"3 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6?w=500",
    desc:"3L 1.4-Butanediol (BDO) container for chemical synthesis and industrial formulation."
  },
  {
    id:"bdo-4l", name:"1.4 Butandiol BDO 4L", category:"bdo", page:"bdo",
    priceNum:299.00, priceLabel:"€299.00", pack:"4 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=500",
    desc:"4L 1.4-Butanediol (BDO) technical supply with secure sealing."
  },
  {
    id:"bdo-5l", name:"1.4 Butandiol BDO 5L", category:"bdo", page:"bdo",
    priceNum:365.00, priceLabel:"€365.00", pack:"5 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1576086213369-97a306d36557?w=500",
    desc:"5L 1.4-Butanediol (BDO) container for commercial polymer and solvent applications."
  },
  {
    id:"bdo-6l", name:"1.4 Butandiol BDO 6L", category:"bdo", page:"bdo",
    priceNum:429.00, priceLabel:"€429.00", pack:"6 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1581093458791-9f3c3250e4b0?w=500",
    desc:"6L 1.4-Butanediol (BDO) industrial volume container."
  },
  {
    id:"bdo-10l", name:"1.4 Butandiol BDO 10L", category:"bdo", page:"bdo",
    priceNum:670.00, priceLabel:"€670.00", pack:"10 Liters", cas:"CAS 110-63-4",
    img:"https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=500",
    desc:"10L 1.4-Butanediol (BDO) bulk canister for ongoing manufacturing operations."
  },
  {
    id:"gel-250ml", name:"GBL Multi Gel Remover 250 ml", category:"gel", page:"bdo",
    priceNum:80.00, priceLabel:"€80.00", pack:"250 ml", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1616671276441-2f2c277b8bf6?w=500",
    desc:"Targeted multi-gel remover 250 ml for precision coating and residue stripping."
  },
  {
    id:"gel-1l", name:"GBL Multi Gel Remover 1L", category:"bdo", page:"bdo",
    priceNum:150.00, priceLabel:"€150.00", pack:"1 Liter", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1579154204601-01588f351e67?w=500",
    desc:"1L GBL multi-gel formula designed to cling to vertical surfaces and break down stubborn coatings."
  },
  {
    id:"gel-25l", name:"GBL Gel Remover 2.5L Canister", category:"bdo", page:"bdo",
    priceNum:225.00, priceLabel:"€225.00", pack:"2.5L Canister", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=500",
    desc:"2.5L canister of GBL gel remover for industrial paint, varnish, and adhesive stripping."
  },
  {
    id:"gel-5l", name:"GBL Multi Gel Remover 5L Canister", category:"bdo", page:"bdo",
    priceNum:400.00, priceLabel:"€400.00", pack:"5L Canister", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1576086213369-97a306d36557?w=500",
    desc:"5L multi-gel remover canister for workshop and industrial surface restoration."
  },
  {
    id:"gel-10l", name:"GBL Multi Gel Remover 10L Canister", category:"bdo", page:"bdo",
    priceNum:750.00, priceLabel:"€750.00", pack:"10L Canister", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1581093458791-9f3c3250e4b0?w=500",
    desc:"10L canister of multi-gel remover for heavy-duty commercial stripping."
  },
  {
    id:"gel-20l", name:"GBL Multi Gel Remover 20L Canister", category:"bdo", page:"bdo",
    priceNum:1250.00, priceLabel:"€1,250.00", pack:"20L Canister", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=500",
    desc:"20L industrial canister of GBL multi-gel remover for large-area operations."
  },
  {
    id:"gel-4x25l", name:"GBL Multi Gel Remover – 4×25L Canisters (100L Total)", category:"bdo", page:"industrial",
    priceNum:5400.00, priceLabel:"€5,400.00", pack:"100L Total (4×25L)", cas:"Gel Solvent",
    img:"https://images.unsplash.com/photo-1563213126-a427aed14b89?w=500",
    desc:"Bulk 100L pallet/canister set of GBL multi-gel remover for industrial contract demand."
  },
  {
    id:"gel-tech-2500", name:"Multi Gel Remover® 2.500 ml Technical Grade", category:"gel", page:"industrial",
    priceNum:188.14, priceLabel:"€188.14", pack:"2,500 ml Canister", cas:"Technical Grade",
    img:"https://images.unsplash.com/photo-1518152006812-edab29b069ac?w=500",
    desc:"Technical grade 2,500 ml canister of Multi Gel Remover® for industrial surface maintenance."
  },
  {
    id:"gel-tech-10l", name:"Multi Gel Remover® 10 Litres Technical Grade Blue", category:"gel", page:"industrial",
    priceNum:684.24, priceLabel:"€684.24", pack:"10L Canister (Blue)", cas:"Technical Grade",
    img:"https://images.unsplash.com/photo-1603126857599-f6e157fa2fe6?w=500",
    desc:"Blue technical grade 10L canister for high-visibility industrial gel application."
  },
  {
    id:"gel-tech-20l", name:"Multi Gel Remover® 20 Litres Technical Grade Blue", category:"gel", page:"industrial",
    priceNum:1188.90, priceLabel:"€1,188.90", pack:"20L Canister (Blue)", cas:"Technical Grade",
    img:"https://images.unsplash.com/photo-1579154204601-01588f351e67?w=500",
    desc:"Blue technical grade 20L canister for large-scale commercial cleaning and stripping."
  },
  {
    id:"vaseline-700g", name:"White Vaseline – Petrolatum (700g)", category:"industrial", page:"industrial",
    priceNum:9.39, priceLabel:"€9.39", pack:"700g Unit", cas:"CAS 8009-03-8",
    img:"https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=500",
    desc:"Refined white petrolatum (Vaseline) 700g for lubrication, moisture barrier, and industrial/cosmetic compounding."
  },
  {
    id:"vaseline-12x700g", name:"White Vaseline – Petrolatum (12×700g Bulk Case)", category:"industrial", page:"industrial",
    priceNum:100.49, priceLabel:"€100.49", pack:"12×700g Case", cas:"CAS 8009-03-8",
    img:"https://images.unsplash.com/photo-1616671276441-2f2c277b8bf6?w=500",
    desc:"Commercial case of 12×700g white petrolatum for wholesale and manufacturing buyers."
  }
];

const DOCS = {
  gbl_law: {
    title: "GBL Law Regulations",
    html: `<p><strong>Global Chemical Solution</strong> operates with attention to regional and international chemical regulations governing gamma-butyrolactone (GBL) and related solvents.</p>
    <ul>
      <li><strong>Industrial &amp; Commercial Use:</strong> Products are supplied for authorized industrial, technical, and commercial applications.</li>
      <li><strong>Regulatory Screening:</strong> Orders may be subject to end-use verification, business/account details, and local import/export rules.</li>
      <li><strong>Buyer Responsibility:</strong> Customers must ensure compliance with national chemical control laws in their destination jurisdiction.</li>
    </ul>`
  },
  privacy: {
    title: "Privacy Statement",
    html: `<p><strong>Global Chemical Solution</strong> respects your privacy and handles inquiry, delivery, and order details responsibly.</p>
    <ul>
      <li><strong>Information Collected:</strong> Contact name, delivery address, email (<code>Bestgbonine.uk@gmail.com</code>), and WhatsApp/phone details needed to coordinate orders.</li>
      <li><strong>Usage:</strong> Used strictly for order processing, logistics coordination, compliance checks, and customer support.</li>
      <li><strong>Security:</strong> We do not sell customer contact lists to third-party data brokers.</li>
    </ul>`
  },
  about: {
    title: "About Global Chemical Solution",
    html: `<p><strong>Global Chemical Solution</strong> (GBL) supplies industrial solvents, 1.4-Butanediol (BDO), gel removers, and specialty raw materials with clear container options and direct support.</p>
    <p style="margin-top:8px"><strong>Registered Address:</strong> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom<br>
    <strong>WhatsApp:</strong> +447983259218<br>
    <strong>Email:</strong> Bestgbonine.uk@gmail.com</p>`
  },
  terms: {
    title: "Terms & Conditions",
    html: `<ul>
      <li><strong>Pricing &amp; Availability:</strong> Listed prices are shown in EUR (€) as displayed in the catalog and are subject to stock and freight terms.</li>
      <li><strong>Order Confirmation:</strong> Orders sent via cart or WhatsApp are confirmed upon stock verification and shipping arrangement.</li>
      <li><strong>Handling &amp; Safety:</strong> Customers must follow Safety Data Sheets (SDS), proper ventilation, and local hazardous/chemical handling rules.</li>
    </ul>`
  },
  compliance: {
    title: "Regulatory & Safety Compliance",
    html: `<p>We support transparent documentation and responsible chemical distribution:</p>
    <ul>
      <li><strong>CAS &amp; Grade Transparency:</strong> CAS numbers and container sizes are listed clearly on chemical items.</li>
      <li><strong>Packaging Integrity:</strong> Sealed containers and drums suitable for transport and storage.</li>
      <li><strong>Compliance Inquiries:</strong> Contact <code>Bestgbonine.uk@gmail.com</code> or <code>+447983259218</code> for documentation requests.</li>
    </ul>`
  }
};

let state = {
  page: "home",
  catFilter: "all",
  cart: {},      // id -> qty
  wishlist: {},  // id -> true
  address: "22 Parks Vw Rd, Inverness IV2 6JJ, UK",
  reviews: [
    { name: "Callum MacLeod", location: "Inverness, UK", text: "Sealed canisters arrived cleanly and matched the exact volume and grade specs." },
    { name: "Hendrik van Dijk", location: "Rotterdam, NL", text: "Clear pricing on BDO and gel removers, fast WhatsApp response for order confirmation." }
  ]
};

function showToast(msg){
  const t = document.getElementById("toast");
  t.innerText = msg;
  t.classList.add("show");
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(()=>t.classList.remove("show"), 2400);
}

function scrollToTop(){ window.scrollTo({ top:0, behavior:"smooth" }); }
function scrollToCatalog(){
  const el = document.getElementById("catalogSection");
  if(el) el.scrollIntoView({ behavior:"smooth", block:"start" });
}

function switchPage(page){
  state.page = page;
  document.querySelectorAll(".page-tab").forEach(btn=>{
    btn.classList.toggle("active", btn.dataset.page === page);
  });
  document.querySelectorAll(".b-item").forEach(b=>b.classList.remove("active"));
  if(page==="home") document.getElementById("bNavHome").classList.add("active");
  if(page==="contact") document.getElementById("bNavSupport").classList.add("active");
  renderPage();
}

function setCategory(cat){
  state.catFilter = cat;
  renderPage();
}

function toggleWish(id){
  state.wishlist[id] = !state.wishlist[id];
  showToast(state.wishlist[id] ? "Saved to favorites ♥" : "Removed from favorites");
  renderPage();
}

function addQty(id, delta){
  const next = (state.cart[id] || 0) + delta;
  if(next <= 0) delete state.cart[id];
  else state.cart[id] = next;
  updateCartUI();
  renderPage();
  if(delta > 0) showToast("Added to cart");
}

function updateCartUI(){
  let totalQty = 0;
  let subtotal = 0;
  let html = "";

  Object.entries(state.cart).forEach(([id, qty])=>{
    const item = CATALOG.find(p=>p.id === id);
    if(!item) return;
    const lineTotal = item.priceNum * qty;
    totalQty += qty;
    subtotal += lineTotal;
    html += `
      <div style="display:flex;gap:10px;align-items:center;background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:10px;margin-bottom:10px">
        <img src="${item.img}" alt="${item.name}" style="width:52px;height:52px;border-radius:10px;object-fit:cover">
        <div style="flex:1">
          <div style="font-size:12px;font-weight:800">${item.name}</div>
          <div style="font-size:10px;color:#64748b">${item.pack} • ${item.priceLabel} each</div>
          <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
            <button onclick="addQty('${item.id}',-1)" style="width:26px;height:26px;border:none;border-radius:7px;background:#e2e8f0;font-weight:900;cursor:pointer">−</button>
            <span style="font-size:12px;font-weight:900;padding:0 4px">${qty}</span>
            <button onclick="addQty('${item.id}',1)" style="width:26px;height:26px;border:none;border-radius:7px;background:#0077b6;color:#fff;font-weight:900;cursor:pointer">+</button>
            <span style="margin-left:auto;font-size:12px;font-weight:900;color:#0077b6">€${lineTotal.toFixed(2)}</span>
          </div>
        </div>
      </div>`;
  });

  document.getElementById("headerCartBadge").innerText = totalQty;
  document.getElementById("bottomCartBadge").innerText = totalQty;
  document.getElementById("heroCartCount").innerText = totalQty;
  document.getElementById("cartTotalVal").innerText = subtotal.toFixed(2);
  document.getElementById("cartDestLabel").innerText = state.address;
  document.getElementById("cartItemsBox").innerHTML = html || `
    <div style="text-align:center;color:#94a3b8;padding:40px 10px">
      <i class="fa fa-box-open" style="font-size:32px;margin-bottom:8px"></i>
      <div style="font-weight:800;font-size:13px">Your chemical order cart is empty</div>
      <div style="font-size:11px;margin-top:4px">Select products from any category to add.</div>
    </div>`;
}

function productCardHTML(p){
  const qty = state.cart[p.id] || 0;
  const liked = !!state.wishlist[p.id];
  const actionBlock = qty > 0
    ? `<div class="qty-row">
         <button onclick="addQty('${p.id}',-1)">−</button>
         <span>${qty}</span>
         <button onclick="addQty('${p.id}',1)">+</button>
       </div>`
    : `<button class="add-cart-btn" onclick="addQty('${p.id}',1)"><i class="fa fa-cart-plus"></i> Add to Cart</button>`;

  return `
    <div class="prod-card">
      <span class="prod-tag">${p.pack}</span>
      <div class="heart-btn ${liked ? 'active' : ''}" onclick="toggleWish('${p.id}')"><i class="fa fa-heart"></i></div>
      <div class="prod-img-box" onclick="showProductDetails('${p.id}')">
        <img src="${p.img}" alt="${p.name}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=500'">
      </div>
      <div>
        <div class="prod-title" onclick="showProductDetails('${p.id}')">${p.name}</div>
        <div class="prod-meta">
          <span>${p.category.toUpperCase()}</span>
          <span class="prod-cas">${p.cas}</span>
        </div>
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
    <img src="${p.img}" alt="${p.name}" style="width:100%;height:170px;object-fit:cover;border-radius:12px;margin-bottom:10px">
    <p><strong>Price:</strong> ${p.priceLabel} &nbsp;|&nbsp; <strong>Packaging:</strong> ${p.pack}</p>
    <p><strong>Identifier / Grade:</strong> ${p.cas}</p>
    <p style="margin-top:8px">${p.desc}</p>
    <button onclick="addQty('${p.id}',1);closeAllOverlays();openCart()" class="primary-btn" style="width:100%">Add to Cart &amp; Open Order Drawer</button>
  `;
  document.getElementById("docModal").classList.add("active");
  document.getElementById("overlay").classList.add("active");
}

function renderCatalogSection(title, items, showFilterBar){
  const filterBar = showFilterBar ? `
    <div class="cat-pills">
      <button class="cat-pill ${state.catFilter==='all'?'active':''}" onclick="setCategory('all')">All (${CATALOG.length})</button>
      <button class="cat-pill ${state.catFilter==='gbl'?'active':''}" onclick="setCategory('gbl')">GBL Solvents</button>
      <button class="cat-pill ${state.catFilter==='bdo'?'active':''}" onclick="setCategory('bdo')">1.4 Butanediol (BDO)</button>
      <button class="cat-pill ${state.catFilter==='gel'?'active':''}" onclick="setCategory('gel')">Gel Removers</button>
      <button class="cat-pill ${state.catFilter==='industrial'?'active':''}" onclick="setCategory('industrial')">Drums, Tech &amp; Vaseline</button>
    </div>` : "";

  return `
    <section id="catalogSection">
      <div class="section-head">
        <h3><i class="fa fa-flask" style="color:var(--primary)"></i> ${title}</h3>
        <span onclick="openSearch()"><i class="fa fa-search"></i> Quick Search</span>
      </div>
      ${filterBar}
      <div class="prod-grid">
        ${items.map(productCardHTML).join("")}
      </div>
    </section>`;
}

function renderReviewsSection(){
  const cards = state.reviews.map(r=>`
    <div class="rev-item">
      <p>"${r.text}"</p>
      <div class="rev-foot"><span>— ${r.name}</span><span>${r.location || 'Verified Buyer'}</span></div>
    </div>`).join("");

  return `
    <section class="panel-card">
      <h3><i class="fa fa-star" style="color:#f59e0b"></i> Customer Reviews</h3>
      <div class="review-grid">${cards}</div>
      <hr style="border:none;border-top:1px solid #e2e8f0;margin:16px 0">
      <h4 style="font-size:14px;font-weight:900">Write a Customer Review</h4>
      <input type="text" id="revNameInput" class="form-control" placeholder="Your Name (e.g. Alistair Reid)">
      <input type="text" id="revLocInput" class="form-control" placeholder="City / Region (optional)">
      <textarea id="revTextInput" rows="3" class="form-control" placeholder="Share your experience with Global Chemical Solution..."></textarea>
      <button class="primary-btn" onclick="submitReview()">Submit Review</button>
    </section>`;
}

function renderComplianceSection(){
  return `
    <section class="panel-card">
      <h3><i class="fa fa-shield-halved" style="color:var(--primary)"></i> GBL Law Regulations &amp; Compliance</h3>
      <p>Global Chemical Solution supplies industrial and technical chemicals with clear product specifications, CAS/HS references, and shipping support from Inverness, United Kingdom.</p>
      <ul>
        <li><strong>GBL Law Regulations:</strong> Intended for commercial, industrial, and authorized technical applications subject to applicable regional laws.</li>
        <li><strong>Compliance:</strong> Order verification, packaging integrity, and safety documentation assistance via <code>Bestgbonine.uk@gmail.com</code>.</li>
        <li><strong>Privacy &amp; Terms:</strong> Transparent handling of customer inquiry and delivery records.</li>
      </ul>
    </section>`;
}

function renderContactSection(){
  return `
    <section class="panel-card">
      <h3><i class="fa fa-headset" style="color:var(--primary)"></i> Contact Global Chemical Solution</h3>
      <p><strong>Company:</strong> Global Chemical Solution (GBL)</p>
      <p><strong>Address:</strong> 22 Parks Vw Rd, Inverness IV2 6JJ, United Kingdom</p>
      <p><strong>Email:</strong> Bestgbonine.uk@gmail.com</p>
      <p><strong>WhatsApp:</strong> +447983259218</p>
      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:12px">
        <button class="primary-btn" style="background:#16a34a" onclick="openWhatsAppDirect()"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</button>
        <a class="primary-btn" style="text-decoration:none;display:inline-flex;align-items:center;gap:6px" href="mailto:Bestgbonine.uk@gmail.com"><i class="fa fa-envelope"></i> Send Email</a>
      </div>
    </section>`;
}

function renderPage(){
  const container = document.getElementById("pageContainer");
  if(state.page === "home"){
    const filtered = state.catFilter === "all"
      ? CATALOG
      : CATALOG.filter(p=>p.category === state.catFilter);
    container.innerHTML =
      renderCatalogSection(`Complete Chemical Catalog (${filtered.length} Items)`, filtered, true) +
      renderReviewsSection();
  } else if(state.page === "gbl"){
    const items = CATALOG.filter(p=>p.category === "gbl");
    container.innerHTML = renderCatalogSection("GBL Solvents & Gamma-Butyrolactone", items, false);
  } else if(state.page === "bdo"){
    const items = CATALOG.filter(p=>p.category === "bdo" || p.category === "gel");
    container.innerHTML = renderCatalogSection("1.4 Butanediol (BDO) & Multi Gel Removers", items, false);
  } else if(state.page === "industrial"){
    const items = CATALOG.filter(p=>p.category === "industrial" || p.priceNum >= 1000);
    container.innerHTML = renderCatalogSection("Bulk Drums, Technical Grade & Petrolatum", items, false);
  } else if(state.page === "compliance"){
    container.innerHTML = renderComplianceSection();
  } else if(state.page === "reviews"){
    container.innerHTML = renderReviewsSection();
  } else if(state.page === "contact"){
    container.innerHTML = renderContactSection();
  }
}

function submitReview(){
  const name = document.getElementById("revNameInput").value.trim();
  const loc = document.getElementById("revLocInput").value.trim();
  const text = document.getElementById("revTextInput").value.trim();
  if(!name || text.length < 3){
    showToast("Please enter your name and review");
    return;
  }
  state.reviews.unshift({ name, location: loc || "Customer", text });
  showToast("Review published!");
  renderPage();
}

function openDeliveryModal(){
  document.getElementById("deliveryModal").classList.add("active");
  document.getElementById("overlay").classList.add("active");
}
function setDeliveryAddr(addr){
  state.address = addr;
  document.getElementById("deliveryAddressText").innerText = addr;
  updateCartUI();
  closeAllOverlays();
  showToast("Delivery address updated");
}
function saveCustomAddress(){
  const val = document.getElementById("customAddrInput").value.trim();
  if(val.length < 3){ showToast("Enter a valid address"); return; }
  setDeliveryAddr(val);
  document.getElementById("customAddrInput").value = "";
}

function openDocModal(key){
  const doc = DOCS[key];
  if(!doc) return;
  document.getElementById("docModalTitle").innerText = doc.title;
  document.getElementById("docModalBody").innerHTML = doc.html;
  document.getElementById("docModal").classList.add("active");
  document.getElementById("overlay").classList.add("active");
}

function openCart(){
  updateCartUI();
  document.getElementById("cartDrawer").classList.add("active");
  document.getElementById("overlay").classList.add("active");
}
function closeCart(){
  document.getElementById("cartDrawer").classList.remove("active");
  document.getElementById("overlay").classList.remove("active");
}

function openSearch(){
  document.getElementById("searchDrawer").classList.add("active");
  document.getElementById("overlay").classList.add("active");
  setTimeout(()=>document.getElementById("searchInput").focus(), 100);
}
function closeSearch(){
  document.getElementById("searchDrawer").classList.remove("active");
  document.getElementById("overlay").classList.remove("active");
}
function runSearch(){
  const q = document.getElementById("searchInput").value.trim().toLowerCase();
  const box = document.getElementById("searchResults");
  if(!q){ box.innerHTML = ""; return; }
  const matches = CATALOG.filter(p=>
    p.name.toLowerCase().includes(q) ||
    p.pack.toLowerCase().includes(q) ||
    p.cas.toLowerCase().includes(q) ||
    p.category.toLowerCase().includes(q)
  );
  if(!matches.length){
    box.innerHTML = `<p style="text-align:center;color:#64748b;padding:20px;font-size:12px">No matching chemical products found.</p>`;
    return;
  }
  box.innerHTML = `<div class="prod-grid" style="margin:0">${matches.map(productCardHTML).join("")}</div>`;
}

function closeAllOverlays(){
  document.getElementById("overlay").classList.remove("active");
  document.getElementById("cartDrawer").classList.remove("active");
  document.getElementById("searchDrawer").classList.remove("active");
  document.querySelectorAll(".modal-bg").forEach(m=>m.classList.remove("active"));
}

function openWhatsAppDirect(){
  const msg = encodeURIComponent("Hello Global Chemical Solution, I would like assistance with a chemical order.");
  window.open("https://wa.me/447983259218?text=" + msg, "_blank");
}

function checkoutWhatsApp(){
  const entries = Object.entries(state.cart);
  if(!entries.length){ showToast("Your cart is empty"); return; }
  let subtotal = 0;
  let lines = ["Hello Global Chemical Solution (GBL),", "New Order Request:", ""];
  entries.forEach(([id, qty])=>{
    const p = CATALOG.find(x=>x.id===id);
    if(!p) return;
    const line = p.priceNum * qty;
    subtotal += line;
    lines.push(`• ${p.name} (${p.pack}) x${qty} = €${line.toFixed(2)}`);
  });
  lines.push("");
  lines.push(`Subtotal: €${subtotal.toFixed(2)}`);
  lines.push(`Delivery Address: ${state.address}`);
  lines.push("Contact Email: Bestgbonine.uk@gmail.com");
  window.open("https://wa.me/447983259218?text=" + encodeURIComponent(lines.join("\n")), "_blank");
}

// Countdown timer next to spinning GBL logo & Flash Deal bar
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
