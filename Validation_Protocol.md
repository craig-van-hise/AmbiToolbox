# AmbiToolbox Validation Protocol

## Phase 1: Unit Testing (Automated)
* **Framework:** `unittest` or `pytest`.
* **Mocking:** You must MOCK `subprocess.run`. Do not actually run FFmpeg during unit tests.
* **Coverage:**
    * Test that file extension detection works.
    * Test that the constructed FFmpeg command string is exactly correct based on selected UI options.
    * Test that the GUI elements (buttons/toggles) update internal state variables.

## Phase 2: Functional Verification (Dry Run)
* The agent must create a "Dry Run" mode where dropping a file prints the *exact* FFmpeg command to the console instead of running it.
* **Success Criteria:** The command must match the PRP specification.

## Phase 3: Human-in-the-Loop (UI Check)
* **Action:** The agent must launch the GUI.
* **Human Check:**
    * Does the Title Bar show "AmbiToolbox | [App Name]"?
    * Is the Accent Color correct?
    * Does the Dark/Light toggle work?
    * Is the "Virtual Virgin" logo present and clickable?