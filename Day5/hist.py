import cv2
import numpy as np

img = cv2.imread('original.jpg',-1)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imwrite('equal.jpg',res)
