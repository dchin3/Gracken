#!usr/bin/python

import pygtk
import gtk
import os

class ExperimentGUI:
	"""
	Explicit value constructor for ExperimentGUI
	Create GUI window, set up parameters, display welcome screen
	@param self
	@param p_iHeight height of GUI window
		default value 500
	@param p_iWidth width of GUI window
		default value 550
	@param p_sTitle title of GUI window
		default value "Gracken v3.0"
	"""	
	def __init__(self, p_iHeight = 500, p_iWidth = 550, p_sTitle = "Gracken v3.0"):
		print "DEBUG: Entering ExperimentGUI(height, width, title) constructor"

		self.__iHeight = p_iHeight
		self.__iWidth = p_iWidth
		self.__sTitle = p_sTitle
		print "DEBUG: \tiHeight =" , self.__iHeight
		print "DEBUG: \tiWidth =" , self.__iWidth
		print "DEBUG: \tsTitle =" , self.__sTitle

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) # creates window at top level
		self.window.set_title(self.__sTitle) # GUI title
		self.window.set_default_size(self.__iHeight, self.__iWidth) # GUI window dimensions
		self.window.set_border_width(20) # sets border width within GUI
		self.window.connect("destroy", gtk.main_quit) # quit when red X is pressed

		# add a vertical box to pack all the contents
		self.oBox1 = gtk.VBox(False, 10)
		self.window.add(self.oBox1)

		# set up welcome screen image
		oWelcomeImg = gtk.Image()
		self.oBox1.pack_start(oWelcomeImg, True, True, 0)
		oWelcomeImg.set_from_file("images\welcome.jpg")
		oWelcomeImg.show()

		# setup and display continue button
		oContinueButton = gtk.Button("Continue")

		oContinueButton.connect("clicked", self.showQuestion, 0)
		oContinueButton.connect_object("clicked", gtk.Widget.destroy, oWelcomeImg)
		oContinueButton.connect_object("clicked", gtk.Widget.destroy, oContinueButton)

		self.oBox1.pack_start(oContinueButton, True, True, 0)
		oContinueButton.show()

		self.oBox1.show() # display box1
		self.window.show() # display window on computer

	# handles the events when self.destroy is called,takes in the data to destroy
	def destroy():
		print "Destroy signal occurred"
		gtk.main_quit()

	# handles the event when red X is pressed, if false then self.destroy will be called.        
	def delete_event(widget,event,data=None):        
		print "User pressed red X on GUI"
		return False

		print "DEBUG: Exiting ExperimentGUI(height, width, title) constructor"

	def showQuestion(self, widget, p_iNameOfImage):
		print "DEBUG: Entering ExperimentGUI.showQuestion(self, widget, nameOfImage)"

                #the file path of the image 
		sImageLocation = "images\\trialImages\\A" + str(p_iNameOfImage) + ".jpg"

		# check if file existed
                bFileExist = os.path.exists(sImageLocation)
		if bFileExist ==  False:
                        p_iNameOfImage =0
                        sImageLocation = "images\\trialImages\\A" + str(p_iNameOfImage) + ".jpg"

                # pack the image to the box so it can be displayed
                oQuestionImg = gtk.Image()
		self.oBox1.pack_start(oQuestionImg, True, True, 0)
		oQuestionImg.set_from_file(sImageLocation)

                oQuestionImg.show()

                # pack the buttons to the box so it can be displayed
		oAbutton = gtk.Button("Choice A")
		oBbutton = gtk.Button("Choice B")

                #action to take when button a is clicked        
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
		oAbutton.connect("clicked", self.showQuestion, p_iNameOfImage+1)#
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oBbutton)
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oAbutton)
		self.oBox1.pack_start(oAbutton, True, True, 0)

                #action to take when button a is clicked  
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
		oBbutton.connect("clicked", self.showQuestion, p_iNameOfImage+1)#
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oAbutton)
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oBbutton)
                self.oBox1.pack_start(oBbutton, True, True, 0)
                
                oAbutton.show()
                oBbutton.show()
                
