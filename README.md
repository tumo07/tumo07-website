# TUMO07 - Minecraft Server Website

A premium, Apple-inspired liquid glass themed website for the TUMO07 Minecraft Fabric server. 

## Features
- **Liquid Glass Aesthetics**: High-end UI with dynamic shimmer effects, blur, and deep dark theme integration (`#121216`).
- **Live Status Feed**: Real-time server status polling synced via Firebase, instantly showing Online/Offline states and power outage detection.
- **Terminal-Style IP Box**: Click-to-copy server IP address wrapped in an interactive terminal component.
- **Steam-Style Dev Notes**: Clean, chronological timeline showcasing the latest server updates and patch notes.

## Architecture & Deployment

The website relies on two main components:
1. **Frontend (GitHub Pages)**: Pure HTML/CSS/JS interface hosted statically.
2. **Backend (Firebase + Python)**: Python watchdog scripts running locally on the server PC push status events directly to a Firebase Realtime Database. The frontend fetches this data to display the live feed.

### Deployment Script

To deploy changes to the live website, simply run the deployment script:
```bash
python deploy.py
```
This script will authenticate via GitHub API, upload your changes to the `tumo07.github.io` domain, and configure the custom domain `www.tumo07.io.vn`.

## Associated Server Scripts
The backend telemetry relies on scripts hosted on the server machine:
- `push_status.py`: Handles sending events like "Server Started", "Server Stopped", or "Power Outage" directly to the Firebase database.
- `LogMonitor.py`: A watchdog that actively monitors server logs for specific events.
