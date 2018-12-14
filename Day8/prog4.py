'''

Perform the DCT transformation


'''

import cv2
import numpy as np


#### In DCT we are taking REAL value ####

img = cv2.imread('messi.png',0)
f1 = np.fft.fft2(img)
fshift = np.fft.fftshift(f1)
magnitude_spectrum = 20*np.log(np.real(fshift))
cv2.imwrite('dct.png',magnitude_spectrum)

#########################################
