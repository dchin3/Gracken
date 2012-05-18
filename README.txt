Gracken Project
Current developers: Douglas Chin, Aaron Shipper, Lin Yuan Wang
Previous developer(s): Paul Yi

Current version: 3.0
Spring 2012

The purpose of this project is to provide an application for use in human
learning experiments. This project is supervised by Professor Kenneth Kurtz of
the Psychology Department at State University of New York at Binghamton.

Technologies used:
Python 2.7, PyGTK 2.24

Note: This experiment is designed under the Windows environment.

File Hierarchy
The overall architectural design for this project is the Model View Controller
due to the flexible demands of a psychology experiment from the administrator's
perspective. The model follows the hierarchy model of a psychology experiment:
an experiment has a set of phases, and each phase has a set of blocks, and each
block has a set of trials.

Model (11 files)

	Driver.py - used to run the program

	Experiment.py - executes a list of Phase subtypes (LearningPhase and TestingPhase)

	Phase.py - parent class for LearningPhase.py and TestingPhase.py
	LearningPhase.py - executes a list of LearningBlock objects
	TestingPhase.py - executes a list of TestingBlock objects

	Block.py - parent class for LearningBlock.py and TestingBlock.py
	LearningBlock.py - executes a set of image trials, informs user of correct answer and enforces a passing rate
	TestingBlock.py - executes a set of image trials, keeps track of user score

	ImageCategory.py - data structure for categories of all images used in an experiment

	Results.py - writes experiment output to a file "ExpResults.txt"

View/Controller (1 file)

	ExperimentGUI.py - PyGTK GUI component

This project uses a folder of images, conveniently named "images". Images that are
specifically used as trial images are located in the subfolder "trialImages".

**********

TO-DO list:
-Integrate the Model and View/Controller components to run together. These
modules were developed separately. Refactoring may be necessary.
-Add flexibility in choosing fixation cross time.
-Integrate the Configuration module with the project. Currently, all experiment
details are explicitly written and passed in the Driver. This is primarily made
for the experiment administrators.

From the administrators:
·      Fixation cross before each “target”? (usually there is, we
usually move it to match the target image placement, usually on screen
for 500 ms)

·      Is there something to display before the target image? (e.g.
class label for target image on observational learning trials)

o   Text or image?

o   How long should that be displayed?

·      What are the “target” images to be displayed in each block

·      Number of “target” images shown on the screen (usually one)

o   Placement of target image(s) (important because images differ in
size, but could be set to center within a certain space)

o   How long should that be displayed by itself? (usually stays on
screen for whole trial, other things are added- usually below)

·      Ask for a response from the learner?

o   What is the wording of the question?

o   How many possible responses (ranges from 2 (e.g. classification)-7
(e.g. typicality ratings)

o   What are the response options?

§  More often than not, these responses have “correct” answers, that
need to be hard coded somewhere

o   Placement of response options (should be evenly spaced, regardless
of number of responses)

o   Are the responses text (e.g. class label) or images (e.g. inference choices)

o   Give feedback on their response on each trial?

§  What does the feedback say?

§  Is it self-timed (learner clicks to continue) (usually is) or is
there are particular amount of time it is displayed for?

·      How long should it be displayed if not self-timed?

·      Is there a criterion? (point at which learner performance moves
them onto the next phase)

o   What is it? (how many correct responses within how many trials?)

·      What is the number of blocks (barring completion of possible criterion)
