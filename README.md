# FCS Commercial Services - SEO Landing Pages

Production-ready HTML mockups for the commercial services section of [fcsfoundationandconcrete.com](https://fcsfoundationandconcrete.com).

## Project Overview

This repository contains a complete set of SEO-optimized landing pages for FCS Foundation & Concrete Services' commercial division. The pages follow a hub-and-spoke content architecture designed to capture commercial foundation repair search traffic in the Dallas-Fort Worth market.

## Site Architecture

```
commercial-services/
├── index.html                    ← Main hub page
│
├── SECTOR PAGES (5 industries)
│   ├── multi-family/index.html   ← Apartments, condos, townhomes
│   ├── office-corporate/index.html ← Office buildings, campuses
│   ├── industrial/index.html     ← Warehouses, distribution, manufacturing
│   ├── medical-offices/index.html ← Clinics, MOBs, dental, rehab
│   └── home-builders/index.html  ← Production, custom, developers
│
├── SERVICE PAGES (6 core services)
│   ├── foundation-repair.html
│   ├── drainage-solutions.html
│   ├── mudjacking-void-fill.html
│   ├── retaining-walls.html
│   ├── concrete-services.html
│   └── excavation.html
│
└── assets/
    ├── css/fcs-commercial.css    ← Shared stylesheet
    └── js/fcs-commercial.js      ← Shared JavaScript (FAQ, nav)
```

## Pages Included

### Phase 1: Hub + Sector Pages (12 pages)
| Page | URL | Target Keywords |
|------|-----|-----------------|
| Commercial Hub | `/commercial-services/` | commercial foundation repair Dallas |
| Multi-Family | `/commercial-services/multi-family/` | apartment foundation repair Dallas |
| Office/Corporate | `/commercial-services/office-corporate/` | office building foundation repair |
| Industrial | `/commercial-services/industrial/` | warehouse foundation repair Dallas |
| Medical Offices | `/commercial-services/medical-offices/` | medical building foundation repair |
| Home Builders | `/commercial-services/home-builders/` | builder foundation services Dallas |

### Phase 2: Core Service Pages (6 pages)
| Page | URL | Target Keywords |
|------|-----|-----------------|
| Foundation Repair | `/commercial-services/foundation-repair/` | commercial foundation repair |
| Drainage Solutions | `/commercial-services/drainage-solutions/` | commercial drainage Dallas |
| Mudjacking/Void Fill | `/commercial-services/mudjacking-void-fill/` | commercial mudjacking |
| Retaining Walls | `/commercial-services/retaining-walls/` | commercial retaining walls |
| Concrete Services | `/commercial-services/concrete-services/` | commercial concrete Dallas |
| Excavation | `/commercial-services/excavation/` | commercial excavation |

## Technical Features

- **Shared CSS/JS**: All pages use `assets/css/fcs-commercial.css` and `assets/js/fcs-commercial.js`
- **Working Navigation**: Dropdown mega-nav with links between all pages
- **Responsive Design**: Mobile-first with breakpoints at 480, 550, 600, 700, 900, and 1000px
- **Schema Markup**: FAQ schema on all pages, LocalBusiness + Service on sector pages
- **FAQ Accordions**: JavaScript-powered FAQ sections with schema
- **FCS Brand System**: Orange (#f7941d), Blue Dark (#1a2b47), Montserrat + Open Sans
- **Breadcrumb Navigation**: Full breadcrumb trail on all sub-pages
- **Internal Linking**: Hub → Sector → Service cross-linking structure

## Deployment Options

### Option A: Static HTML (Recommended for Review)
Open any `index.html` in a browser. Navigation uses relative paths.

### Option B: WordPress Integration
1. Create pages in WordPress matching the URL structure
2. Copy HTML content into each page template
3. Enqueue `fcs-commercial.css` in your theme
4. Add `fcs-commercial.js` to your theme's scripts

### Option C: WordPress Plugin / Custom Post Type
Create a custom page template that loads the shared CSS/JS and uses the HTML as content blocks.

## Brand Design Tokens

```css
--fcs-orange: #f7941d
--fcs-orange-dark: #e07d0a
--fcs-blue-dark: #1a2b47
--fcs-blue-medium: #2c4a6e
--font-heading: 'Montserrat'
--font-body: 'Open Sans'
```

## Future Phases

- **Phase 3**: 25 sector-service intersection pages (e.g., `/multi-family/foundation-repair/`)
- **Phase 4**: GPR services, multi-family sub-type pages, individual case studies

## SEO Strategy Documents

See `/docs/` folder for:
- `SITE-ARCHITECTURE.md` - Full URL structure and keyword mapping
- `FCS-Foundation-SEO-Audit-Report.md` - Technical SEO audit
- `FCS-Competitive-Analysis-Report.md` - Competitive landscape analysis

---

Built for **FCS Foundation Repair and Concrete Services** | Dallas-Fort Worth, TX | 877-554-8284
