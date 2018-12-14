import cv2
import numpy as np 

img = cv2.imread('sap.png',0)

#sap can be removed by median filter

row,col = img.shape
tempu = img

for i in range(1,row-1):
	for j in range(1,col-1):
		temp = [0]*9
		temp[0] = img[i-1,j-1]
		temp[1] = img[i-1,j]
		temp[2] = img[i-1,j+1]
		temp[3] = img[i,j-1]
		temp[4] = img[i,j]
		temp[5] = img[i,j+1]
		temp[6] = img[i+1,j-1]
		temp[7] = img[i+1,j]
		temp[8] = img[i+1,j+1]
		temp.sort()
		tempu[i,j] = temp[4]

cv2.imwrite('sap_removed.png',tempu)