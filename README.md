# what the dog doing

Official website for the **what the dog doing** team.

## Team Members

| Name | Role | GitHub |
|------|------|--------|
| Ash | Frontend Developer | [@17poi](https://github.com/17poi) |
| Felix | Hardware Engineer | [@WanShang2026](https://github.com/WanShang2026) |
| Howie | Backend Developer | [@Howie-jbg](https://github.com/Howie-jbg) |
| Max | Project Manager | [@HMZ766](https://github.com/HMZ766) |
| Joe | UI/UX Designer | [@SONATA360](https://github.com/SONATA360) |
| David | Full Stack Developer | [@Excalibuuuuur](https://github.com/Excalibuuuuur) |

## About Us

Welcome to the what the dog doing team! We are a group of passionate and determined heroes, dedicated to paving the way with knives and shields in our hands. Our name comes from an image that we particularly like.

## Tech Stack

- **HTML5** – Semantic structure
- **CSS3** – Apple-style UI, glassmorphism, responsive design
- **Vanilla JavaScript** – Hash routing, data-driven rendering, interactive animations

## Features

- **Animated Gradient Homepage**: Flowing gradient background with smooth color transitions
- **Separate Pages**: "About us" (team intro) and "Team members" (individual profiles) are independent sections
- **Hash-based routing** (`#home`, `#intro`, `#members`, `#member-0`~`#member-5`, `#exercise-0`~`#exercise-4`, `#project`, `#exercises`)
- **Apple-inspired UI** – Frosted glass navbar, gradient backgrounds, card hover effects, 360° avatar flip animation
- **Fully responsive** – Optimized for desktop, tablet, and mobile devices (1024px, 768px, 480px, 360px breakpoints)
- **Data-driven** – Member info, projects, and exercises stored in JS objects for easy updates
- **GIF showcase** – Interactive image reveal with smooth fade animation
- **Member Detail Pages** – Individual profiles with Bio, Email, Hobbies, and Assignments
- **Exercise Detail Pages** – Local hash routing with detailed content for each exercise
- **Transparent Navbar** – Optimized opacity for seamless gradient background integration
- **Hardcoded Assignment Content** – Exercise 1 includes complete Arduino documentation with 30 embedded images for instant loading
- **File Upload System** – Upload and manage files (PDF, JPG, PNG, DOC, DOCX, MP4, MP3, etc.) in Homework and Final Project pages with local storage

## Project Structure

```
ZWU-2026-2-001/
├── index.html                  # Main entry (single-page application)
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── data/
│   └── assignment 1.docx      # Exercise 1 assignment document (dynamically loaded)
├── assets/
│   └── image/
│       ├── avatars/
│       │   ├── Ash.jpg              # Ash's avatar
│       │   ├── Felix.jpg            # Felix's avatar
│       │   ├── howie-avatar.jpg     # Howie's avatar
│       │   ├── Max.jpg              # Max's avatar
│       │   ├── Joe.jpg              # Joe's avatar
│       │   ├── Excalibuuuuur.jpg    # David's avatar
│       │   └── default-avatar.png   # Default member avatar
│       └── eggs/
│           └── what-the-dog-doing.gif  # Team branding GIF
```

## Hardcoded Assignment Content

### Overview
Exercise 1 ("Arduino OUTPUT") contains complete assignment documentation directly embedded in HTML, eliminating the need for dynamic file loading.

### Features
- ⚡ **Instant Loading** – No network requests or parsing delays
- 🖼️ **30 Embedded Images** – Including 29 PNG images and 1 GIF animation
- 📝 **Complete Documentation** – Covers Arduino hardware, IDE usage, coding methods, and open-source project analysis
- 🎨 **Styled Content** – Dark theme with cyan headings (#00d4ff) and pink accents (#ff00d4)

### Content Structure
The assignment includes:
- **Hardware Introduction**: Arduino UNO R4 WiFi specifications and features
- **Arduino IDE Guide**: Interface overview, setup process, and basic coding structure
- **Hardware Connection**: LED, resistors, buttons, buzzers, sensors, and relay modules
- **Open Source Project Analysis**: 
  - A. Autoware (Autonomous driving software stack)
  - B. Autonomous Vehicle eHMI Prototype
  - C. Harmoware-HMI (Human-computer interaction)
  - D. Smart Cane (Assistive device for visually impaired)
  - E. OpenHapticGlove (Haptic navigation glove)
  - F. Smartpole-VR-AWSIM (VR simulation platform)
- **MIT License Explanation**: Legal terms and usage rights

### Image Location
All images are stored in `images/assignment 1/` folder:
- `1.png` to `30.png` (static images)
- `20.gif` (animated GIF for Autoware section)

## File Upload Feature

### Supported File Types
- **Documents**: PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX
- **Images**: JPG, JPEG, PNG
- **Media**: MP4, MP3

### Features
- 📁 **Multiple File Selection** – Upload multiple files at once
- 💾 **Local Storage** – Files stored in browser localStorage (Base64 encoded)
- 📥 **Download & Delete** – Manage uploaded files easily
- 🎨 **File Type Icons** – Automatic icon recognition by file type
- 📏 **Size Limit** – Maximum 50MB per file

### Storage Structure
- Final Project: `project_files` in localStorage
- Exercises: `exercise_{id}_files` in localStorage (e.g., `exercise_0_files`)

## Getting Started

1. Clone or download the repository
2. Open `index.html` in any modern browser
3. Navigate using the top menu or hash links

## Deployment

Deployed on **GitHub Pages**:
```
https://nexmaker-fab.github.io/ZWU-2026-2-001/#home
```

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
