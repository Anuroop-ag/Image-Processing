import cv2
import numpy as np 


img = cv2.imread('3.jpg',-1)
#res = cv2.resize(img,(4000,3000),interpolation = cv2.INTER_CUBIC)
res = cv2.resize(img,None,fx = 5, fy = 5 , interpolation = cv2.INTER_CUBIC)
cv2.imwrite('resized_image.jpg',res)