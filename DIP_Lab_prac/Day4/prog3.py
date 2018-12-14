import cv2
import numpy as np 

img = cv2.imread('original.png',0)
row,col = img.shape

c = (256-1)/np.log(256)
gamma = 0.5

for i in range(0,row):
	for j in range(0,col):
		val = c*(img[i,j]**gamma)
		while(val>255):
			val = val - 255
		img[i,j] = val

cv2.imwrite('gamma_transform.png',img)