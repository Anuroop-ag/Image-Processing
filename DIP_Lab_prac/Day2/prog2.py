import cv2
import numpy as np 


img = cv2.imread('45g.jpg',0)
row,col = img.shape
temp  = np.zeros((row,col),np.uint8)
for i in range(0,row):
	for j in range(0,col):
		if(img[i,j]>127):
			temp[i,j] = 255
		else:
			temp[i,j] = 0

cv2.imwrite('binary_from_gray.jpg',temp)

