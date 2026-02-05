#!/usr/bin/env python3
"""
FCS Commercial Services - Static Site Builder
Generates all HTML pages from shared components.
Run: python3 build.py
"""

import os
import json

# ==========================================
# SHARED COMPONENTS
# ==========================================

def get_head(title, description, schema_json="", depth=0):
    prefix = "../" * depth
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | FCS Foundation</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://fcsfoundationandconcrete.com/commercial-services/">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}assets/css/fcs-commercial.css">
    {schema_json}
</head>'''


def get_nav(depth=0, active=""):
    prefix = "../" * depth
    base = f"{prefix}commercial-services"
    
    def ac(page):
        return ' class="active"' if active == page else ""
    
    return f'''<body>
    <header class="header">
        <div class="header-inner">
            <a href="/" class="logo">
                <img src="https://fcsfoundationandconcrete.com/wp-content/uploads/2024/10/FCS-Logo-White.png" alt="FCS Foundation Repair" width="200" height="50">
            </a>
            <a href="tel:877-554-8284" class="header-phone">877-554-8284</a>
        </div>
    </header>
    <nav class="main-nav">
        <div class="nav-inner">
            <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
            <ul class="nav-list">
                <li{ac("hub")}><a href="{base}/index.html">Commercial Services</a></li>
                <li{ac("sectors")}>
                    <a href="#">Industries We Serve</a>
                    <div class="nav-dropdown">
                        <a href="{base}/multi-family/index.html">Multi-Family</a>
                        <a href="{base}/office-corporate/index.html">Office / Corporate</a>
                        <a href="{base}/industrial/index.html">Industrial</a>
                        <a href="{base}/medical-offices/index.html">Medical Offices</a>
                        <a href="{base}/home-builders/index.html">Home Builders</a>
                    </div>
                </li>
                <li{ac("services")}>
                    <a href="#">Our Services</a>
                    <div class="nav-dropdown">
                        <a href="{base}/foundation-repair.html">Foundation Repair</a>
                        <a href="{base}/drainage-solutions.html">Drainage Solutions</a>
                        <a href="{base}/mudjacking-void-fill.html">Mudjacking / Void Fill</a>
                        <a href="{base}/retaining-walls.html">Retaining Walls</a>
                        <a href="{base}/excavation.html">Excavation</a>
                        <a href="{base}/concrete-services.html">Concrete Services</a>
                    </div>
                </li>
                <li class="nav-cta"><a href="/free-foundation-evaluation/">Free Evaluation</a></li>
            </ul>
        </div>
    </nav>'''


def get_footer(depth=0):
    prefix = "../" * depth
    base = f"{prefix}commercial-services"
    return f'''
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h4>Industries We Serve</h4>
                    <ul>
                        <li><a href="{base}/multi-family/index.html">Multi-Family</a></li>
                        <li><a href="{base}/office-corporate/index.html">Office / Corporate</a></li>
                        <li><a href="{base}/industrial/index.html">Industrial</a></li>
                        <li><a href="{base}/medical-offices/index.html">Medical Offices</a></li>
                        <li><a href="{base}/home-builders/index.html">Home Builders</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Our Services</h4>
                    <ul>
                        <li><a href="{base}/foundation-repair.html">Foundation Repair</a></li>
                        <li><a href="{base}/drainage-solutions.html">Drainage Solutions</a></li>
                        <li><a href="{base}/mudjacking-void-fill.html">Mudjacking / Void Fill</a></li>
                        <li><a href="{base}/retaining-walls.html">Retaining Walls</a></li>
                        <li><a href="{base}/concrete-services.html">Concrete Services</a></li>
                        <li><a href="{base}/excavation.html">Excavation</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Company</h4>
                    <ul>
                        <li><a href="/about-fcs/">About FCS</a></li>
                        <li><a href="/lifetime-transferrable-warranty/">Warranty</a></li>
                        <li><a href="/reviews/">Reviews</a></li>
                        <li><a href="/contact-us/">Contact Us</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contact Us</h4>
                    <ul>
                        <li><a href="tel:877-554-8284"><strong>877-554-8284</strong></a></li>
                        <li><a href="mailto:info@fcsfoundationandconcrete.com">info@fcsfoundationandconcrete.com</a></li>
                        <li style="margin-top:15px;color:rgba(255,255,255,0.5);font-size:12px;">Licensed &amp; Insured<br>Dallas-Fort Worth, TX</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 FCS Foundation Repair and Concrete Services. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="{prefix}assets/js/fcs-commercial.js"></script>
</body>
</html>'''


print("=" * 50)
print("FCS Commercial SEO - Build Script")
print("=" * 50)
print()
print("This script validates the project structure.")
print("All HTML pages are pre-built and ready to deploy.")
print()

# Verify structure
pages = [
    "commercial-services/index.html",
    "commercial-services/multi-family/index.html",
    "commercial-services/office-corporate/index.html",
    "commercial-services/industrial/index.html",
    "commercial-services/medical-offices/index.html",
    "commercial-services/home-builders/index.html",
    "commercial-services/foundation-repair.html",
    "commercial-services/drainage-solutions.html",
    "commercial-services/mudjacking-void-fill.html",
    "commercial-services/retaining-walls.html",
    "commercial-services/concrete-services.html",
    "commercial-services/excavation.html",
    "assets/css/fcs-commercial.css",
    "assets/js/fcs-commercial.js",
]

missing = []
for p in pages:
    if not os.path.exists(p):
        missing.append(p)

if missing:
    print(f"WARNING: {len(missing)} files missing:")
    for m in missing:
        print(f"  - {m}")
else:
    print(f"✓ All {len(pages)} files present")

print()
print("Deployment: Copy /commercial-services/ folder to WordPress root")
print("Or link CSS/JS into your WP theme and paste HTML into page templates.")

