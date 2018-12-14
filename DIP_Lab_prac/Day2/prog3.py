import cv2
import numpy as np 
import os

img  = cv2.imread('3.jpg',-1)
sinfo = os.stat('3.jpg')
print("size of 3.jpg is " + str(sinfo.st_size) + " bytes")
#print("size of 3.jpg is " + str(os.stat('3.jpg').st_size) + " bytes")
row,col,channel = img.shape
print(str(row) + "rows " + str(col)+ " columns" )