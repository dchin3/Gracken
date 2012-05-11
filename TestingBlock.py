#!usr/bin/python

from Block import *

class TestingBlock(Block):
	"""
	Explicit value constructor for TestingBlock
	@param self
	@param p_oBlockImages list of images to iterate through in this testing block
		default value []
	"""
	def __init__(self, p_oBlockImages = []):
		print "DEBUG: Entering TestingBlock(oBlockImages) constructor"

		self.__oBlockImages = p_oBlockImages
		print "DEBUG: \toBlockImages =" , self.__oBlockImages

		print "DEBUG: Exiting TestingBlock(oBlockImages) constructor"

	"""
	Execute through all trial images in this testing block once
	@param self
	@param p_oCategoryList list of categories for all images
	@param p_oResults an instance of a Results object for output
	"""
	def runTrials(self, p_oCategoryList, p_oResults):
		print "DEBUG: Entering TestingBlock.runTrials(oResults)"
		p_oResults.writeToFile("\tEntering testing block\n")

		iNumCorrect = 0
		fUserScore = 0.0
		# iterate through all images specified in oBlockImages
		for ii in range(self.__oBlockImages.__len__()):
			print "DEBUG: \tDoing trial" , ii + 1 , "out of" , self.__oBlockImages.__len__() , ":" , self.__oBlockImages[ii]
			p_oResults.writeToFile("\t\tDoing trial " + str(ii + 1) + " out of " + str(self.__oBlockImages.__len__()) + ": " + self.__oBlockImages[ii] + "\n")

			bCorrectAnswer = False
			sChooseAnswer = "A" # hard-coded to always choose category A
			for jj in range(p_oCategoryList.__len__()):
				if(p_oCategoryList[jj].getCategoryName() == sChooseAnswer):
					if(p_oCategoryList[jj].findImage(self.__oBlockImages[ii], p_oResults)):
						bCorrectAnswer = True
						break
			
			if(bCorrectAnswer):
				iNumCorrect += 1
				print "DEBUG: \t\tUser answered correctly for trial" , ii + 1 , "with choice:" , sChooseAnswer
				p_oResults.writeToFile("\t\tUser answered correctly for trial " + str(ii + 1) + " with choice: " + sChooseAnswer + "\n")
			else:
				print "DEBUG: \t\tUser answered incorrectly for trial" , ii + 1 , "with choice:", sChooseAnswer
				p_oResults.writeToFile("\t\tUser answered incorrectly for trial " + str(ii + 1) + " with choice: " + sChooseAnswer + "\n")

		fUserScore = (float(iNumCorrect) / self.__oBlockImages.__len__()) * 100.0 # calculate user's score for the block

		# finished all trials in block
		print "DEBUG: \tUser completed testing block with score:" , fUserScore , "%"
		p_oResults.writeToFile("\tUser completed testing block with score: " + str(fUserScore) + "%\n")

		print "DEBUG: Exiting TestingBlock.runTrials(oResults)"
