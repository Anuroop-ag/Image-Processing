#Convert a grayscale image to a colour image with the following adjustments:
# if I>245 then R=I-20,G=I-10,B=I-5
# else R=I+10,G=I+10,B=I+5


import cv2
import numpy as np


img = cv2.imread('45g.jpg',0) 
height = np.size(img,0)
width = np.size(img,1)

print 'height ',height
print 'width ',width

mat= np.zeros((len(img),len(img[0]),3),np.uint8)

for i in range(0,height):
	for j in range(0,width):
		if img[i,j] > 245:
			intensity = img[i,j]
			temp=[]
			temp.append(intensity-40) 
			temp.append(intensity-30) 
			temp.append(intensity-50) 
			mat[i,j]=temp
			#print 'temp in if ', temp
		else:
			intensity = img[i,j]
			temp=[]
			temp.append(intensity+20) 
			temp.append(intensity+20) 
			temp.append(intensity+20) 
			mat[i,j]=temp
			#print 'temp in else ', temp



cv2.imwrite('45g_in_colour.jpg',mat)

