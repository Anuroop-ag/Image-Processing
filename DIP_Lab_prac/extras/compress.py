import cv2
import numpy as np 
import os

img = cv2.imread('lenna.png',0)


img = cv2.resize(img,(800,800),interpolation=cv2.INTER_CUBIC)
#print (os.stat('lenna.png').st_size)
'''for i in range(0,row):
	for j in range(0,col):
'''
segments = []
for i in range(0,701,100):
	for j in range(0,701,100):
		start = (i,j,i+100,j+100)
		segments.append(start)
print(segments)		
list_of_img = []
count = 0
for item in segments:
	count = count+1
	x1 = int(item[0])
	y1 = int(item[1])
	x2 = int(item[2])
	y2 = int(item[3])
	temp_img = np.zeros((100,100))
	for i in range(x1,x2):
		for j in range(y1,y2):
			temp_img[i-x1,j-y1] = img[i,j]
			list_of_img.append(temp_img)


#print(len(list_of_img))
print(count)
cv2.imwrite('1.png',list_of_img[0])
cv2.imwrite('2.png',list_of_img[1])
cv2.imwrite('3.png',list_of_img[2])

'''
d = cv2.dct(np.float32(img))
cv2.imwrite('dct.png',d)
print (os.stat('dct.png').st_size)
'''