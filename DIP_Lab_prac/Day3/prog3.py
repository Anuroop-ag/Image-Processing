import cv2
import numpy as np 

img = cv2.imread('3.jpg',-1)
x1 = 100
x2 = 400
y1 = 200
y2 = 400

roi = img[x1:x2,y1:y2]
cv2.imwrite('cropped_img.jpg',roi)