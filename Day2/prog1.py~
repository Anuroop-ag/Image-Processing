#WAP to store a image in different formats and record the size of these images


import cv2
import numpy as np
import os

img=cv2.imread('3.jpg',-1)

#####size of png#################################
cv2.imwrite('store_3_as_png.png',img)
sinfo=os.stat('store_3_as_png.png')
print 'size of png file in bytes : ',sinfo.st_size

############size of jpg##################################
cv2.imwrite('store_3_as_jpg.jpg',img)
sinfo=os.stat('store_3_as_jpg.jpg')
print 'size of jpg file in bytes : ',sinfo.st_size

########size of tif############################################
cv2.imwrite('store_3_as_tif.tif',img)
sinfo=os.stat('store_3_as_tif.tif')
print 'size of tif file in bytes : ',sinfo.st_size

