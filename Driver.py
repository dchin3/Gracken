#!usr/bin/python

from LearningBlock import *
from TestingBlock import *

from LearningPhase import *
from TestingPhase import *

from Experiment import *

from ExperimentGUI import *

from Results import *

"""
Main method that runs Gracken program
"""
def main():
    print "DEBUG: Entering Driver.main()"

    expGUI = ExperimentGUI() # create new ExperimentGUI object using default values    

    res = Results() # create new Results object using default value
    res.writeToFile(expGUI.window.get_title() + " Experiment\n\n")

   # http://www.pygtk.org/dist/pygtk2-tut.pdf
    

    lb1 = LearningBlock(["B0.jpg", "B1.jpg", "B2.jpg"], 80.0)
    lb2 = LearningBlock(["B3.jpg", "B4.jpg", "B5.jog"], 75.0)
    tb1 = TestingBlock(["A0.jpg", "A1.jpg", "A2.jpg"])
    tb2 = TestingBlock(["A3.jpg", "A4.jpg"])

    lblockList = [lb1, lb2]
    tblockList = [tb1, tb2]
    
    lp = LearningPhase(lblockList)
    tp = TestingPhase(tblockList)
    phaseList = [lp, tp]
    exp = Experiment(phaseList)
    exp.runPhases(res)
    
    print "DEBUG: Entering gtk.main()"

    gtk.main()

    print "DEBUG: Exiting gtk.main()"

    print "DEBUG: Exiting Driver.main()"

if __name__ == "__main__":
    main()
