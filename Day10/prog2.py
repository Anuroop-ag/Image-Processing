'''
consider a straight line form by the following:
0011223324

find line by hough transform
'''

import cv2
import numpy as np

img = cv2.imread('lenna.png',0)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('lenna.png',-1) 
'''
img[20,10] = 0
img[20,11] = 0
img[20,12] = 1
img[20,13] = 1
img[20,14] = 2
img[20,15] = 2
img[20,16] = 3
img[20,17] = 3
img[20,18] = 2
img[20,19] = 4
'''
#cv2.line(img,(0,0),(400,400),(0,0,0),5)
cv2.line(img,(0,300),(300,0),(255,255,255),5)
cv2.imwrite('lined_image.png',img)

edges = cv2.Canny(img,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.png',img2)
