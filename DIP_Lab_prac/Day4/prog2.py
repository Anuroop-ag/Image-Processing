import cv2
import numpy as np 

img = cv2.imread('original.png',0)
row,col = img.shape
c = (256-1)/np.log(256)

for i in range(0,row):
	for j in range(0,col):
		img[i,j] = min(np.exp(img[i,j]/c)-1,255)
cv2.imwrite('inverse_log_transform.png',img)