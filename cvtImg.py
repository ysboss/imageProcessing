import numpy as np
import cv2
from method import saveImage

with open('results4.txt', 'r') as fd:
    lines = fd.readlines()
    for line in lines: 
        l = line.split(' ')
        #print (l[0]+' '+l[1])
        saveImage(l[0], int(l[1]))
fd.close() 