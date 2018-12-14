import cv2
import numpy as np

img = cv2.imread('one.jpg',0)
img2 = img
cv2.imwrite('original.jpg',img)
row,column = img.shape

for i in range(1,row-1):
    for j in range(1,column-1):
        img2[i,j] = (img[i,j]*2+img[i+1,j]+img[i-1,j]+img[i,j+1]+img[i,j-1])/6

        #img2[i,j] = (img[i,j]+img[i+1,j]+img[i-1,j]+img[i,j+1]+img[i,j-1]+img[i-1,j-1]+img[i-1,j+1]+img[i+1,j+1]+img[i+1,j-1])/9
cv2.imwrite('mean.jpg',img2)

