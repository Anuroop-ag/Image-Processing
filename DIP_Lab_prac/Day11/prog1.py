import cv2
import numpy as np 

img = cv2.imread('j.png',0)
row,col = img.shape

# performing negative
for i in range(0,row):
	for j in range(0,col):
		img[i,j] = 255-img[i,j]


#print(img)
#cv2.imwrite('j_neg.png',img)
## operating on j negative ###

for i in range(0,row):
	for j in range(0,col):
		if(img[i,j]>127):
			img[i,j] = 255
		else:
			img[i,j] = 0

str_ele = [255,255,255] # taking 3X1 structuring element

erode = np.zeros((row,col),np.uint8)
dilate = np.zeros((row,col),np.uint8)

#### erosion ###################

for i in range(1,row-1):
	for j in range(1,col-1):
		if(img[i,j] == 255 and img[i,j+1]==255 and img[i,j-1]==255):
			erode[i,j] = 255
		else:
			erode[i,j] = 0
'''			
newp=np.zeros((row,col),np.uint8)
for i in range(0,row):
	for j in range(0,col):
		if(img[i,j]!=erode[i,j]):
			newp[i,j] = 255
cv2.imwrite("erodenew.png",newp)
'''
cv2.imwrite('eroded.png', erode)

####### dilated ##################

for i in range(1,row-1):
	for j in range(1,col-1):
		if(img[i,j] == 255):
			dilate[i,j-1] = 255
			dilate[i,j+1] = 255
cv2.imwrite('dilated.png',dilate)