# Imagined Finger Sequence Task (iFST)
Available in **English, Spanish, French & German** (see below to implement the task in other languages)

The iFST is a behavioural paradigm aiming to assess the ability to maintain movement imagery with temporal precision. If you are interested in assessing Movement Imagery ability, visit this [Task Platform Project](https://movementimageryability.github.io/) for an overview of open-source behavioural tasks.

Finger Sequence Tasks (FSTs) are widely used in motor control research (e.g. [Doyon et al. 1997](https://doi.org/10.1006/brcg.1997.0899)) and movement imagery (e.g. [Pascual-Leone et al. 1995](10.1152/jn.1995.74.3.1037)). In the iFST, participants are asked to type and imagine finger sequences, and the time employed is measured ([Dahm et al. 2023](https://link.springer.com/article/10.1007/s00426-022-01645-3)). During imagery, participants must simulate pressing the keys until the sequence is completed, hence the paradigm assesses the ability to maintain movement imagery.

This version of the task, as developed by Moreno-Verdú et al. ([preprint](https://doi.org/10.1101/2025.10.20.683365) currently under review), consists in typing/imagining different 8-digit sequences with the index, middle, ring and little fingers of the dominant hand. The present implementation employs two types of sequences that differ based on their complexity (considering the number of changes in direction, with equivalent number of repeats per digit). This allows to observe effects of sequence complexity on both execution and imagery times, as a fundamental effect of the paradigm. 

The present repository contains the materials for an open-source version of the iFST for local and online use. Subsequent updates in native software ([PsychoPy](https://www.psychopy.org/)) may need adjustments. As developers, we are not responsible for implementing these in every use case.

An example of the setup is shown below.

![iFST Animation](iFST_example.gif)

## Repository information
This repository has two main folders, which contain **PsychoPy** experiments (`.psyexp`), together with associated files to run them **locally** (lab/desktop experiments) or **online** (in a browser). 
Please consult the accompanying manuscript [Moreno-Verdú et al., 2026](https://link.springer.com/article/10.3758/s13428-026-03002-3) on the [Movement Imagery Ability Task Platform](https://movementimageryability.github.io/) for a guide on necessary steps to run a task in each of the deployment modes, which can help with the decision.
- [iFST PsychoPy local](/iFST_local_PsychoPy)
- [iFST PsychoPy online](/iFST_online_PsychoPy)
- [iFST OpenSesame local](/iFST_local_OpenSesame)
- [iFST OpenSesame online](/iFST_online_OpenSesame)

The version provided in this repository may allow flexibility in terms of key task parameters of the iFST:
- types of sequences
- number of sequences
- length of sequences
- repetitions
- feedback provision

The optimal protocol is at the user's discretion, but sensible defaults have been implemented.

## Language expansion
If you want to contribute to this repository by providing a language translation, or want to run the task in your own language, expansions can be done relatively easily thanks to the implementation of language localisations (please read each README to understand how to implement these). You can also see these demos showing how to implement a language localisation in [PsychoPy](https://github.com/mmorenoverdu/language_localisation_demo) and [OpenSesame](https://github.com/carlacz/OpenSesame_Language-Localisation-Demo) with virtually no code.
