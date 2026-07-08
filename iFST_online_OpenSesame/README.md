# IMAGINED FINGER SEQUENCE TASK (iFST) — Online version (OpenSesame / OSWeb)

**Author:** Marcos Moreno Verdú  
**Software:** OpenSesame 4.1.9 · OSWeb backend · Deployed via JATOS  
**Experiment type:** Online (browser-based)  
**Languages supported:** English (EN) · Spanish (ES) · French (FR) · German (DE)

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built with [OpenSesame](https://osdoc.cogsci.nl/) 4.1.9 using the **OSWeb** backend, which compiles the experiment to JavaScript and runs it in a standard web browser. Deployment is handled through [JATOS](https://www.jatos.org/) (Just Another Tool for Online Studies).

All experiment logic is written as **inline JavaScript** (`inline_javascript` items). Because OSWeb does not support `await` inside item run phases, input collection is handled exclusively through dedicated OpenSesame items (`keyboard_response`, `mouse_response`, `sampler`) rather than JS polling loops.

If you are unfamiliar with OpenSesame or OSWeb, refer to the [documentation](https://osdoc.cogsci.nl/) on their website.

---------------------------------------

## SETUP INSTRUCTIONS

**Requirements:** OpenSesame 4.1.9 or later · a JATOS server (for online deployment) · Chrome or Firefox (recommended browsers for participants).

### Testing locally

1. **Install** OpenSesame 4.1.9 or later.
2. **Open** `iFST_online.osexp`.
3. Verify the backend is set to **OSWeb** in General Properties.
4. Click **Run in browser** (the globe icon) to test in your default browser.

### Deploying online via JATOS

1. In OpenSesame, go to **Tools → OSWeb → Export experiment as JATOS study**.
2. **Upload** the resulting `.zip` to your JATOS instance.
3. **Add** the study to a batch worker, generate participant links, and distribute.
4. **Download data** from the JATOS interface after data collection.

> **⚠️ Browser compatibility:** Chrome and Firefox are fully supported. Safari may have issues with audio autoplay policy.

> **⚠️ File paths:** Do not rename or move any files or subfolders. The experiment locates pool resources by filename; the folder structure on disk mirrors the pool layout for maintainability.

> **⚠️ Updating pool files:** If you edit any CSV, PNG, or WAV file on disk, you must also update the copy inside `iFST_online.osexp`. Open the file in OpenSesame → **File Pool** panel → select the file → replace. Alternatively, use a Python patcher script.

---------------------------------------

## LANGUAGE LOCALISATION

All on-screen text is loaded at runtime from `messages.csv`. Participants select their language at the start of the experiment via a form (`language_form`); `setup_script` then reads `language_localiser.csv` to resolve the ISO code and loads all message strings into `vars.*`.

### How language switching works

`setup_script` calls `readPoolCsv('messages.csv')` and iterates over every row. For each row, `vars[row.message]` is set to the value in the column matching the participant's ISO code, falling back to `EN` if a translation is missing.

### Adding a new language

#### 1. Update `language_form`

In OpenSesame, open `language_form` and add the new language name (e.g., `Italiano`) to the options list in the widget properties.

#### 2. Add a row to `language_localiser.csv`

```csv
language,ISO_code
...
Italiano,IT
```

#### 3. Add a column to `messages.csv`

Each row is one message key; each column after the first is a language identified by its ISO code. Add a new column `IT` and provide a translation for every row. Missing entries fall back to `EN`.

| message | EN | ES | … | IT |
| :--- | :--- | :--- | :--- | :--- |
| welcome_msg | Welcome to the experiment! | ¡Bienvenido/a! | … | Benvenuto! |
| adv_msg | Press SPACE to continue | Presiona ESPACIO | … | Premi SPAZIO |

#### 4. Add columns to `ifst_files/self_assess_questions.csv`

Add four new columns per question following the naming pattern:

| Column | Description |
| :--- | :--- |
| `self_assess_question_IT` | Question text |
| `label_min_IT` | Anchor label for the minimum (0) |
| `label_middle_IT` | Anchor label for the midpoint (5) |
| `label_max_IT` | Anchor label for the maximum (10) |

#### 5. Update the pool

Replace the updated CSV files in `iFST_online.osexp` via the File Pool panel.

> **⚠️ Text formatting:** In `messages.csv`, use `\n` (literal backslash-n) for line breaks. The `draw_paragraphs()` helper handles word-wrapping automatically. HTML tags are **not** supported in OSWeb canvas text.

> **⚠️ Key names:** Do not change the `message` column or any variable names. The experiment looks up strings by exact key name.

---------------------------------------

## TECHNICAL DETAILS

### Folder structure

```
iFST_online_OpenSesame/
│
├── iFST_online.osexp               ← Main experiment file (self-contained archive)
│
├── language_localiser.csv          ← Maps language names → ISO codes
├── messages.csv                    ← All localised text strings (one key per row)
│
├── ifst_files/
│   ├── conditions_left.csv         ← Trial conditions (left hand)
│   ├── conditions_right.csv        ← Trial conditions (right hand)
│   ├── instructions.csv            ← Instruction slide content + image paths
│   └── self_assess_questions.csv   ← VAS question texts and anchor labels
│
├── ifst_images/                    ← Instruction slide images (sequence diagrams)
│   └── seq_*.png  (10 files)
│
└── ifst_stimuli/                   ← Trial stimulus images + audio feedback
    ├── simple_execution_left.png
    ├── simple_execution_right.png
    ├── complex_execution_left.png
    ├── complex_execution_right.png
    ├── simple_imagery_left.png
    ├── simple_imagery_right.png
    ├── complex_imagery_left.png
    ├── complex_imagery_right.png
    ├── correct_sound.wav           ← Must be 48 000 Hz PCM
    └── incorrect_sound.wav         ← Must be 48 000 Hz PCM
```

### The file pool

`iFST_online.osexp` is a **self-contained gzip-tar archive**. Inside it, a flat `pool/` directory contains every resource the experiment needs at runtime — all CSVs, PNGs, and WAV files — without subdirectories. The folder structure above is maintained on disk for readability only.

At runtime, `setup_script` calls `readPoolCsv(filename)` to access CSV files by their bare filename. The `sequence_picture` values in `conditions_*.csv` and the `inst_pic` values in `instructions.csv` include a directory prefix (`ifst_stimuli/`, `ifst_images/`) for local readability; at runtime the experiment calls `basename()` on these paths so only the filename is used to access the pool.

### Key files

| File | Description |
| :--- | :--- |
| `iFST_online.osexp` | Main experiment file. Open in OpenSesame to run or modify. Self-contained: all pool resources are embedded. |
| `messages.csv` | One row per message key, one column per language. Loaded at startup. |
| `language_localiser.csv` | Maps the full language name to its ISO code. |
| `ifst_files/conditions_left.csv` | Trial conditions for left-handed participants. Columns: `hand`, `stim`, `sequence_code`, `sequence_type`, `trial_type`, `key_presses`, `sequence_picture`. |
| `ifst_files/conditions_right.csv` | Same structure for right-handed participants. |
| `ifst_files/instructions.csv` | Instruction slide content: text per language, image path (`inst_pic`), image layout fractions (`image_w`, `image_h`, `text_x`). Filtered at runtime by handedness. |
| `ifst_files/self_assess_questions.csv` | 8 self-assessment questions with texts and anchor labels for each language. |
| `ifst_stimuli/correct_sound.wav` | Auditory feedback for correct responses (practice block). |
| `ifst_stimuli/incorrect_sound.wav` | Auditory feedback for incorrect responses (practice block). |

> **⚠️ Audio:** Both WAV files must be at **48 000 Hz** to match `set sound_freq 48000` in the experiment settings. Re-sample with `ffmpeg` if you replace them: `ffmpeg -i input.wav -ar 48000 output.wav`

### Implementation notes

- All inline scripts are **JavaScript** (`inline_javascript` items).
- `await` is never used in run phases. All input collection uses `keyboard_response`, `mouse_response`, or `sampler` items.
- Audio feedback is played via two `sampler` items (`fb_sound_correct`, `fb_sound_incorrect`) with `run_if` conditions, replacing any JS-based audio playback.
- The self-assessment scale uses a `mouse_response` item (`sa_mouse`) inside a loop (`sa_input_loop`) that checks click position in `sa_update_script` and exits when `vars.sa_confirmed = 'yes'`.
- OSWeb does not support `Canvas.text({html: true})`. All multi-line text is rendered by `draw_paragraphs(canvas, text, x, y, max_width, style)`, defined in `setup_script`. The entire canvas is rebuilt from scratch on every update (individual element properties cannot be modified after drawing).
- `clock` is not available in OSWeb JavaScript. Timestamps are captured with `Date.now()`.

---------------------------------------

## EXPERIMENT SETTINGS

Global parameters are set in the **Prepare phase** of `exp_settings_script`. Open that item in OpenSesame and edit the `Global experiment parameters` section.

### Available parameters

| Variable | Default | Description |
| :--- | :--- | :--- |
| `n_reps` | `1` | Repetitions of the conditions file per task block. With 4 conditions and `n_reps = 1`, each task block contains 2 executed trials. |
| `practice_blocks` | `1` | Number of practice blocks. |
| `task_blocks` | `2` | Number of task blocks. |
| `total_blocks` | `3` | Total blocks (`practice_blocks + task_blocks`). |
| `target_per_stim` | `1` | Correct trials required per stimulus to exit the practice block. |

### Counterbalancing

Sequence type assignment across task blocks is determined automatically from `subject_nr`:

| `subject_nr` parity | `group` | Block 2 | Block 3 |
| :--- | :--- | :--- | :--- |
| Even | `0` | Simple sequence | Complex sequence |
| Odd  | `1` | Complex sequence | Simple sequence |

`group` is computed in `exp_settings_script` and does not need to be set manually.

### Changing the defaults

1. Open `exp_settings_script` in the Overview panel.
2. Select the **Prepare** tab.
3. Edit the variable assignments in the `Global experiment parameters` section.

```javascript
vars.target_per_stim = 3;    // require 3 correct trials per stimulus
```

> **⚠️** Only modify the parameters section. Do not alter other parts of the script unless you are familiar with the experiment logic.

### Screen scaling

`vars.sc = Math.min(width / 1024, height / 768)` is computed once in `exp_settings_script`, using the browser window dimensions (`width` and `height`) provided by OSWeb. All pixel coordinates throughout the experiment are multiplied by `sc`, making the layout resolution-independent.

### Testing without full-screen

Click **Run in browser** in OpenSesame. OSWeb runs in a browser tab; there is no forced full-screen mode during local testing. Full-screen behaviour in deployed studies depends on JATOS and browser configuration.

---------------------------------------

## PARTICIPANT WORKFLOW

Once started, the experiment guides the participant through each stage without further supervision.

1. **Language selection:** The participant selects one of four languages (EN / ES / FR / DE) from a dropdown form and clicks OK. All subsequent text is displayed in the chosen language.
2. **Demographics:** Age (text entry) and gender (multiple choice).
3. **Handedness:** The participant selects Left-handed or Right-handed. This determines which conditions file is loaded and which instruction slides are shown.
4. **Instructions:** A series of slides (filtered by handedness) explains the task, the key mapping (F G H J), and the distinction between execution and imagery trials. SPACE advances each slide.
5. **Practice block (Block 1):** Criterion-based. Trials repeat (up to 30 cycles) until each stimulus has been performed correctly `target_per_stim` times. Colour-coded accuracy feedback and auditory feedback are provided after every trial. No self-assessment after this block.
6. **Task block 1 (Block 2):** No feedback. Trials from the participant's assigned sequence type (simple or complex). Followed by 8 VAS self-assessment questions.
7. **Task block 2 (Block 3):** Same structure, complementary sequence type. Followed by another self-assessment.
8. **Goodbye:** A brief thank-you message is displayed for 3 seconds.

### iFST trial procedure

Each trial follows this sequence:

1. **Pre-trial prompt** (SPACE to begin): purple screen = imagery trial; blue screen = execution trial.
2. **Stimulus screen:** The sequence diagram is shown at the centre. Four response boxes aligned with keys **F G H J** appear at the bottom.
3. **Response collection:** The participant presses the required number of keys (8 for execution, 2 for imagery). In the practice block, the pressed key's box briefly lights up after each press (100 ms flash via `box_flash_wait` keyboard_response timeout).
4. **Feedback (practice only):** A colour-coded message shows accuracy, execution time, and criterion progress. Displayed for 3 s (correct) or 5 s (incorrect), accompanied by an auditory cue. Advance is automatic.

### Self-assessment questionnaire

After each task block, 8 questions are presented sequentially on a 0–10 visual analogue scale. Questions cover aspects of motor imagery quality (vividness, kinesthetic experience, visual perspective, errors). The participant clicks a point on the scale to select a value, then clicks the **Next** button (which appears only after a selection) to confirm and advance. The interaction loop (`sa_input_loop`) runs at most 200 iterations and exits when `vars.sa_confirmed = 'yes'`. Responses are stored in `sa_response`.

---------------------------------------

## OUTPUT

JATOS writes results to its database. Download data from the JATOS interface after data collection. Each row in the exported file is either a trial row or a self-assessment row.

> **Note:** Only trials where `run_trial = 'yes'` are logged. Skipped trials (wrong sequence type in task blocks, or stimulus already at criterion in practice) are not written to the file.

### Variable documentation

#### Trial rows (`block_type = 'practice'` or `'task'`)

| Variable | Type | Description |
| :--- | :--- | :--- |
| `subject_nr` | integer | Participant ID, set at experiment launch. |
| `datetime` | string | Date and time of the logged event. |
| `block_iter` | integer | Block index (1 = practice, 2–3 = task). |
| `block_type` | string | `'practice'` or `'task'`. |
| `trial_type` | string | `'execution'` or `'imagery'`. |
| `stim` | integer | Stimulus ID (1–4). |
| `sequence_code` | string | Target key sequence (e.g., `'fghjjhgf'`). |
| `sequence_type` | string | `'simple'` or `'complex'`. |
| `key_presses` | integer | Keys required (8 execution / 2 imagery). |
| `feedback` | integer | 1 = feedback shown (practice), 0 = no feedback (task). |
| `run_trial` | string | Always `'yes'` in logged rows. |
| `seq_typed` | string | Keys the participant actually pressed. |
| `seq_acc` | integer | 1 = correct sequence, 0 = incorrect. |
| `seq_time` | float | Time from first to last keypress (s). `999.0` if fewer than 2 presses. |
| `seq_resp_keys` | string | Semicolon-separated keys pressed (e.g., `'f;g;h;j;j;h;g;f'`). |
| `seq_resp_rt` | string | Semicolon-separated RTs in seconds from trial onset (captured with `Date.now()`). |
| `crit_counter` | integer | Correct-trial count for this stimulus in practice (blank in task rows). |
| `task_trial_count` | integer | Executed-trial count in this task block (blank in practice rows). |
| `group` | integer | Counterbalancing group (0 = simple first, 1 = complex first). |
| `handedness` | string | `'left'` or `'right'`. |
| `lang_code` | string | ISO code of the selected language. |
| `age_response` | string | Participant's age entry. |
| `gender_response` | string | Participant's gender selection. |
| `self_assess_construct` | string | Blank in trial rows. |
| `sa_response` | blank | Blank in trial rows. |

#### Self-assessment rows (one per question, after each task block)

| Variable | Type | Description |
| :--- | :--- | :--- |
| `subject_nr` | integer | Participant ID. |
| `datetime` | string | Timestamp of the logged event. |
| `block_iter` | integer | Block index (2 or 3). |
| `block_type` | string | Always `'task'`. |
| `self_assess_construct` | string | Short label for the question construct (e.g., `'overall_vividness'`). |
| `sa_response` | integer | Response on the 0–10 visual analogue scale. |

All trial-level variables are blank in self-assessment rows, and vice versa.

---------------------------------------

Before collecting data, test the experiment end-to-end in the target browser, verify localised text, audio feedback, and JATOS data export. OSWeb and OpenSesame version updates may require adjustments to the experiment file.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. (2026)](https://link.springer.com/article/10.3758/s13428-026-03002-3) when using this resource.
