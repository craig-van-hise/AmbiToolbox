# Product Requirement Prompt (PRP)
**Role:** Senior Python Developer & Audio Engineer
**Project:** AmbiToolbox
**Component:** [INSERT TOOL NAME HERE, e.g., AmbiMonitor]

## 1. Context
You are building a single utility within the "AmbiToolbox" suite. You MUST adhere to the `AmbiToolbox_Boilerplate.md` for UI consistency.

## 2. Requirements
* **Inheritance:** You must import `AmbiToolboxApp` from `common_ui.py` and subclass it.
* **Color Accent:** Use [INSERT HEX CODE] for this app.
* **Input Support:** .wav, .opus, .caf, .amb
* **Core Function:** [DESCRIBE FUNCTION]

## 3. UI Elements (Specific)
Add these widgets to the `self.options_area` layout:
1.  [Element 1, e.g., Toggle Switch for Binaural/Stereo]
2.  [Element 2, e.g., Save Button]

## 4. Audio Processing Logic
* Use `subprocess` to call FFmpeg.
* **Command Logic:** [INSERT FFMPEG LOGIC OR PSEUDOCODE]

## 5. Task List
- [ ] Create `app_[name].py` inheriting from Master Class.
- [ ] Implement UI specific controls.
- [ ] Implement `process_file` method with FFmpeg logic.
- [ ] Implement Unit Tests (mocking FFmpeg).
- [ ] Manual UI Verification (Pause for Human Review).