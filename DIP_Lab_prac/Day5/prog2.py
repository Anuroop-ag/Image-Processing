import cv2
import numpy as np 

img = cv2.imread('original.png',0)
row,col = img.shape

for i in range(1,row-1):
	for j in range(1,col-1):
		img[i,j] = int((img[i-1,j-1] + 2*img[i-1,j] + img[i-1,j+1] + 2*img[i,j-1] + 4*img[i,j] + 2*img[i,j+1] + img[i+1,j-1] + 2*img[i+1,j] + img[i+1,j+1])/16)

	
cv2.imwrite('mean.png',img)	