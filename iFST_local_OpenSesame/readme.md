# IMAGINED FINGER SEQUENCE TASK (iFST) — Local version (OpenSesame / PsychoPy)

**Author:** Marcos Moreno Verdú, 08/07/2026  
**Software:** OpenSesame 4.1.9 · psycho (PsychoPy) backend  
**Experiment type:** Local (runs on the experimenter's computer)  
**Languages supported:** English (EN) · Spanish (ES) · French (FR) · German (DE)

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built with [OpenSesame](https://osdoc.cogsci.nl/) 4.1.9 using the **psycho** (PsychoPy) backend and is intended for **local, in-lab execution**. Make sure you are running OpenSesame 4.1.x or later with the psycho backend available; other versions or backends may behave unexpectedly.

All experiment logic is written as **inline Python scripts**. The experiment runs in **full-screen mode** and automatically detects the monitor resolution at runtime, scaling all visual elements proportionally via a uniform scale factor `sc`. No manual resolution adjustment is needed on different screens.

If you are unfamiliar with OpenSesame, refer to the [documentation](https://osdoc.cogsci.nl/) on their website.

---------------------------------------

## SETUP INSTRUCTIONS

**Requirements:** OpenSesame 4.1.9 or later with the **psycho** backend (requires a working PsychoPy installation).

1. **Download** all files from the repository and place them in a dedicated folder.
2. **Open** `iFST_local.osexp` in OpenSesame.
3. If required, **adapt** the [experiment settings](#experiment-settings) and save the file.
4. Click the **green triangle** (or press Ctrl+R) to run the experiment.
5. The output `.csv` file is generated automatically in the experiment folder as `subject-<subject_nr>.csv` (e.g., `subject-1.csv`). Do not rename it.
6. **Process the data** using the provided R or Python script.

> **⚠️ Full-screen on a new computer:** Every click on **Run** (not Quick Run) opens an "Experiment Settings" dialog (subject number, logfile, **Fullscreen** checkbox) *before* the experiment starts. This checkbox — not the experiment's own `fullscreen` setting in General Properties — is what actually decides whether the window is full-screen, and OpenSesame remembers its state **per computer**. On a computer where it has never been ticked (e.g. a colleague's fresh install), the experiment will run in a window even though it ran full-screen for you. **The fix:** tick **Fullscreen** in that dialog once on each new computer — OpenSesame will then default to full-screen automatically on every subsequent Run on that machine.

> **⚠️ Cloud sync:** If the experiment folder is inside a cloud-synced location (e.g., OneDrive), **pause synchronisation before running**. Active syncing can corrupt the `.csv` file while OpenSesame writes to it.

> **⚠️ File paths:** Do not rename or move any files or subfolders. The experiment locates all resources by relative path from the experiment folder.

---------------------------------------

## LANGUAGE LOCALISATION

All on-screen text is loaded at runtime from `messages.xlsx`. Participants select their language at the start of the experiment; the chosen ISO code is then used to look up the matching column in `messages.xlsx` and `ifst_files/self_assess_questions.xlsx`.

### How language switching works

In `exp_settings_script` (Prepare phase), the helper function `experiment.update_messages(lang_code)` is registered on the experiment object. It iterates over all rows in `messages.xlsx` and sets `var.<key>` to the value in the column matching the chosen language, falling back to `EN` if a translation is missing. The function is called once at startup (defaulting to English) and again in `lang_select_script` when the participant clicks a language button.

### Adding a new language

#### 1. Add a column to `messages.xlsx`

Each row is one message key; each column after the first is a language identified by its ISO code (e.g., `IT`). Add a new column `IT` and provide a translation for every row. Missing entries fall back to `EN`.

| message | EN | ES | … | IT |
| :--- | :--- | :--- | :--- | :--- |
| welcome_msg | Welcome to the experiment! | ¡Bienvenido/a! | … | Benvenuto! |
| adv_msg | Press SPACE to continue | Presiona ESPACIO | … | Premi SPAZIO |

#### 2. Add columns to `ifst_files/self_assess_questions.xlsx`

Add four new columns per language following the naming pattern:

| Column | Description |
| :--- | :--- |
| `self_assess_question_IT` | Question text |
| `label_min_IT` | Anchor label for the minimum (0) |
| `label_middle_IT` | Anchor label for the midpoint (5) |
| `label_max_IT` | Anchor label for the maximum (10) |

#### 3. Update the language selection screen

Open `lang_select_script` in OpenSesame → **Run** tab. Add an entry to the `btns` list and redistribute the x-positions:

```python
btns = [
    ('EN', 'English',   int(-300 * sc)),
    ('ES', 'Español',   int(-150 * sc)),
    ('FR', 'Français',  int(   0 * sc)),
    ('DE', 'Deutsch',   int( 150 * sc)),
    ('IT', 'Italiano',  int( 300 * sc)),  # new language
]
```

> **⚠️ Text formatting:** `messages.xlsx` supports HTML tags (`<b>`, `<br>`, `<i>`, `<span style='color:…'>`). Use `<br>` for line breaks within a cell.

> **⚠️ Key names:** Do not change the `message` column or any variable names. The experiment looks up strings by exact key name.

---------------------------------------

## TECHNICAL DETAILS

### Folder structure

```
iFST_local_OpenSesame/
│
├── iFST_local.osexp                ← Main experiment file
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

`iFST_local.osexp` is a plain-text OpenSesame script file (not an archive). All resource files are referenced by path relative to the experiment folder and must remain in place.

### Key files

| File | Description |
| :--- | :--- |
| `iFST_local.osexp` | Main experiment file. Open in OpenSesame to run or modify. |
| `messages.xlsx` | One row per message key, one column per language. Loaded at startup. |
| `language_localiser.xlsx` | Maps the full language name to its ISO code. |
| `ifst_files/conditions_left.xlsx` | Trial conditions for left-handed participants. Columns: `hand`, `stim`, `sequence_code`, `sequence_type`, `trial_type`, `key_presses`, `sequence_picture`. |
| `ifst_files/conditions_right.xlsx` | Same structure for right-handed participants. |
| `ifst_files/instructions.xlsx` | Instruction slide content: text per language, image path (`inst_pic`), image layout fractions (`image_w`, `image_h`, `text_x`). Filtered at runtime by handedness. |
| `ifst_files/self_assess_questions.xlsx` | 8 self-assessment questions with texts and anchor labels for each language. |
| `ifst_stimuli/correct_sound.wav` | Auditory feedback for correct responses (practice block). |
| `ifst_stimuli/incorrect_sound.wav` | Auditory feedback for incorrect responses (practice block). |

> **⚠️ Audio:** Both WAV files must be at **48 000 Hz** to match `set sound_freq 48000` in the experiment settings. Re-sample with `ffmpeg` if you replace them: `ffmpeg -i input.wav -ar 48000 output.wav`

### Implementation notes

- All inline scripts are **Python** (`inline_script` items with a Run and a Prepare phase).
- Audio feedback is played via `Sampler(path)` followed by `.play()`.
- The self-assessment scale (`self_assess_script`) uses `Mouse.get_click()` with an interaction loop for click-based VAS input.
- Images are loaded with PIL and displayed on an OpenSesame `Canvas` using computed scale factors.

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
| `lang_code` | `'EN'` | Default language ISO code. Participants can override at runtime. |
| `handedness` | `'right'` | Default handedness; overwritten by the participant's choice at the welcome screen. |

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

```python
var.target_per_stim = 3    # require 3 correct trials per stimulus
var.lang_code       = 'ES' # default to Spanish
```

> **⚠️** Only modify the parameters section. Do not alter other parts of the script unless you are familiar with the experiment logic.

### Screen scaling

`pyglet` is used to query the primary screen dimensions at startup. A uniform scale factor `experiment.sc = min(screen_width / 1024, screen_height / 768)` is computed and applied to all pixel coordinates throughout the experiment. If screen detection fails, `sc` defaults to `1.0` (1024 × 768 design resolution).

### Testing without full-screen

Toggling **Full-screen mode** in **Tools → General Properties** does *not* control this in OpenSesame 4.1.9 — that value is overridden every time by the **Fullscreen** checkbox in the "Experiment Settings" dialog that appears on Run (see the full-screen note under [Setup Instructions](#setup-instructions)). To test windowed, simply **untick Fullscreen in that dialog** when you click Run; tick it again before data collection. The checkbox state is remembered per computer, so this only needs doing once each way.

---------------------------------------

## PARTICIPANT WORKFLOW

Once started, the experiment guides the participant through each stage without further supervision.

1. **Language selection:** The participant clicks one of four language buttons (EN / ES / FR / DE). All subsequent text is displayed in the chosen language.
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
3. **Response collection:** The participant presses the required number of keys (8 for execution, 2 for imagery). In the practice block, the pressed key's box briefly lights up after each press (100 ms flash).
4. **Feedback (practice only):** A colour-coded message shows accuracy, execution time, and criterion progress. Displayed for 3 s (correct) or 5 s (incorrect), accompanied by an auditory cue. Advance is automatic.

### Self-assessment questionnaire

After each task block, 8 questions are presented sequentially on a 0–10 visual analogue scale. Questions cover aspects of motor imagery quality (vividness, kinesthetic experience, visual perspective, errors). The participant clicks a point on the scale to select a value, then clicks the **Next** button (which appears only after a selection) to confirm and advance. Responses are stored in `sa_response`.

---------------------------------------

## OUTPUT

A `.csv` file is generated automatically in the experiment folder for each run: `subject-<subject_nr>.csv`. It contains one row per logged event — one per executed trial, or one per self-assessment question.

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
| `seq_resp_rt` | string | Semicolon-separated RTs in seconds from trial onset. |
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

Before collecting data, test the display geometry, key responses, timing, localised text, and CSV output on the target hardware. OpenSesame version updates may require adjustments to the experiment file.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. (2026)](https://link.springer.com/article/10.3758/s13428-026-03002-3) when using this resource.
