import cv2
import numpy as np 

img = cv2.imread('3.jpg',-1)
row,col,channel = img.shape


while(True):
	cv2.imshow('contrast',img)
	key = cv2.waitKey(0)
	cv2.destroyAllWindows()
	if(key == ord('i')):
		print("Increasing contrast")
		for i in range(0,row):
			for j in range(0,col):
				for k in range(0,channel):
					if(img[i,j,k]>127):
						img[i,j,k] = min(255, img[i,j,k] + 20)
					else:
						img[i,j,k] = max(0, img[i,j,k] - 20)
	else:
		cv2.destroyAllWindows()
		cv2.imwrite('high_contrast.jpg',img)
		break
