#brightness control of an image

import cv2
import numpy as np


def reduce_b(img,height,width):
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,3):
                try:
                    if img[i,j,k] >= 50:
                        img[i,j,k]= img[i,j,k] - 50
                except IndexError:
                    continue
    
              
def increase_b(img,height,width):
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,3):
                try:
                    if img[i,j,k] <= 205:
                        img[i,j,k]= img[i,j,k] + 50
                except IndexError:
                    continue
    

img = cv2.imread('3.jpg',-1)

height = np.size(img[0])
width = np.size(img[1])

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if k == ord('i'):
        increase_b(img,height,width)
    elif k == ord('r'):
        reduce_b(img,height,width)
    else:
        cv2.destroyAllWindows()
        break

        
    
