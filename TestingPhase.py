#!usr/bin/python

from Phase import *

class TestingPhase(Phase):
	"""
	Explicit value constructor for TestingPhase
	@param self
	@param p_oPhaseBlocks list of testing blocks to use in this phase
		default value []
	"""
	def __init__(self, p_oPhaseBlocks = []):
		print "DEBUG: Entering TestingPhase(oPhaseBlocks) constructor"

		self.__oPhaseBlocks = p_oPhaseBlocks
		print "DEBUG: \toPhaseBlocks =" , self.__oPhaseBlocks

		print "DEBUG: Exiting TestingPhase(oPhaseBlocks) constructor"

	"""
	Execute all blocks for this testing phase
	@param self
	@param p_oCategoryList list of categories for all images
	@param p_oResults an instance of a Results object for output
	"""
	def runBlocks(self, p_oCategoryList, p_oResults):
		print "DEBUG: Entering TestingPhase.runBlocks(oCategoryList, oResults)"

		for ii in range(self.__oPhaseBlocks.__len__()):
			print "DEBUG: \tEntering testing block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__()
			p_oResults.writeToFile("\tEntering testing block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + "\n")

			self.__oPhaseBlocks[ii].runTrials(p_oCategoryList, p_oResults)	

			print "DEBUG: \tExiting testing block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__()
			p_oResults.writeToFile("\tExiting testing block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + "\n\n")

		print "DEBUG: Exiting TestingPhase.runBlocks(oCategoryList, oResults)"
