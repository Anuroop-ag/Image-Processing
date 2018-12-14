'''
#Compute intersection of two images(take minimum pixel)
#merge two grayscale images using XOR and XNOR
'''

import numpy as np
import cv2

img1 = cv2.imread('lena.jpg',0)
img2 = cv2.imread('one.jpg',0)

img1 = cv2.resize(img1,(400,400))
img2 = cv2.resize(img2,(400,400))

'''cv2.imshow('img1',img1)
cv2.waitKey(0)

cv2.imshow('img2',img2)
cv2.waitKey(0)
'''

#########INTERSECT################################

temp_img = cv2.resize(img2,(400,400))

for i in range(0,400):
    for j in range(0,400):
        temp_img[i,j] = min(img1[i,j],img2[i,j])

cv2.imwrite('intersect.jpg',temp_img)

temp_i = temp_img
##########XOR#####################################

for i in range(0,400):
    for j in range(0,400):
        temp_img[i,j] =img1[i,j]^img2[i,j]

cv2.imwrite('xor.jpg',temp_img)

xor_i = temp_img
#########XNOR#######################################
for i in range(0,400):
    for j in range(0,400):
        temp_img[i,j] = ~temp_img[i,j]
cv2.imwrite('xnor.jpg',temp_img)

xnor_i = temp_img
###############################################

#res = np.hstack((temp_i,xor_i,xnor_i))
#cv2.imwrite('result.jpg',res)
