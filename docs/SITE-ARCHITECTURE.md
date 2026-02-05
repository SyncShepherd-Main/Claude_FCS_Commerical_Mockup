# FCS Commercial Services - Revised Site Architecture
## Based on Client Requirements - February 2026

---

## OVERVIEW

The client has provided a clear hierarchical structure for their commercial services that differs from the competitor-based approach. Their structure is organized by:

1. **Sectors/Industries Served** (who they serve)
2. **Core Service Offerings** (what they do)
3. **Sub-categories within each sector** (specific property types)

This is a more logical B2B approach that speaks directly to property managers and commercial decision-makers.

---

## PROPOSED URL STRUCTURE

```
/commercial-services/                          [MAIN HUB PAGE]
│
├── SECTORS (Industry Pages)
│   ├── /commercial-services/multi-family/
│   │   ├── /commercial-services/multi-family/foundation-repair/
│   │   ├── /commercial-services/multi-family/drainage-solutions/
│   │   ├── /commercial-services/multi-family/retaining-walls/
│   │   ├── /commercial-services/multi-family/concrete-services/
│   │   └── /commercial-services/multi-family/excavation/
│   │
│   ├── /commercial-services/office-corporate/
│   │   ├── /commercial-services/office-corporate/foundation-repair/
│   │   ├── /commercial-services/office-corporate/drainage-solutions/
│   │   ├── /commercial-services/office-corporate/retaining-walls/
│   │   ├── /commercial-services/office-corporate/concrete-services/
│   │   └── /commercial-services/office-corporate/excavation/
│   │
│   ├── /commercial-services/industrial/
│   │   ├── /commercial-services/industrial/foundation-repair/
│   │   ├── /commercial-services/industrial/drainage-solutions/
│   │   ├── /commercial-services/industrial/retaining-walls/
│   │   ├── /commercial-services/industrial/concrete-services/
│   │   └── /commercial-services/industrial/excavation/
│   │
│   ├── /commercial-services/medical-offices/
│   │   ├── /commercial-services/medical-offices/foundation-repair/
│   │   ├── /commercial-services/medical-offices/drainage-solutions/
│   │   ├── /commercial-services/medical-offices/retaining-walls/
│   │   ├── /commercial-services/medical-offices/concrete-services/
│   │   └── /commercial-services/medical-offices/excavation/
│   │
│   └── /commercial-services/home-builders/
│       ├── /commercial-services/home-builders/foundation-repair/
│       ├── /commercial-services/home-builders/drainage-solutions/
│       ├── /commercial-services/home-builders/retaining-walls/
│       ├── /commercial-services/home-builders/concrete-services/
│       └── /commercial-services/home-builders/excavation/
│
└── SERVICES (Core Offering Pages)
    ├── /commercial-services/foundation-evaluations/
    ├── /commercial-services/foundation-repair/
    ├── /commercial-services/mudjacking-void-fill/
    ├── /commercial-services/retaining-walls/
    ├── /commercial-services/excavation/
    ├── /commercial-services/drainage-solutions/
    ├── /commercial-services/concrete-services/
    └── /commercial-services/gpr-services/        [Optional]
```

---

## MULTI-FAMILY SUB-CATEGORIES

The Multi-Family sector page should address these specific property types:

- Apartment Communities
- Townhome Communities  
- Condominium Complexes
- Student Housing
- Senior Living Facilities
- Affordable Housing (HUD / LIHTC)
- Duplexes & Fourplexes

These can be addressed on the main Multi-Family page with dedicated sections, or broken into sub-pages later if content depth warrants it.

---

## PAGE HIERARCHY & PRIORITY

### PHASE 1: Essential Pages (Weeks 1-3)
1. **Commercial Services Main Hub** - /commercial-services/
2. **Multi-Family** - /commercial-services/multi-family/
3. **Office/Corporate** - /commercial-services/office-corporate/
4. **Industrial** - /commercial-services/industrial/
5. **Medical Offices** - /commercial-services/medical-offices/
6. **Home Builders** - /commercial-services/home-builders/

### PHASE 2: Core Service Pages (Weeks 4-6)
7. **Commercial Foundation Repair** - /commercial-services/foundation-repair/
8. **Commercial Drainage Solutions** - /commercial-services/drainage-solutions/
9. **Mudjacking/Void Fill** - /commercial-services/mudjacking-void-fill/
10. **Retaining Walls** - /commercial-services/retaining-walls/
11. **Commercial Concrete Services** - /commercial-services/concrete-services/
12. **Excavation Services** - /commercial-services/excavation/

### PHASE 3: Sector-Service Combinations (Weeks 7-12)
Create the intersection pages (e.g., /multi-family/foundation-repair/) 
- 5 sectors × 5 services = 25 pages
- These can be templated for efficiency

### PHASE 4: Optional/Future
- GPR Services page
- Individual multi-family sub-type pages
- Case study pages per sector

---

## NAVIGATION STRUCTURE

```
Commercial Services (Main Nav Item)
├── Overview
├── Industries We Serve
│   ├── Multi-Family
│   ├── Office / Corporate
│   ├── Industrial
│   ├── Medical Offices
│   └── Home Builders
├── Our Services
│   ├── Foundation Evaluations
│   ├── Foundation Repair
│   ├── Mudjacking / Void Fill
│   ├── Retaining Walls
│   ├── Excavation
│   ├── Drainage Solutions
│   └── Concrete Services
└── Request Commercial Estimate
```

---

## TARGET KEYWORDS BY PAGE

### Main Hub Page
- commercial foundation repair Dallas
- commercial concrete services Dallas
- commercial foundation company DFW

### Multi-Family Page
- apartment foundation repair Dallas
- multifamily foundation repair
- apartment complex foundation problems
- HOA foundation repair Dallas

### Office/Corporate Page
- office building foundation repair Dallas
- commercial building foundation repair
- corporate facility foundation services

### Industrial Page
- warehouse foundation repair Dallas
- industrial foundation repair
- manufacturing plant foundation repair

### Medical Offices Page
- medical building foundation repair
- healthcare facility foundation services
- clinic foundation repair Dallas

### Home Builders Page
- builder foundation services Dallas
- new construction foundation repair
- home builder foundation contractor DFW

---

## CONTENT REQUIREMENTS PER PAGE TYPE

### Main Hub Page (2,500-3,000 words)
- Hero with commercial-focused messaging
- Sectors grid with links to each industry page
- Services overview with links to service pages
- Why choose FCS for commercial (differentiators)
- Commercial process overview
- Trust signals (insurance, bonding, warranty)
- Case studies teaser
- FAQ section (8-10 questions)
- Service areas
- Contact/CTA

### Sector Pages (1,500-2,000 words each)
- Hero specific to that industry
- Industry-specific challenges and pain points
- Services offered for that sector
- Sub-categories/property types within sector
- Why FCS for this industry
- Case study relevant to sector
- FAQ specific to sector (5-7 questions)
- CTA

### Service Pages (1,500-2,000 words each)
- Hero specific to service
- Service explanation and process
- Industries served with this service
- Methods/techniques used
- Benefits and outcomes
- FAQ specific to service
- CTA

### Sector-Service Intersection Pages (800-1,200 words each)
- Combined focus (e.g., "Foundation Repair for Multi-Family Properties")
- Specific challenges for this combination
- Case study if available
- Link back to parent sector and service pages
- CTA

---

## HTML MOCKUPS TO CREATE

1. **commercial-services.html** - Main hub page
2. **multi-family.html** - Multi-family sector page
3. **office-corporate.html** - Office/Corporate sector page  
4. **industrial.html** - Industrial sector page
5. **medical-offices.html** - Medical offices sector page
6. **home-builders.html** - Home builders sector page
7. **commercial-foundation-repair.html** - Foundation repair service page
8. **commercial-drainage.html** - Drainage service page
9. **sector-service-template.html** - Template for intersection pages

---

## NOTES FOR DEVELOPERS

- All pages should use the existing FCS theme/styling
- Mobile responsiveness is critical for property managers on-site
- Include schema markup for LocalBusiness + Service
- FAQ sections should use FAQ schema
- Breadcrumb navigation on all sub-pages
- Internal linking strategy between sectors and services
- Contact forms should have "Commercial" pre-selected or separate commercial forms
