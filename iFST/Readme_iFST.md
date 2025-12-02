# Imagined Finger Sequence Task (iFST)

Marcos Moreno Verdu, 02/12/2025


PsychoPy version 2025.1.0


Hybrid Experiment (Local/Online both possible with this experiment)


Languages supported: English, Spanish, French. Further languages can be added.


---------------------------------------
## GENERAL INSTRUCTIONS: ##

This README is not intended to explain how PsychoPy generally works, but the specific aspects of this experiment.

If you have never used PsychoPy, please have a look at the documentation on their webpage or tutorials, especially regarding conditions files, variables, routines and loops. This will save you time if you decide to modify any parameters from this experiment.

If you have never used PsychoPy, you should know that once you have decompressed the .zip file, you must not change the names of the files/folders, as the .psyexp file is going to look for specific names at specific locations. Additionally, you should avoid, wherever possible, changing any variable names, as again, the code depending on that variable name will need to be adjusted as well. Bear this in mind.

---------------------------------------
## SETUP INSTRUCTIONS ##

To run this task you need to have installed PsychoPy version 2025.1.0 or superior.

There are no dependencies for this task.

The data output MUST be processed to obtain meaningful information. An example of data processing (in R) can be found in the folder of this experiment. 

Step-by-step instructions:

1) Download all files from the repository

2) Unzip the file in  NEW folder WITHOUT any other PsychoPy experiments in it.

3) Open the file 'iFST_local.psyexp' in PsychoPy.



If you want to use the experiment online, there are further steps:



4) In the Pavlovia tab, link your Pavlovia account if you haven't done so already.



5) In the Pavlovia tab, click on "No project", this will start the process of linking the experiment to a Pavlovia experiment.

6) Follow the procedure PsychoPy indicates.

7) Go to your Pavlovia dashboard. You should see the project now appears there under the same name of your PsychoPy experiment.

8) Change the mode from inactive to pilot.

9) Click pilot and run the experiment online!



---------------------------------------

## LANGUAGE LOCALISATION ##



We need 2 Excel sheets (with extension type .xlsx) to store:

- The available language localisations: "language_localiser.xlsx"

- The list of messages to use as variables to display text on screen: "messages.xlsx"



In the Experiment Settings button, in the Basic tab, the Experiment Info section must have a "language" field with the list of languages. This allows to select the language **before** every run of the Experiment through a dropdown menu in the pop-up dialogue box (both if you run it locally or online). These languages need to be specified as in the language column of the language localiser Excel sheet.


All the text components which should be dynamically updated for language should have their "Text" field in "Set to every repeat". This allows to change dynamically the value of the variable, which therefore changes the text to be shown.

The routine 'load language' is wrapped in a loop with the same name. This routine only has a code component. The code autotranslates to JS and is divided into two tabs:
  - BEGIN EXPERIMENT: the code creates a variable with the ISO code to be used and sets its default value to english (EN).
  - BEGIN ROUTINE: the code updates the ISO code based on the participant's choice in the dialogue box. 

Note: the "language_localiser.xlsx" containing all available languages is automatically imported by PsychoPy because it is used as conditions file in the loop. The number of rows in the localiser Excel sheet **should match** with the number of conditions that PsychoPy identifies in the loop. If not, click on the loop name and **refresh the Excel sheet by clicking on the green arrows**.
 
The routine 'update messages' is wrapped in a loop with the same name. The routine only has a code component. The code DOES NOT autotranslate to JS and is only located in the BEGIN ROUTINE tab:
  - Creates variables to iterate across the "messages.xlsx".
  - Iterates across the list of messages and updates the values according to the updated language code (updated in the 'load language' routine).
  - Adds all messages as global variables, using the "globals()" method in Python and the "window[]" mehtod in JS.
  - Now all messages are updated according to the language and ready to be used for text presentation!

Note: the "messages.xlsx" containing all messages and their translations to the available languages is automatically imported by PsychoPy because it is used as conditions file in the loop.

Every text component in the experiment has a variable name in their "Text" field (e.g., "welcome_msg" for the welcome_text component). This variable will be **automatically** updated based on the language choice in the dialogue box. The variable name **MUST BE an existing message as defined in 'messages.xlsx'** before the experiment is launched.



**Adding a new language**



If you just want to add a new language without any further modifications (i.e., you do not want to provide other messages than the ones already used), you just need to modify 4 things:

1. In language_localiser.xlsx, add a new **ROW** with your new language and its code. Write this in English (e.g., "Chinese", "CH").

2. In messages.xlsx, add a new **COLUMN**, titled with the code you used in the previous step (e.g., "CH"). For each message, provide the corresponding translation into your desired language.

3. In PsychoPy, go to Experiment Settings and add a new language to the list of languages in the **language field**, with the name being the language you used in Step 1. It is critical that you add your language using '' (e.g., 'Chinese'). If you want your language to be the default choice every time you run the experiment, you just have to **place it at the beginning of the list**.

4. Add the corresponding columns with your language to the different instructions file(s) (Excel sheets).



---------------------------------------
## TECHNICAL DETAILS: ##

**The experiment has the following subfolders:**

-stimuli: It contains the stimuli to be used in the task. This is images of finger sequences (simple/complex) with the left and right hands. Based on the handedness of the participant, only stimuli for the dominant hand will be shown.
	
-images: It has the images to display in the instructions of the experiment.

**The experiment has the following files:**

-instructions.xlsx: Encodes the instructions and images to be displayed. Contains text and images for left-handed and right-handed participants. These will be filtered dynamically based on the handedness reported by the participant (i.e., only instructions for the corresponding hand will be shown). The columns finished in '_EN', '_ES', etc. show the corresponding text for the different screens in the instructions. If you want to add your own language, you just have to create a new column named as the other ones but finished with '_YOURCODE', and provide your corresponding translation in each row.

-conditions_**.xlsx: Encodes the actual variables to show instructions throughout the task (for left and right stimuli in separate Excel sheets). Variables:
	

	-hand: which hand this stimulus belongs to. This column is used to filter dynamically in PsychoPy.
	

	-stim: which unique stimulus this is (2 sequences x 2 conditions = 4).
	

	-sequence_code: what is the actual string for the sequence. Depends on handedness, condition and sequence type.
	

	-sequence_type: simple or complex.
	

	-trial_type: execution or imagery conditions.
	

	-key_presses: if execution, the whole sequence is typed (8 keys). If imagery, only the first and last elements are typed (2 keys).
	

	-sequence_picture: image to show while typing/imagining the sequence.
	

	-prompt_before: column to show text indicating if the next trial is execution or imagery. The language is dynamically updated thanks to the language localisation.
	

	-prompt: similar to the previous one, but this text is shown on screen **while** the subject is in trial.

-self_assess_questions.xlsx: Encodes qualitative questions to be answered on 11-point rating scales by the participant after each main task block. They work with language localistion as explained above.
	

	-self_assess_question_**: Question to be displayed on screen in the localised language.
	

	-label_min_**: Label to show for the minimum possible rating (0).



        -label_middle_**: Label to show for the midpoint rating.
	

	-label_max_**: Label to show for the maximum possible rating (10).

---------------------------------------
## EXPERIMENT SETTINGS (parameters to choose):

The experiment is not intended to be flexible in terms of the parameters to choose (i.e., types of sequences, etc). In the experiment settings routine, you will be able to specify the number of trials per conditions to be collected (default is 10, so 40 trials overall (10 x 2 sequences x 2 trial types).


In the dialogue box the user can input:

-participant: optional. ID of the participant. Can be a number or a name.

-session: optional. ID of the session. Can be a number or a name.

-language: mandatory.
	
	-Options: English (default)/Spanish/French.
	
	-Further languages could be implemented (see Language Localisation above).


In addition to these variables in the dialogue box, in the first screen of the experiment the participant has to decide what is their preferred hand. This choice is used to determine which stimuli (for left-handed or right-handed) are presented.


If you want to modify the parameters of this experiment (e.g. types of sequences), you should create your own stimuli including images, text, etc. We are not responsible for providing modified versions for every use case.
	
---------------------------------------
## PARTICIPANT WORKFLOW:

Once the experiment starts, it will guide the participant through it without the need for any other explicit supervision. There will be:
-A welcome screen with some text indicating the participant to select their "preferred" hand (left or right).
	
-A couple of screens with instructions.

-A practice block with all 4 conditions (simple-complex x execution-imagery).

	-The participant will go through the conditions in the order simple-execution, simple-imagery, complex-execution and complex-imagery. This is to help them understand the differences between the 4 conditions.

	-In this practice block, participants receive online feedback (which key they press) through 4 small boxes at the bottom of the screen (1 per finger). They also receive feedback on the accuracy of the trial (if they typed the correct keys).
	
	-Participants need to provide AT LEAST 2 CORRECT RESPONSES PER CONDITION to advance to the main task blocks. This is printed on screen after each trial. You can modify this quite easily in the experiment settings routine via changing the value of the corresponding variable.

-2 main task blocks (1 per sequence type, simple or complex in a randomized order via a counterbalance routine):
	
	-Trials for execution and imagery are always alternated within the block.
	
	-Every trial, on-screen text indicates whether this is an imagery or execution trial.
	
	-There is no online or offline feedback in this section.
	
	-At the end of the block, the participant must respond to qualitative questions about imagery (as explained above).

-A goodbye screen.

---------------------------------------
## OUTPUT:

The output file that PsychoPy will generate will be a .csv file in a subfolder "data". This .csv will contain all the variables encoded in the experiment. It will always be named with the participant field and the date.

The output variables we will be interested in, specifically for the iFST, are:
	
-seq_resp.rt: Encodes a list with response times per key press. It does it in SECONDS. The last minus de first time determines the time employed to type/imagine the sequence in that trial.

-seq_resp.keys: Encodes the actual keys that were pressed in that trial.

Aside from those, we will need to retain the variables from our conditions file for analysis:
	-hand
	-sequence_type
	-trial_type
	-sequence_code


If you are interested in the self-assessments, the relevant variables to retain for analysis is:

	-slider.rating: Contains the response to every question (0-10).


All the variables shown in the dialog box will be saved.

