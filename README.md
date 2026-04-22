# what the dog doing

Official website for the **what the dog doing** team.

## Team Members

| Name | Chinese Name | Role | GitHub |
|------|--------------|------|--------|
| Ash | 范洲豪 | Frontend Developer | [@17poi](https://github.com/17poi) |
| Felix | 徐克丰 | Hardware Engineer | [@WanShang2026](https://github.com/WanShang2026) |
| Howie | 吴浩瑜 | Backend Developer | [@Howie-jbg](https://github.com/Howie-jbg) |
| Max | 韩明哲 | Project Manager | [@HMZ766](https://github.com/HMZ766) |
| Joe | 张敏强 | UI/UX Designer | [@SONATA360](https://github.com/SONATA360) |
| David | 叶骁纬 | Full Stack Developer | [@Excalibuuuuur](https://github.com/Excalibuuuuur) |

## About Us

Welcome to the what the dog doing team! We are a group of passionate and determined heroes, dedicated to paving the way with knives and shields in our hands. Our name comes from an image that we particularly like.

## Tech Stack

- **HTML5** – Semantic structure
- **CSS3** – Apple-style UI, glassmorphism, responsive design
- **Vanilla JavaScript** – Hash routing, data-driven rendering, interactive animations

## Features

### Core Features
- **Animated Gradient Homepage**: Flowing gradient background with smooth color transitions
- **Separate Pages**: "About us" (team intro) and "Team members" (individual profiles) are independent sections
- **Hash-based routing** (`#home`, `#intro`, `#members`, `#member-0`~`#member-5`, `#exercise-0`~`#exercise-4`, `#project`, `#exercises`)
- **Apple-inspired UI** – Frosted glass navbar, gradient backgrounds, card hover effects, 360° avatar flip animation
- **Fully responsive** – Optimized for desktop, tablet, and mobile devices (1024px, 768px, 480px, 360px breakpoints)
- **Data-driven** – Member info, projects, and exercises stored in JS objects for easy updates
- **GIF showcase** – Interactive image reveal with smooth fade animation
- **Member Detail Pages** – Individual profiles with Bio, Email, Hobbies, and Assignments
- **Exercise Detail Pages** – Local hash routing with detailed content for each exercise

### Advanced UI/UX
- **Smart Navbar** – Auto-hide on scroll down, show on scroll up for immersive reading experience
- **Back to Top Button** – Appears after scrolling 300px, smooth scroll to top with one click
- **Compact Mode** – Navbar automatically shrinks when viewing exercise details for better content focus
- **Transparent Navbar** – Optimized opacity for seamless gradient background integration
- **Sidebar Table of Contents** – Sticky navigation sidebar in exercise detail pages with scroll spy highlighting
- **Enhanced Typography** – Multi-level heading system with distinct colors (cyan h4, pink h5, gold h6) and glow effects

### File Management
- **File Upload System** – Upload and manage files (PDF, JPG, PNG, DOC, DOCX, MP4, MP3, etc.) in Homework and Final Project pages with local storage

## Project Structure

```
ZWU-2026-2-001/
├── index.html                  # Main entry (single-page application)
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
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

## Smart Navigation Features

### Auto-Hide Navbar
- **Scroll Down**: Navbar smoothly hides to maximize content viewing area
- **Scroll Up**: Navbar reappears for easy navigation access
- **Threshold**: Hides after scrolling down more than 100px
- **Animation**: Smooth 0.4s cubic-bezier transition

### Back to Top Button
- **Position**: Fixed at bottom-right corner (2rem from edges)
- **Appearance**: Circular button with cyan gradient background
- **Visibility**: Shows when scrolled more than 300px from top
- **Action**: Smooth scroll to page top on click
- **Hover Effect**: Button lifts up with enhanced shadow

### Compact Mode
- Automatically activates when viewing exercise detail pages
- Reduces navbar size and padding for better content focus
- Deactivates when returning to exercise list

## Enhanced Typography System

### Color-Coded Headings
- **H4 (Main Sections)**: Bright Cyan (#00e5ff) with glow effect - ~32px
- **H5 (Subsections)**: Vibrant Pink (#ff4081) with glow effect - ~24px
- **H6 (Minor Sections)**: Warm Gold (#ffd740) - ~20px
- **Body Text**: Light gray with increased size - ~18px

### Visual Hierarchy
- Clear distinction between heading levels through color and size
- Subtle text shadows on h4 and h5 for modern tech aesthetic
- Optimized spacing between sections for comfortable reading

## Table of Contents

### Sidebar Navigation
- **Position**: Sticky left sidebar in exercise detail pages
- **Auto-Generation**: Dynamically builds from document headings (Week 1)
- **Scroll Spy**: Highlights current section while scrolling
- **Smooth Scrolling**: Click any TOC item to jump to that section
- **Hierarchical Display**: Main sections and subsections indented
- **Borderless Design**: Clean, minimal appearance without frames

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
