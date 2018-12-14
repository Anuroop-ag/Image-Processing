import cv2
import numpy as np 



def checkPixel(img,list_of_tuples):
	x1 = int(list_of_tuples[0][0])
	y1 = int(list_of_tuples[0][1])
	x2 = int(list_of_tuples[0][2])
	y2 = int(list_of_tuples[0][3])

	for i in range(x1+1,x2-1):
		for j in range(y1+1,y2-1):
			d1 = abs(img[i,j]-img[i,j+1])
			d2 = abs(img[i,j]-img[i,j-1])
			d3 = abs(img[i,j]-img[i-1,j])
			d4 = abs(img[i,j]-img[i+1,j])

			if(d1>15 or d2>15 or d3>15 or d4>15):
				return 1
	return 0

def segmentImage(list_of_tuples):
	x1 = int(list_of_tuples[0][0])
	y1 = int(list_of_tuples[0][1])
	x2 = int(list_of_tuples[0][2])
	y2 = int(list_of_tuples[0][3])
	
	del list_of_tuples[0]
	list_of_tuples.append((x1,y1,(x1+x2)/2,(y1+y2)/2))
	list_of_tuples.append((x1,(y1+y2)/2,(x1+x2)/2,y2))
	list_of_tuples.append(((x1+x2)/2,y1,x2,(y1+y2)/2))
	list_of_tuples.append(((x1+x2)/2,(y1+y2)/2,x2,y2))

	return list_of_tuples

def sameColour(img,list_of_tuples):
	x1 = int(list_of_tuples[0][0])
	y1 = int(list_of_tuples[0][1])
	x2 = int(list_of_tuples[0][2])
	y2 = int(list_of_tuples[0][3])
	val = img[x1,y1]
	for i in range(x1,x2):
		for j in range(y1,y2):
			if(i==x1 or i==x2-1 or j==y1 or j==y2-1):
				img[i,j] = 0
			else:
				img[i,j] = val

			


	return img




img = cv2.imread('fr.jpeg',0)
row,col = img.shape

ini_cor = (0,0,row-1,col-1)
list_of_tuples = []
list_of_tuples.append(ini_cor)

while(list_of_tuples):

	if(checkPixel(img,list_of_tuples)==1):
		list_of_tuples = segmentImage(list_of_tuples)
	else:
		img = sameColour(img,list_of_tuples)
		del list_of_tuples[0]

cv2.imwrite('decomposed.jpeg',img)