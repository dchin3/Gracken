#!/usr/bin/python

import os, sys, signal
import math
from string import *
from numpy import *
from ftplib import FTP
from random import random, randint, shuffle
import time
import numpy as np
import numpy.numarray as na
from scipy import ndimage
from array import *


 
def load_all_images(self, directory):
    imgarray = []
    
    for files in os.walk(directory):
        for f in files:
            imgarray.append(f)
            
    for i in imgarray:
        print i
    return imgarray
