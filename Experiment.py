#!usr/bin/python

class Experiment:
	"""
	Explicit value constructor for Experiment
	@param self
	@param p_oExperimentPhases list of phases in this experiment
		default value []
	"""
	def __init__(self, p_oExperimentPhases = []):
		print "DEBUG: Entering Experiment(oExperimentPhases) constructor"

		self.__oExperimentPhases = p_oExperimentPhases
		print "DEBUG: \texperimentPhases =" , self.__oExperimentPhases

		print "DEBUG: Exiting Experiment(oExperimentPhases) constructor"

	"""
	Execute all phases for this experiment
	@param self
	@param p_oCategoryList list of categories for all images
	@param p_oResults an instance of a Results object for output
	"""
	def runPhases(self, p_oCategoryList, p_oResults):
		print "DEBUG: Entering Experiment.runPhases(oCategoryList, oResults)"

		for ii in range(self.__oExperimentPhases.__len__()):
			print "DEBUG: \tEntering phase" , ii + 1 , "out of" , self.__oExperimentPhases.__len__() , ":" , self.__oExperimentPhases[ii].__class__.__name__
			p_oResults.writeToFile("Entering phase " + str(ii + 1) + " out of " + str(self.__oExperimentPhases.__len__()) + " : " + str(self.__oExperimentPhases[ii].__class__.__name__) + "\n")

			self.__oExperimentPhases[ii].runBlocks(p_oCategoryList, p_oResults)

			print "DEBUG: \tExiting phase" , ii + 1 , "out of" , self.__oExperimentPhases.__len__()
			p_oResults.writeToFile("Exiting phase " + str(ii + 1) + " out of " + str(self.__oExperimentPhases.__len__()) + "\n\n")

		print "DEBUG: Exiting Experiment.runPhases(oCategoryList, oResults)"
