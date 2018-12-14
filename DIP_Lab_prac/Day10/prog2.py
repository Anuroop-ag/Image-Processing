'''
consider a straight line form by the following:
0011223324

find line by hough transform
'''

import cv2
import numpy as np

img = cv2.imread('lenna.png',0)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('lenna.png',-1) 

img[10,0] = 0
img[11,1] = 0
img[12,2] = 1
img[13,3] = 1
img[14,4] = 2
img[15,5] = 2
img[16,6] = 3
img[17,7] = 3
img[18,8] = 2
img[19,9] = 4

cv2.imwrite('noise_lenna.png',img)

list_of_points = [[10,0],[11,1],[12,2],[13,3],[14,4],[15,5],[16,6],[17,7],[18,8],[19,9]]

# we will vary c from -20 to 20 and m from -2 to 2

list_of_mc = []
for i in list_of_points:
	x1 = i[0]
	y1 = i[1]
	for m in range(-2,3):
		c = (-1)*m*x1+y1
		if(c>=-20 and c<=20):
			temp = []
			temp.append(m)
			temp.append(c)
			list_of_mc.append(temp)
			
		

#print(list_of_mc)
count_max =0
max_item = []
for item in list_of_mc:
	count = 0
	for x in list_of_mc:
		if(item == x):
			count = count+1

	if(count>count_max):
		count_max = count
		max_item = item
print(max_item)

m = max_item[0]
c = max_item[1]

# if x = 40 , y =?
x1 = 10
y1 = m*x1+c 

# if y=60, x =?

y2 =60
x2 = int((y2-c)/m)

cv2.line(img2,(x1,y1),(x2,y2),(255,255,255),5)
cv2.imwrite('hough_lenna.png',img2)