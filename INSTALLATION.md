# Installation & Deployment Guide

## Prerequisites
- Python 3.8 or higher
- Flet framework
- Web browser for viewing

## Installation

### 1. Install Flet
```bash
pip install flet
```

### 2. Clone the Repository
```bash
git clone https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio.git
cd MarthaHeitaPortfolio
```

### 3. Run the Application Locally
```bash
flet run portfolio.py
```

The application will open in your default web browser at `http://localhost:8000`

## Deployment Options

### Option 1: Flet Web Deployment (Recommended)
```bash
flet publish portfolio.py
```

### Option 2: GitHub Pages (Static HTML)
1. Export as static HTML
2. Push to `gh-pages` branch
3. Enable GitHub Pages in repository settings

### Option 3: Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flet
CMD ["flet", "run", "portfolio.py", "--web"]
```

## Project Structure

```
MarthaHeitaPortfolio/
├── portfolio.py              # Main Flet application
├── matlab_certificates.py    # MATLAB certificates reference
├── requirements.txt          # Python dependencies
├── index.html               # To-Do List (static demo)
├── styles.css               # Global styling
├── script.js                # JavaScript utilities
├── clock.html               # Digital Clock (static demo)
├── clock-styles.css         # Clock styling
├── clock-script.js          # Clock logic
├── README.md                # Main documentation
├── INSTALLATION.md          # This file
├── TODO-README.md           # To-Do List documentation
├── CLOCK-README.md          # Digital Clock documentation
└── PORTFOLIO-STRUCTURE.md   # Portfolio architecture guide
```

## Running the Portfolio

### Development Mode
```bash
flet run portfolio.py --debug
```

### Production Mode
```bash
flet run portfolio.py
```

## Features

✅ **Dashboard** - Overview with statistics
✅ **Project Timeline** - Weekly contributions log
✅ **MATLAB Achievement Hub** - 6/8 courses completed
✅ **Technical Blog** - Data Structures & Algorithms post
✅ **GitHub Evidence** - Commit history and PRs
✅ **About Section** - Portfolio overview

## Assessment Components

| Component | Weight | Status |
|-----------|--------|--------|
| Flet Implementation | 30% | ✓ Complete |
| GitHub Evidence | 25% | ✓ Complete |
| Blog & Video | 25% | ✓ Complete |
| MATLAB Courses | 20% | ✓ 6/8 Complete |

## Troubleshooting

### Port Already in Use
```bash
flet run portfolio.py --port 8080
```

### Module Not Found
```bash
pip install -r requirements.txt
```

### Browser Won't Open
Manually navigate to `http://localhost:8000` in your browser

## Support

For issues or questions:
- Check GitHub Issues: https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio/issues
- Review documentation in README.md

## License

This portfolio is part of Computer Programming I course assessment.
