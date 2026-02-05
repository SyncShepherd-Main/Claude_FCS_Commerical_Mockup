# Claude Code Instructions

## Project: FCS Commercial Services SEO Pages

This is a static HTML site for FCS Foundation Repair's commercial services section.

### Repository Setup
```bash
git init
git add .
git commit -m "Initial commit: FCS Commercial SEO pages - hub, 5 sectors, 6 services"
gh repo create fcs-commercial-seo --public --source=. --push
```

### Quick Deploy to GitHub Pages
```bash
# After pushing to GitHub:
# Settings > Pages > Source: Deploy from branch > main > / (root)
```

### Project Structure
- `commercial-services/` - All HTML pages
- `assets/css/` - Shared stylesheet
- `assets/js/` - Shared JavaScript
- `docs/` - SEO strategy documents
- `build.py` - Build validation script

### Key Notes
- All pages use relative paths for navigation
- CSS variables defined in `:root` of fcs-commercial.css
- FAQ sections use FAQ schema markup
- Sector pages have inline styles (self-contained) - migration to shared CSS is in progress
- Service pages already use the shared stylesheet

### WordPress Integration
When moving to WordPress:
1. Each HTML file maps to a WordPress page
2. The CSS should be enqueued in the theme
3. Navigation should be replaced with WP nav menus
4. FAQ sections can use ACF repeater fields
5. Schema markup should be preserved
