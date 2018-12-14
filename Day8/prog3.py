'''

Perform the DST transformation


'''

import cv2
import numpy as np

#### In DST we are taking IMAGINARY value #####

img = cv2.imread('messi.png',0)
f1 = np.fft.fft2(img)
fshift = np.fft.fftshift(f1)
magnitude_spectrum = 20*np.log(np.imag(fshift))
cv2.imwrite('dst.png',magnitude_spectrum)

###############################################
