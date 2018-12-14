''' Find edges using Sobel operator'''

import numpy as np
import cv2


i1 = cv2.imread('Apply_Sobel.png',0)
sobelx = cv2.Sobel(i1,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(i1,cv2.CV_64F,0,1,ksize=5)

i2 = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv2.imwrite('Sobel_result.png',i2)
