#!usr/bin/python

class Block:
	"""
	Explicit value constructor for Block
	@param self
	@param p_oBlockImages list of images to iterate through this block
	"""
	def __init__(self, p_oBlockImages = []):
		print "DEBUG: Entering Block(oBlockImages) constructor"

		self.__oBlockImages = p_oBlockImages
		print "DEBUG: oBlockImages =" , self.__oBlockImages

		print "DEBUG: Exiting Block(oBlockImages) constructor"

	"""
	Execute through all trial images in this block
	@param self
	@param p_oResults an instance of a Results object for output
	"""
	def runTrials(self, p_oResults):
		print "DEBUG: Entering Block.runTrials(oResults)"

		print "DEBUG: Exiting Block.runTrials(oResults)"
