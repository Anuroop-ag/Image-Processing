import cv2
import numpy as np 
'''
#fft
img = cv2.imread('original.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = np.abs(fshift)
ifshift = np.fft.ifftshift(fshift)
i_f = np.fft.ifft2(ifshift)
cv2.imwrite('inverted_fourier.png',np.abs(i_f))

#dct
img = cv2.imread('original.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = np.real(fshift)
ifshift = np.fft.ifftshift(mag)
i_f = np.fft.ifft2(ifshift)
cv2.imwrite('inverted_cos.png',np.abs(i_f))


#dst
img = cv2.imread('original.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = np.imag(fshift)
ifshift = np.fft.ifftshift(mag)
i_f = np.fft.ifft2(ifshift)
cv2.imwrite('inverted_sin.png',np.abs(i_f))
'''
img = cv2.imread('original.png',0)
f = np.fft.fft2(img)
#f= np.abs(f)
#cv2.imwrite('fourier.png',f)
#print(f.shape)
'''
img = cv2.imread('original.png',0)
d = cv2.dct(np.float32(img))'''
#cv2.imwrite('cos.png',d)
#print(d.shape)

img = cv2.imread('original.png',0)
f = np.fft.fft2(img)

row,col = f.shape
s = np.zeros((row,col),dtype=complex) 

for i in range(0,row):
	for j in range(0,col):
		#s[i,j] = np.sqrt(abs(f[i,j]**2 - d[i,j]**2))
		s[i,j] = np.imag(f[i,j])

#cv2.imwrite('sin.png',s)
row,col = f.shape
d = np.zeros((row,col),dtype=complex) 
for i in range(0,row):
	for j in range(0,col):
		#s[i,j] = np.sqrt(abs(f[i,j]**2 - d[i,j]**2))
		d[i,j] = np.real(f[i,j])


row,col = f.shape
f = np.zeros((row,col),dtype=complex) 
for i in range(0,row):
	for j in range(0,col):
		#s[i,j] = np.sqrt(abs(f[i,j]**2 - d[i,j]**2))
		#f[i,j] = np.sqrt(abs(d[i,j]**2 + s[i,j]**2))
		f[i,j] = d[i,j] + (s[i,j]*1j)

'''
cv2.imwrite('fourier.png',5*np.log(np.abs(f)+1))
cv2.imwrite('cos.png',5*np.log(np.abs(d)+1))
cv2.imwrite('sin.png',5*np.log(np.abs(s)+1))
'''
inv =np.fft.ifft2(d)
cv2.imwrite('inverted_cos.png',np.abs(inv))

inv = np.fft.ifft2(f)
cv2.imwrite('inverted_fourier.png',np.abs(inv))

inv = np.fft.ifft2(s)
cv2.imwrite('inverted_sine.png',np.abs(inv))
