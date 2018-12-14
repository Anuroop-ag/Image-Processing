#Contrast adjustment

import cv2
import numpy as np


img= cv2.imread('3.jpg',0)
height = np.size(img[0])
width = np.size(img[1])

#print 'height ', height
#print 'width ', width

for i in range(0,height-1):
    for j in range(0,width-1):
        try:
            if img[i,j] >= 127:
                img[i,j] = 250
            else:
                img[i,j] = 50
        except IndexError:
            continue
        
#cv2.imshow('high_contrast',img)
cv2.imwrite('high_contrast_img.jpg',img)
#cv2.waitKey(0)
