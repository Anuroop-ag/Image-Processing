import cv2
import numpy as np 


img = cv2.imread('3.jpg',-1)
row,col,channel  = img.shape
while(True):
	
	cv2.imshow('original_bright',img)
	key = cv2.waitKey(0)
	cv2.destroyAllWindows()
	if(key == ord('i')):
		print('Increasing brightness......')
		for i in range(0,row):
			for j in range(0,col):
				for k in range(0,channel):
					img[i,j,k] = min(255,img[i,j,k]+40)
		print('Brightness increased......')
	else:
		cv2.destroyAllWindows()
		cv2.imwrite('bright.jpg',img)
		break


	


