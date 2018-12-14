import cv2
import numpy as np 

img  = cv2.imread('original.png',0)
r = []

for i in range(0,256):
	r.append(i)
#print(r)
row,col = img.shape
total = row*col
count = [0]*256
#print(count)
for i in range(0,row):
	for j in range(0,col):
		count[img[i,j]] = count[img[i,j]] + 1

p_r = [0.0]*256
for i in range(0,256):
	p_r[i]  = count[i]/total
#print(p_r)
cum_p_r = [0.0]*256
z = 0 
for i in range(0,256):
	cum_p_r[i] = p_r[i] + z
	z = cum_p_r[i]
#print (cum_p_r)
s_min = min(cum_p_r)
#print(s_min)
s_dash = [0]*256
for i in range(0,256):
	s_dash[i] = int((cum_p_r[i]-s_min)/(1-s_min)*255+0.5)

for i in range(0,row):
	for j in range(0,col):
		img[i,j] = s_dash[img[i,j]]

cv2.imwrite('hist_equalized.png',img)