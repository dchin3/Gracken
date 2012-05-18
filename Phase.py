#!usr/bin/python

from Results import *

class Phase:
	"""
	Explicit value constructor for Phase
	@param self
	@param p_oPhaseBlocks list of blocks to use in this phase
		default value []
	"""
	def __init__(self, p_oPhaseBlocks = []):
		print "DEBUG: Entering Phase(oPhaseBlocks) constructor"

		self.__oPhaseBlocks = p_oPhaseBlocks
		print "DEBUG: \toPhaseBlocks =" , self.__oPhaseBlocks

		print "DEBUG: Exiting Phase(oPhaseBlocks) constructor"

	"""
	Execute all blocks for this phase
	@param self
	@param p_oCategoryList list of categories for all images
	@param p_oResults an instance of a Results object for output
	"""
	def runBlocks(self, p_oCategoryList, p_oResults):
		print "DEBUG: Entering Phase.runBlocks(oCategoryList, oResults)"

		print "DEBUG: Exiting Phase.runBlocks(oCategoryList, oResults)"
