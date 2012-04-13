#!usr/bin/python

from Phase import *

class LearningPhase(Phase):
	"""
	Explicit value constructor for LearningPhase
	@param self
	@param p_oPhaseBlocks list of learning blocks to use in this phase
		default value []
	@param p_oPhaseImages list of images to use in this phase
		default value []
	@param p_fPassRate required passing percentage rate for each learning block
		default value 0.0
	"""
	def __init__(self, p_oPhaseBlocks = [], p_oPhaseImages = [], p_fPassRate = 0.0):
		print "DEBUG: Entering LearningPhase(oPhaseBlocks, oPhaseImages, fPassRate) constructor"

		self.__oPhaseBlocks = p_oPhaseBlocks
		self.__oPhaseImages = p_oPhaseImages
		self.__fPassRate = p_fPassRate
		print "DEBUG: \toPhaseBlocks =" , self.__oPhaseBlocks
		print "DEBUG: \toPhaseImages =" , self.__oPhaseImages
		print "DEBUG: \tfPassRate =" , self.__fPassRate

		print "DEBUG: Exiting LearningPhase(oPhaseBlocks, oPhaseImages, fPassRate) constructor"

	"""
	Execute all learning blocks for this learning phase
	@param self
	@param p_oResults an instance of a Results object for output
	"""
	def runBlocks(self, p_oResults):
		print "DEBUG: Entering LearningPhase.runBlocks(results)"

		for ii in range(self.__oPhaseBlocks.__len__()):
			print "DEBUG: \tEntering learning block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__() , ":" , self.__oPhaseImages.__len__() , "trials"
			p_oResults.writeToFile("\tEntering learning block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + " : " + str(self.__oPhaseImages.__len__()) + " trials\n")

			self.__oPhaseBlocks[ii].runTrials(p_oResults)

			print "DEBUG: \tExiting learning block" , ii + 1 , "out of" , self.__oPhaseBlocks.__len__()
			p_oResults.writeToFile("\tExiting learning block " + str(ii + 1) + " out of " + str(self.__oPhaseBlocks.__len__()) + "\n\n")

		print "DEBUG: Exiting LearningPhase.runBlocks(results)"
