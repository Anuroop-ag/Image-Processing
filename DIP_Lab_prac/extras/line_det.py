import cv2
import numpy as np 

img  = cv2.imread('hori_ver.jpg',0)
verti = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
hori = [[-1,-1,-1],[2,2,2],[-1,-1,-1]]
verti = np.array(verti)
hori = np.array(hori)

v = cv2.filter2D(img,-1,verti)
h = cv2.filter2D(img,-1,hori)

cv2.imwrite('hori.jpg',h)
cv2.imwrite('verti.jpg',v)