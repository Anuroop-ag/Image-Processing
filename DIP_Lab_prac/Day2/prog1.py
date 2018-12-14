import cv2
import numpy as np
#0.71*R+0.21*G+0.07*B
img = cv2.imread('3.jpg',-1)
row,col,channel = img.shape
temp = np.zeros((row,col),np.uint8)
for i in range(0,row):
	for j in range(0,col):
		temp[i,j] = int(img[i,j,0]*0.71 + img[i,j,1]*0.21 + img[i,j,2]*0.07)

cv2.imwrite('gray_from_color.jpg',temp)
