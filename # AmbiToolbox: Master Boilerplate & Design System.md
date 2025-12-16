# AmbiToolbox: Master Boilerplate & Design System

## 1. Project Overview
AmbiToolbox is a suite of simple, drag-and-drop desktop utilities for Ambisonics audio workflows. 
**Target Audience:** Audio Engineers.
**Vibe:** Professional, Dark Mode, Minimalist, "Dark Studio."

## 2. Tech Stack
* **Language:** Python 3.10+
* **GUI Framework:** PyQt6 (Strict adherence required)
* **Icons:** `qtawesome` (Use Google Material Design icons: `mdi.*`)
* **Audio Backend:** FFmpeg (via `subprocess` calls)
* **Packaging:** PyInstaller (for final builds)

## 3. Visual Identity (Strict)
* **Window Style:** Frameless, Custom Title Bar.
* **Fonts:** * *Brand Line:* "Montserrat" (Medium)
    * *App Name:* "Jost" (Bold)
    * *UI Text:* "Roboto" (Regular)
* **Colors:**
    * Background: `#1E1E1E` (Charcoal)
    * Panel/DropZone: `#2D2D2D`
    * Text: `#E0E0E0`
    * **Accents (Per App):**
        * Ambix2Opus: `#9b59b6` (Purple)
        * Ambix2CAF: `#95a5a6` (Silver)
        * AmbiOrder: `#3498db` (Blue)
        * AmbiSwap: `#e67e22` (Orange)
        * AmbiRotate: `#e74c3c` (Red)
        * AmbiMonitor: `#2ecc71` (Green)

## 4. File Structure
```text
/AmbiToolbox
  /assets
    vv_logo.png       # Virtual Virgin Brand Logo (Only local asset required)
  /src
    common_ui.py      # CONTAINS THE MASTER CLASS
    app_monitor.py    # Specific App logic
  requirements.txt    # Must include: PyQt6, qtawesome