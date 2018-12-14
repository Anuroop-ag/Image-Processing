'''Enhance the grayscale image using median filter of size 3*3 and 5*5 mask.'''

import cv2
import numpy as np

img = cv2.imread('Apply_Median_Filter.jpg',0)
temp = cv2.imread('Apply_Median_Filter.jpg',0)
row,col = img.shape

###################3*3 mask median filter##################################

for i in range(1,row-1):
	for j in range(1,col-1):
		
		my_list = []
		
		for x in range(i-1,i+2):
			for y in range(j-1,j+2):
				my_list.append(img[x,y])
		
		my_list.sort()


		temp[i,j] = my_list[4]
		


cv2.imwrite('Median_Filter_3_3_output.jpg',temp)


##########################5*5 mask median filter##############################

temp = cv2.imread('Apply_Median_Filter.jpg',0)

for i in range(1,row-2):
	for j in range(1,col-2):
		
		my_list = []
		
		for x in range(i-2,i+3):
			for y in range(j-2,j+3):
				my_list.append(img[x,y])
		
		my_list.sort()


		temp[i,j] = my_list[12]

cv2.imwrite('Median_Filter_5_5_output.jpg',temp)
