#!usr/bin/python

from Results import *

class Phase:
	"""
	Explicit value constructor for Phase
	@param self
	@param p_oPhaseBlocks list of blocks to use in this phase
		default value []
	@param p_oPhaseImages list of images to use in this phase
		default value []
	"""
	def __init__(self, p_oPhaseBlocks = [], p_oPhaseImages = []):
		print "DEBUG: Entering Phase(oPhaseBlocks, oPhaseImages) constructor"

		self.__oPhaseBlocks = p_oPhaseBlocks
		self.__oPhaseImages = p_oPhaseImages
		print "DEBUG: \toPhaseBlocks =" , self.__oPhaseBlocks
		print "DEBUG: \toPhaseImages =" , self.__oPhaseImages

		print "DEBUG: Exiting Phase(oPhaseBlocks, oPhaseImages) constructor"

	"""
	Execute all blocks for this phase
	@param self
	@param p_oResults an instance of a Results object for output
	"""
	def runBlocks(self, p_oResults):
		print "DEBUG: Entering Phase.runBlocks(oResults)"

		print "DEBUG: Exiting Phase.runBlocks(oResults)"
