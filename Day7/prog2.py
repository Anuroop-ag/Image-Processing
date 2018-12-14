#Removing salt and pepper noise
#median filter

#we will make our own median filter

import cv2
import numpy as np

img = cv2.imread('sap.png',0)
temp = cv2.imread('sap.png',0)
row,col = img.shape

for i in range(1,row-1):
	for j in range(1,col-1):
		my_list = []
		
		my_list.append(img[i-1,j-1])
		my_list.append(img[i-1,j])
		my_list.append(img[i-1,j+1])
		my_list.append(img[i,j-1])
		my_list.append(img[i,j])
		my_list.append(img[i,j+1])
		my_list.append(img[i+1,j-1])
		my_list.append(img[i+1,j])
		my_list.append(img[i+1,j+1])
	
		my_list.sort()


		temp[i,j] = my_list[4] 

cv2.imwrite('sap_removed.png',temp)
