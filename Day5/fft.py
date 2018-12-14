import numpy as np
import cv2

img = cv2.imread('original.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
cv2.imwrite('fft.jpg',magnitude_spectrum)

'''img_back = cv2.idft(np.abs(f))
cv2.imwrite('invfft.jpg',img_back)
'''
