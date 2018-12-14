'''

Take a color image. Convert to :

1.Grayscale
2.Binary

'''

import cv2
import numpy as np

################# grayscale #######################

img_gray = cv2.imread('messi.png',0)
cv2.imwrite('gray_img.png',img_gray)

## for BINARY we are taking a threshold of 127 ###

rows,col = img_gray.shape

for i in range(0,rows):
	for j in range(0,col):
		if(img_gray[i,j]>=127):
			img_gray[i,j] = 255
		else:
			img_gray[i,j] = 0

cv2.imwrite('bin_img.png',img_gray)

###################################################
