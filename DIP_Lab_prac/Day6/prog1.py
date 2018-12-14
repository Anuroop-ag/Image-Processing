import cv2
import numpy as np 

img = cv2.imread('one.jpg',-1)
row,col,channel = img.shape

red = np.zeros((row,col),np.uint8)
green = np.zeros((row,col),np.uint8)
blue = np.zeros((row,col),np.uint8)


for i in range(0,row):
	for j in range(0,col):
		for k in range(0,channel):
			if(k==0):
				blue[i,j] = img[i,j,k]
			elif(k==1):
				green[i,j] = img[i,j,k]
			else:
				red[i,j] = img[i,j,k]

cv2.imwrite("red.jpeg",red)
cv2.imwrite("blue.jpeg",blue)
cv2.imwrite("green.jpeg",green)

for i in range(0,row):
	for j in range(0,col):
		for k in range(0,channel):
			if(k==0):
				img[i,j,k] = blue[i,j]
			elif(k==1):
				img[i,j,k] = green[i,j]
			else:
				img[i,j,k] = red[i,j]

cv2.imwrite('merged.jpg',img)