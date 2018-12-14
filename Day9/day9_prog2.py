#### DAY 9  11/10/2017 #####
'''
Take an image, convert to grayscale.
Perform Segmentation.
'''


import cv2
import numpy as np

################## SEGMENTATION #############################

img2 = cv2.imread('mimg.jpg',0)
'''cv2.imwrite('my_img_g.jpg',img)
'''
cloud = cv2.imread('mimg.jpg',0)
trees = cv2.imread('mimg.jpg',0)
water = cv2.imread('mimg.jpg',0)

## showing cloud ##
row,col = cloud.shape

for i in range(0,row):
	for j in range(0,col):
		if(cloud[i,j]>240 and cloud[i,j]<=255):
			#print('cloud')
			continue
		else:
			cloud[i,j] = 0

cv2.imwrite('cloud.jpg',cloud)

## showing trees ##
row,col = trees.shape

for i in range(0,row):
	for j in range(0,col):
		if(trees[i,j]>=60 and trees[i,j]<70):
			#print('tree')
			continue
		else:
			trees[i,j] = 255


cv2.imwrite('trees.jpg',trees)

## showing water ##

row,col = water.shape


for i in range(0,row):
	for j in range(0,col):
		if(water[i,j]>120 and water[i,j]<180):
			#print('water')
			continue
		else:
			water[i,j] = 255


cv2.imwrite('water.jpg',water)
