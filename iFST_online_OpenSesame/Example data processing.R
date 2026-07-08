##### EXAMPLE OF OUTPUT PROCESSING FROM IMAGINED FINGER SEQUENCE TASK (iFST) ####
## Online version (OpenSesame / OSWeb backend, deployed via JATOS)

## The data processing consists in the following steps:
## 1. Select the necessary columns
## 2. Filter the necessary rows (those from the task blocks)
## 3. Generate summary (accuracy and sequence completion time)
## 4. Process self-assessment data
## 5. Export data

# Load packages -----------------------------------------------------------

# you need to have the following packages installed:
library(tidyverse) # to read and wrangle data
library(this.path) # to set path automatically
library(openxlsx)  # to export to Excel sheet

# Load data ---------------------------------------------------------------

# this sets the working directory to the location of the script
setwd(here())

# JATOS exports result data per participant as plain text (CSV format).
# To download: JATOS interface → your study → Results → Export → Result Data.
# Place the exported CSV file(s) in a 'data/' subfolder, or adjust the path below.
# If JATOS exports a combined file with multiple participants, use read_csv() and
# bind_rows() to combine them, or process files individually.
data_raw <- read_csv("data/subject-1.csv")

# inspect the data
str(data_raw)

# Parameters --------------------------------------------------------------

# Participant-level parameters (one row per participant)
# Note: group, handedness, lang_code, age_response, gender_response are logged by
# OpenSesame as variables and will appear in the file after a full run.
parameters <- data_raw |>
  select(subject_nr, datetime,
         any_of(c("group", "handedness", "lang_code",
                   "age_response", "gender_response"))) |>
  slice(1)

# Separate trial rows from self-assessment rows ---------------------------

# Trial rows have seq_acc set; self-assessment rows have self_assess_construct set.
data_trials_raw <- data_raw |>
  filter(!is.na(seq_acc) & seq_acc != "")

data_sa_raw <- data_raw |>
  filter(!is.na(self_assess_construct) & self_assess_construct != "")

# Process trial data ------------------------------------------------------

# Select columns, filter to task blocks, and rename for clarity.
# Unlike the PsychoPy version, OpenSesame already computes seq_acc (0/1)
# and seq_time (seconds from first to last keypress) — no string parsing needed.
# Timestamps in seq_resp_rt are captured with Date.now() in the browser (ms precision).
data <- data_trials_raw |>
  select(subject_nr,
         block      = block_iter,      # block index (1 = practice, 2-3 = task)
         block_type,                   # 'practice' or 'task'
         any_of(c("handedness")),      # 'left' or 'right' (present in full runs)
         sequence   = sequence_type,   # 'simple' or 'complex'
         condition  = trial_type,      # 'execution' or 'imagery'
         code       = sequence_code,   # target key sequence (e.g., 'fghjjhgf')
         typed      = seq_typed,       # keys actually pressed
         correct    = seq_acc,         # 1 = correct, 0 = incorrect
         seq_time,                     # duration from first to last keypress (s)
         seq_resp_keys,                # semicolon-separated keys pressed
         seq_resp_rt) |>               # semicolon-separated RTs from trial onset (s)
  # retain only task blocks (remove practice)
  filter(block_type == "task") |>
  mutate(correct  = as.integer(correct),
         seq_time = as.numeric(seq_time))

# Obtain summary ----------------------------------------------------------

# What is the accuracy (i.e. proportion of correct sequences) by the factors?
accuracy <- data |>
  group_by(condition, sequence) |>
  summarise(mean = mean(correct, na.rm = TRUE) * 100) |>  # express as percentage
  mutate(mean = round(mean, digits = 2))

# What is the sequence completion time by the factors?
# We only consider CORRECT trials for this analysis.
time <- data |>
  filter(correct == 1) |>  # retain only correct trials
  group_by(condition, sequence) |>
  summarise(n    = n(),
            mean = mean(seq_time, na.rm = TRUE)) |>
  mutate(mean = round(mean, digits = 2))

# Process self-assessment data --------------------------------------------

# Self-assessment rows contain one response per VAS question per block.
# There are 8 questions after each task block (blocks 2 and 3).
data_sa <- data_sa_raw |>
  select(subject_nr,
         block     = block_iter,
         construct = self_assess_construct,  # question construct label
         response  = sa_response) |>         # 0-10 VAS response
  mutate(response = as.numeric(response))

# Summary of self-assessment responses across blocks
sa_summary <- data_sa |>
  group_by(construct) |>
  summarise(mean = mean(response, na.rm = TRUE),
            sd   = sd(response, na.rm = TRUE)) |>
  mutate(across(where(is.numeric), ~ round(.x, digits = 2)))

# Export ------------------------------------------------------------------

# Trial data
write_csv(data, "data_processed.csv")

# All sheets in one Excel file
write.xlsx(list(trials          = as.data.frame(data),
                self_assessment = as.data.frame(data_sa),
                accuracy        = as.data.frame(accuracy),
                time            = as.data.frame(time),
                sa_summary      = as.data.frame(sa_summary)),
           "data_processed.xlsx")
