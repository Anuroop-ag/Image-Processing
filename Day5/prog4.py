import numpy as np
import cv2


i1 = cv2.imread('original.jpg',0)
sobelx = cv2.Sobel(i1,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(i1,cv2.CV_64F,0,1,ksize=5)

i2 = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#cv2.imshow('sobel',i2)

f = np.fft.fft2(i1)
fshift = np.fft.fftshift(f)
magnitude_spectrum_1 = 20*np.log(np.abs(fshift))

f = np.fft.fft2(i2)
fshift = np.fft.fftshift(f)
magnitude_spectrum_2 = 20*np.log(np.abs(fshift))

row,col = magnitude_spectrum_1.shape


mat  = magnitude_spectrum_1
for i in range(0,row):
    for j in range(0,col):
        mat[i,j]=(magnitude_spectrum_1[i,j]*magnitude_spectrum_2[i,j])/255
cv2.imwrite('multiply.jpg',mat)


