# Project Design Report (PDR)
## what the dog doing - Team Showcase Website

**Version:** 2.0  
**Date:** April 5, 2026  
**Team:** what the dog doing  
**Repository:** https://github.com/NexMaker-Fab/ZWU-2026-2-001  
**Deployment:** https://nexmaker-fab.github.io/ZWU-2026-2-001/

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Team Members](#2-team-members)
3. [Technical Architecture](#3-technical-architecture)
4. [Project Structure](#4-project-structure)
5. [Core Features](#5-core-features)
6. [User Interface Design](#6-user-interface-design)
7. [Data Management](#7-data-management)
8. [Exercise Modules](#8-exercise-modules)
9. [Final Project Module](#9-final-project-module)
10. [Responsive Design](#10-responsive-design)
11. [Performance Optimization](#11-performance-optimization)
12. [Future Enhancements](#12-future-enhancements)

---

## 1. Project Overview

### 1.1 Project Background

The "what the dog doing" team showcase website is a multi-page application (MPA) designed to present our team's identity, members, and course work portfolio. The project name originates from a memorable image that resonates with our team spirit.

### 1.2 Project Objectives

- **Showcase Team Identity**: Present team branding through visual design and interactive elements
- **Member Profiles**: Display detailed information about each team member including roles, skills, and assignments
- **Portfolio Display**: Organize and present 5 exercise projects and final project with rich media content
- **File Management**: Enable upload and management of project files directly in the browser
- **Modern UX**: Deliver Apple-inspired user experience with smooth animations and intuitive navigation

### 1.3 Target Audience

- Course instructors and evaluators
- Potential collaborators and employers
- Team members for internal reference
- General visitors interested in our work

---

## 2. Team Members

| Name | Chinese Name | Role | GitHub | Email |
|------|--------------|------|--------|-------|
| Ash | 范洲豪 | Frontend Developer | [@17poi](https://github.com/17poi) | - |
| Felix | 徐克丰 | Hardware Engineer | [@WanShang2026](https://github.com/WanShang2026) | - |
| Howie | 吴浩瑜 | Backend Developer | [@Howie-jbg](https://github.com/Howie-jbg) | - |
| Max | 韩明哲 | Project Manager | [@HMZ766](https://github.com/HMZ766) | - |
| Joe | 张敏强 | UI/UX Designer | [@SONATA360](https://github.com/SONATA360) | - |
| David | 叶骁纬 | Full Stack Developer | [@Excalibuuuuur](https://github.com/Excalibuuuuur) | - |

**Team Slogan:** *"We are a group of passionate and determined heroes, dedicated to paving the way with knives and shields in our hands."*

---

## 3. Technical Architecture

### 3.1 Technology Stack

#### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: 
  - Flexbox & Grid layouts
  - CSS animations and transitions
  - Glassmorphism effects (backdrop-filter)
  - Custom properties (CSS variables)
- **Vanilla JavaScript (ES6+)**:
  - DOM manipulation
  - Event handling
  - LocalStorage API
  - File API (FileReader)
  - Smooth scrolling
  - Intersection Observer API

#### No Build Tools Required
- Pure HTML/CSS/JS implementation
- No framework dependencies (React, Vue, etc.)
- No bundlers (Webpack, Vite)
- Direct file serving via GitHub Pages

### 3.2 Architecture Pattern

**Multi-Page Application (MPA)**

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  index.html │────▶│ about-us.html│────▶│ dailyhomework/   │────▶│ final-project.html│
│  (Home)     │     │ (About Us)   │     │ index.html       │     │ (Final Project)   │
─────────────┘     └──────────────┘     └──────────────────┘     └─────────────────┘
                          │                       │
                          ▼                       ▼
                    Member Detail          Exercise Detail
                    Pages                  Pages (5 exercises)
```

**Key Characteristics:**
- Each page is an independent HTML file
- Navigation via standard `<a>` links
- Shared CSS stylesheet (`assets/css/style.css`)
- Page-specific JavaScript embedded in each HTML file
- Consistent navbar across all pages

### 3.3 Routing Strategy

**Hash-based Navigation (within pages)**

Used for section switching within single pages:
- `#home`, `#intro`, `#members` - About Us page sections
- `#member-0` ~ `#member-5` - Individual member detail views
- `#exercises`, `#exercise-0` ~ `#exercise-4` - Daily Homework sections
- `#project` - Final Project section

**Implementation:**
```javascript
// Section visibility control via CSS classes
.page-section { display: none; }
.page-section.active { display: block; }

// Hash change handler
window.addEventListener('hashchange', handleRoute);
```

---

## 4. Project Structure

```
ZWU-2026-2-001/
├── index.html                      # Home page (Hero section)
├── about-us.html                   # About Us + Team Members
├── final-project.html              # Final Project showcase
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── PDR.md                          # This document
│
├── assets/
│   ├── css/
│   │   └── style.css               # Global styles (1060 lines)
│   │
│   ├── image/
│   │   ├── avatars/                # Team member avatars
│   │   │   ├── Ash.jpg
│   │   │   ├── Felix.jpg
│   │   │   ├── howie-avatar.jpg
│   │   │   ├── Max.jpg
│   │   │   ├── Joe.jpg
│   │   │   ├── Excalibuuuuur.jpg
│   │   │   └── default-avatar.png
│   │   │
│   │   └── eggs/                   # Easter egg / branding
│   │       └── what-the-dog-doing.gif
│   │
│   └── dailyhomework/
│       ├── index.html              # Daily Homework index (1531 lines)
│       │
│       ├── assignment-0/           # Exercise 0: Project Management
│       │   ├── index.html
│       │   └── image/
│       │       ├── 1.png ~ 21.png  # 21 screenshots
│       │
│       ├── assignment-1/           # Exercise 1: Arduino Output&Input
│       │   ├── index.html
│       │   ── image/
│       │       ├── 1.png ~ 30.png  # 30 images + 1 GIF
│       │
│       ├── assignment-2/           # Exercise 2: Arduino Basic
│       │   ├── index.html
│       │   └── image/
│       │       ├── 1.png ~ 10.png  # 9 images + 1 GIF
│       │
│       ├── assignment-3/           # Exercise 3: CAD Design
│       │   ├── index.html
│       │   ── image/
│       │       ├── 1.png, 3.png ~ 9.png  # 8 images
│       │
│       └── assignment-4/           # Exercise 4: 3D Printing
│           ├── index.html
│           └── image/
│               ├── 1.png ~ 15.png  # 14 images + 1 GIF
│
└── (Legacy files - not in use)
    ├── index (1).html              # SPA backup version
    ├── fix_*.py                    # Python scripts for fixes
    ├── rebuild_*.py                # Python scripts for rebuilding
    └── _temp_*.html                # Temporary files
```

### 4.1 File Statistics

| Category | Count | Total Size |
|----------|-------|------------|
| HTML Files | 9 | ~180 KB |
| CSS Files | 1 | 45 KB |
| Avatar Images | 7 | ~500 KB |
| Assignment Images | 82 | ~15 MB |
| GIFs | 3 | ~50 MB |
| **Total** | **102** | **~65 MB** |

---

## 5. Core Features

### 5.1 Animated Gradient Homepage

**Description:** Full-screen hero section with flowing gradient background animation

**Implementation:**
```css
.hero {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientFlow 15s ease infinite;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
```

**Features:**
- 4-color gradient palette
- 15-second infinite loop
- Smooth cubic-bezier easing
- Centered team branding text

### 5.2 Smart Navigation Bar

**Apple-Inspired Frosted Glass Design**

**Visual Properties:**
- Semi-transparent background: `rgba(20, 20, 30, 0.3)`
- Backdrop blur: `blur(30px)`
- Border radius: 16px
- Fixed positioning with center alignment

**Interactive Behaviors:**

#### Auto-Hide on Scroll
```javascript
// Hide when scrolling down > 100px
if (currentScrollY > lastScrollY && currentScrollY > 100) {
    navbar.classList.add('hidden');
} else {
    navbar.classList.remove('hidden');
}
```

**Animation:**
- Transform: `translateY(-150%)`
- Duration: 0.4s
- Easing: `cubic-bezier(0.4, 0, 0.2, 1)`

#### Compact Mode
Automatically activates when viewing exercise details:
- Reduced padding: 0.625rem → 0.875rem
- Smaller border radius: 12px → 16px
- Narrower width for better content focus

### 5.3 Back to Top Button

**Design Specifications:**
- Position: Fixed bottom-right (2rem offset)
- Size: 50px × 50px circular button
- Background: Cyan gradient (#00d4ff → #0099cc)
- Visibility threshold: Scroll > 500px
- Action: Smooth scroll to top

**Hover Effect:**
```css
.back-to-top:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.5);
}
```

### 5.4 Interactive Image Reveal

**Feature:** Toggle button to show/hide team branding GIF

**Implementation:**
```javascript
function toggleImage() {
    const container = document.getElementById('image-container');
    const btn = document.querySelector('.show-image-btn');
    
    if (container.style.display === 'none') {
        container.style.display = 'block';
        btn.textContent = 'Hide Image';
    } else {
        container.style.display = 'none';
        btn.textContent = 'Show Image';
    }
}
```

**Location:** About Us page, bottom section

### 5.5 Member Profile System

**Card Grid Layout:**
- Responsive grid: 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Hover effect: Scale 1.05 + shadow enhancement
- Click action: Navigate to individual member detail page

**Detail Page Content:**
- Large avatar display (200px)
- Bio section (editable)
- Contact email
- Hobbies list
- Assignments completed
- Skills tags

**Data Structure:**
```javascript
const members = [
    {
        id: 0,
        name: 'Ash',
        chineseName: '范洲豪',
        role: 'Frontend Developer',
        github: '@17poi',
        email: 'ash@example.com',
        bio: 'Passionate about creating beautiful web interfaces...',
        hobbies: ['Coding', 'Gaming', 'Photography'],
        assignments: ['Website Development', 'API Integration'],
        avatar: './assets/image/avatars/Ash.jpg'
    },
    // ... 5 more members
];
```

---

## 6. User Interface Design

### 6.1 Design Philosophy

**Apple-Inspired Aesthetic:**
- Minimalist layout with generous whitespace
- Frosted glass effects (glassmorphism)
- Smooth, subtle animations
- High contrast typography
- Rounded corners (border-radius: 12-16px)

**Color Palette:**
- **Primary Background:** #000000 (Pure black)
- **Secondary Background:** #0a0a0f (Near black)
- **Text Primary:** #ffffff (White)
- **Text Secondary:** rgba(255, 255, 255, 0.7)
- **Accent Cyan:** #00d4ff (Links, buttons, highlights)
- **Accent Pink:** #ff00d4 (Subheadings, emphasis)
- **Accent Gold:** #ffd740 (Minor headings)
- **Success Green:** #00ff88 (Notifications)
- **Error Red:** #ff6b6b (Error states)

### 6.2 Typography System

**Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
             'Helvetica Neue', Arial, sans-serif;
```

**Heading Hierarchy:**

| Level | Size | Color | Weight | Usage |
|-------|------|-------|--------|-------|
| H1 | 3.5rem | White | 700 | Page titles |
| H2 | 2.5rem | White | 600 | Section headers |
| H3 | 1.75rem | White | 600 | Subsection headers |
| H4 | 1.5rem | #00e5ff (Cyan) | 600 | Main content sections |
| H5 | 1.25rem | #ff4081 (Pink) | 500 | Subsections |
| H6 | 1.125rem | #ffd740 (Gold) | 500 | Minor sections |
| Body | 1rem | rgba(255,255,255,0.8) | 400 | Paragraph text |

**Special Effects:**
- Text shadows on H4/H5 for glow effect
- Letter spacing: 0.5px on headings
- Line height: 1.6 for body text

### 6.3 Component Library

#### Cards
```css
.card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
    border-color: rgba(0, 212, 255, 0.3);
}
```

#### Buttons
```css
.btn-primary {
    background: linear-gradient(135deg, #00d4ff, #0099cc);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4);
}
```

#### Code Blocks
```css
pre {
    background: rgba(0, 212, 255, 0.05);
    border: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    max-height: 600px;
}

code {
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.8rem;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.9);
}
```

#### Images
```css
img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    object-fit: contain;
}
```

### 6.4 Sidebar Navigation (Table of Contents)

**Location:** Exercise detail pages (left sidebar)

**Features:**
- Sticky positioning during scroll
- Auto-generated from document headings (H4, H5)
- Hierarchical indentation for subsections
- Scroll spy highlighting
- Smooth scroll to section on click

**Structure:**
```html
<aside class="exercise-sidebar">
    <h3>Contents</h3>
    <ul class="toc-list" id="toc-list-{exerciseId}">
        <li><a href="#section-exercise-info">Exercise X</a></li>
        <li><a href="#section-exercise-content">Exercise Content</a></li>
        <li><a href="#section-homework">Assignment Content</a></li>
        <li class="toc-sub"><a href="#section-step1">Step 1</a></li>
        <li class="toc-sub"><a href="#section-step2">Step 2</a></li>
        <!-- ... dynamically generated ... -->
    </ul>
</aside>
```

**Scroll Spy Implementation:**
```javascript
function setupScrollSpy() {
    const sections = document.querySelectorAll('[id^="section-"]');
    const tocLinks = document.querySelectorAll('.toc-list a');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.pageYOffset >= sectionTop - 150) {
                current = section.getAttribute('id');
            }
        });

        tocLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}
```

---

## 7. Data Management

### 7.1 LocalStorage Architecture

**Storage Keys:**
- `teamWebsiteData` - Main data store (JSON)
- `project_files` - Final Project uploaded files
- `exercise_{id}_files` - Exercise-specific files (e.g., `exercise_0_files`)

**Data Schema:**
```javascript
{
    exercises: Array<Exercise>,
    project: {
        title: String,
        description: String,
        progress: String,
        progressPercent: Number,
        achievements: String
    },
    lastModified: ISO8601_DateString
}
```

### 7.2 File Upload System

**Supported File Types:**
- **Documents:** PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX
- **Images:** JPG, JPEG, PNG
- **Media:** MP4, MP3

**Upload Process:**
1. User selects file(s) via `<input type="file" multiple>`
2. FileReader converts file to Base64 string
3. Metadata extracted (name, size, type, date)
4. Stored in localStorage as JSON array
5. Rendered in file list with type-specific icons

**File Object Structure:**
```javascript
{
    name: "document.pdf",
    size: 1024567,  // bytes
    type: "application/pdf",
    data: "data:application/pdf;base64,JVBERi0xLjQK...",
    uploadDate: "2026-04-05T10:30:00.000Z"
}
```

**Size Limit:** 50MB per file (enforced client-side)

**Management Features:**
- Download file (creates temporary Blob URL)
- Delete file (removes from localStorage)
- Display file count and total size
- Type-based icon recognition

### 7.3 Data Persistence Strategy

**Advantages:**
- No backend server required
- Instant load times
- Works offline after initial load
- Simple deployment (GitHub Pages)

**Limitations:**
- Browser storage quota (~5-10MB per domain)
- Data lost if user clears browser cache
- No cross-device synchronization
- Base64 encoding increases file size by ~33%

**Mitigation:**
- Regular export functionality (download JSON backup)
- Clear warnings about data persistence
- Encourage users to keep local backups

---

## 8. Exercise Modules

### 8.1 Exercise 0: Project Management

**Topic:** Website Development Guide  
**Completion Date:** Week 0  
**Assets:** 21 screenshots

**Content Structure:**
1. **Preparation**
   - GitHub account setup
   - GitHub Desktop installation
   - AI agent (Tongyi Lingma) configuration

2. **Repository Creation**
   - Create public repository
   - Configure GitHub Pages settings
   - Invite team members as collaborators

3. **Local Development**
   - Clone repository to local machine
   - Design website structure with AI assistance
   - Implement HTML/CSS/JavaScript features

4. **Deployment**
   - Upload files via GitHub Desktop
   - Verify live site on GitHub Pages
   - Test responsive design

**Key Screenshots:**
- Repository creation workflow (5 images)
- GitHub Pages configuration (3 images)
- AI-assisted code generation (6 images)
- File upload process (4 images)
- Live site preview (3 images)

### 8.2 Exercise 1: Arduino Output&Input

**Topic:** Interactive Visualization Project  
**Completion Date:** Week 1-2  
**Assets:** 30 images + 1 GIF

**Hardware Components:**
- Arduino R4 WiFi board
- OLED display (128×64, SSD1306)
- RFID reader (MFRC522)
- WS2812 LED strip
- Photoresistor sensor
- Temperature sensor
- Push buttons

**Software Features:**
- RFID card detection and validation
- OLED animation rendering
- LED strip pattern control (rotating red effect)
- Sensor data acquisition
- Serial communication debugging

**Code Highlights:**
```cpp
// RFID Card Detection
if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    String uid = getUID();
    if (uid == "ELDERLY_CARD_UID") {
        playElderlyAnimation();
        rotateRedLEDs();
    }
}

// OLED Animation
void playElderlyAnimation() {
    display.clearDisplay();
    display.drawBitmap(x, y, elderly_icon, width, height, WHITE);
    display.display();
}

// LED Strip Control
void rotateRedLEDs() {
    for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = CRGB::Red;
        FastLED.show();
        delay(50);
        leds[i] = CRGB::Black;
    }
}
```

**Documentation:**
- Complete circuit diagram (Fritzing)
- Wiring connections table
- Pin mapping reference
- Troubleshooting guide
- Performance demonstration GIF

### 8.3 Exercise 2: Arduino Basic

**Topic:** Basic Input/Output Operations  
**Completion Date:** Week 2  
**Assets:** 9 images + 1 GIF

**Learning Objectives:**
- Digital input reading (buttons)
- Digital output control (LEDs)
- Pull-up/pull-down resistor concepts
- Debouncing techniques
- State machine implementation

**Projects Completed:**
1. Button-controlled LED toggle
2. Multi-button input detection
3. LED blinking patterns
4. PWM brightness control
5. Serial monitor debugging

**Code Example:**
```cpp
const int BUTTON_PIN = 2;
const int LED_PIN = 13;
bool ledState = false;
unsigned long lastDebounceTime = 0;

void loop() {
    int reading = digitalRead(BUTTON_PIN);
    
    if (reading != lastButtonState) {
        lastDebounceTime = millis();
    }
    
    if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != buttonState) {
            buttonState = reading;
            if (buttonState == HIGH) {
                ledState = !ledState;
                digitalWrite(LED_PIN, ledState);
            }
        }
    }
    lastButtonState = reading;
}
```

### 8.4 Exercise 3: CAD Design

**Topic:** 3D Model Design with Fusion 360  
**Completion Date:** Week 3  
**Assets:** 8 images

**Tools Used:**
- Autodesk Fusion 360
- Python API for automation
- AI-assisted design optimization

**Design Process:**
1. **Concept Sketching**
   - Initial idea brainstorming
   - Rough dimension planning
   - Material selection considerations

2. **3D Modeling**
   - Parametric sketch creation
   - Extrude and revolve operations
   - Fillet and chamfer applications
   - Assembly constraints

3. **AI Enhancement**
   - Generate design variations via AI prompts
   - Optimize geometry for 3D printing
   - Reduce material usage while maintaining strength

4. **Export Preparation**
   - Mesh generation (STL format)
   - Wall thickness verification
   - Support structure planning

**Python Script Example:**
```python
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        # Create new document
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Create sketch
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        
        # Draw rectangle
        lines = sketch.sketchCurves.sketchLines
        lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), 
                            adsk.core.Point3D.create(10, 0, 0))
        
        # Extrude
        extrudes = rootComp.features.extrudeFeatures
        profile = sketch.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(5)
        extrudes.addSimple(profile, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

**Deliverables:**
- Fusion 360 source file (.f3d)
- STL export for 3D printing
- Design documentation with screenshots
- Python automation script

### 8.5 Exercise 4: 3D Printing

**Topic:** Additive Manufacturing Technology  
**Completion Date:** Week 4  
**Assets:** 14 images + 1 GIF

**Printer Used:** Bambu Lab X1 Carbon

**Technology Overview:**
- FDM (Fused Deposition Modeling)
- Layer-by-layer construction
- Thermoplastic filament melting
- Precision nozzle deposition (0.4mm)

**Material Selection:**
- **PLA (Polylactic Acid):** Easy to print, biodegradable
- **PETG:** Stronger, chemical resistant
- **ABS:** Durable, heat resistant
- **TPU:** Flexible, rubber-like
- **Carbon Fiber Nylon:** High strength, lightweight

**Bambu Lab Advantages:**
- RFID chip automatic recognition
- ±0.03mm filament diameter tolerance
- EU food contact safety certification
- AMS (Automatic Material System) multi-color support

**Workflow:**

1. **Modeling (Blender)**
   - Create simple integrated model
   - Export as .3mf format
   - Verify mesh integrity

2. **Slicing (Bambu Studio)**
   - Import .3mf file
   - Select material profile
   - Configure layer height (0.2mm recommended)
   - Generate support structures
   - Preview print time and material usage

3. **Printer Connection**
   - Connect via mobile app (Bambu Handy)
   - Verify printer status
   - Load filament into AMS

4. **Printing**
   - Start print job remotely
   - Monitor progress via camera
   - Check first layer adhesion
   - Wait for completion (~2-8 hours typical)

5. **Post-Processing**
   - Remove support structures
   - Sand rough edges
   - Apply finishing touches

**Print Settings:**
- Layer Height: 0.2mm
- Infill Density: 20%
- Infill Pattern: Gyroid
- Wall Loops: 3
- Print Speed: 200mm/s (default)
- Nozzle Temperature: 220°C (PLA)
- Bed Temperature: 60°C

**Troubleshooting:**
- First layer adhesion issues → Clean bed, adjust Z-offset
- Stringing → Increase retraction, lower temperature
- Warping → Use brim, increase bed temperature
- Layer shifting → Check belt tension, reduce speed

**Demonstration:**
- Time-lapse GIF of complete print
- Before/after post-processing comparison
- Dimensional accuracy measurements

---

## 9. Final Project Module

### 9.1 Project Overview

**Status:** In Progress  
**Progress:** 75%  
**Expected Completion:** TBD

**Project Description:**
[To be filled by team - describe the final project concept, objectives, and scope]

### 9.2 Key Achievements

- Completed preliminary research and planning
- Established technical architecture
- Developed core functionality modules
- Conducted initial testing and iteration

### 9.3 Remaining Tasks

- [ ] Complete remaining feature development
- [ ] Perform comprehensive testing
- [ ] Optimize performance and UX
- [ ] Prepare final documentation
- [ ] Deploy to production environment

### 9.4 File Management

**Uploaded Files:** Stored in `project_files` localStorage key  
**Current Count:** [Dynamic - check live site]  
**Total Size:** [Dynamic - check live site]

**Access:** Visit Final Project page to view/download uploaded files

---

## 10. Responsive Design

### 10.1 Breakpoint Strategy

| Device | Width Range | Layout Adjustments |
|--------|-------------|-------------------|
| Desktop | ≥ 1024px | Full 3-column grid, wide margins |
| Tablet | 768px - 1023px | 2-column grid, reduced padding |
| Mobile Large | 480px - 767px | Single column, stacked elements |
| Mobile Small | < 480px | Compact spacing, smaller fonts |

### 10.2 Responsive Techniques

**CSS Media Queries:**
```css
/* Desktop */
@media (min-width: 1024px) {
    .card-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

/* Tablet */
@media (max-width: 1023px) {
    .card-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .navbar {
        width: calc(100% - 2rem);
    }
}

/* Mobile */
@media (max-width: 767px) {
    .card-grid {
        grid-template-columns: 1fr;
    }
    .hero h1 {
        font-size: 2rem;
    }
    .exercise-layout {
        flex-direction: column;
    }
    .exercise-sidebar {
        position: static;
        width: 100%;
    }
}
```

**Flexible Units:**
- `rem` for typography (scales with root font size)
- `%` and `vw/vh` for layout dimensions
- `auto` and `fr` for grid/flex sizing
- `clamp()` for fluid typography

**Mobile-First Approach:**
- Base styles target mobile devices
- Progressive enhancement for larger screens
- Touch-friendly tap targets (≥ 44px)
- Optimized image loading (lazy loading)

### 10.3 Testing Devices

- iPhone 14 Pro (393×852)
- iPad Air (820×1180)
- MacBook Pro 14" (1512×982)
- Samsung Galaxy S23 (360×800)
- Various desktop resolutions (1920×1080, 2560×1440)

---

## 11. Performance Optimization

### 11.1 Loading Performance

**Strategies Implemented:**
- Minimal external dependencies (only Mammoth.js for DOCX parsing)
- Inline critical CSS in HTML head
- Async loading of non-critical scripts
- Lazy loading of images below fold
- Compressed image assets (PNG optimization)

**Metrics:**
- Initial HTML size: ~3-5 KB per page
- Total CSS size: 45 KB (single file)
- Largest image: ~24 MB (3D printing GIF)
- Average page load time: < 1 second (cached)

### 11.2 Rendering Performance

**Optimizations:**
- `will-change` property for animated elements
- `transform` and `opacity` for GPU-accelerated animations
- `requestAnimationFrame` for scroll handlers
- Passive event listeners for scroll/touch events
- Debounced resize handlers

**Avoided Anti-Patterns:**
- No forced synchronous layouts
- Minimized DOM manipulations
- Efficient CSS selectors (avoid universal selector)
- No memory leaks (proper cleanup of event listeners)

### 11.3 Storage Efficiency

**LocalStorage Best Practices:**
- Compress data before storage (JSON.stringify)
- Limit file uploads to 50MB per file
- Provide export/cleanup functionality
- Warn users about storage limitations

**Alternative Considerations:**
- IndexedDB for larger datasets (future enhancement)
- Service Workers for offline caching
- CDN for static asset delivery

---

## 12. Future Enhancements

### 12.1 Short-Term Improvements (1-2 weeks)

1. **Add Search Functionality**
   - Search across exercises and projects
   - Filter by tags/categories
   - Highlight matching text

2. **Improve File Management**
   - Cloud storage integration (Google Drive, Dropbox)
   - File preview thumbnails
   - Batch download/upload
   - Version history tracking

3. **Enhance Accessibility**
   - ARIA labels for screen readers
   - Keyboard navigation support
   - High contrast mode toggle
   - Font size adjustment controls

4. **Analytics Integration**
   - Track page views and user interactions
   - Monitor file upload/download statistics
   - Identify popular content sections

### 12.2 Medium-Term Enhancements (1-2 months)

1. **Backend Integration**
   - Node.js/Express API server
   - MongoDB/PostgreSQL database
   - User authentication system
   - Real-time collaboration features

2. **Advanced Features**
   - Comment system for exercises
   - Rating/review functionality
   - Social sharing integration
   - Newsletter subscription

3. **Performance Upgrades**
   - Image lazy loading with blur placeholders
   - Code splitting for JavaScript
   - Service Worker for offline support
   - Progressive Web App (PWA) capabilities

4. **Content Management**
   - Admin dashboard for content editing
   - WYSIWYG editor for markdown
   - Automated image optimization
   - Scheduled content publishing

### 12.3 Long-Term Vision (3-6 months)

1. **Multi-Language Support**
   - Internationalization (i18n) framework
   - Language switcher UI
   - RTL (Right-to-Left) language support
   - Community translation contributions

2. **Mobile App**
   - React Native / Flutter cross-platform app
   - Push notifications
   - Offline-first architecture
   - Native device features (camera, file system)

3. **AI Integration**
   - Chatbot for Q&A about projects
   - AI-powered code suggestions
   - Automated content summarization
   - Smart search with natural language processing

4. **Community Features**
   - User profiles and portfolios
   - Project collaboration tools
   - Discussion forums
   - Mentorship matching system

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **MPA** | Multi-Page Application - separate HTML files for each page |
| **SPA** | Single-Page Application - one HTML file with dynamic routing |
| **Glassmorphism** | UI design trend featuring translucent backgrounds with blur effects |
| **Hash Routing** | Using URL fragment identifiers (#section) for navigation |
| **LocalStorage** | Browser API for persistent client-side data storage |
| **Base64** | Encoding scheme to represent binary data as ASCII text |
| **FDM** | Fused Deposition Modeling - 3D printing technology |
| **RFID** | Radio Frequency Identification - wireless data transmission |
| **OLED** | Organic Light-Emitting Diode display technology |
| **CAD** | Computer-Aided Design - software for 3D modeling |
| **AMS** | Automatic Material System - multi-filament 3D printer feature |
| **Scroll Spy** | UI pattern that highlights navigation based on scroll position |
| **Debouncing** | Technique to limit function call frequency |
| **Intersection Observer** | API for detecting element visibility in viewport |

---

## Appendix B: References

### Documentation
- [MDN Web Docs](https://developer.mozilla.org/)
- [W3C HTML5 Specification](https://www.w3.org/TR/html5/)
- [CSS Tricks](https://css-tricks.com/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

### Libraries & Tools
- [Mammoth.js](https://github.com/mwilliamson/mammoth.js) - DOCX to HTML converter
- [Fusion 360 API](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-820F6E4E-7F95-4D4F-9E5D-7C5E5F5E5F5E)
- [Arduino Documentation](https://www.arduino.cc/reference/en/)
- [Bambu Lab Wiki](https://wiki.bambulab.com/)

### Design Inspiration
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Dribbble - Glassmorphism](https://dribbble.com/search/glassmorphism)
- [Awwwards - Modern Web Design](https://www.awwwards.com/)

---

## Appendix C: Change Log

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | March 2026 | Initial PDR draft | Team |
| 2.0 | April 5, 2026 | MPA migration, exercise content restoration, image path fixes | Team |

---

**Document End**

*This PDR is maintained by the what the dog doing team. Last updated: April 5, 2026*
