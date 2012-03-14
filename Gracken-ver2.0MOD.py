#!/usr/bin/python

from fractions import Fraction
import pygtk
import gtk
import sys, os
from random import *
from Grackenconfig import *
#from lib.Grackenlib import *
import time

#global
numtrials = confignumTrials # number of questions
numOfLearning = confignumLearning # number of learning questions
learningnum = 1 #counter for current learning questions given
trialnum = 1 #counter for current trial number
rannum = 0
iarray = []
imgA = []
imgB = []
completeImageList = [] #only used when one image option is enabled
oneImageAnswer = 'A' #only used when one image option is enabled
learningCorrect = 0
numOfBlocks = confignumBlocks
blockMode = configBlockMode
numOfImageOption = configImageNumOption

class Gracken:
    
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
    
    def setupButton(self):
        
        #button alignment/box creation
        self.hboxbuttons = gtk.HBox(True, 100)
        self.buttonA = gtk.Button("Button A") #adds buttons to window
        self.buttonB = gtk.Button("Button B")
        self.buttonA.connect("clicked", self.choseA, "A chosen")
        self.buttonB.connect("clicked", self.choseB, "B chosen")
        self.hboxbuttons.add(self.buttonA)          #puts button on box
        self.hboxbuttons.add(self.buttonB)

    def setupLearningButton(self):
        
        #button alignment/box creation
        self.hboxbuttons = gtk.HBox(True, 100)
        self.buttonA = gtk.Button("Button A") #adds buttons to window
        self.buttonB = gtk.Button("Button B")
        self.testSignalA = self.buttonA.connect("clicked", self.choseAlearning, "A chosen")
        self.testSignalB = self.buttonB.connect("clicked", self.choseBlearning, "B chosen")
        self.hboxbuttons.add(self.buttonA)          #puts button on box
        self.hboxbuttons.add(self.buttonB)


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

    def welcomeClose(self, widget, data):
        #button trigger to close welcome box and show the experiment trial
        print "Close instructions event occurred"
        print "Instructions read"
        print "User pressed %s " % data
        self.window.remove(self.welcomeBox)
        self.window.add(self.overallbox)           #adds box to window
        self.window.show_all()
        self.choicePhase()

    def choicePhase(self):#choose to do learning phase, testing 1 or testing 2
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

    def choseAlearning(self, widget, data):
        global learningnum
        global rannum
        global learningCorrect
        global numOfImageOption
        print "Learning: A was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 1:
                print "Learning: correct answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", A chosen, correct\n")
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
                print "Learning: incorrect answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", A chosen, incorrect\n")
                self.window.remove(self.overallbox)
                self.window.add(self.incorrectbox)
                self.window.show_all()
                while gtk.events_pending():
                    gtk.main_iteration(False)
                time.sleep(3)
                self.window.remove(self.incorrectbox)
                self.window.add(self.overallbox)
                self.window.show_all()
        if (numOfImageOption == 1):
            if (oneImageAnswer == 'A'):
                print "Learning: correct answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", A chosen, correct\n")
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
                print "Learning: incorrect answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", A chosen, incorrect\n")
                self.window.remove(self.overallbox)
                self.window.add(self.incorrectbox)
                self.window.show_all()
                while gtk.events_pending():
                    gtk.main_iteration(False)
                time.sleep(3)
                self.window.remove(self.incorrectbox)
                self.window.add(self.overallbox)
                self.window.show_all()
        self.endTrialLearning()
    

    def choseBlearning(self, widget, data):
        global numOfLearning
        global rannum
        global learningCorrect
        global numOfImageOption
        print "Learning: B was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 2:
                print "Learning: correct answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", B chosen, correct\n")
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
                print "Learning: incorrect answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", B chosen, incorrect\n")
                self.window.remove(self.overallbox)
                self.window.add(self.incorrectbox)
                self.window.show_all()
                while gtk.events_pending():
                    gtk.main_iteration(False)
                time.sleep(3)
                self.window.remove(self.incorrectbox)
                self.window.add(self.overallbox)
                self.window.show_all()
        if (numOfImageOption == 1):
            if (oneImageAnswer == 'B'):
                print "Learning: correct answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", B chosen, correct\n")
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
                print "Learning: incorrect answer chosen"
                self.datafile.write("learning trial number: " + str(trialnum) + ", B chosen, incorrect\n")
                self.window.remove(self.overallbox)
                self.window.add(self.incorrectbox)
                self.window.show_all()
                while gtk.events_pending():
                    gtk.main_iteration(False)
                time.sleep(3)
                self.window.remove(self.incorrectbox)
                self.window.add(self.overallbox)
                self.window.show_all()
        self.endTrialLearning()
        
    def endTrialLearning(self):
        global numOfLearning
        global learningnum
        global learningCorrect
        if (configLearningOption == "trials") :
            learningnum += 1
            if learningnum > numOfLearning:
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
    
    def destroy(self, widget, data=None):
        #kills the program
        self.datafile.close()
        print "destroy signal occurred"
        gtk.main_quit()
    
    def choseA(self, widget, data):
        global trialnum
        global rannum
        global numOfImageOption
        print "A was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 1:
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", A chosen, correct\n")
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", A chosen, incorrect\n")
            if blockMode == False :
                self.endTrial()
            else:
                self.doTrialOne()
        if (numOfImageOption == 1):
            if oneImageAnswer == 'A':
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", A chosen, correct\n")
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", A chosen, incorrect\n")
            if blockMode == False :
                self.endTrial()
            else:
                self.doTrialOne()
    
    def choseB(self, widget, data):
        global trialnum
        global rannum
        global numOfImageOption
        print "B was chosen"
        if (numOfImageOption == 2):
            if correctanswer[rannum] == 2:
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", B chosen, correct\n")
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", B chosen, incorrect\n")
            if blockMode == False :
                self.endTrial()
            else:
                self.doTrialOne()
        if (numOfImageOption == 1):
            if oneImageAnswer == 'B':
                print "correct answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", B chosen, correct\n")
            else:
                print "incorrect answer chosen"
                self.datafile.write("trial number: " + str(trialnum) + ", B chosen, incorrect\n")
            if blockMode == False :
                self.endTrial()
            else:
                self.doTrialOne()

    
    def endTrial(self): 
        global numtrials
        global trialnum
        trialnum += 1
        if trialnum > numtrials:
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

            
    def setImageTrailTwo(self,image1File,image2File):# set and show the image for trial 2
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

    def doTrialOne(self): #shows questions for 1 image experiments
        print "doing trial"
        global rannum
        global completeImageList
        global oneImageAnswer
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
                self.endOfBlock()

    def endOfBlock(self): # used to determine if more blocks needs to be shown at the end of a block
        global numOfBlocks
        print "end of block"
        numOfBlocks -= 1
        if numOfBlocks > 0:
            self.setupImages()
            self.doTrialOne()
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
        print "window is now setup"
        self.overallbox = gtk.VBox(False, 0)
        self.setupPictureFrames()
        self.setupButton()
        self.setupWelcome()
        
        self.datafile = open("testdata.dat","w")
        self.datafile.write("Gracken Trial\n")
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
        
        print "main"
        gtk.main()
        print"after main"

    #def runExp(self):
        
        

print __name__
if __name__ == "__main__":
    grack = Gracken()
    grack.main()
