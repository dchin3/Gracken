from fractions import Fraction
#icon images
icon_img = "images/icon.png"

#image directory - location of the folder with the images
imgdir = "images/"

blockMode = True # True or False if block method is used
configLearningOption = "ratio" #so far only "trials" and "ratio"

numtrials = 7 #number of trials images shown
learningRatio = Fraction('1/2') #used only if learning option is set to ratio

numImageSets = 5 # sets of image
numOfBlocks = 2 #number of blocks

correctanswer = [1,2,1,2,1] #used for 2 sets

numOfImageOption = 1 # only works for 1 or 2

learning = False

