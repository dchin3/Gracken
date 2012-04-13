#!usr/bin/python

from Phase import *

class TestingPhase(Phase):
	"""
	Explicit value constructor for TestingPhase
	@param self
	@param p_oPhaseBlocks list of testing blocks to use in this phase
		default value []
	@param p_oPhaseImages list of images to use in this phase
		default value []
	"""
	def __init__(self, p_oPhaseBlocks = [], p_oPhaseImages = []):
		print "DEBUG: Entering TestingPhase(oPhaseBlocks, oPhaseImages) constructor"

		self.__oPhaseBlocks = p_oPhaseBlocks
		self.__oPhaseImages = p_oPhaseImages
		print "DEBUG: \toPhaseBlocks =" , self.__oPhaseBlocks
		print "DEBUG: \toPhaseImages =" , self.__oPhaseImages

		print "DEBUG: Exiting TestingPhase(oPhaseBlocks, oPhaseImages) constructor"

	"""
	Execute all blocks for this testing phase
	@param self
	@param p_oResults an instance of a Results object for output
	"""
	def runBlocks(self, p_oResults):
		print "DEBUG: Entering TestingPhase.runBlocks(results)"

		for ii in range(self.__oPhaseBlocks.__len__()):
			print "DEBUG: \tEntering testing block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__() , ":" , self.__oPhaseImages.__len__() , "trials"
			p_oResults.writeToFile("\tEntering testing block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + " : " + str(self.__oPhaseImages.__len__()) + " trials\n")

			self.__oPhaseBlocks[ii].runTrials(p_oResults)	

			print "DEBUG: \tExiting testing block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__()
			p_oResults.writeToFile("\tExiting testing block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + "\n\n")

		print "DEBUG: Exiting TestingPhase.runBlocks(results)"
