#remove gaussian noise
#gaussian filter

import cv2
import numpy as np

img = cv2.imread('gauss.png',0)
img2 = cv2.imread('gauss2.png',0)

gauss_filtered = cv2.GaussianBlur(img,(5,5),0)
gauss_filtered2 = cv2.GaussianBlur(img2,(5,5),0)

res = np.hstack((img,gauss_filtered))
res2 = np.hstack((img2,gauss_filtered2))

cv2.imwrite('gauss_filtered_result.png',res)
cv2.imwrite('gauss2_filtered_result.png',res2)
