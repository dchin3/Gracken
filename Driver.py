#!usr/bin/python

from ImageCategory import *

from LearningBlock import *
from TestingBlock import *

from LearningPhase import *
from TestingPhase import *

from Experiment import *

from ExperimentGUI import *

from Results import *

from datetime import datetime

"""
Main method that runs Gracken program
"""
def main():
    print "DEBUG: Entering Driver.main()"

    expGUI = ExperimentGUI() # create new ExperimentGUI object using default values    

    res = Results() # create new Results object using default value
    res.writeToFile(expGUI.window.get_title() + " Experiment\n")
    res.writeToFile("Experiment started at: " + str(datetime.now()) + "\n\n")

    gtk.main()

   # http://www.pygtk.org/dist/pygtk2-tut.pdf
    
    catA = ImageCategory("A", ["A0.jpg", "A1.jpg", "A2.jpg", "A3.jpg", "A4.jpg", "A5.jpg"])
    catB = ImageCategory("B", ["B0.jpg", "B1.jpg", "B2.jpg", "B3.jpg", "B4.jpg"])

    categories = [catA, catB]
    
    lb1 = LearningBlock(["A0.jpg", "A1.jpg", "B2.jpg"], 10.0)
    lb2 = LearningBlock(["B3.jpg", "B4.jpg", "A1.jpg"], 15.0)
    tb1 = TestingBlock(["A0.jpg", "A1.jpg", "B2.jpg"])
    tb2 = TestingBlock(["A3.jpg", "B4.jpg"])

    lblockList = [lb1, lb2]
    tblockList = [tb1, tb2]
    
    lp = LearningPhase(lblockList)
    tp = TestingPhase(tblockList)
    phaseList = [lp, tp]
    exp = Experiment(phaseList)
    exp.runPhases(categories, res)
    
    print "DEBUG: Entering gtk.main()"
    
    #gtk.main()
    
    print "DEBUG: Exiting gtk.main()"

    res.writeToFile("Experiment ended at: " + str(datetime.now()))

    print "DEBUG: Exiting Driver.main()"

if __name__ == "__main__":
    main()
