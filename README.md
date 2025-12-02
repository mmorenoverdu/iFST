# Imagined Finger Sequence Task (iFST)
**Available in English, Spanish, French** (see below to implement the task in other languages)

The iFST is a behavioural paradigm aiming to assess the ability to maintain movement imagery with temporal precision. If you are interested in assessing Movement Imagery ability, visit this [Task Platform Project](https://movementimageryability.github.io/) for an overview of open-source behavioural tasks.

Finger Sequence Tasks (FSTs) are widely used in motor control research (e.g. [Doyon et al. 1997](https://doi.org/10.1006/brcg.1997.0899)) and movement imagery (e.g. [Pascual-Leone et al. 1995](10.1152/jn.1995.74.3.1037)). In the iFST, participants are asked to type and imagine finger sequences, and the time employed is measured ([Dahm et al. 2023](https://link.springer.com/article/10.1007/s00426-022-01645-3)). During imagery, participants must simulate pressing the keys until the sequence is completed, hence the paradigm assesses the ability to maintain movement imagery.

This version of the task, as developed by Moreno-Verdú et al. ([preprint](https://doi.org/10.1101/2025.10.20.683365) currently under review), consists in typing/imagining different 8-digit sequences with the index, middle, ring and little fingers of the dominant hand. The present implementation employs two types of sequences that differ based on their complexity (considering the number of changes in direction, with equivalent number of repeats per digit). This allows to observe effects of sequence complexity on both execution and imagery times, as a fundamental effect of the paradigm. 

The present repository contains the materials for an open-source version of the iFST for local and online use. Subsequent updates in native software ([PsychoPy](https://www.psychopy.org/)) may need adjustments. As developers, we are not responsible for implementing these in every use case.

An example of the setup is shown below.
![iFST Animation](iFST_example.gif)

## Repository information
The repository has 1 main folder, which contain **PsychoPy experiment (.psyexp)** and associated files to be able to run the task **locally or online**. Please consult the Readme file before using the task. This experiment is provided as an hybrid PsychoPy experiment, this means it should work locally and online without adjustments. The Readme file contain extensive documentation on the most relevant task settings and detailed information to allow the user further customization.

The version provided in this repository may allow flexibility in terms of key task parameters of the iFST (e.g. types of sequences, number of sequences, length of sequences, etc). The optimal protocol is at the user's discretion, but sensible defaults have been implemented.

## Language expansion
If you want to contribute to this repository by providing a language translation, or want to run the task in your own language, expansions can be done relatively easily thanks to the implementation of **language localisations** (please read the Readme to understand how to implement these). You can also see [this demo](https://github.com/mmorenoverdu/language_localisation_local) showing how to implement a language localisation in PsychoPy with virtually no code.
