# DevOps Notes - Taller

## Overview
This is a DevOps workshop and learning resources web application. It provides a clean, modern interface for organizing and accessing DevOps-related materials, notes, and resources.

**Purpose**: Educational workspace for DevOps concepts and workshop materials  
**Current State**: Fully functional static website with Python HTTP server  
**Created**: November 6, 2025

## Project Architecture

### Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Backend**: Python 3.11 with built-in HTTP server
- **Server**: Simple HTTP server bound to 0.0.0.0:5000

### Project Structure
```
.
├── index.html          # Main HTML page
├── styles.css          # Styling and responsive design
├── script.js           # Client-side JavaScript
├── server.py           # Python HTTP server (port 5000)
├── README.md           # Original repository README
├── replit.md           # This documentation file
└── .gitignore          # Python-specific ignore patterns
```

### Key Features
- Responsive design with gradient background
- Six topic cards covering:
  - Docker
  - Kubernetes
  - CI/CD
  - Monitoring
  - Infrastructure as Code
  - Cloud Platforms
- Clean, modern UI with hover effects
- No-cache headers for immediate updates

## Development Setup

### Running Locally
The web server is configured to run automatically via the workflow system:
- Server binds to `0.0.0.0:5000`
- Serves static files from the project root
- Includes cache-control headers for development

### Server Configuration
The Python server (`server.py`) includes:
- Host: 0.0.0.0 (allows Replit proxy access)
- Port: 5000 (frontend requirement)
- Cache-Control headers to prevent stale content
- Auto-redirect from `/` to `/index.html`

## Deployment

### Configuration
- **Deployment Type**: Autoscale (stateless web application)
- **Run Command**: `python3 server.py`
- **Port**: 5000

The autoscale deployment is ideal for this static website as it:
- Only runs when requests are made
- Scales automatically with traffic
- Requires no persistent state

## Recent Changes

### November 6, 2025 - Initial Setup
- Created static website structure (HTML, CSS, JS)
- Implemented Python HTTP server with proper configuration
- Configured workflow for port 5000 with webview output
- Set up deployment configuration for autoscale
- Added Python .gitignore patterns
- Created project documentation

## Future Enhancements
Consider adding:
- Individual pages for each DevOps topic
- Interactive tutorials or code examples
- Search functionality for notes
- Markdown support for note-taking
- Local storage for user preferences
- Dark mode toggle
