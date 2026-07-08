# IMAGINED FINGER SEQUENCE TASK (iFST) — Online version (PsychoPy / Pavlovia)

**Author:** Marcos Moreno Verdú  
**Software:** PsychoPy 2025.2.4 or later · Deployed via [Pavlovia](https://pavlovia.org/)  
**Experiment type:** Online (browser-based, via Pavlovia)  
**Languages supported:** English (EN) · Spanish (ES) · French (FR) · German (DE)

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built using [PsychoPy](https://www.psychopy.org/) (Builder) and is intended for **online execution via [Pavlovia](https://pavlovia.org/)**. Please make sure you are running PsychoPy 2025.2.4 or later, as other versions might behave unexpectedly.

PsychoPy compiles the experiment to JavaScript for browser-based execution. All code components contain both Python and JavaScript tabs so the experiment runs correctly both locally (for testing) and online (via Pavlovia).

This README details the structure and customisation of this iFST implementation. If you are unfamiliar with PsychoPy, refer to the [documentation](https://www.psychopy.org/documentation.html) on their website — especially regarding conditions files, variables, routines, and loops.

---------------------------------------

## SETUP INSTRUCTIONS

**Requirements:** PsychoPy 2025.2.4 or later · a Pavlovia account.

### Testing locally

1. **Download** all files from the repository and place them in a dedicated folder.
2. **Open** `iFST.psyexp` in PsychoPy.
3. Click the **green triangle** to run locally — useful for checking logic and layout before deploying.

### Deploying online via Pavlovia

4. **Link** your Pavlovia account in the Pavlovia tab of PsychoPy (if not already done).
5. Click **"No project"** in the Pavlovia tab to link the experiment to a new Pavlovia project and follow the prompts.
6. **Check** your Pavlovia dashboard — the project should appear under the same name as the experiment file.
7. **Change** the study mode from Inactive to **Piloting** (for testing) or **Running** (for data collection).
8. Click **Pilot** or share the participant link to run the experiment online.
9. **Download data** from the Pavlovia dashboard after data collection and process it using the `Example data processing.R` script provided.

> **⚠️ File paths:** Do not rename or move any files or subfolders. The experiment locates all resources by relative path.

> **⚠️ Browser compatibility:** Chrome and Firefox are recommended. Safari may have issues with audio autoplay policy.

---------------------------------------

## LANGUAGE LOCALISATION

This experiment uses two external spreadsheet files to manage on-screen text and translations: `language_localiser.xlsx` and `messages.xlsx`. The language is selected via the PsychoPy startup dialog (`language` field) before every run — both locally and on Pavlovia. The name entered must exactly match an entry in the `language` column of `language_localiser.xlsx`.

### How language switching works

The routine `load language` contains a code component that (a) defaults to English (`EN`) at experiment start, and (b) updates the ISO code based on the participant's startup-dialog choice. This code auto-translates to JavaScript for online use.

The routine `update messages` iterates across all rows in `messages.xlsx` and exposes each message as a global variable (`globals()` in Python, `window[]` in JS), ready for use in text components. Every text component whose content should update by language must have its "Text" field set to **"Set to every repeat"**.

### Adding a new language

#### 1. Add a row to `language_localiser.xlsx`

| language | ISO_code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |
| Italian | IT |

#### 2. Add a column to `messages.xlsx`

Add a column named with the ISO code (e.g., `IT`) and provide a translation for every message key. Missing entries fall back to `EN`.

| message | EN | ES | … | IT |
| :--- | :--- | :--- | :--- | :--- |
| welcome_msg | Welcome to the experiment! | ¡Bienvenido/a! | … | Benvenuto! |
| adv_msg | Press SPACE to continue | Presiona ESPACIO | … | Premi SPAZIO |

#### 3. Add columns to `ifst_files/self_assess_questions.xlsx`

Add four new columns per language following the naming pattern:

| Column | Description |
| :--- | :--- |
| `self_assess_question_IT` | Question text |
| `label_min_IT` | Anchor label for the minimum (0) |
| `label_middle_IT` | Anchor label for the midpoint (5) |
| `label_max_IT` | Anchor label for the maximum (10) |

#### 4. Update the startup dialog

In PsychoPy: **Experiment Settings** (cogwheel) → Basic → Experiment Info → update the `language` dropdown to include the new language name. It must exactly match the entry in `language_localiser.xlsx`. Save and re-sync to Pavlovia.

> **⚠️ Tip:** `language_localiser.xlsx` and `messages.xlsx` are imported as conditions files. If the `load language` loop shows a row-count mismatch, click on the loop and refresh the sheet with the green arrows.

> **⚠️ Key names:** Do not change the `message` column or any variable names. The experiment looks up strings by exact key name.

---------------------------------------

## TECHNICAL DETAILS

### Folder structure

```
iFST_online_PsychoPy/
│
├── iFST.psyexp                     ← Main experiment file
├── iFST_lastrun.py                 ← Auto-generated by PsychoPy (do not edit)
│
├── language_localiser.xlsx         ← Maps language names → ISO codes
├── messages.xlsx                   ← All localised text strings
│
├── ifst_files/
│   ├── conditions_left.xlsx        ← Trial conditions (left hand)
│   ├── conditions_right.xlsx       ← Trial conditions (right hand)
│   ├── instructions.xlsx           ← Instruction slide content + image paths
│   └── self_assess_questions.xlsx  ← VAS question texts and anchor labels
│
├── ifst_images/                    ← Instruction slide images (sequence diagrams)
│   └── seq_*.png  (10 files)
│
├── ifst_stimuli/                   ← Trial stimulus images + audio feedback
│   ├── simple_execution_left.png
│   ├── simple_execution_right.png
│   ├── complex_execution_left.png
│   ├── complex_execution_right.png
│   ├── simple_imagery_left.png
│   ├── simple_imagery_right.png
│   ├── complex_imagery_left.png
│   ├── complex_imagery_right.png
│   ├── correct_sound.wav
│   └── incorrect_sound.wav
│
├── data/                           ← Output data for local test runs
│   └── Example_iFST_data.csv
│
└── Example data processing.R       ← R script for data processing
```

### Key files

| File | Description |
| :--- | :--- |
| `iFST.psyexp` | Main experiment file. Open in PsychoPy to run or modify. |
| `messages.xlsx` | One row per message key, one column per language. Loaded at startup. |
| `language_localiser.xlsx` | Maps the full language name to its ISO code. |
| `ifst_files/conditions_left.xlsx` | Trial conditions for left-handed participants. Columns: `hand`, `stim`, `sequence_code`, `sequence_type`, `trial_type`, `key_presses`, `sequence_picture`, `prompt_before`, `prompt`. |
| `ifst_files/conditions_right.xlsx` | Same structure for right-handed participants. |
| `ifst_files/instructions.xlsx` | Instruction slide content: text per language and handedness (column suffixes `_EN`, `_ES`, etc.), image path (`inst_pic`). Filtered at runtime by handedness. |
| `ifst_files/self_assess_questions.xlsx` | 8 self-assessment questions with texts and anchor labels for each language. |
| `ifst_stimuli/correct_sound.wav` | Auditory feedback for correct responses (practice block). |
| `ifst_stimuli/incorrect_sound.wav` | Auditory feedback for incorrect responses (practice block). |

### Implementation notes

- The experiment is built entirely in **PsychoPy Builder**; all custom logic is in code components with Python (local) and JavaScript (online) tabs. The JS tab executes when the experiment runs in the browser via Pavlovia.
- `iFST_lastrun.py` is auto-generated by PsychoPy on each local run. Do not edit it.
- Instruction slides are filtered at runtime based on handedness using a conditions-file row selector.
- Global variable exposure: Python uses `globals()`, JavaScript uses `window[]` — both are handled automatically in the `update messages` code component.

---------------------------------------

## EXPERIMENT SETTINGS

Most parameters are **not** in the startup dialog — they are set in the `experiment settings` code component and must be edited directly in PsychoPy.

### Available parameters (startup dialog)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `participant` | — | Participant ID (used in the output filename). |
| `session` | — | Session ID. |
| `language` | English | Language of the experiment. Must match an entry in `language_localiser.xlsx`. |
| `age` | — | Participant age. |
| `gender` | — | Participant gender (Female / Male / Non-binary / Transgender / Other / Prefer not to say). |

### Other configurable settings (in the experiment-settings code component)

| Parameter | Default | Description |
| :--- | :--- | :--- |
| Trials per condition | 10 | Gives 40 trials per task block (10 × 2 sequence types × 2 trial types). |
| Minimum correct to advance | 2 | Correct responses required per condition to pass the practice block. |

### Counterbalancing

Sequence type assignment across task blocks is counterbalanced automatically from the participant ID:

| Participant ID parity | Block 2 | Block 3 |
| :--- | :--- | :--- |
| Even | Simple sequence | Complex sequence |
| Odd  | Complex sequence | Simple sequence |

### Handedness

The participant's dominant hand is selected on the **first screen of the experiment** (not the startup dialog). This determines which conditions file (`conditions_left.xlsx` or `conditions_right.xlsx`) and which instruction slides are loaded.

### Testing without full-screen

Go to **Experiment Settings** (cogwheel) → Screen → uncheck **Full-screen window**. Re-enable before deploying to Pavlovia.

---------------------------------------

## PARTICIPANT WORKFLOW

Once started, the experiment guides the participant through each stage without further supervision.

1. **Language selection:** Selected via the startup dialog (on Pavlovia, participants see this as the first screen).
2. **Welcome screen:** Brief task description. The participant selects their dominant hand.
3. **Instructions:** A series of slides (filtered by handedness) explaining the task, the key mapping (F G H J), and the distinction between execution and imagery trials. SPACE advances each slide.
4. **Practice block (Block 1):** Criterion-based. All 4 conditions are presented in fixed order (simple-execution, simple-imagery, complex-execution, complex-imagery). Per-key feedback boxes and accuracy feedback are shown after each trial. Participants must achieve at least 2 correct responses per condition to advance.
5. **Task block 1 (Block 2):** No feedback. Trials from the participant's assigned sequence type (simple or complex). Followed by 8 VAS self-assessment questions.
6. **Task block 2 (Block 3):** Same structure, complementary sequence type. Followed by another self-assessment.
7. **Goodbye:** Brief thank-you screen.

### iFST trial procedure

Each trial follows this sequence:

1. **Pre-trial prompt** (SPACE to begin): colour-coded text indicates execution (blue) or imagery (purple) trial.
2. **Stimulus screen:** The sequence diagram is shown at the centre. Four response boxes aligned with keys **F G H J** appear at the bottom.
3. **Response collection:** The participant presses the required number of keys (8 for execution, 2 for imagery). In the practice block, each keypress briefly illuminates the corresponding box.
4. **Feedback (practice only):** Accuracy feedback is displayed, accompanied by an auditory cue.

### Self-assessment questionnaire

After each task block, 8 questions are presented sequentially on a 0–10 visual analogue scale (slider). Questions cover motor imagery quality (vividness, kinesthetic experience, visual perspective, errors). Responses are stored in `slider.rating`.

---------------------------------------

## OUTPUT

Online data is saved to Pavlovia and can be downloaded from the Pavlovia dashboard as a `.csv` file per participant, named `<participant>_<date>.csv`. It contains every variable encoded in the experiment — one row per trial event (trials and self-assessment responses are interleaved).

An example data processing script in R (`Example data processing.R`) is provided in the experiment folder.

### Variable documentation

#### Trial rows

| Variable | Type | Description |
| :--- | :--- | :--- |
| `participant` | character/numeric | Participant ID from the startup dialog. |
| `session` | character/numeric | Session ID from the startup dialog. |
| `blocks_loop.thisN` | integer | Block loop index (0 = practice; > 0 = task blocks). |
| `hand` | string | Dominant hand selected by the participant (`'left'` / `'right'`). |
| `sequence_type` | string | `'simple'` or `'complex'`. |
| `trial_type` | string | `'execution'` or `'imagery'`. |
| `sequence_code` | string | Target key sequence (e.g., `'fghjjhgf'`). |
| `seq_resp.keys` | list | Keys pressed by the participant (Python/JS list format). |
| `seq_resp.rt` | list | Response times in seconds for each keypress. Trial duration = last − first value. |
| `counterbalance.group` | integer | Counterbalancing group (0 = simple first, 1 = complex first). |
| `age` | string | Participant age from the startup dialog. |
| `gender` | string | Participant gender from the startup dialog. |

#### Self-assessment rows (one per question, after each task block)

| Variable | Type | Description |
| :--- | :--- | :--- |
| `slider.rating` | numeric (0–10) | Response on the visual analogue scale. |

---------------------------------------

Before collecting data online, always run a full pilot test on the target browsers, check the data download from Pavlovia, and verify the R processing output. PsychoPy version updates may require adjustments to the experiment file.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. (2026)](https://link.springer.com/article/10.3758/s13428-026-03002-3) when using this resource.
