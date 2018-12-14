import cv2
import numpy as np 

img = cv2.imread('original.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = np.abs(fshift)
ifshift = np.fft.ifftshift(fshift)
i_f = np.fft.ifft2(ifshift)
cv2.imwrite('inverted_fourier.png',np.abs(i_f))



