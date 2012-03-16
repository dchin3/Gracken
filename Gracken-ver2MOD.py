#!/usr/bin/python

from fractions import Fraction
import pygtk
import gtk
import sys, os
from random import *
from Grackenconfig import *
#from lib.Grackenlib import *
import time

#global variables

#these variables are imported from Grakenconfig
#numtrials # number of trials images shown
#numOfBlocks  #number of blocks
#blockMode# True or False if block method is used
#numOfImageOption # only works for 1 or 2
learningnum = 1 # counter for current learning questions given
g_trialNumber = 1 # counter for current trial number in phase
rannum = 0
iarray = []
imgA = []
imgB = []
completeImageList = [] #only used when one image option is enabled
oneImageAnswer = 'A' #only used when one image option is enabled
learningCorrect = 0


class Gracken:

    # Set up GUI parameters (window, title, size, borders)
    def setupWindow(self):
        print("setupWindow")
        
        #code block for the window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) #creates the window
        self.window.set_title("Gracken")              #Sets the title
        self.window.set_size_request(500,550)
        self.window.set_icon_from_file(icon_img)      #creates top left icon from icon_img defined in Grackenconfig
        self.window.connect("delete_event", self.delete_event) #window closing event
        self.window.set_border_width(10)             #sets border width of window
        
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
        #creates separator or the line within the window
        self.separator = gtk.HSeparator()

    # Set up single picture in GUI
    def setupPictureFrames (self):
            self.image1 = gtk.Image()
            self.image1.set_from_file("images/A0.jpg")
            #self.image2 = gtk.Image()
            #self.image2.set_from_file("images/A0.jpg")
            self.correctimage = gtk.Image()
            self.incorrectimage = gtk.Image()
            self.correctimage.set_from_file("images/correct.jpg")
            self.incorrectimage.set_from_file("images/incorrect.jpg")
            
            self.frame = gtk.Frame()
            
            self.hboximg = gtk.HBox(False, 100)
            self.hboximg.set_border_width(10)
            self.hboximg.add(self.image1)
            #self.hboximg.add(self.image2)
            
            self.frame.set_label("Pictures")
            self.frame.set_label_align(1.0,0.0)
            self.frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
            self.frame.add(self.hboximg)
            
            self.correctbox = gtk.VBox(False, 100)
            self.correctbox.add(self.correctimage)
            self.incorrectbox = gtk.VBox(False, 100)
            self.incorrectbox.add(self.incorrectimage)
            
            #self.con
            
            self.correctbox.show()
            self.incorrectbox.show()
            self.correctimage.show()
            self.incorrectimage.show()

    # Set up two pictures in GUI
    def setupTwoPictureFrames(self):
            self.image1 = gtk.Image()
            self.image1.set_from_file("images/A0.jpg")
            self.image2 = gtk.Image()
            self.image2.set_from_file("images/A0.jpg")
            self.correctimage = gtk.Image()
            self.incorrectimage = gtk.Image()
            self.correctimage.set_from_file("images/correct.jpg")
            self.incorrectimage.set_from_file("images/incorrect.jpg")
            
            self.frame = gtk.Frame()
            
            self.hboximg = gtk.HBox(False, 100)
            self.hboximg.set_border_width(10)
            self.hboximg.add(self.image1)
            self.hboximg.add(self.image2)
            
            self.frame.set_label("Pictures")
            self.frame.set_label_align(1.0,0.0)
            self.frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
            self.frame.add(self.hboximg)
            
            self.correctbox = gtk.VBox(False, 100)
            self.correctbox.add(self.correctimage)
            self.incorrectbox = gtk.VBox(False, 100)
            self.incorrectbox.add(self.incorrectimage)
            
            #self.con
            
            self.correctbox.show()
            self.incorrectbox.show()
            self.correctimage.show()
            self.incorrectimage.show()

    # Set up button choices: A, B
    def setupButton(self):
        #button alignment/box creation
        self.hboxbuttons = gtk.HBox(True, 100)
        self.buttonA = gtk.Button("Button A") #adds buttons to window
        self.buttonB = gtk.Button("Button B")
        self.buttonA.connect("clicked", self.choseA, "A chosen")
        self.buttonB.connect("clicked", self.choseB, "B chosen")
        self.hboxbuttons.add(self.buttonA)          #puts button on box
        self.hboxbuttons.add(self.buttonB)

    # Set up
    def setupWelcome(self):
        self.contBox = gtk.HBox(True, 0)
        self.valBox = gtk.VBox(False, 0)
        self.welcomeBox = gtk.VBox(False, 0)
        self.valignCont = gtk.Alignment(0.5, 1, 0, 0)
        self.valBox.pack_start(self.valignCont)
        self.halignCont = gtk.Alignment(0.528, 1, 0, 0)
        
        self.welcomeimg = gtk.Image()
        self.welcomeimg.set_from_file("images/welcome.jpg")
        self.welcomeBox.add(self.welcomeimg)

        self.contButton = gtk.Button("Continue")
        self.contButton.set_size_request(200, 40)
        self.continueSignal = self.contButton.connect("clicked", self.welcomeClose, "contButton")
        
        self.halignCont.add(self.contBox)
        self.valBox.pack_start(self.halignCont, False, False, 3)        
        self.contBox.add(self.contButton)
        self.welcomeBox.add(self.valBox)
        self.window.add(self.welcomeBox)
        
        #show methods for the welcome screen
        self.contBox.show()
        self.valBox.show()
        self.valignCont.show()
        self.halignCont.show()
        self.welcomeimg.show()
        self.contButton.show()
        self.welcomeBox.show()

    # 
    def welcomeClose(self, widget, data):
        #button trigger to close welcome box and show the experiment trial
        print "Close instructions event occurred"
        print "Instructions read"
        print "User pressed %s " % data
        self.window.remove(self.welcomeBox)
        self.window.add(self.overallbox)           #adds box to window
        self.window.show_all()
        self.choicePhase()

    # Choose to do learning phase, testing 1 or 2
    def choicePhase(self):
        global numOfImageOption
        if (learning == True):
            self.learningPhase()
        else:
            print numOfImageOption
            if(numOfImageOption == 1):
                self.doTrialOne()
            elif(numOfImageOption == 2):
                self.doTrialTwo()
            else:
                print "wrong num of image option"
        
    def endTrialLearning(self):
        global numtrials
        global learningnum
        global learningCorrect
        if (configLearningOption == "trials") :
            learningnum += 1
            if learningnum > numtrials:
                self.endallLearning()
            else:
                self.doTrialLearning()
        if (configLearningOption == "ratio"):
            if learningnum > 2:
                if ((Fraction(learningCorrect,learningnum)) > configLearningRatio):
                    self.endallLearning()
                else:
                    self.doTrialLearning()
            self.doTrialLearning()


    def endallLearning(self):
        self.window.remove(self.overallbox)
        self.buttonA.disconnect(self.testSignalA)
        self.buttonB.disconnect(self.testSignalB)
        self.buttonA.connect("clicked", self.choseA, "A chosen")
        self.buttonB.connect("clicked", self.choseB, "B chosen")
        self.window.add(self.overallbox)
        self.doTrial()


    def learningPhase(self):
        print "learning trial begun"
        self.doTrialLearning()

    def setImageTrialLearning(self,image1File,image2File):
        self.image1.set_from_file(image1File)
        self.image2.set_from_file(image2File)
        self.image1.show()
        self.image2.show()
        self.window.show_all()

    def doTrialLearning(self):
        global rannum
        global completeImageList
        global oneImageAnswer
        global numOfImageOption
        if (numOfImageOption == 2):
            rannum = randint(0, numImageSets)
            temp1 = "images/%s" %imgA[rannum]
            print temp1
            temp2 = "images/%s" %imgB[rannum]
            print temp2
            self.setImageTrialLearning(temp1,temp2)
        if (numOfImageOption == 1):
            rannum = randint(0, len(completeImageList)-1)
            temp1 = "images/%s" %completeImageList[rannum]
            print temp1
            self.image1.set_from_file(temp1)
            oneImageAnswer = completeImageList[rannum]
            oneImageAnswer = oneImageAnswer[0]
            self.image1.show()
            self.window.show_all()

    def setupImages(self):
        #sets up the images by randomly generating an image that wasn't used yet
        global imgA
        global imgB
        global completeImageList
        global numOfImageOption
        iarray = self.load_all_images("images/")
        if(numOfImageOption == 2):
            imgA = self.sort_array(iarray,'A')
            imgB = self.sort_array(iarray,'B')
        if(numOfImageOption == 1):
            completeImageList = self.sort_array(iarray,'A')
            imgB = self.sort_array(iarray,'B')
            completeImageList.extend(imgB)
            print completeImageList
    
    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.

        print "Delete event occurred"
        print "User manually closed the program"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    # Called when user presses Red X on GUI, closes output stream to log
    def destroy(self, widget, data=None):
        #kills the program
        self.datafile.close()
        print "Destroy signal occurred"
        gtk.main_quit()
    
    def choseA(self, widget, data):
        global g_trialNumber
        global rannum
        global numOfImageOption
        global learningCorrect
        print "A was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 1:
                print "Correct answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", A chosen, correct\n")
                if(learning == True):
                    learningCorrect+=1
                    self.window.remove(self.overallbox)
                    self.window.add(self.correctbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.correctbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()
            else:
                print "Incorrect answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", A chosen, incorrect\n")
                if(learning==True):
                    self.window.remove(self.overallbox)
                    self.window.add(self.incorrectbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.incorrectbox)
                    self.window.add(self.overallbox)
                    self.window.show_all() 

            if blockMode == False:
                if learning == True:
                    self.endTrialLearning()
                self.endTrial()
            else:
                self.doTrialOne()
        if (numOfImageOption == 1):
            if oneImageAnswer == 'A':
                print "Correct answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", A chosen, correct\n")
                if learning == True:
                    learningCorrect += 1
                    self.window.remove(self.overallbox)
                    self.window.add(self.correctbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.correctbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()
            else:
                print "Incorrect answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", A chosen, incorrect\n")
                if learning == True:
                    self.window.remove(self.overallbox)
                    self.window.add(self.incorrectbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.incorrectbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()   
            if blockMode == False :
                if learning == True:
                    self.endTrialLearning()
                self.endTrial()
            else:
                self.doTrialOne()
    
    def choseB(self, widget, data):
        global g_trialNumber
        global rannum
        global numOfImageOption
        global learningCorrect
        print "B was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 2:
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", B chosen, correct\n")
                if learning == True:
                    learningCorrect += 1
                    self.window.remove(self.overallbox)
                    self.window.add(self.correctbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.correctbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", B chosen, incorrect\n")
                if learning == True:
                    self.window.remove(self.overallbox)
                    self.window.add(self.incorrectbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.incorrectbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()
            if blockMode == False:
                if learning == True:
                    self.endTrialLearning()
                self.endTrial()
            else:
                self.doTrialOne()
        if (numOfImageOption == 1):
            if oneImageAnswer == 'B':
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", B chosen, correct\n")
                if learning == True:
                    learningCorrect += 1
                    self.window.remove(self.overallbox)
                    self.window.add(self.correctbox)
                    self.window.show_all()
                    while gtk.events_pending():
                        gtk.main_iteration(False)
                    time.sleep(3)
                    self.window.remove(self.correctbox)
                    self.window.add(self.overallbox)
                    self.window.show_all()
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(g_trialNumber) + ", B chosen, incorrect\n")
                self.window.remove(self.overallbox)
                self.window.add(self.incorrectbox)
                self.window.show_all()
                while gtk.events_pending():
                    gtk.main_iteration(False)
                time.sleep(3)
                self.window.remove(self.incorrectbox)
                self.window.add(self.overallbox)
                self.window.show_all()
            if blockMode == False :
                if learning == True:
                    self.endTrialLearning()
                self.endTrial()
            else:
                self.doTrialOne()

    
    def endTrial(self): 
        global numtrials
        global g_trialNumber
        g_trialNumber += 1
        if g_g_trialNumber > numtrials:
            self.endall()
        else:
            self.doTrial()
    
    def setupQuestions(self, numberOfImg, number, mode): #number is how many questions or blocks
        # mode is whether is its questions or blocks// blocks or questions should be placed
        global completeImageList
        global numtrials
        global blockMode
        global numOfImageOption
        if(mode == "blocks"):
            blockMode = True
        else:
            blockMode = False
        if(numberOfImg == 1):
            numOfImageOption = 1

            
    def setImageTrialTwo(self,image1File,image2File):# set and show the image for trial 2
        self.image1.set_from_file(image1File)
        self.image2.set_from_file(image2File)
        self.image1.show()
        self.image2.show()
        self.window.show_all()
        
    def doTrialTwo(self): #do trial when two images are involved
        print "doing trial"
        global rannum
        global completeImageList
        global oneImageAnswer
        rannum = randint(0, numImageSets-1)
        temp1 = "images/%s" %imgA[rannum]
        print temp1
        temp2 = "images/%s" %imgB[rannum]
        print temp2
        self.setImageTrialTwo(self,temp1,temp2)

    # Trial for one image
    def doTrialOne(self): #shows questions for 1 image experiments
        global g_trialNumber # g_trialNumber dependent on number of available images, in this case 11
        global rannum
        global completeImageList
        global oneImageAnswer
        print "One image trial", g_trialNumber
        g_trialNumber += 1
        
        if len(completeImageList) > 0:
                rannum = randint(0, len(completeImageList)-1)
                temp1 = "images/%s" %completeImageList[rannum]
                print temp1
                self.image1.set_from_file(temp1)
                self.image1.show()
                oneImageAnswer = completeImageList[rannum]
                oneImageAnswer = oneImageAnswer[0]
                completeImageList.remove(completeImageList[rannum])
                self.window.show_all()
        else:
                g_trialNumber = 1 # reset g_trialNumber to 1
                self.endOfBlock()

    def endOfBlock(self): # used to determine if more blocks needs to be shown at the end of a block
        global numOfBlocks
        print "End of block ", numOfBlocks
        numOfBlocks -= 1
        if numOfBlocks > 0:
            self.setupImages()
            self.doTrialOne() # Doug: Hard-coded to always do trial one?
        else:
            self.endall()
    
    def load_all_images(self, directory):
        imgarray = []
        for files in os.listdir(directory):
            imgarray.append(files)
        return imgarray
    
    def sort_array(self, array, firstletter):
        #sorts the array given in the parameter to only have the images
        #with the filenames that begin with firstletter
        sorted = []
        for img in array:
            if img[0].upper() == firstletter:
                sorted.append(img)
        return sorted
    
    def endall(self): #end of the experiment... also shows the end of the experiment screen
        print "end of trial"
        self.welcomeBox.remove(self.valBox)
        self.contButton.set_label("Exit")
        self.contButton.disconnect(self.continueSignal)
        self.contButton.connect("clicked", self.destroy, "contButton")
        
        self.window.remove(self.overallbox)
        self.endbox = gtk.VBox(False, 0)
        self.endimg = gtk.Image()
        self.endimg.set_from_file("images/ThankYou.jpg")
        self.endbox.add(self.endimg)
        #self.endButton = gtk.Button("Exit")
        #self.endButton.connect("clicked", self.destroy, "endButton")
        #self.endbox.add(self.endButton)
        self.endbox.add(self.valBox)
        self.window.add(self.endbox)
        self.endimg.show()
        #self.endButton.show()
        self.endbox.show()
    
    def __init__(self):
        self.setupQuestions(1, 2, "blocks")
        self.setupWindow()
        print "Window has been set up"
        self.overallbox = gtk.VBox(False, 0)
        self.setupPictureFrames()
        self.setupButton()
        self.setupWelcome()
        
        self.datafile = open("testdata.txt","w")
        self.datafile.write("Gracken Experiment: One Image, Testing Mode\n") # current configuration being worked on
        self.setupImages()
        
        self.overallbox.pack_start(self.frame, False, False, 20)
        self.overallbox.pack_start(self.separator, False, True, 30)
        self.overallbox.pack_start(self.hboxbuttons, False, False, 0)
        
        #shows the window and others...
        #self.buttonA.show()
        #self.buttonB.show()
        #self.image1.show()
        #self.image2.show()
        #self.hbox1.show()
        #self.hboximg.show()
        #self.overallbox.show()
        
        self.window.show()

    def main(self):
        
        print "In main"
        gtk.main()
        print "After main: now closing"

    #def runExp(self):
        
print __name__
if __name__ == "__main__":
    grack = Gracken()
    grack.main()
