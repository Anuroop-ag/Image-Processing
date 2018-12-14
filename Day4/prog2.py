'''Write a program to detect
a.Horizontal line
b.vertical line'''


import numpy as np
import cv2



i1 = cv2.imread('hori_ver.jpg',0)
sobelx = cv2.Sobel(i1,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(i1,cv2.CV_64F,0,1,ksize=5)

#########Detecting horizontal lines###############
i2 = cv2.addWeighted(sobelx,0,sobely,1,0)
cv2.imwrite('hori_result.jpg',i2)

#########Detecting vertical lines###############
i3 = cv2.addWeighted(sobelx,1,sobely,0,0)
cv2.imwrite('verti_result.jpg',i3)
