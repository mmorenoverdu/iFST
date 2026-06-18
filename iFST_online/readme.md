# IMAGINED FINGER SEQUENCE TASK (iFST)

**Author:** Marcos Moreno Verdu, 18/06/2026  
**Software used:** PsychoPy 2025.2.4 (or superior)
**Experiment Type:** Hybrid (Local and Online, via [Pavlovia](https://pavlovia.org/))  
**Languages supported:** English (EN) = default, Spanish (ES), French (FR) and German (DE). Further languages can be added with no code changes (see [Language Localisation](#language-localisation)).

---------------------------------------

## GENERAL INSTRUCTIONS

This experiment is built using [PsychoPy](https://www.psychopy.org/) (Builder) and is intended for **both local and online execution** (via Pavlovia). Please make sure you are running a compatible PsychoPy version, as other versions might behave unexpectedly.

This README is not intended to explain how PsychoPy generally works, but rather the specific aspects of this **iFST** implementation. If you have never used PsychoPy before, please refer to the [documentation](https://www.psychopy.org/documentation.html) on their website, or available tutorials — especially regarding conditions files, variables, routines, and loops. This will save you time if you decide to modify any parameters of this experiment.

This README specifically details the structure and customization of this **iFST** implementation.

---------------------------------------

## SETUP INSTRUCTIONS

To run this task, you need to have **PsychoPy** installed. There are no other dependencies for local use.

The data output **must** be processed to obtain meaningful information. An example of data processing (in R) is provided in the experiment folder.

**Step-by-step instructions (local):**
1. **Download** all files from the repository.
2. **Unzip** the files into a **new** folder, making sure it contains no other PsychoPy experiments.
3. **Open** the file `iFST.psyexp` in PsychoPy.
4. **Run** the experiment locally and **process the data** using the script provided.

**Additional steps if running online (via Pavlovia):**
5. **Link** your Pavlovia account in the Pavlovia tab, if you haven't already.
6. **Click** "No project" in the Pavlovia tab to start linking the experiment to a new Pavlovia project, and **follow** the procedure PsychoPy indicates.
7. **Check** your Pavlovia dashboard — the project should now appear there under the same name as your PsychoPy experiment.
8. **Change** the mode from inactive to Pilot.
9. **Click** Pilot to run the experiment online.
10. **Process the data** using the script provided, after retrieving it from Pavlovia.

---------------------------------------

## LANGUAGE LOCALISATION

This experiment uses two external spreadsheet files to manage on-screen text and translations:
- `language_localiser.xlsx` — the available language localisations.
- `messages.xlsx` — the list of messages used as variables to display text on screen.

The language can be selected via the PsychoPy startup dialog (Experiment Settings → Basic → Experiment Info → `language` field) **before every run, whether local or online**. These language names must exactly match the entries in the `language` column of `language_localiser.xlsx`.

All text components that should update dynamically by language must have their "Text" field set to **"Set to every repeat."** This allows the displayed text to update dynamically from the corresponding language variable.

### How language switching works

The routine `load language` (wrapped in a loop of the same name) contains a single code component, split into two tabs:
- **Begin Experiment:** creates a variable holding the ISO code to use, defaulting to English (`EN`).
- **Begin Routine:** updates that ISO code based on the participant's choice in the startup dialog.

This code auto-translates to JS, so it functions both locally and online.

The routine `update messages` (wrapped in a loop of the same name) also contains a single code component, located only in its **Begin Routine** tab:
- Creates variables to iterate across `messages.xlsx`.
- Iterates across the list of messages and updates their values according to the current ISO code (set by `load language`).
- Exposes every message as a global variable, using Python's `globals()` locally and JS's `window[]` online.

Once this runs, every message is available as a global variable, ready for text presentation.

Every text component's "Text" field holds a variable name (e.g., `welcome_msg`), which is automatically updated based on the language choice. This name **must already exist** as a message in `messages.xlsx` before the experiment is launched.

> **Tip:** `language_localiser.xlsx` and `messages.xlsx` are both imported automatically by PsychoPy as conditions files for their respective loops. If the number of rows in `language_localiser.xlsx` doesn't match the number of conditions PsychoPy detects in the `load language` loop, click on the loop and refresh the Excel sheet using the green refresh arrows.

### Adding a new language

#### 1. Open the relevant files
- `language_localiser.xlsx`
- `messages.xlsx`

#### 2. Extend `language_localiser.xlsx` by adding a new row

The file must contain the columns:
- `language`
- `ISO_code`

Example:

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |

Add your new language (e.g., Chinese) in a new row:

| language | code |
| :--- | :--- |
| English | EN |
| Spanish | ES |
| French | FR |
| German | DE |
| Chinese | CH |

#### 3. Extend `messages.xlsx` by adding a new column

The file must contain:
- a `message` column (variable names used inside PsychoPy), and
- one column per language (named by *ISO_code*).

Example:

| message | EN | ES | 
| :--- | :--- | :--- |
| welcome_msg | Welcome! | Bienvenido! | 
| adv_msg | Press SPACE to continue | Presiona ESPACIO para continuar | 

Add a new column titled with your new code (e.g., `IT`) and provide a translation for every message key:

| message | EN | ES | IT |
| :--- | :--- | :--- | :--- |
| welcome_msg | Welcome! | Bienvenido! | Benvenuti al compito! |
| adv_msg | Press SPACE to continue | Presiona ESPACIO para continuar | Premi SPAZIO per continuare |

⚠️ Do this consistently for **all** message keys used by the experiment!

#### 4. Update the experiment
1. Open `.psyexp` in PsychoPy.
2. Go to **Experiment Settings** (cogwheel icon) → Basic → Experiment Info.
3. Update the `language` entry by adding your new language name (e.g., `Italian`). It must exactly match the entry in `language_localiser.xlsx`.
4. Save the experiment.

> ⚠️ **Important:** Do not change folder or file names. Do not rename variables. Do not move files after decompressing the repository. The experiment depends on exact paths and identifiers. Moving or renaming files may cause crashes.

---------------------------------------

## TECHNICAL DETAILS

The decompressed repository includes:
- `iFST.psyexp` — main PsychoPy experiment file
- `language_localiser.xlsx` — language configuration file
- `messages.xlsx` — the list of messages used as variables to display text on screen
- `instructions.xlsx` — instructions text and images, with one column set per language (suffixes `_EN`, `_ES`, etc.) and per handedness; filtered dynamically based on the participant's reported handedness. To add a language, create a new set of columns with your own suffix (e.g., `_YOURCODE`) and provide translations.
- `conditions_**.xlsx` — encodes the trial-level variables for the task, in separate files/sheets for left- and right-hand stimuli:
  - `hand`: which hand this stimulus belongs to (used to filter dynamically in PsychoPy).
  - `stim`: which unique stimulus this is (2 sequences × 2 conditions = 4).
  - `sequence_code`: the actual key-sequence string, depending on handedness, condition, and sequence type.
  - `sequence_type`: simple or complex.
  - `trial_type`: execution or imagery.
  - `key_presses`: number of keys to be typed (8 for execution = full sequence; 2 for imagery = first and last elements only).
  - `sequence_picture`: image shown while typing/imagining the sequence.
  - `prompt_before`: text shown before the trial, indicating whether it's an execution or imagery trial (language-localised).
  - `prompt`: similar text, shown on screen **during** the trial.
- `self_assess_questions.xlsx` — qualitative questions (11-point rating scales) answered after each main task block, language-localised via the same suffix convention:
  - `self_assess_question_**`: the question text.
  - `label_min_**` / `label_middle_**` / `label_max_**`: labels for the minimum (0), midpoint, and maximum (10) ratings.
- a data-processing script in R.

**Folder `stimuli`:**
- Images of finger sequences (simple/complex) for both left and right hands. Only the stimuli matching the participant's reported dominant hand are shown.

**Folder `images`:**
- Images displayed in the instructions.

**Folder `data`:**
- Storage location for output data when running locally.

---------------------------------------

## EXPERIMENT SETTINGS (parameters to choose)

Unlike the HLJT readmes, most of this experiment's settings are **not** exposed in the startup dialog — they're hardcoded in the experiment-settings routine and must be edited directly in PsychoPy.

### Available Parameters (startup dialog)

| Variable | Options | Description |
| :--- | :--- | :--- |
| `participant` | Free text/number (optional) | ID of the participant. |
| `session` | Free text/number (optional) | ID of the session. |
| `language` | • **English** (Default)<br>• Spanish<br>• French | Sets the language of the experiment; selectable both locally and online. |
| `age` | Free entry | Participant age. |
| `gender` | Female/Male/Non-binary/Trans-gender/Other/Prefer not to say | Participant gender. |

### Other configurable settings (not in the startup dialog)

- **Trials per condition:** set in the experiment-settings routine/code (default 10, giving 40 trials total: 10 × 2 sequence types × 2 trial types).
- **Minimum correct responses to advance the practice block:** also set in the experiment-settings routine (source only states "at least 2 correct responses per condition" as the default; exact variable name not given).
- **Preferred/dominant hand:** chosen by the participant on the **first screen of the experiment itself** (not the startup dialog) — this determines which stimulus set (left- or right-hand sequences) is used for the remainder of the task.

If you want to modify the task's core parameters (e.g., sequence types), you'll need to create your own stimuli (images, text, etc.) — these aren't provided for every possible variation.

---------------------------------------

## PARTICIPANT WORKFLOW

Once the experiment starts, it guides the participant through it without the need for further supervision.

1. **Welcome screen:** A brief description of the task; the participant also selects their preferred (dominant) hand here.
2. **Instructions:** A couple of screens explaining the task, filtered based on the selected handedness.
3. **Practice Block:** All 4 conditions (simple/complex × execution/imagery), always presented in this fixed order — simple-execution, simple-imagery, complex-execution, complex-imagery — to help participants understand the differences between conditions.
   - Online feedback is given via 4 small boxes at the bottom of the screen (one per finger), showing which key was pressed, plus accuracy feedback per trial.
   - Participants must achieve at least 2 correct responses per condition (printed on screen) to advance to the main task blocks.
4. **Main Task Blocks** (2 total — one per sequence type, simple/complex — order randomized via a counterbalance routine):
   - Execution and imagery trials always alternate within a block; on-screen text indicates which type each trial is.
   - No online or offline feedback is given during these blocks.
   - At the end of each block, participants complete the self-assessment questions (see Output).
5. **Completion:** Goodbye screen.

#### iFST trial procedure
1. A pre-cue, color-coded text indicates whether the next trial is a physical or imagined trial.
2. The individual presses SPACE to start the trial
3. The trial shows the diagram of the sequence to be executed/imagined, alongside with a color-coded text indicating the task to do.
4. The trial does not finish until the required number of key presses is registered (e.g. 8 for execution, 2 for imagery).
	→ *Automatic advance to the next trial.*

---------------------------------------

## OUTPUT

Output is saved as a `.csv` file in a `data/` subfolder, always named using the participant field and the date, containing every variable encoded in the experiment.

An example script for data processing in R is provided in the experiment folder.

> **Note:** This script relies on the standard PsychoPy output structure, expecting a participant ID column (`participant`) and the response columns `seq_resp.rt` and `seq_resp.keys`, plus the conditions-file columns `hand`, `sequence_type`, `trial_type`, and `sequence_code`, and (for self-assessments) `slider.rating`. 
### Variable Documentation

#### 1. Task Block Trials Data

*One row per trial*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `participant` | character/numeric | Participant ID, as entered in the startup dialog. |
| `session` | character/numeric | Session ID, as entered in the startup dialog (if used). |
| `hand` | factor | Dominant hand selected by the participant ("left"/"right"); also used to filter stimuli. |
| `sequence_type` | factor | "simple" or "complex". |
| `trial_type` | factor | "execution" or "imagery". |
| `sequence_code` | character | The key sequence for that trial. |
| `seq_resp.rt` | list (numeric, one value per key press) | Response times, in **seconds**, for each key press in the trial. Trial duration = last − first value. |
| `seq_resp.keys` | list (character, one value per key press) | The actual keys pressed during the trial. |

#### 2. Self-Assessment Data

*One row per question, per main task block*

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `slider.rating` | numeric (0–10) | Response to each self-assessment question, given on an 11-point scale, after each of the 2 main task blocks. |

#### 3. Demographic Data

| Variable Name | Type | Description |
| :--- | :--- | :--- |
| `age` | integer | Participant age in years. |
| `gender` | character | Gender (options: Female, Male, Non-binary, Trans-gender, Other, Prefer not to say). |
| `handedness` | character | Hand dominance (options: Left, Ambidextrous, Right). |

---------------------------------------

PsychoPy version updates may require adjustments. Developers are not responsible for adapting the task to every use case.
Before collecting data, always test the experiment and check the data output.
Contributions are welcome.

---------------------------------------

## REFERENCE

Please cite [Moreno-Verdú et al. (2026)](https://link.springer.com/article/10.3758/s13428-026-03002-3) when using this resource.
