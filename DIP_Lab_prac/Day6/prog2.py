import cv2
import numpy as np 


img1 = cv2.imread('i1.jpg',0)
img2 = cv2.imread('i2.jpg',0)

img1 = cv2.resize(img1,(400,400))
img2 = cv2.resize(img2,(400,400))

row,col = img1.shape

intersect = np.zeros((400,400),np.uint8)
for i in range(0,row):
	for j in range(0,col):
		intersect[i,j] = min(img2[i,j],img1[i,j])
		
		

cv2.imwrite('intersect.jpg',intersect)