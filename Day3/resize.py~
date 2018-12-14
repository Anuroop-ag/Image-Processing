#resize an image


import cv2
import numpy as np

img = cv2.imread('3.jpg',-1)

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('enlarged_image.jpg',res)

'''cv2.imshow('enlarged_image',res)
cv2.waitKey(0)'''

res = cv2.resize(img,None,fx=0.5 , fy=0.5, interpolation = cv2.INTER_CUBIC)
cv2.imwrite('diminished_image.jpg',res)

'''cv2.imshow('diminished_image',res)
cv2.waitKey(0)'''
