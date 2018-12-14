
''' 

Crop a portion of the image,
enhance it,
place it back in the original image

'''

import cv2
import numpy as np

img = cv2.imread('original.png',0)

row,col = img.shape

roi = img[200:450,200:450]
equ = cv2.equalizeHist(roi)

img[200:450,200:450] = equ

cv2.imwrite('enhanced_cropped.png',img)



