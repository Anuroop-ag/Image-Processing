#Convert grayscale image to binary

import cv2
import numpy as np

img = cv2.imread('45g.jpg',-1)
ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imwrite('45g_as_binary.jpg',thresh_img)
