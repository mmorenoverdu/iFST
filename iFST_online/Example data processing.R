##### EXAMPLE OF OUTPUT PROCESSING FROM IMAGINED FINGER SEQUENCE TASK (iFST) ####

## The data processing consists in the following steps:
## 1. Select the necessary columns
## 2. Filter the necessary rows (those from the test blocks)
## 3. Generate summary
## 4. Export data

# Load packages -----------------------------------------------------------

# you need to have the following packages installed:
library(tidyverse) # to read and wrangle data
library(this.path) # to set path automatically
library(openxlsx) # to export to Excel sheet

# Load data ---------------------------------------------------------------

# this sets the working directory to the location of the script
setwd(here())

# if the script is in the experiment folder, a 'data' folder can be called directly
data_raw <- read_csv("data/Example_iFST_data.csv")

# inspect the data
str(data_raw)

# Parameters -------------------------------------------------------------

# parameters of the task
parameters <- data_raw |>
  select(participant,
         order = counterbalance.group,
         session,
         date,
         psychopyVersion,
         frameRate) |>
  slice(1)

# Process data from task -----------------------------------------------------

# Select columns, filter relevant rows and put data in an optimal format
data <- data_raw |>
  # select relevant columns and rename them in a single step
  select(participant,
         block = blocks_loop.thisN, # iteration for the block loop (starts at 0)
         hand,
         sequence = sequence_type, # sequence = simple or complex
         condition = trial_type,  # condition = execution or imagery
         code = sequence_code, # the string that should have been typed
         # 2 COLUMNS
         key = seq_resp.keys,  # keys that ware pressed by the participant
         rt = seq_resp.rt) |> # what was the reaction time for each key press (in seconds)?
  # remove all rows in which no key was pressed, and therefore no reaction time was recorded
  # also retain only main task blocks, so remove the practice block, which is the first
  filter(!is.na(rt), block > 0) |>
  # PsychoPy returns the keys and reaction times as lists of strings, so we need to reformat them
  mutate(typed = str_replace_all(key, "[\\[\\]\\\"\\,\\'\\s]", ""), # get only the keys
         correct = ifelse(typed == code, 1, 0), # compared with the expected key for that sequence
         key_start = as.numeric(str_extract(rt, '(?<=\\[)[^,\\]]+')), # get the first time
         key_end = as.numeric(str_extract(rt, '[^,\\]]+(?=\\])')), # get the last time
         seq_time = key_end - key_start, # substract the times to get the completion time for that trial
         block = block + 1 # start at 1 for convenience
         )

# Obtain summary ----------------------------------------------------------

# What is the accuracy (i.e. number of correct sequences) by the factors?
accuracy <- data |>
  group_by(condition, sequence) |>
  summarise(mean = mean(correct)*100) |> # calculate the mean and put in %
  mutate(mean = round(mean, digits = 2)) # round

# What is the duration by the factors? We only consider the CORRECT trials for this
time <- data |>
  group_by(condition, sequence) |>
  filter(correct == 1) |> # we filter the data frame to consider only correct trials
  summarise(n = n(), # how many trials did we retain after filtering
            mean = mean(seq_time)) |> # calculate mean
  mutate(mean = round(mean, digits = 2)) # round

# Export ------------------------------------------------------------------

# We can export the main data frame in case you want to analyse it in another software
write_csv(data, "data_processed.csv")
write.xlsx(data, "data_processed.xlsx")


