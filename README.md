# Martha Heita - Computer Programming I Portfolio Showcase

## Overview
This repository contains Martha Heita's static portfolio showcase for Computer Programming I, featuring interactive web applications and projects.

## Live Site
The GitHub Pages URL will use the student's GitHub username and repository name after deployment.

## Projects & Applications

### 1. **To-Do List Application** 📝
A modern, fully functional to-do list application with local storage functionality.
- Add, complete, and delete tasks
- Filter tasks by status (All, Active, Completed)
- Persistent storage using browser's localStorage
- Responsive design for all devices
- **Files**: `index.html`, `styles.css`, `script.js`, `README.md`

### 2. **Digital Clock - Multiple Time Zones** ⏰
A beautiful, real-time digital clock displaying current time in different time zones.
- Real-time updates every second
- Display time in 40+ time zones
- Toggle between 12-hour and 24-hour formats
- Add/remove time zones dynamically
- UTC offset information
- Persistent storage of selected time zones
- **Files**: `clock.html`, `clock-styles.css`, `clock-script.js`, `CLOCK-README.md`

## Tech Stack
- Static HTML, CSS, and JavaScript
- GitHub Pages
- GitHub Actions
- LocalStorage API for data persistence
- Intl API for time zone support

## Static Deployment Architecture
GitHub Pages serves the static site. All applications are client-side with no backend dependencies.

## Local Preview
```bash
python -m http.server 8000
```

Open:
```text
http://localhost:8000
```

Then navigate to:
- **To-Do List**: `http://localhost:8000/index.html`
- **Digital Clock**: `http://localhost:8000/clock.html`

## Project Structure
```
MarthaHeitaPortfolio/
├── index.html              # To-Do List application
├── styles.css              # To-Do List styling
├── script.js               # To-Do List logic
├── README.md               # To-Do List documentation
├── clock.html              # Digital Clock application
├── clock-styles.css        # Digital Clock styling
├── clock-script.js         # Digital Clock logic
├── CLOCK-README.md         # Digital Clock documentation
└── site/                   # GitHub Pages deployment folder
    └── assets/
        ├── screenshots/    # Evidence assets
        └── certificates/   # Certificate files (if available)
```

## Features Showcase

### To-Do List Features ✨
- ✅ Task management (add, complete, delete)
- 🔍 Smart filtering system
- 💾 Automatic persistence
- 📱 Fully responsive design
- 🛡️ XSS protection
- 🎨 Modern UI with smooth animations

### Digital Clock Features 🕐
- 🌍 40+ international time zones
- 🔄 Real-time updates
- 📊 Detailed time information
- 🎨 Beautiful gradient design
- 📱 Mobile-responsive
- 💾 User preference persistence

## Browser Support
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## GitHub Pages Deployment
GitHub Actions uploads the site folder. Pages source is configured for GitHub Actions deployment.

## Maintenance Notes
- Keep private role documents out of Git
- Keep tokens in local terminal environment variables only
- All applications are client-side with no sensitive data exposure

## Student Contribution
Martha Heita created both web applications from scratch, demonstrating proficiency in:
- HTML5 semantic markup
- Modern CSS3 with animations
- Vanilla JavaScript (ES6+)
- DOM manipulation and event handling
- Browser APIs (LocalStorage, Intl)
- Responsive web design
- User experience optimization

## Evidence Assets
Evidence screenshots and certificates are organized in `site/assets/`:
- `site/assets/screenshots/` - Application screenshots
- `site/assets/certificates/` - Completion certificates (when available)

## Future Enhancements
Planned features for expansion:
- Additional interactive applications
- Enhanced portfolio design
- Project showcase gallery
- Contact/about sections
- Skills and experience timeline

---

**Made with ❤️ by Martha Heita**
**Last Updated: June 2026**
