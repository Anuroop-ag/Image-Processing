'''

Perform the FFT transformation


'''

import cv2
import numpy as np


#### In FFT we are taking ABSOLUTE value ###########

img = cv2.imread('messi.png',0)
f1 = np.fft.fft2(img)
fshift = np.fft.fftshift(f1)
magnitude_spectrum = 20*np.log(np.abs(fshift))
cv2.imwrite('fft.png',magnitude_spectrum)

####################################################
