# ERIFY™ Brand Assets Guide

## Visual Identity Assets

### Primary Logo Assets

#### Supreme 4PW Crown Seal (Main Logo)
```
/dist/crest-supreme4-full.png    - Full brand representation (high-res)
/dist/crest-supreme4.png         - Standard usage version
/dist/crest-supreme4.webp        - Web-optimized format
/src/svg/crest-supreme4.svg      - Scalable vector format
```

**Usage Guidelines:**
- Primary logo for all official communications
- Minimum size: 120px width
- Clear space: 2x logo height on all sides
- Background: Dark themes preferred (#0A0B0C base)

#### Neon Crown Series (Campaign Assets)
```
/dist/neon-goallin.png          - "Total commitment" campaign
/dist/neon-elitehust.png        - "Relentless drive" campaign  
/dist/neon-ego.png              - "DC ERIFY THE GREAT" campaign
/dist/neon-eggo.png             - "ERIFY • GERIZO • ORIGIN" campaign
```

**Campaign Applications:**
- **GOALLIN**: Achievement-focused messaging and goal-oriented campaigns
- **ELITEHUST**: Motivation campaigns, drive and perseverance themes
- **EGO**: Premium leadership positioning, executive communications
- **EGGO**: Heritage branding, foundation and origin storytelling

### Favicon and Icons
```
/src/pages/favicon.svg          - Website favicon (scalable)
```

## Color Specifications

### Primary Brand Palette
```css
/* Core ERIFY™ Colors */
--erify-primary: #11C9FF;       /* Electric Blue - Innovation & Technology */
--erify-luxury: #FFD700;        /* Premium Gold - Luxury & Excellence */
--erify-energy: #FF6B35;        /* Energy Orange - Passion & Drive */
--erify-foundation: #0A0B0C;    /* Deep Space - Stability & Foundation */
--erify-clarity: #EEF2F6;       /* Pearl White - Clarity & Precision */
```

### Extended Color System
```css
/* Blue Variations */
--erify-blue-light: #66D9FF;    /* Light Blue - Accessibility */
--erify-blue-medium: #11C9FF;   /* Primary Blue - Brand */
--erify-blue-dark: #0099CC;     /* Dark Blue - Depth */

/* Gold Variations */
--erify-gold-light: #FFE55C;    /* Light Gold - Highlights */
--erify-gold-medium: #FFD700;   /* Primary Gold - Luxury */
--erify-gold-dark: #B8860B;     /* Dark Gold - Elegance */

/* Gray Scale */
--erify-gray-lightest: #EEF2F6; /* Pearl White */
--erify-gray-light: #AAB6C2;    /* Light Gray - Subtlety */
--erify-gray-medium: #4A5568;   /* Medium Gray - Supporting */
--erify-gray-dark: #0A0B0C;     /* Deep Space - Foundation */
```

### Color Usage Matrix
| Color | Primary Use | Secondary Use | Avoid |
|-------|-------------|---------------|-------|
| Electric Blue (#11C9FF) | CTAs, Links, Active States | Brand Emphasis | Large Text Areas |
| Premium Gold (#FFD700) | VIP Features, Highlights | Premium Content | Backgrounds |
| Energy Orange (#FF6B35) | Notifications, Alerts | Engagement Indicators | Body Text |
| Deep Space (#0A0B0C) | Backgrounds, Containers | Primary Text Areas | Small Text |
| Pearl White (#EEF2F6) | Primary Text, Icons | Contrasting Elements | Dark Backgrounds |

## Typography System

### Primary Typeface: Inter
```css
font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
```

**Characteristics:**
- Modern, clean, highly legible
- Excellent cross-platform consistency
- Optimal for both display and text
- Professional fintech appearance

### Typography Scale
```css
/* Display Typography */
.erify-display-xl {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.erify-display-lg {
  font-size: clamp(28px, 3.8vw, 44px);
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.01em;
}

/* Heading Typography */
.erify-heading-xl {
  font-size: clamp(24px, 3.2vw, 36px);
  font-weight: 700;
  line-height: 1.3;
}

.erify-heading-lg {
  font-size: clamp(20px, 2.6vw, 28px);
  font-weight: 600;
  line-height: 1.4;
}

.erify-heading-md {
  font-size: clamp(18px, 2.2vw, 24px);
  font-weight: 600;
  line-height: 1.4;
}

/* Body Typography */
.erify-body-lg {
  font-size: clamp(16px, 1.8vw, 20px);
  font-weight: 400;
  line-height: 1.6;
}

.erify-body-md {
  font-size: clamp(14px, 1.7vw, 18px);
  font-weight: 400;
  line-height: 1.6;
}

.erify-body-sm {
  font-size: clamp(12px, 1.4vw, 14px);
  font-weight: 400;
  line-height: 1.5;
}
```

### Font Weight Guidelines
- **900 (Black)**: Hero headlines, brand statements
- **800 (Extra Bold)**: Major section headers
- **700 (Bold)**: Buttons, CTAs, emphasis
- **600 (Semi Bold)**: Subheadings, navigation
- **400 (Regular)**: Body text, content
- **300 (Light)**: Supporting text, metadata

## Component Library

### Button Components

#### Primary Button
```css
.btn-primary {
  background: linear-gradient(135deg, 
    rgba(17, 201, 255, 0.1), 
    rgba(17, 201, 255, 0.2)
  );
  border: 1px solid rgba(17, 201, 255, 0.4);
  color: #EEF2F6;
  padding: 12px 24px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 16px;
  transition: all 0.2s ease;
  backdrop-filter: blur(10px);
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 25px rgba(17, 201, 255, 0.25);
  border-color: rgba(17, 201, 255, 0.6);
  background: linear-gradient(135deg, 
    rgba(17, 201, 255, 0.15), 
    rgba(17, 201, 255, 0.25)
  );
}
```

#### VIP Button
```css
.btn-vip {
  background: linear-gradient(135deg, 
    rgba(255, 215, 0, 0.1), 
    rgba(255, 215, 0, 0.2)
  );
  border: 1px solid rgba(255, 215, 0, 0.4);
  color: #EEF2F6;
  /* Inherit structure from .btn-primary */
}

.btn-vip:hover {
  box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25);
  border-color: rgba(255, 215, 0, 0.6);
}
```

### Card Components

#### Premium Card
```css
.card-premium {
  background: linear-gradient(180deg, 
    rgba(20, 22, 24, 0.95), 
    rgba(20, 22, 24, 0.8)
  );
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 24px;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.card-premium:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.16);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(17, 201, 255, 0.1);
}
```

#### VIP Card
```css
.card-vip {
  background: linear-gradient(180deg, 
    rgba(20, 22, 24, 0.95), 
    rgba(20, 22, 24, 0.8)
  );
  border: 1px solid rgba(255, 215, 0, 0.2);
  border-radius: 16px;
  padding: 24px;
  position: relative;
  overflow: hidden;
}

.card-vip::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 215, 0, 0.8), 
    transparent
  );
}
```

### Glow Effects System

#### Primary Glow
```css
.glow-primary {
  box-shadow: 0 0 20px rgba(17, 201, 255, 0.3);
}

.glow-primary-intense {
  box-shadow: 
    0 0 20px rgba(17, 201, 255, 0.4),
    0 0 40px rgba(17, 201, 255, 0.2),
    0 0 60px rgba(17, 201, 255, 0.1);
}
```

#### VIP Glow
```css
.glow-vip {
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
}

.glow-vip-intense {
  box-shadow: 
    0 0 20px rgba(255, 215, 0, 0.4),
    0 0 40px rgba(255, 215, 0, 0.2),
    0 0 60px rgba(255, 215, 0, 0.1);
}
```

## Layout System

### Spacing Scale
```css
/* ERIFY™ Spacing System */
:root {
  --space-1: 4px;     /* Micro spacing */
  --space-2: 8px;     /* Small spacing */
  --space-3: 12px;    /* Medium spacing */
  --space-4: 16px;    /* Standard spacing */
  --space-5: 20px;    /* Large spacing */
  --space-6: 24px;    /* Extra large spacing */
  --space-8: 32px;    /* Section spacing */
  --space-10: 40px;   /* Major sections */
  --space-12: 48px;   /* Page sections */
  --space-16: 64px;   /* Hero sections */
}
```

### Grid System
```css
.grid-container {
  display: grid;
  gap: var(--space-6);
  padding: var(--space-6);
  max-width: 1200px;
  margin: 0 auto;
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

.grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

/* Responsive Grid */
@media (max-width: 768px) {
  .grid-2,
  .grid-3,
  .grid-4 {
    grid-template-columns: 1fr;
  }
}
```

### Responsive Breakpoints
```css
/* Mobile First Approach */
:root {
  --breakpoint-sm: 640px;   /* Small devices */
  --breakpoint-md: 768px;   /* Medium devices */
  --breakpoint-lg: 1024px;  /* Large devices */
  --breakpoint-xl: 1280px;  /* Extra large devices */
  --breakpoint-2xl: 1536px; /* 2X Extra large devices */
}
```

## Asset Implementation

### HTML Implementation
```html
<!-- Primary Logo -->
<img src="/dist/crest-supreme4-full.png" 
     alt="ERIFY™ Supreme 4PW Crown Seal" 
     class="erify-logo-primary" />

<!-- Responsive Logo -->
<picture class="erify-logo-responsive">
  <source media="(min-width: 768px)" 
          srcset="/dist/crest-supreme4-full.webp">
  <source media="(max-width: 767px)" 
          srcset="/dist/crest-supreme4.webp">
  <img src="/dist/crest-supreme4.png" 
       alt="ERIFY™ Crown Seal">
</picture>

<!-- Neon Crown Series -->
<img src="/dist/neon-goallin.png" 
     alt="GOALLIN - Total commitment" 
     class="neon-crown-asset" />
```

### CSS Implementation
```css
/* Logo Sizing */
.erify-logo-primary {
  width: min(300px, 90vw);
  height: auto;
  display: block;
}

.erify-logo-compact {
  width: min(200px, 60vw);
  height: auto;
}

/* Neon Crown Assets */
.neon-crown-asset {
  width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.neon-crown-asset:hover {
  transform: scale(1.02);
  box-shadow: 0 10px 30px rgba(17, 201, 255, 0.2);
}
```

## Quality Standards

### Image Specifications
- **Resolution**: 300 DPI minimum for print, 72-144 DPI for web
- **Format**: PNG (transparency), WebP (web optimization), SVG (scalability)
- **Compression**: Balanced quality/file size optimization
- **Color Space**: sRGB for web, CMYK for print

### File Naming Convention
```
erify-[component]-[variant]-[size].[extension]

Examples:
- erify-logo-primary-large.svg
- erify-crest-supreme4-full.png
- erify-neon-goallin-banner.webp
- erify-icon-crown-small.svg
```

### Version Control
- **Source Files**: Maintain original design files (AI, PSD, Sketch)
- **Export Settings**: Document export parameters for consistency
- **Asset Registry**: Catalog all assets with usage guidelines
- **Update Process**: Version new assets and deprecate old ones

---

*Comprehensive brand assets guide for the ERIFY™ luxury fintech ecosystem*

**© 2025 ERIFY™. All rights reserved.**