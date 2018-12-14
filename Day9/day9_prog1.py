#### DAY 9  11/10/2017 #####
'''
Take an image, convert to grayscale, display only those pixels which are in a particular range.
'''


import cv2
import numpy as np

img = cv2.imread('45g.jpg',0)
cv2.imshow('original_img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("enter range of pixels : ")
print ("Enter range start: ")
u = int(input())
print ("Enter range end: ")	
v = int(input())

row,col = img.shape

for i in range(0,row):
	for j in range(0,col):
		if(img[i,j]>u and img[i,j]<v):
			pass
		else:
			img[i,j] = 255

cv2.imshow('result_img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

