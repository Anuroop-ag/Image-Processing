#Convert a colour image to grayscale using formula
#Formula(memorise) : I = 0.21*R+0.71*G+0.07*B


import cv2
import numpy as np


img = cv2.imread('3.jpg',-1) 
height = np.size(img,0)
width = np.size(img,1)

print 'height ',height
print 'width ',width

for i in range(0,height):
	for j in range(0,width):
		#print img[i,j][0]
		img[i,j] = img[i,j][0]*0.07+img[i,j][1]*0.71+img[i,j][2]*0.21


cv2.imwrite('3_in_grayscale.jpg',img)

