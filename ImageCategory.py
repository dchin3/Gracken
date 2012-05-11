#!usr/bin/python

class ImageCategory:
	"""
	Explicit value constructor for ImageCategory
	@param self
	@param p_sCategoryName name of this category
	@param p_oImagesList list of images that belong in this category
	"""
	def __init__(self, p_sCategoryName = "", p_oImagesList = []):
		print "DEBUG: Entering ImageCategory(categoryName, imagesList) constructor"

		self.__sCategoryName = p_sCategoryName
		self.__oImagesList = p_oImagesList
		print "DEBUG: \tcategoryName =", self.__sCategoryName
		print "DEBUG: \timagesList =" , self.__oImagesList

		print "DEBUG: Exiting ImageCategory(categoryName, imagesList) constructor"

	"""
	Getter for sCategoryName
	*I know this is not Pythonic code. This is a placeholder method for now.
	@param self
	"""
	def getCategoryName(self):
		return self.__sCategoryName

	"""
	Check to see if image is within this category
	@param self
	@param p_sImage name of image to search within this category
	@param p_oResults an instance of a Results object for output
	@return true if found, else false
	"""
	def findImage(self, p_sImage, p_oResults):
		print "DEBUG: Entering ImageCategory.findImage(image, results)"

		bFoundImage = False

		for ii in range(self.__oImagesList.__len__()):
			if(p_sImage == self.__oImagesList[ii]):
				bFoundImage = True
				break

		print "DEBUG: Exiting ImageCategory.findImage(image, results)"

		return bFoundImage
