#!usr/bin/python
#!/usr/bin/env python
# example packbox.py
import pygtk
import gtk
import os
import sys,string
import time

"""
Contains GUI logic using PyGTK as part of the Model-View-Controller
@author Lin Yuan Wang
"""
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
		self.window.fullscreen() # sets the GUI to be full screen
		self.window.connect("destroy", gtk.main_quit) # quit when red X is pressed

		# add a vertical box to pack all the contents(The box that packs the image and the buttons)
		self.oBox1 = gtk.VBox(False, 10)
		self.window.add(self.oBox1)

		# set up welcome screen image
		oWelcomeImg = gtk.Image()
		self.oBox1.pack_start(oWelcomeImg, True, True, 0)
		oWelcomeImg.set_from_file("images\welcome.jpg")
		oWelcomeImg.show()

		#create a horizontal box to pack all the buttons (Buttons only)
		self.oBox2 = gtk.HBox(False, 10)
		self.oBox1.pack_end(self.oBox2,False,False,0)

		#Seperater
		separator = gtk.HSeparator()
		self.oBox1.pack_end(separator, False, True, 5)
		separator.show()

		# setup and display continue button
		oContinueButton = gtk.Button("Continue")
		oContinueButton.set_size_request(20,20)
		oContinueButton.connect("clicked", self.showQuestion, 1)
		oContinueButton.connect_object("clicked", gtk.Widget.destroy, oWelcomeImg)
		oContinueButton.connect_object("clicked", gtk.Widget.destroy, oContinueButton)

		self.oBox2.pack_start(oContinueButton, True, True, 0)
		oContinueButton.show()

		self.oBox2.show()
		self.oBox1.show() # display oBox1
		self.window.show() # display window on computer

		print "DEBUG: Exiting ExperimentGUI(height, width, title) constructor"

	# handles the events when self.destroy is called,takes in the data to destroy
	def destroy():
		print "Destroy signal occurred"
		gtk.main_quit()

	# handles the event when red X is pressed, if false then self.destroy will be called.        
	def delete_event(widget,event,data = None):        
		print "User pressed red X on GUI"
		return False

	def showRedDot(self):
		self.redDotBox = gtk.VBox(False,10)
		redDotImageLocation = "images\\fixation_cross.jpg"
		redDot = gtk.Image()
		self.redDotBox.pack_start(redDot, True, True, 0)
		redDot.set_from_file(redDotImageLocation)

		#Hbox to pack all the buttons
		self.redDotButton = gtk.HBox()
		# buttons to show
#		oAbutton = gtk.Button("Choice A")
#		oBbutton = gtk.Button("Choice B")
#		oCbutton = gtk.Button("Choice C")
		#create image button
		buttonImage = gtk.Image()
		buttonImage.set_from_file("images\\fixation_cross.jpg")
		buttonImage.show()
		button = gtk.Button()
		button.add(buttonImage)
		# pack all the button to Hbox
#		self.redDotButton.pack_start(oAbutton, True, True, 0)
#		self.redDotButton.pack_end(oBbutton, True, True, 0)
#		self.redDotButton.pack_end(oCbutton, True, True, 0)
		#pack the HBox to the VBox that contain the image
		self.redDotBox.pack_end(self.redDotButton,True,True,0)
		
		redDot.show()
		self.redDotBox.show()

	"""
	Fetches an image filename from business logic
	"""
	def fetchImage(self, p_sNameOfImage):
		self.showQuestion(self, p_sNameOfImage)

	def showQuestion(self, widget, p_iNameOfImage):
		print "DEBUG: Entering ExperimentGUI.showQuestion(self, widget, iNameOfImage)"
		# First display the red dot and then the image
		self.showRedDot()
		self.window.remove(self.oBox1)
		self.window.add(self.redDotBox)
		self.window.show_all()
		while gtk.events_pending():
			gtk.main_iteration(False)
		time.sleep(0.75)
		self.window.remove(self.redDotBox)
		self.window.add(self.oBox1)

		#the file path of the image
		sImageLocation = "images\\trialImages\\MATT" + str(p_iNameOfImage) + ".jpg"

		# check if file existed, else reset iNameOfImage = 0
		bFileExist = os.path.exists(sImageLocation)
		if bFileExist ==  False:
			p_iNameOfImage = 1
			sImageLocation = "images\\trialImages\\GEORGE" + str(p_iNameOfImage) + ".jpg"

		# pack the image to the box so it can be displayed
		oQuestionImg = gtk.Image()
		self.oBox1.pack_start(oQuestionImg, True, True, 0)
		oQuestionImg.set_from_file(sImageLocation)
		oQuestionImg.show()

		oAbutton = gtk.Button("George")
		oBbutton = gtk.Button("Matt")
#		oCbutton = gtk.Button("Test")
		
		#create image button
		buttonImage = gtk.Image()
		buttonImage.set_from_file("images\\trialImages\\test7.jpg")
		buttonImage.show()
		button = gtk.Button()
		button.add(buttonImage)
		
		#action to take when button a is clicked        
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
		oAbutton.connect("clicked", self.showQuestion, p_iNameOfImage + 1) # increment image #
#		oAbutton.connect_object("clicked", gtk.Widget.destroy, button)
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oBbutton)
#		oAbutton.connect_object("clicked", gtk.Widget.destroy, oCbutton)
		oAbutton.connect_object("clicked", gtk.Widget.destroy, oAbutton)
		self.oBox2.pack_start(oAbutton, True, True, 0)
		
		#action to take when button b is clicked  
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
		oBbutton.connect("clicked", self.showQuestion, p_iNameOfImage + 1) # increment image #
#		oBbutton.connect_object("clicked", gtk.Widget.destroy, button)
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oAbutton)
#		oBbutton.connect_object("clicked", gtk.Widget.destroy, oCbutton)
		oBbutton.connect_object("clicked", gtk.Widget.destroy, oBbutton)
                self.oBox2.pack_start(oBbutton, True, True, 0)
		
		#action to take when button c is clicked
#		oCbutton.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
#		oCbutton.connect("clicked", self.showQuestion, p_iNameOfImage + 1) # increment image #
#		oCbutton.connect_object("clicked", gtk.Widget.destroy, button)
#		oCbutton.connect_object("clicked", gtk.Widget.destroy, oAbutton)
#		oCbutton.connect_object("clicked", gtk.Widget.destroy, oBbutton)
#		oCbutton.connect_object("clicked", gtk.Widget.destroy, oCbutton)
#		self.oBox2.pack_start(oCbutton, True, True, 0)
	
		#action to take when image button is clicked
#		button.connect_object("clicked", gtk.Widget.destroy, oQuestionImg)
#		button.connect("clicked", self.showQuestion, p_iNameOfImage + 1) # increment image #
#		button.connect_object("clicked", gtk.Widget.destroy, oAbutton)
#		button.connect_object("clicked", gtk.Widget.destroy, oBbutton)
#		button.connect_object("clicked", gtk.Widget.destroy, oCbutton)
#		button.connect_object("clicked", gtk.Widget.destroy, button)
#		self.oBox2.pack_start(button, True, True, 0)
                print "DEBUG: Displaying image:" , sImageLocation

                oAbutton.show()
		oBbutton.show()
		#oCbutton.show()
		button.show()

		print "DEBUG: Exiting ExperimentGUI.showQuestion(self, widget, iNameOfImage)"
