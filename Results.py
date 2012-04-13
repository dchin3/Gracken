#!usr/bin/python

class Results:
	"""
	Explicit value constructor for Results
	Opens output stream to file
	@param self
	@param p_sOutputFileName name of file to create and output results to
		default value "ExpResults.txt"
	"""
	def __init__(self, p_sOutputFileName = "ExpResults.txt"):
		print "DEBUG: Entering Results(outputFileName) constructor"

		self.__sOutputFileName = p_sOutputFileName
		self.__oOutputFile = open(self.__sOutputFileName, "w")
		print "DEBUG: \tself.__sOutputFileName =" , self.__sOutputFileName
		print "DEBUG: \tOpening write stream to:" , self.__oOutputFile

		print "DEBUG: Exiting Results(outputFileName) constructor"

	"""
	Writes a line of text to output into the file
	@param self
	@param p_sLineToWrite line of text to write
	"""
	def writeToFile(self, p_sLineToWrite):
		print "DEBUG: Entering Results.writeToFile(lineToWrite)"

		self.__oOutputFile.write(p_sLineToWrite)
		print "DEBUG: \tWrote to output file:" , p_sLineToWrite

		print "DEBUG: Exiting Results.writeToFile(lineToWrite)"

	"""
	Destructor for Results
	Closes output stream to file
	@param self
	"""
	def __del__(self):
		print "DEBUG: Entering Results destructor"

		self.__oOutputFile.close()
		print "DEBUG: \tOutput stream closed for:" , self.__sOutputFileName

		print "DEBUG: Exiting Results destructor"
