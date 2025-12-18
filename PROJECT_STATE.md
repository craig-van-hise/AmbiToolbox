# AmbiToolbox - Project State Report

**Date:** December 17, 2025
**Version:** 1.5.1 (CLI Fixes)

## 1. Executive Summary
The **AmbiToolbox** project is evolving into a modular suite of applications. The flagship module, **Ambix2Bin**, has undergone a complete rendering engine overhaul to resolve spatial accuracy and stability issues.

**Global Status:** 🟢 **Active & Operational**

## 2. Directory Structure Changes
The project structure has been reorganized to support multiple distinct applications:

*   **`apps/Ambix2Bin/`**: Contains the full source code for the Binaural Monitor.
    *   `app_ambix2bin.py`: GUI Entry point.
    *   `saf_wrapper.py`: The isolated Audio Worker process (Updated with robust CLI arg parsing).
*   **`assets/`**: Shared resources (HRTF SOFA files, FFmpeg binaries).
*   **`libs/`**: Shared libraries (`libsaf`).

## 3. High-Level Achievements
*   **Modularization:** applications are now self-contained in `apps/`.
*   **Stability:** Moved away from fragile C-bindings for file I/O to robust Python implementations.
*   **Audio Quality:** Solved critical spatial rendering flaws (Dead Front/Back, Timbral Distortion) by implementing a new Virtual Speaker architecture.

## 4. Next Steps
*   Expand the suite with new tools (e.g., AmbiTrim).
*   Maintain the Agentic workflow for continuous improvement.
