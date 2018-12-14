#crop an image

import cv2
import numpy as np

img = cv2.imread('3.jpg',0)
temp_img = cv2.imread('3.jpg',0)
 
or_h = np.size(img[0])
or_w = np.size(img[1])

for i in range(0,or_h):
    for j in range(0,or_w):
        try:
            temp_img[i,j]=0
        except IndexError:
            continue
            


print "Enter top left coordinates: "
x1 = int(raw_input())
y1 = int(raw_input())

print "Enter bottom right coordinates: "
x2 = int(raw_input())
y2 = int(raw_input())

for i in range(y1,y2+1):
    for j in range(x1,x2+1):
        try:
            temp_img[i,j]=img[i,j]
        except IndexError:
            continue
        
cv2.imwrite('cropped.jpg',temp_img)



