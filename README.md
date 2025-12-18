# AmbiToolbox

**A "Swiss Army Knife" for Ambisonics & Spatial Audio.**

AmbiToolbox is a suite of professional, standalone desktop utilities designed to solve the "annoying little problems" in spatial audio workflows. From format swapping to quick monitoring, these tools are built to be frictionless: **Drag, Drop, Done.**

---

## 🛠 The Toolkit

The suite consists of 6 specialized utilities, sharing a unified "Dark Studio" design language.

| Utility | Accent Color | Function |
| :--- | :--- | :--- |
| **Ambix2Opus** | 🟣 Purple | Compresses `.wav`/`.amb` to **Ogg Opus** for web/Unity. |
| **Ambix2CAF** | ⚪ Silver | Converts to Apple **Core Audio Format (.caf)** with spatial tags. |
| **AmbiOrder** | 🔵 Blue | Reduces spatial resolution (e.g., 3rd Order $\to$ 1st Order). |
| **AmbiSwap** | 🟠 Orange | Swaps formats between **AmbiX** (ACN/SN3D) and **FuMa**. |
| **AmbiRotate** | 🔴 Red | Fixes orientation issues (Yaw/Pitch/Roll) without a DAW. |
| **Ambix2Bin** | 🟢 Green | Quick preview tool. Toggles between **Binaural** (Headphones) and **Stereo** (Speakers). |

---

## 🏗 Technical Stack

* **Language:** Python 3.10+
* **GUI Framework:** PyQt6 (Cross-platform, High-DPI support)
* **Audio Backend:** FFmpeg (via `subprocess`)
* **Packaging:** PyInstaller (One-file executables)

## 🎨 Visual Identity

AmbiToolbox uses a strict **"Dark Studio"** design system to match professional audio software environments.

* **Theme:** Dark Charcoal (`#1E1E1E`) background, Off-white text.
* **Typography:**
    * *Product Line:* **Montserrat** (Structural, Foundation)
    * *App Name:* **Jost** (Geometric, Modern)
    * *UI Text:* **Roboto** (Clean, Readable)
* **Interaction:** All tools feature a prominent "Drop Zone" with visual feedback.
* **Branding:** Features the **Virtual Virgin** logo and a custom frameless title bar.

---

## 📂 Development Structure

This project uses a "Master Class" architecture to ensure consistency across all apps.

```text
/AmbiToolbox
│
├── /assets                 # Common Assets: Logos (VV Logo), Fonts
├── /apps                   # Application Logic
│   ├── /Ambix2Bin          # App-specific code & assets
│   │   ├── /assets
│   │   │   └── /hrtf       # HRTF for Binaural Rendering
│   │   └── app_ambix2bin.py
│   ├── /Ambix2Opus
│   └── ...
├── /src
│   └── common_ui.py        # THE CORE: Master Boilerplate & Style Engine
│
├── AmbiToolbox_Boilerplate.md  # Source of Truth for Design/Code standards
├── PRP_Template.md             # Prompt template for AI Agent task generation
├── requirements.txt            # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites
1.  Install **Python 3.10+**.
2.  Install **FFmpeg** and ensure it is in your system PATH.

### Installation
```bash
git clone [https://github.com/YourRepo/AmbiToolbox.git](https://github.com/YourRepo/AmbiToolbox.git)
cd AmbiToolbox
pip install -r requirements.txt
```

### Running a Tool
To launch the **Ambix2Bin** tool (for example):
```bash
python apps/Ambix2Bin/app_ambix2bin.py
```

---

## 🤖 Development Workflow (AI-Assisted)

This project utilizes AI Agents for rapid development. Each tool is generated using a **Product Requirement Prompt (PRP)** that references the `AmbiToolbox_Boilerplate.md`.

1.  **Define:** Create a PRP for the specific tool.
2.  **Generate:** Agent builds the script inheriting from `common_ui.py`.
3.  **Validate:**
    * **Unit Tests:** Verify FFmpeg command strings (Mocked).
    * **UI Check:** Verify "Look & Feel" against the Style Guide.

---

## 📜 License & Branding

**AmbiToolbox** is a product of **[Virtual Virgin](https://www.virtualvirgin.net/)**.
* **License:** Open Source (MIT pending).
* **Concept:** Simple, reliable tools for engineers. No bloat.